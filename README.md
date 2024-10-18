## Running Locally
```
poetry run uvicorn journal_bot:app --reload
```

## Migrations
Generate migration file:
```
poetry run alembic revision --autogenerate -m "migration message"
```
Edit the migration file as appropriate.

Apply the migration:
```
poetry run alembic upgrade head
```