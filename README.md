
 #  API DJANGO 

 API DJANGO est une API contenant plusieurs endpoints pour gérer la détermination des années bissextiles et la gestion de l'historique des appels. 

### Versions utilisées

- Python : 3.10.12
- Django : 3.2.5
  
## Installation
Pour installer l’API depuis GITHUB il faut utiliser pip avec  ``` pip install git+https://github.com/Mariecls/API-Django.git ```

Créez un environnement virtuel pour isoler les dépendances du projet avec la commande : ``` python -m venv venv  ```

Pour activer l’environnement virtuel sur Ubuntu il faut utiliser :  ``` source venv/bin/activate  ```

Utiliser pip pour installer toutes les dépendances du projet à partir du fichier requirements.txt : ```pip install -r requirements.txt ```

## Usage


### Technologies utilisées

- Framework Django
- Langage Python

#### Versions utilisées

- Python : 3.10.12
- Django : 3.2.5

###   Lancer l'API :

```bash
python manage.py runserver
```

### Premier endpoint :

**URL :** `/is_leap_year/{year}/`  
**Méthode HTTP :** POST  
**Paramètres :**  
- `{year}` : L'année à vérifier (entier)  

**Réponse :**  
- `true` : Si l'année est bissextile  
- `false` : Si l'année n'est pas bissextile  

**Exemple de réponse JSON :**  
```json
{
    "year": 2024,
    "is_leap_year": true
}

```
### Deuxième endpoint :

**URL :** `/leap_years_in_range/{start_year}/{end_year}/`  
**Méthode HTTP :** POST  
**Paramètres :**  
- `{start_year}` : Année de début de la plage (entier)  
- `{end_year}` : Année de fin de la plage (entier)  

**Réponse :**  

- `Exemple de réponse JSON :`  

```json
{
    "leap_years": [2020, 2024, 2028]
}
```
### Troisième endpoint :

**URL :** `/history/`  
**Méthode HTTP :** POST  

**Réponse :**  

- `Exemple de réponse JSON :`  

```json
{
    "history": [
        {
            "endpoint": "is_leap_year",
            "input": {"year": 2024},
            "output": true,
            "timestamp": "2024-03-07 12:30:45 UTC"
        },
        {
            "endpoint": "leap_years_in_range",
            "input": {"start_year": 2020, "end_year": 2030},
            "output": [2020, 2024, 2028],
            "timestamp": "2024-03-07 12:35:22 UTC"
        }
    ]
}


