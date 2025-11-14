import google.generativeai as genai

genai.configure(api_key="AIzaSyBmMsZBG0J5u6Ej5OxFyLkNNUpkZEUVNCA")

model = genai.GenerativeModel("gemini-2.0-flash")

print("\n🤖 Alexo iniciado!\n")

while True:
    pergunta = input("Você: ")

    if pergunta.lower() in ["sair", "exit", "quit"]:
        break

    try:
        resposta = model.generate_content(pergunta)
        print("IA:", resposta.text)

    except Exception as erro:
        print("⚠️ ERRO:", erro)
