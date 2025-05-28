GENDER = "female"  # "female" ou "male"

# ⚠️ Important
# The number should be a string, not an integer ("10" and not 10)         🇺🇸
# O número deve ser uma string, não um inteiro ("10" e não 10)            🇧🇷
# El número debe ser una cadena, no un entero ("10" y no 10)              🇪🇸
# Le numéro doit être une chaîne, pas un entier ("10" et non 10)          🇫🇷
# Die Zahl muss ein String sein, kein Integer ("10" und nicht 10)         🇩🇪
# Il numero deve essere una stringa, non un intero ("10" e non 10)        🇮🇹

REPLACE_FOLDERS = {
    "female": {
        "accs": [],
        "beards": [],
        "berd": [],
        "decl": [],
        "feet": [],
        "hair": [],
        "hand": [],
        "head": [],
        "jbib": [],
        "lowr": [],
        "p_ears": [],
        "p_eyes": [],
        "p_lwrist": [],
        "p_rwrist": [],
        "task": [],
        "teef": [],
        "uppr": [],
    },
    "male": {
        "accs": [],
        "beards": [],
        "berd": [],
        "decl": [],
        "feet": [],
        "hair": [],
        "hand": [],
        "head": [],
        "jbib": [],
        "lowr": [],
        "p_ears": [],
        "p_eyes": [],
        "p_lwrist": [],
        "p_rwrist": [],
        "task": [],
        "teef": [],
        "uppr": [],
    },
}

DEBUG_MODE = True  # True or False

# 🇧🇷 pt (Português), 🇺🇸 en (English), 🇪🇸 es (Español), 🇫🇷 fr (Français), 🇩🇪 de (Deutsch), 🇮🇹 it (Italiano)
LANGUAGE = "fr"

# 🔠 Mapeamento de categorias / Mapping of piece names to target folders
PIECE_TO_FOLDER = {
    "accs": "accs=tshirts",
    "beards": "beards=facialhair",
    "berd": "berd=mask",
    "decl": "decl=decls",
    "feet": "feet=shoes",
    "hair": "hair=hair",
    "hand": "hand=bags",
    "head": "head=faceskinss",
    "jbib": "jbib=jackets",
    "lowr": "lowr=pants",
    "p_head": "head=head",
    "p_ears": "p_ears=earringss",
    "p_eyes": "p_eyes=glassess",
    "p_lwrist": "p_lwrist=watchess",
    "p_rwrist": "p_rwrist=braceletss",
    "task": "task=bodyarmor",
    "teef": "teef=chains",
    "uppr": "uppr=arms",
}

# 🧬 Dados por gênero / Gender-specific configuration
GENDER_CONFIGS = {
    "female": {
        "code": "fc",
        "prefix": "mp_f_freemode_01_fc",
        "ped_name": "mp_f_freemode_01",
    },
    "male": {
        "code": "mc",
        "prefix": "mp_m_freemode_01_mc",
        "ped_name": "mp_m_freemode_01",
    },
}

# 📁 Diretórios padrão / Default directories
DOWNLOAD_DIR = "download"
REVIEW_DIR = f"{DOWNLOAD_DIR}/revisao"
