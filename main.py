# 📂 Script Principal / 📂 Main Script

from config import LANGUAGE
from lang import MESSAGES
from processor import process_single_mod

# 🌐 Seleciona mensagens no idioma configurado / Select messages in configured language
msg = lambda key, **kwargs: MESSAGES[LANGUAGE][key].format(**kwargs)

def main():
    print(msg("start")) 
    process_single_mod()
    print(msg("done"))

if __name__ == "__main__":
    main()
