import os
import re
import shutil
import json
from config import (
    GENDER,
    LANGUAGE,
    REPLACE_FOLDERS,
    PIECE_TO_FOLDER,
    GENDER_CONFIGS,
    DOWNLOAD_DIR,
    REVIEW_DIR,
    DEBUG_MODE,
)

from lang import MESSAGES, DIFF_HEADERS

# 🌐 Função para obter mensagens multilíngues / Function to get multilingual messages
msg = lambda key, **kwargs: MESSAGES[LANGUAGE][key].format(**kwargs)


def ensure_required_directories():
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    os.makedirs(REVIEW_DIR, exist_ok=True)
    for gender_key, config in GENDER_CONFIGS.items():
        base = os.path.join("[clothes]", config["code"], "stream")
        os.makedirs(base, exist_ok=True)
        os.makedirs(os.path.join("sumary", config["code"]), exist_ok=True)
        for folder in PIECE_TO_FOLDER.values():
            os.makedirs(os.path.join(base, folder), exist_ok=True)
            os.makedirs(os.path.join("sumary", config["code"], folder), exist_ok=True)


def get_ydd_files():
    return [f for f in os.listdir(DOWNLOAD_DIR) if f.endswith(".ydd")]


def get_piece_name(filename):
    base_name = os.path.splitext(filename)[0].lower()
    match = None
    if "^" in base_name:
        match = re.search(r"\^([a-z_]+)_\d{3}(?:_[a-z])?", base_name)
    else:
        match = re.match(r"([a-z_]+)_\d{3}(?:_[a-z])?", base_name)
    return match.group(1) if match else "unknown"


def generate_meta_and_fxmanifest():
    for gender_key, config in GENDER_CONFIGS.items():
        base_path = os.path.join("[clothes]", config["code"])
        stream_path = os.path.join(base_path, "stream")
        os.makedirs(stream_path, exist_ok=True)

        meta_name = f"{config['prefix']}.meta"
        meta_path = os.path.join(base_path, meta_name)
        meta_content = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<ShopPedApparel>
    <pedName>{config['ped_name']}</pedName>
    <dlcName>{config['code']}</dlcName>
    <fullDlcName>{config['prefix']}</fullDlcName>
    <eCharacter>SCR_CHAR_MULTIPLAYER</eCharacter>
    <creatureMetaData>MP_CreatureMetadata_{config['code']}</creatureMetaData>
    <pedOutfits></pedOutfits>
    <pedComponents></pedComponents>
    <pedProps></pedProps>
</ShopPedApparel>"""
        with open(meta_path, "w", encoding="utf-8") as f:
            f.write(meta_content)

        fxmanifest_path = os.path.join(base_path, "fxmanifest.lua")
        fxmanifest_content = f"""fx_version 'bodacious'
game {{ 'gta5' }}

files {{
  '{meta_name}'
}}

data_file 'SHOP_PED_APPAREL_META_FILE' '{meta_name}'
"""
        with open(fxmanifest_path, "w", encoding="utf-8") as f:
            f.write(fxmanifest_content)


def generate_diff_report():
    diff_data = {"fc": {}, "mc": {}}
    for gender_key in ["fc", "mc"]:
        stream_path = os.path.join("[clothes]", gender_key, "stream")
        if not os.path.exists(stream_path):
            continue
        for category in os.listdir(stream_path):
            cat_path = os.path.join(stream_path, category)
            if not os.path.isdir(cat_path):
                continue
            for folder in sorted(
                os.listdir(cat_path), key=lambda x: int(x) if x.isdigit() else x
            ):
                final_path = os.path.join(cat_path, folder)
                if os.path.isdir(final_path):
                    diffs = [
                        f
                        for f in os.listdir(final_path)
                        if f.endswith(".ytd") and "diff" in f.lower()
                    ]
                    letters = [
                        re.search(r"_diff_\d{3}_([a-z])", f).group(1)
                        for f in diffs
                        if re.search(r"_diff_\d{3}_([a-z])", f)
                    ]
                    if category not in diff_data[gender_key]:
                        diff_data[gender_key][category] = {}
                    diff_data[gender_key][category][folder] = {
                        "total": len(letters),
                        "letters": letters,
                    }

    header = DIFF_HEADERS.get(LANGUAGE, DIFF_HEADERS["en"])

    with open("diff_report.lua", "w", encoding="utf-8") as f:
        f.write(header)
        f.write("diffs = {\n")
        for gender, categories in diff_data.items():
            f.write(f"    {gender} = {{\n")
            for category, folders in categories.items():
                f.write(f'        ["{category}"] = {{\n')
                for folder, data in folders.items():
                    letter_str = ", ".join(f'"{l}"' for l in data["letters"])
                    f.write(f'            ["{folder}"] = {{\n')
                    f.write(f'                total = {data["total"]},\n')
                    f.write(f"                letters = {{ {letter_str} }}\n")
                    f.write(f"            }},\n")
                f.write("        },\n")
            f.write("    },\n")
        f.write("}\n")

    print(msg("report_generated"))


def process_single_mod():
    ensure_required_directories()
    generate_meta_and_fxmanifest()

    ydd_files = get_ydd_files()
    if not ydd_files:
        generate_diff_report()
        print(msg("no_ydd"))
        return

    unique = {}
    for f in ydd_files:
        piece = get_piece_name(f)
        if piece != "unknown" and piece not in unique:
            unique[piece] = f
        if len(unique) == 5:
            break

    for piece_name, ydd_file in unique.items():
        ydd_path = os.path.join(DOWNLOAD_DIR, ydd_file)
        gender_code = GENDER_CONFIGS[GENDER]["code"]
        prefix = GENDER_CONFIGS[GENDER]["prefix"]

        category_folder = PIECE_TO_FOLDER.get(piece_name)
        if not category_folder:
            print(msg("unrecognized", file=ydd_file))
            continue

        category_path = os.path.join(
            "[clothes]", gender_code, "stream", category_folder
        )

        replace_indices = REPLACE_FOLDERS.get(GENDER, {}).get(piece_name, [])
        folder_num = None

        if replace_indices:
            folder_num = replace_indices[0]
            print(msg("replacing", categoria=piece_name, num=folder_num))
        else:
            existentes = [
                d
                for d in os.listdir(category_path)
                if os.path.isdir(os.path.join(category_path, d)) and d.isdigit()
            ]
            usados = [int(d) for d in existentes]
            next_num = 0
            while next_num in usados:
                next_num += 1
            folder_num = str(next_num)
            print(msg("creating", categoria=piece_name, num=folder_num))

        final_folder = os.path.join(category_path, folder_num)
        if os.path.exists(final_folder):
            shutil.rmtree(final_folder)
        os.makedirs(final_folder, exist_ok=True)

        new_ydd_name = f"{prefix}^{piece_name}_{folder_num.zfill(3)}_u.ydd"
        if DEBUG_MODE:
            print(f"[DEBUG] YDD → {new_ydd_name}")
        shutil.move(ydd_path, os.path.join(final_folder, new_ydd_name))
        print(msg("ydd_moved", name=new_ydd_name))

        image_found = None
        for ext in [".png", ".jpg", ".jpeg"]:
            for f in os.listdir(DOWNLOAD_DIR):
                if f.lower().endswith(ext):
                    image_found = os.path.join(DOWNLOAD_DIR, f)
                    break
            if image_found:
                break

        if image_found:
            sumary_path = os.path.join("sumary", gender_code, category_folder)
            os.makedirs(sumary_path, exist_ok=True)
            new_img_name = f"{folder_num}.png"
            if DEBUG_MODE:
                print(f"[DEBUG] IMG → {new_img_name}")
            shutil.copy(image_found, os.path.join(sumary_path, new_img_name))
            os.remove(image_found)
            print(msg("image_moved", name=new_img_name))

        base_name = os.path.splitext(os.path.basename(ydd_path))[0].lower()
        number_match = re.search(r"_(\d{3})_", base_name)
        number_code = number_match.group(1) if number_match else folder_num.zfill(3)

        texture_letters = "abcdefghijklmnopqrstuvwxyz"
        index = 0
        for f in sorted(os.listdir(DOWNLOAD_DIR)):
            if f.endswith(".ytd") and f"_{number_code}_" in f:
                src = os.path.join(DOWNLOAD_DIR, f)
                number_code = folder_num.zfill(3)


for f in sorted(os.listdir(DOWNLOAD_DIR)):
    if not f.endswith(".ytd"):
        continue
    if piece_name in f and f"_{number_code}_" in f:
        src = os.path.join(DOWNLOAD_DIR, f)

        if "diff" in f.lower():
            letter = texture_letters[index]
            new_ytd = f"{prefix}^{piece_name}_diff_{number_code}_{letter}_uni.ytd"
            if DEBUG_MODE:
                print(f"[DEBUG] YTD → {new_ytd}")
            shutil.move(src, os.path.join(final_folder, new_ytd))
            print(msg("ytd_moved", name=new_ytd))
            index += 1
        else:
            shutil.move(src, os.path.join(REVIEW_DIR, f))
            print(msg("ytd_invalid", file=f))
