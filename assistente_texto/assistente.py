import datetime
import os
import wikipedia
import pywhatkit
from colorama import Fore, Style, init

# === Inicializa o Colorama ===
init(autoreset=True)

# === Configuração da Wikipedia ===
wikipedia.set_lang("pt")

def falar(texto, cor=Fore.CYAN):
    print(cor + f"🤖 Assistente: {texto}" + Style.RESET_ALL)

def linha():
    print(Fore.MAGENTA + "═" * 60 + Style.RESET_ALL)

def menu():
    linha()
    print(Fore.YELLOW + "🌟 COMANDOS DISPONÍVEIS 🌟" + Style.RESET_ALL)
    print(Fore.GREEN + """
  ⏰ hora                 → mostra a hora atual
  🎵 tocar [música]       → toca música no YouTube
  🌐 pesquisar [termo]    → busca resumo na Wikipedia
  🧮 abrir calculadora    → abre a calculadora
  📝 abrir bloco de notas → abre o bloco de notas
  🌍 abrir navegador      → abre o Google Chrome
  ❌ sair                 → encerra o assistente
""" + Style.RESET_ALL)
    linha()

def executar_comando(comando):
    comando = comando.lower().strip()

    if comando in ["menu", "ajuda", "comandos"]:
        menu()

    elif "hora" in comando:
        hora = datetime.datetime.now().strftime("%H:%M")
        falar(f"Agora são {hora}.", Fore.LIGHTGREEN_EX)

    elif comando.startswith("tocar") or comando.startswith("toque"):
        musica = comando.replace("tocar", "").replace("toque", "").strip()
        if musica:
            falar(f"Tocando {musica} no YouTube...", Fore.LIGHTYELLOW_EX)
            pywhatkit.playonyt(musica)
        else:
            falar("Você precisa dizer o nome da música.", Fore.RED)

    elif comando.startswith("abrir"):
        app = comando.replace("abrir", "").strip()
        if not app:
            falar("Diga o nome do aplicativo que deseja abrir.", Fore.RED)
            return

        falar(f"Abrindo {app}...", Fore.LIGHTBLUE_EX)

        # Exemplos para Windows
        if "bloco de notas" in app:
            os.system("notepad")
        elif "calculadora" in app:
            os.system("calc")
        elif "navegador" in app or "chrome" in app:
            os.system("start chrome")
        else:
            falar("Desculpe, ainda não sei abrir esse aplicativo.", Fore.RED)

    elif comando.startswith("pesquisar") or comando.startswith("procure"):
        termo = comando.replace("pesquisar", "").replace("procure", "").strip()
        if termo:
            falar(f"Pesquisando por {termo} na Wikipedia...", Fore.LIGHTCYAN_EX)
            try:
                resultado = wikipedia.summary(termo, sentences=2)
                print(Fore.LIGHTWHITE_EX + "📘 Resultado:\n" + resultado)
            except:
                falar("Não encontrei resultados para esse termo.", Fore.RED)
        else:
            falar("Diga o que deseja pesquisar.", Fore.RED)

    elif comando in ["sair", "fechar", "encerrar"]:
        falar("Encerrando o assistente. Até logo! 👋", Fore.LIGHTRED_EX)
        exit()

    else:
        falar("Comando não reconhecido. Digite 'menu' para ver as opções.", Fore.YELLOW)


def iniciar_assistente():
    linha()
    print(Fore.CYAN + "🤖 BEM-VINDO AO ASSISTENTE VIRTUAL DE TEXTO!" + Style.RESET_ALL)
    print(Fore.MAGENTA + "Digite 'menu' para ver os comandos disponíveis." + Style.RESET_ALL)
    linha()

    while True:
        comando = input(Fore.LIGHTWHITE_EX + "🧑 Você: " + Style.RESET_ALL)
        executar_comando(comando)


# === Inicia o programa ===
if __name__ == "__main__":
    iniciar_assistente()
