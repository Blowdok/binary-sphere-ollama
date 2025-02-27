from flask import Flask, jsonify
from flask_cors import CORS
import ollama
import time

app = Flask(__name__)
CORS(app)  # Permet les requêtes cross-origin (CORS)

@app.route('/quote')
def get_quote():
    """Génère une citation inspirante en utilisant Ollama"""
    try:
        # Utilise la fonction generate d'Ollama pour créer une citation
        response = ollama.generate(
            model='llama3.2:1b-instruct-q8_0',  # Remplacez par votre modèle
            prompt="Génère une citation inspirante sur la technologie, le code ou l'IA en une seule phrase courte mais profonde. Ne signe pas la citation.",
            options={
                'temperature': 0.7,
                'top_p': 0.9,
                'max_tokens': 30,
            }
        )
        
        # Extraire le texte de la réponse et le nettoyer
        quote_text = response['response'].strip()
        # Supprimer les guillemets s'ils sont présents
        quote_text = quote_text.replace('"', '').replace("'", '')
        # S'assurer que la citation se termine par un point
        if not quote_text.endswith('.') and not quote_text.endswith('!') and not quote_text.endswith('?'):
            quote_text += '.'
            
        return jsonify({
            'text': quote_text,
            'attribution': 'Blowdok',
            'timestamp': time.time()
        })
        
    except Exception as e:
        print(f"Erreur lors de la génération de citation: {e}")
        # La citation de secours utilisée uniquement en cas d'erreur avec Ollama
        return jsonify({
            'text': "Erreur de connexion avec le modèle IA. Veuillez vérifier que Ollama est bien lancé.",
            'attribution': 'Système',
            'error': True,
            'timestamp': time.time()
        }), 500

# Route pour vérifier si le serveur est en ligne
@app.route('/status')
def status():
    return jsonify({'status': 'online'})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)