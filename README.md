# definition

FastAPI est un framework web Python moderne, rapide et performant, spécialement conçu pour créer des API RESTful de manière simple et intuitive. 

Il se distingue par :
	- Rapidité: Basé sur Starlette, il offre des performances comparables à celles de Node.js et Go.
	- Typage statique: Utilise les annotations de type de Python pour une validation automatique des données et une meilleure lisibilité du code.
	- Asynchrone: Prend en charge les opérations asynchrones pour gérer efficacement les requêtes concurrentes.
	- Documentation interactive: Génère automatiquement une documentation interactive de votre API, basée sur OpenAPI (Swagger).
	- Facile à apprendre: La syntaxe est concise et proche de la syntaxe Python naturelle.

N.B : le point fort du FrameWork FastAPI est le faite qu'il est asynchrone (multi-tâches) qui se base sur Starlette de ASGI.

# pip install
pip install fastapi uvicorn pydantic


# dépôt

echo "# FastAPI" >> README.md
git init
git add .
git commit -m "first commit of FastAPI project"
git remote add origin https://github.com/GenyCom/FastAPI.git
git push -u origin master

# run
uvicorn main:app --reload

http://127.0.0.1:8000/tasks
