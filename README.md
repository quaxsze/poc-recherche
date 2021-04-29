# PoC Recherche

## Usage

### Development

Launch backend:

```
python3 -m venv pyenv
. pyenv/bin/activate
cd backend
flask init-db
FLASK_ENV=development FLASK_APP=app flask run
```

Launch frontend:

```
cd frontend
yarn
yarn serve
```

The frontend is available on http://localhost:8080 and uses the API available at http://localhost:5000.
