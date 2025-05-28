# 📚 Mensagens multilíngues para o script / Multilingual messages for the script

MESSAGES = {
    "pt": {
        "start": "🚀 Iniciando processamento...",
        "done": "✅ Mod processado com sucesso.",
        "no_ydd": "⚠️ Nenhum arquivo .ydd encontrado na pasta de download.",
        "unrecognized": "❌ Tipo não reconhecido no nome do arquivo: {file}",
        "replacing": "♻️ Substituindo conteúdo de {categoria}/{num}...",
        "creating": "📁 Criando nova pasta para {categoria}/{num}...",
        "skip_not_replace": "⏭️ {category} ignorado: não marcado para replace.",
        "report_generated": "📄 diff_report.lua gerado com sucesso.",
        "image_moved": "🖼️ Imagem movida: {name}",
        "ydd_moved": "✅ Arquivo .ydd movido: {name}",
        "ytd_moved": "🎨 Textura movida: {name}",
        "ytd_invalid": "⚠️ {file} enviado para revisao (sem diff).",
    },
    "en": {
        "start": "🚀 Starting mod processing...",
        "done": "✅ Mod successfully processed.",
        "no_ydd": "⚠️ No .ydd file found in the download folder.",
        "unrecognized": "❌ Unrecognized type in file name: {file}",
        "replacing": "♻️ Replacing contents of {categoria}/{num}...",
        "creating": "📁 Creating new folder for {categoria}/{num}...",
        "skip_not_replace": "⏭️ {category} skipped: not marked for replacement.",
        "report_generated": "📄 diff_report.lua successfully generated.",
        "image_moved": "🖼️ Image moved: {name}",
        "ydd_moved": "✅ .ydd file moved: {name}",
        "ytd_moved": "🎨 Texture moved: {name}",
        "ytd_invalid": "⚠️ {file} sent to review (missing diff).",
    },
    "es": {
        "start": "🚀 Iniciando el procesamiento...",
        "done": "✅ Mod procesado con éxito.",
        "no_ydd": "⚠️ No se encontró ningún archivo .ydd en la carpeta de descarga.",
        "unrecognized": "❌ Tipo no reconocido en el nombre del archivo: {file}",
        "replacing": "♻️ Reemplazando el contenido de {categoria}/{num}...",
        "creating": "📁 Creando nueva carpeta para {categoria}/{num}...",
        "skip_not_replace": "⏭️ {category} omitido: no marcado para reemplazo.",
        "report_generated": "📄 diff_report.lua generado con éxito.",
        "image_moved": "🖼️ Imagen movida: {name}",
        "ydd_moved": "✅ Archivo .ydd movido: {name}",
        "ytd_moved": "🎨 Textura movida: {name}",
        "ytd_invalid": "⚠️ {file} enviado a revisión (sin diff).",
    },
    "fr": {
        "start": "🚀 Démarrage du traitement...",
        "done": "✅ Mod traité avec succès.",
        "no_ydd": "⚠️ Aucun fichier .ydd trouvé dans le dossier de téléchargement.",
        "unrecognized": "❌ Type non reconnu dans le nom du fichier : {file}",
        "replacing": "♻️ Remplacement du contenu de {categoria}/{num}...",
        "creating": "📁 Création d'un nouveau dossier pour {categoria}/{num}...",
        "skip_not_replace": "⏭️ {category} ignoré : non marqué pour remplacement.",
        "report_generated": "📄 diff_report.lua généré avec succès.",
        "image_moved": "🖼️ Image déplacée : {name}",
        "ydd_moved": "✅ Fichier .ydd déplacé : {name}",
        "ytd_moved": "🎨 Texture déplacée : {name}",
        "ytd_invalid": "⚠️ {file} envoyé en révision (sans diff).",
    },
    "de": {
        "start": "🚀 Mod-Verarbeitung wird gestartet...",
        "done": "✅ Mod erfolgreich verarbeitet.",
        "no_ydd": "⚠️ Keine .ydd-Datei im Download-Ordner gefunden.",
        "unrecognized": "❌ Nicht erkannter Typ im Dateinamen: {file}",
        "replacing": "♻️ Ersetze Inhalt von {categoria}/{num}...",
        "creating": "📁 Erstelle neuen Ordner für {categoria}/{num}...",
        "skip_not_replace": "⏭️ {category} übersprungen: nicht zum Ersetzen markiert.",
        "report_generated": "📄 diff_report.lua erfolgreich erstellt.",
        "image_moved": "🖼️ Bild verschoben: {name}",
        "ydd_moved": "✅ .ydd-Datei verschoben: {name}",
        "ytd_moved": "🎨 Textur verschoben: {name}",
        "ytd_invalid": "⚠️ {file} zur Überprüfung gesendet (kein diff).",
    },
    "it": {
        "start": "🚀 Avvio del processo...",
        "done": "✅ Mod elaborato con successo.",
        "no_ydd": "⚠️ Nessun file .ydd trovato nella cartella download.",
        "unrecognized": "❌ Tipo non riconosciuto nel nome del file: {file}",
        "replacing": "♻️ Sostituzione del contenuto di {categoria}/{num}...",
        "creating": "📁 Creazione nuova cartella per {categoria}/{num}...",
        "skip_not_replace": "⏭️ {category} ignorato: non contrassegnato per la sostituzione.",
        "report_generated": "📄 diff_report.lua generato con successo.",
        "image_moved": "🖼️ Immagine spostata: {name}",
        "ydd_moved": "✅ File .ydd spostato: {name}",
        "ytd_moved": "🎨 Texture spostata: {name}",
        "ytd_invalid": "⚠️ {file} inviato alla revisione (manca diff).",
    },
}
# 📝 Cabeçalho multilíngue para diff_report.lua 
# Multilingual header for diff_report.lua

DIFF_HEADERS = {
    "pt": """--[[
📄 diff_report.lua
Resumo automático das texturas (diffs) detectadas por peça e pasta.

Gêneros:
- fc = feminino (mp_f_freemode_01)
- mc = masculino (mp_m_freemode_01)

Cada entrada mostra:
- total = número de arquivos .ytd com 'diff'
- letters = letras associadas a cada textura (ex: diff_001_a)

Use este relatório como base para configurar manualmente o .ymt.
]] ---@diagnostic disable: redundant-value, undefined-field
""",
    "en": """--[[
📄 diff_report.lua
Automatically generated summary of texture diffs per clothing item and folder.

Genders:
- fc = female (mp_f_freemode_01)
- mc = male (mp_m_freemode_01)

Each entry includes:
- total = number of .ytd files with 'diff'
- letters = suffix letters for each texture (e.g. diff_001_a)

Use this report to help configure your .ymt manually.
]] ---@diagnostic disable: redundant-value, undefined-field
""",
    "es": """--[[
📄 diff_report.lua
Resumen automático de texturas (diffs) detectadas por ítem y carpeta.

Géneros:
- fc = femenino (mp_f_freemode_01)
- mc = masculino (mp_m_freemode_01)

Cada entrada incluye:
- total = número de archivos .ytd con 'diff'
- letters = letras asociadas a cada textura (por ejemplo, diff_001_a)

Utiliza este informe como base para configurar manualmente el archivo .ymt.
]] ---@diagnostic disable: redundant-value, undefined-field
""",
    "fr": """--[[
📄 diff_report.lua
Résumé automatique des textures (diffs) détectées par pièce et dossier.

Genres :
- fc = féminin (mp_f_freemode_01)
- mc = masculin (mp_m_freemode_01)

Chaque entrée contient :
- total = nombre de fichiers .ytd avec 'diff'
- letters = lettres associées à chaque texture (ex : diff_001_a)

Utilisez ce rapport pour configurer manuellement le fichier .ymt.
]] ---@diagnostic disable: redundant-value, undefined-field
""",
    "de": """--[[
📄 diff_report.lua
Automatisch generierte Zusammenfassung der Textur-Diffs pro Kleidungsstück und Ordner.

Geschlechter:
- fc = weiblich (mp_f_freemode_01)
- mc = männlich (mp_m_freemode_01)

Jeder Eintrag enthält:
- total = Anzahl der .ytd-Dateien mit 'diff'
- letters = Buchstaben, die jeder Textur zugeordnet sind (z. B. diff_001_a)

Verwenden Sie diesen Bericht zur manuellen Konfiguration der .ymt-Datei.
]] ---@diagnostic disable: redundant-value, undefined-field
""",
    "it": """--[[
📄 diff_report.lua
Riepilogo automatico delle texture diff per capo e cartella.

Generi:
- fc = femminile (mp_f_freemode_01)
- mc = maschile (mp_m_freemode_01)

Ogni voce mostra:
- total = numero di file .ytd con 'diff'
- letters = lettere associate a ogni texture (es: diff_001_a)

Usa questo report per configurare manualmente il file .ymt.
]] ---@diagnostic disable: redundant-value, undefined-field
""",
}
