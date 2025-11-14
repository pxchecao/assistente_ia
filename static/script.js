function addMessage(author, text, error = false) {
    const chat = document.getElementById("chat");
    const msg = document.createElement("p");

    if (error) msg.style.color = "red";

    const strong = document.createElement("strong");
    strong.textContent = author + ": ";
    msg.appendChild(strong);

    const span = document.createElement("span");
    span.textContent = text;
    msg.appendChild(span);

    chat.appendChild(msg);
    chat.scrollTop = chat.scrollHeight;
}

function enviarComando() {
    const input = document.getElementById("inputComando");
    const texto = input.value.trim();
    if (!texto) return;

    addMessage("Você", texto);
    input.value = "";

    fetch("/comando", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ texto })
    })
    .then(res => {
        if (!res.ok) throw new Error("Erro ao se comunicar com servidor");
        return res.json();
    })
    .then(data => {
        addMessage("Assistente", data.resposta);
    })
    .catch(err => {
        addMessage("Erro", "Não foi possível obter resposta.", true);
        console.error(err);
    });
}

document.getElementById("inputComando").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        e.preventDefault();
        enviarComando();
    }
});
