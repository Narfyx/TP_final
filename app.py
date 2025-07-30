from flask import Flask, jsonify, request
from prometheus_flask_exporter import PrometheusMetrics
import time
import random
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Métriques statiques par défaut (requêtes, latence, etc.)
metrics.info('app_info', 'Application info', version='1.0.0')

@app.route('/')
def index():
    """Route principale de l'application."""
    logger.info("Requête reçue sur la route /")
    return jsonify({"message": "Bienvenue sur l'API !"})

@app.route('/slow')
def slow_request():
    """Route simulant un traitement lent."""
    wait_time = random.uniform(0.5, 1.5)
    logger.info(f"Requête lente sur /slow. Temps d'attente : {wait_time:.2f}s")
    time.sleep(wait_time)
    return jsonify({"message": f"Réponse après {wait_time:.2f} secondes."})

@app.route('/error')
def error_request():
    """Route qui génère systématiquement une erreur 500."""
    logger.error("Génération d'une erreur 500 sur la route /error")
    # Simule une division par zéro pour provoquer une exception
    try:
        result = 1 / 0
    except Exception as e:
        return jsonify({"error": "Une erreur interne est survenue.", "details": str(e)}), 500

if __name__ == '__main__':
    # L'application est lancée par un serveur de production comme Gunicorn dans le Dockerfile
    # Cette partie est utile pour le développement local sans Docker
    app.run(host='0.0.0.0', port=5000)
