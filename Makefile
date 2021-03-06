.PHONY: run shell env db

DB=db.sqlite

help:
	@echo "Use \`make <target>\` with one of targets:"
	@echo "  env    create virtualenv"
	@echo "  db     initialize db"
	@echo "  run    run development server"
	@echo "  shell  start python shell"

run:
	env/bin/python manage.py runserver

shell:
	env/bin/python manage.py shell

env:
	virtualenv env
	env/bin/pip install -r requirements.txt

db: create-db populate-db

create-db:
	env/bin/python manage.py syncdb --noinput

populate-db:
	env/bin/python manage.py collectmedia --noinput
