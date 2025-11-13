from flask import Flask, render_template, request, jsonify
import datetime
import wikipedia
import webbrowser
import os

app = Flask(__name__)

wikipedia.set_lang("pt")

# Função que executa os comandos
def executar_comando(comando):
    comando = comando.lower().strip()
    resposta = ""

    if comando in ["menu", "ajuda", "comandos"]:
        resposta = (
            "⏰ hora → mostra a hora atual\n"
            "🎵 tocar [música] → toca música no YouTube\n"
            "🌐 pesquisar [termo] → busca resumo na Wikipedia\n"
            "🧮 abrir calculadora → abre a calculadora\n"
            "📝 abrir bloco de notas → abre o bloco de notas\n"
            "🌍 abrir navegador → abre o Google Chrome\n"
            "❌ sair → encerra o assistente"
        )

    elif "hora" in comando:
        hora = datetime.datetime.now().strftime("%H:%M")
        resposta = f"Agora são {hora}."

    elif comando.startswith("tocar") or comando.startswith("toque"):
        musica = comando.replace("tocar", "").replace("toque", "").strip()
        if musica:
            resposta = f"Tocando {musica} no YouTube..."
            webbrowser.open(f"https://www.youtube.com/results?search_query={musica}")
        else:
            resposta = "Você precisa dizer o nome da música."

    elif comando.startswith("abrir"):
        app_name = comando.replace("abrir", "").strip()
        if "bloco de notas" in app_name:
            os.system("notepad")
            resposta = "Abrindo bloco de notas..."
        elif "calculadora" in app_name:
            os.system("calc")
            resposta = "Abrindo calculadora..."
        elif "navegador" in app_name or "chrome" in app_name:
            os.system("start chrome")
            resposta = "Abrindo navegador..."
        else:
            resposta = "Não sei abrir esse aplicativo."

    elif comando.startswith("pesquisar") or comando.startswith("procure"):
        termo = comando.replace("pesquisar", "").replace("procure", "").strip()
        if termo:
            try:
                resultado = wikipedia.summary(termo, sentences=2)
                resposta = resultado
            except:
                resposta = "Não encontrei resultados para esse termo."
        else:
            resposta = "Diga o que deseja pesquisar."

    elif comando in ["sair", "fechar", "encerrar"]:
        resposta = "Encerrando o assistente. Até logo!"
    else:
        resposta = "Comando não reconhecido. Digite 'menu' para ver os comandos."

    return resposta

# Rota principal
@app.route("/")
def home():
    return render_template("index.html")

# Rota para processar comando via AJAX
@app.route("/comando", methods=["POST"])
def comando():
    data = request.json
    texto = data.get("texto", "")
    resposta = executar_comando(texto)
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(debug=True)
