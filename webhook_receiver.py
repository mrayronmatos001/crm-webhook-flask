from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print("Webhook recebido:", request.json)
    return '', 204

if __name__ == '__main__':
    app.run(port=5001)
