# Titre du projet : "Déploiement et Supervision d’une Application Web Répartie avec Alerting Automatisé"
Projet Final – Supervision d’une Infrastructure Répartie
Objectifs pédagogiques :
- ​ Mettre en œuvre des outils de supervision (Prometheus, Grafana, ELK, etc.)
-  Superviser une application répartie (multi-services / conteneurs)
-  Mettre en place un système d’alerting efficace
- Automatiser la supervision via des scripts ou des playbooks (Ansible, Terraform, etc.)
- S’intégrer dans une démarche DevOps (CI/CD, monitoring, logs, performances)

Contexte :
Vous êtes une équipe DevOps en charge de l’exploitation d’une application web distribuée composée de plusieurs microservices conteneurisés (par exemple : un front-end, une API, une base de données, un service de cache).

Votre mission est de :
- Déployer l’infrastructure avec des outils d’Infrastructure as Code (Docker Compose,
	Kubernetes, Terraform selon niveau).
- Mettre en place la supervision de cette application avec des outils open source.
- Configurer des dashboards visuels (Grafana, Kibana) pour la métrologie et les logs.
- Définir des règles d’alerting pertinentes (par e-mail, Slack, etc.)
- Réaliser un rapport d’exploitation et un plan de remédiation.

🧩 Livrables attendus :	
	📁 Documentation complète du système supervisé (schéma d’architecture + description)
	📊 Dashboards (Grafana, Kibana) opérationnels
	📦 Scripts de déploiement (Ansible, Docker Compose, ou Helm Charts)
	🔔 Alerting fonctionnel (ex : alerte CPU > 80%, base de données indisponible, etc.)
	🎥 Démo enregistrée ou live (facultatif)

📄 Rapport final : retour d’expérience, points d’amélioration, incidents simulés
Technologies proposées (modifiable selon niveau) :
- Infrastructure : Docker / Kubernetes (Minikube, K3s), Ansible, Terraform
- Monitoring : Prometheus, Grafana
- Alerting : Alertmanager, mail, Slack webhook
- CI/CD (facultatif) : GitHub Actions / GitLab CI

Exemples de cas d’usage à superviser :
- API trop lente (temps de réponse > 1s)​
- Taux d’erreur HTTP 5xx​
- Mémoire consommée par le container > 500MB​
- Requêtes SQL trop lentes ou base indisponible​
- Conteneur down / redémarré automatiquement
