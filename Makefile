.PHONY: install migrate localrun productionrun
	
install:
	pip install --upgrade setuptools pip
	pip install -r requirements.txt

migrate:
	python djangosrc/manage.py makemigrations --settings=djangostarter.local
	python djangosrc/manage.py migrate --settings=djangostarter.local

collectstatic:
	python djangosrc/manage.py collectstatic --settings=djangostarter.local

localrun:
	python djangosrc/manage.py runserver 0.0.0.0:8080 --settings=djangostarter.local

productionrun:
	python djangosrc/manage.py runserver 0.0.0.0:8080 --settings=djangostarter.production
