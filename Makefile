run-db:
	docker run --name fastapi_alembic -p 5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=alembic -v ${PWD}/db_data:/var/lib/postgresql/data -d postgres
	