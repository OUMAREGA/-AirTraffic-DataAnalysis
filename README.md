# Air traffic data analysis

### Contexte
L'Aéroport de Paris (ADP) fait en effet face à un trafic aérien en constante augmentation annuellement.
MAIS en parallèle à un nombre croissant de dysfonctionnements : 

* retards
* annulation de vols
* passagers qui passent la nuit à l’aéroport etc

et à d'éventuels autres problèmes à découvrir lors de votre fouille dans la DB

Votre rôle est de donner le maximum d’éléments (reporting à partir des données du passé) pour prédire les problèmes et ainsi mieux se préparer (analyse prédictive).
L’objectif est d’aider votre manager à la prise de décision.· Votre rôle est de donner le maximum d’éléments (reporting à partir des données du passé) pour prédire les problèmes et ainsi mieux se préparer (analyse prédictive). L’objectif est d’aider votre manager à la prise de décision.

### Version

```
python --version
python -m pip --version
```

### Récupérez le projet

    git clone git@github.com:OUMAREGA/AirTrafficDataAnalysis.git
    cd AirTrafficDataAnalysis
    
### Les fichiers csv

<a href="https://onedrive.live.com/?authkey=%21ALM9Iew1PvlBqvM&id=6C6D756296D4662%21772304&cid=06C6D756296D4662" >Pour télécharger les fichiers CSV</a>   

Après téléchargement, veuillez les mettre dans le dossier **csv_data**.


### Configurer le virtual env si nécessaire
    
    python3 -m venv ./venv
    .\venv\Scripts\Activate.ps1 (Si vous êtes sur powershell)
    .\venv\Scripts\Activate.bat (Sur tout autre shell windows)
    source ./venv/bin/activate (Linux/Mac)
    pip install ipython (Installe une coloration syntaxique dans l'environnement) 
    
### Démarrer la base de données

    docker-compose up

### Joindre la base de données à PyMySQL

Il est nécessaire à ce que PyMySQL puisse contacter la base de données, 
que ça soit pour l'importation des fichiers ou l'exécution des requêtes.

**Pour ce faire :**
- Copier le fichier .env.dist en **.env**
- Remplir chaque variable de la manière suivante :
```env
DB_HOST=localhost
DB_PORT=30000
DB_NAME=avions
DB_USER=root
DB_PWD=root
```
### Installez les dépendances
[pip](https://pypi.python.org/pypi/pip) est le gestionnaire de dépendances qui
va nous permettre d'installer tout ce qui est nécessaire à ce projet. Vous
pouvez évidemment travailler dans un [virtualenv](https://virtualenv.pypa.io/en/stable/)
dédié à la formation. Si vous utilisez un IDE tel que PyCharm, vous pouvez
l'utiliser pour créer ce virtualenv. Placez vous alors à la racine du projet et
saisissez

```
pip install -r requirements.txt
```
ou

```
python -m pip install -r requirements.txt
```

Votre environnement contient alors toutes les dépendances nécessaires. 

### Front-End : ReactJS

```
cd /src
npm install
```

### Flask

```
python	app.py
```

ou

```
flask run
```

### Importation des données CSV

```
python import.py
```

### Jupyter Notebooks

Dans un terminal à partir du répertoire racine du projet, exécutez la commande

```
jupyter notebook
```
ou
```
python -m jupyter notebook
```