from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/alerta', methods=['POST'])
def alerta():
    # Executa o script diretamente sem tentar ler ou validar o JSON do Grafana
    subprocess.run(["/home/juliano/projeto_observabilidade/alerta_telegram.sh"])
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
