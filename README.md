# Sphère Binaire avec Citations IA générer dynamiquement

Une visualisation 3D immersive d'une sphère binaire (0 et 1) avec des citations générées par un modèle de langage Ollama.

## 🌟 Fonctionnalités

- Sphère 3D interactive avec chiffres binaires lumineux
- Affichage de l'heure et de la date en temps réel
- Citations générées par votre modèle Ollama local
- Système anti-répétition pour les citations
- Interface visuelle élégante en noir et effets lumineux

## 📋 Prérequis

- [Ollama](https://ollama.ai/) installé et configuré
- Un modèle Ollama (par défaut: `llama3.2:1b-instruct-q8_0`)
- Python 3.7+ et pip
- Un navigateur web moderne

## 🚀 Installation

1. **Cloner ou télécharger ce dépôt**

## Installation d'un environnement virtuel Python

Étapes (Terminal/Command Prompt)
1. Créer un environnement virtuel

Windows:
## Naviguez vers le dossier de votre projet
cd chemin/vers/votre/projet
## Créer l'environnement virtuel
python -m venv venv
## Activer l'environnement virtuel
venv\Scripts\activate

Une fois activé, vous devriez voir (venv) au début de votre ligne de commande.
## Désactiver l'environnement virtuel (quand vous avez terminé)
deactivate

macOS/Linux:
## Naviguez vers le dossier de votre projet
cd chemin/vers/votre/projet
## Créer l'environnement virtuel
python3 -m venv venv
## Activer l'environnement virtuel
source venv/bin/activate
Une fois activé, vous devriez voir (venv) au début de votre ligne de commande.
## Désactiver l'environnement virtuel (quand vous avez terminé)
deactivate

2. **Installer les dépendances Python**

   ```bash
   pip install -r requirements.txt
   ```

3. **Assurez-vous qu'Ollama est installé**
   
   Suivez les instructions sur [https://ollama.ai/]

4. **Vérifiez que votre modèle Ollama est disponible**

   ```bash
   ollama list
   ```
   
   Si vous n'avez pas `llama3.2:1b-instruct-q8_0`, vous pouvez le télécharger ou utiliser un autre modèle:
   
   ```bash
   ollama pull llama3.2:1b-instruct-q8_0
   ```

## 🔧 Configuration

Avant de démarrer, vous pouvez ajuster les paramètres dans les fichiers:

### Serveur Python (quote-server.py)

- Modifiez le nom du modèle Ollama si nécessaire (ligne 15)
- Ajustez les options de génération (température, etc.)

### Interface HTML (earth-binary-sphere-with-proxy.html)

Vous pouvez modifier les paramètres de configuration dans l'objet `CONFIG` (vers la ligne 420):

```javascript
const CONFIG = {
    apiEndpoint: 'http://127.0.0.1:5000/quote', // API Python locale
    statusEndpoint: 'http://127.0.0.1:5000/status', // Vérification du statut
    checkInterval: 5000,  // Vérifier la connexion toutes les 5 secondes
    quoteInterval: 13000,  // Changer de citation toutes les 13 secondes
    maxStoredQuotes: 50,   // Nombre maximum de citations à stocker
    minQuotesToDisplay: 1, // Minimum de citations avant d'afficher
    historySize: 12,       // Citations récentes à ne pas répéter
    maxTries: 15           // Essais max pour trouver une citation non-répétée
};
```

## ▶️ Utilisation

1. **Démarrer le serveur Python en premier**

   ```bash
   python quote-server.py
   ```

   Un message confirmera que le serveur est en cours d'exécution sur `http://127.0.0.1:5000/`

2. **Ouvrir le fichier HTML dans votre navigateur**

   Ouvrez `earth-binary-sphere-with-proxy.html` dans votre navigateur web préféré.

3. **Profitez de l'expérience**

   - Le point vert en bas à droite indique que la connexion avec Ollama est établie
   - Les citations alternent entre les deux côtés de l'écran
   - La sphère binaire tourne lentement avec des chiffres qui clignotent

## 📁 Structure des fichiers

- **quote-server.py** - Serveur Python qui communique avec Ollama et expose une API REST
- **earth-binary-sphere-with-proxy.html** - Interface web avec la sphère 3D et l'affichage des citations
- **requirements.txt** - Dépendances Python nécessaires

## 🔍 Fonctionnement

1. Le serveur Python établit une connexion avec Ollama
2. L'interface web se connecte au serveur Python
3. Lorsqu'une citation est demandée, le serveur interroge Ollama
4. Ollama génère une citation inspirante
5. La citation est renvoyée à l'interface et affichée

## 🔄 Système anti-répétition

Le système garde en mémoire les 12 dernières citations affichées et évite de les montrer à nouveau tant que d'autres citations sont disponibles. Cela garantit une expérience variée, même avec un nombre limité de citations générées.

## 📱 Compatibilité

- ✅ Desktop (Chrome, Firefox, Safari, Edge)
- ✅ Mobile (versions récentes des navigateurs)
- ❌ Internet Explorer (non supporté)

## 📝 Licence

Ce projet est distribué sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## 🙏 Crédits

- Three.js pour le rendu 3D
- Ollama pour la génération de texte
- Flask et Flask-CORS pour l'API Python

---

Créé avec ❤️ par Blowdok alias BlowCoder
"# binary-sphere-ollama" 
