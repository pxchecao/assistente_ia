function enviarComando() {
    const input = document.getElementById("inputComando");
    const chat = document.getElementById("chat");
    const texto = input.value.trim();
    if (!texto) return;

    // Adiciona a mensagem do usuário
    chat.innerHTML += `<p><strong>Você:</strong> ${texto}</p>`;
    input.value = "";

    // Scroll automático para baixo (antes da resposta para evitar "pular")
    chat.scrollTop = chat.scrollHeight;

    fetch("/comando", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ texto })
    })
    .then(res => {
        if (!res.ok) throw new Error("Erro na resposta do servidor");
        return res.json();
    })
    .then(data => {
        chat.innerHTML += `<p><strong>Assistente:</strong> ${data.resposta}</p>`;
        chat.scrollTop = chat.scrollHeight; // Scroll no final após adicionar resposta
    })
    .catch(err => {
        chat.innerHTML += `<p style="color: red;"><strong>Erro:</strong> Não foi possível obter resposta.</p>`;
        chat.scrollTop = chat.scrollHeight;
        console.error(err);
    });
}

// Permite enviar com Enter
document.getElementById("inputComando").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        e.preventDefault(); // Previne envio de formulário se tiver form
        enviarComando();
    }
});
