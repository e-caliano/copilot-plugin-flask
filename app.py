from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    return "<h2>✅ Il server Flask è attivo!</h2>"


@app.route("/analyze-text", methods=["POST"])
def analyze_text():
    data = request.json

    # Controllo input
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field in JSON body"}), 400

    input_text = data["text"]

    # Logica simulata del plugin (puoi sostituire con qualsiasi logica Python)
    response = {
        "original_text": input_text,
        "word_count": len(input_text.split()),
        "uppercase_version": input_text.upper(),
        "security_analysis": "Nessuna minaccia rilevata"  # Simulazione
    }

    return jsonify(response)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

    
