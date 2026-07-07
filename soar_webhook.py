import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

TOKEN = "8698633984:AAFX-Hlbxo73j9ZbsM9lECjFxdx3YyWAl08"
CHAT_ID = "7193967281"

@app.route('/alerta', methods=['GET', 'POST'])
def handle_alert():
    data = request.json
    print(f"Dados recebidos: {data}")
    
    if not data:
        return jsonify({"erro": "Nenhum dado JSON recebido"}), 400

    file_name = data.get('file', 'Desconhecido')
    severity = data.get('severity', 'Info')
    msg = data.get('message', 'Sem detalhes')

    text = (f"🚨 *Alerta de Segurança THOR*\n\n"
            f"Arquivo: `{file_name}`\n"
            f"Classificação: {severity}\n"
            f"Detalhes: {msg}")

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    
    try:
        response = requests.post(url, json=payload)
        print(f"DEBUG: Resposta do Telegram: {response.text}")
        
        if response.status_code == 200:
            return jsonify({"status": "sucesso"}), 200
        else:
            return jsonify({"status": "erro", "telegram_msg": response.text}), 500
    except Exception as e:
        return jsonify({"status": "erro", "detalhe": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
