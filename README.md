# api-with-fastAPI
Squelette d'API avec FastAPI et documentation OpenAPI

Cette api est basée sur [FastAPI](https://fastapi.tiangolo.com/), [pyODBC](https://github.com/mkleehammer/pyodbc).

URL Description :

- '/documentation/docs' : The OpenAPI UI
- '/documentation/redoc' : The ReDOC UI

# Commencer

Copier la table **QIWS/QCUSTCDT** dans votre bibliothèque.

Exécuter le projet
```
uvicorn main:app --host 0.0.0.0 --reload
```

Par défaut, le port 8000 est utilisé.