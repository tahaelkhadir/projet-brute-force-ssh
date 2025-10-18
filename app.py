from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'projet_brute_force_ssh_2025'

@app.route('/bruteforce')
def bruteforce():
   
    return render_template('bruteforce.html')

@app.route('/exercices')
def exercices():
    return render_template('exercices.html')

@app.route('/sources')
def sources():
    return render_template('sources.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom = request.form.get('nom')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Afficher dans la console
        print(f"\n{'='*50}")
        print(f"NOUVEAU MESSAGE REÇU")
        print(f"{'='*50}")
        print(f"Nom: {nom}")
        print(f"Email: {email}")
        print(f"Message: {message}")
        print(f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"{'='*50}\n")
        
        # Retourner la page avec message de succès
        return render_template('contact.html', success=True)
    
    return render_template('contact.html')

# Gestionnaire d'erreur 404
@app.errorhandler(404)
def page_not_found(e):
    """Rediriger vers la page principale en cas d'erreur 404"""
    return render_template('bruteforce.html'), 404

if __name__ == '__main__':
    print("\n" + "="*70)
    print("🔒 PROJET BRUTE FORCE SSH - SERVEUR DÉMARRÉ")
    print("="*70)
    print("📡 URL: http://localhost:5000")
    print("🌐 Pages disponibles :")
    print("   - http://localhost:5000/bruteforce  (Page principale)")
    print("   - http://localhost:5000/exercices   (5 exercices)")
    print("   - http://localhost:5000/sources     (Ressources)")
    print("   - http://localhost:5000/contact     (Notre équipe)")
    print("="*70)
    print("⚡ Appuyez sur CTRL+C pour arrêter le serveur")
    print("="*70 + "\n")
    
    # Lancer le serveur Flask
    app.run(debug=True, host='0.0.0.0', port=5000)