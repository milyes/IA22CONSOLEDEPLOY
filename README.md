# 🧬 IA22CONSOLEDEPLOY

**Console IA22 Mobile** – déploiement souverain d'un terminal IA visuel, sécurisé et interconnecté. Ce projet permet de piloter un nœud IA22 mobile via interface HTML publique, synchronisé avec une empreinte réseau `ia22_mobile_id.json`.

---

## 🔍 Aperçu

Accédez à la console ici 👉 [https://milyes.github.io/IA22CONSOLEDEPLOY/](https://milyes.github.io/IA22CONSOLEDEPLOY/)

- 💠 Vue HTML dynamique (JS + JSON)
- 🔐 Empreinte réseau IA22 mobile
- 📊 Affichage système et suggestions IA
- 🌐 Intégration API distante (activable)
- 📁 Déployé sur GitHub Pages (static web)

---

## 🚀 Fonctionnalités

| Module               | Description                                         |
|----------------------|-----------------------------------------------------|
| `index.html`         | Interface cockpit IA visuelle                       |
| `ia22_mobile_id.json`| Identité technique du nœud mobile IA22              |
| `ia22_server.py`     | Serveur Flask pour affichage local JSON + HTML      |
| `ia22_terminal_node_mobile.py` | Script Python IA pour Android / Termux         |
| `README.md`          | Documentation du projet IA22                        |

---

## 📦 Installation locale

```bash
git clone https://github.com/milyes/IA22CONSOLEDEPLOY.git
cd IA22CONSOLEDEPLOY
pip install flask
python ia22_server.py
# Accéder à http://localhost:8080# IA22CONSOLEDEPLOY
