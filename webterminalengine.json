function authIA() {
  const pwd = document.getElementById("password").value;
  if (pwd === "1776") {
    document.getElementById("auth").style.display = "none";
    document.getElementById("cli").style.display = "block";
    document.getElementById("output").textContent = "✅ Accès IA22 autorisé";
  } else {
    document.getElementById("output").textContent = "❌ Mot de passe invalide";
  }
}

function listFiles() {
  fetch("terminal_state.json")
    .then(r => r.json())
    .then(data => {
      const files = data.files || ["(aucun fichier)"];
      document.getElementById("output").textContent = files.map(f => "📄 " + f).join("\n");
    });
}

function systemInfo() {
  fetch("terminal_state.json")
    .then(r => r.json())
    .then(data => {
      let info = `🧠 Système IA22 :\n`;
      info += `Utilisateur : ${data.user}\n`;
      info += `Répertoire : ${data.cwd}`;
      document.getElementById("output").textContent = info;
    });
}

function runCommand() {
  const cmd = prompt("Commande à exécuter:");
  document.getElementById("output").textContent = `⏳ Simulé : ${cmd}`;
}

function exportJSON() {
  fetch("terminal_state.json")
    .then(r => r.json())
    .then(data => {
      document.getElementById("output").textContent = JSON.stringify(data, null, 2);
    });
}
