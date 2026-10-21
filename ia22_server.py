from flask import Flask, render_template_string, jsonify
import json

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>IA22 Terminal Mobile</title>
  <style>
    body { background-color:#0d1117; color:#c9d1d9; font-family:monospace; padding:20px; }
    .panel { border:1px solid #30363d; padding:10px; margin-bottom:20px; background:#161b22; }
    h1, h2 { color:#58a6ff; }
    .tag { color:#10b981; }
    .alert { color:#f43f5e; }
  </style>
</head>
<body>
  <h1>🧬 IA22 TERMINAL MOBILE</h1>

  {% if data %}
  <div class="panel">
    <h2>📄 Empreinte système IA22</h2>
    <p><span class="tag">Appareil:</span> {{ data.device }}</p>
    <p><span class="tag">IP Publique:</span> {{ data.ip_public }}</p>
    <p><span class="tag">Utilisateur:</span> {{ data.owner }}</p>
    <p><span class="tag">Module:</span> {{ data.module }}</p>
    <p><span class="tag">Horodatage:</span> {{ data.timestamp }}</p>
    <p><span class="tag">Signature IA:</span> {{ data.signature }}</p>
  </div>
  {% else %}
  <div class="panel"><p>Aucune donnée IA22 disponible</p></div>
  {% endif %}

  <div class="panel">
    <h2>💡 Suggestion IA</h2>
    <p><em>> Synchroniser ce terminal avec cockpit principal IA22</em></p>
  </div>
</body>
</html>
"""

@app.route("/")
def index():
    try:
        with open("ia22_mobile_id.json") as f:
            data = json.load(f)
    except:
        data = None
    return render_template_string(HTML_TEMPLATE, data=data)

@app.route("/json")
def raw_json():
    with open("ia22_mobile_id.json") as f:
        return jsonify(json.load(f))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
