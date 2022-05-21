
## Tech Stack
- Python
- Django
- Flask
- Docker
- Redis
- MySQL
- PostgreSQL


## Installation
### Catalog Service
```bash
$ cd catalog
$ docker-compose build
$ docker-compose up
```
```bash
# new terminal
$ docker-compose exec backend sh
# in docker container bash
$ python manager.py db init
$ python manager.py db migrate
$ python manager.py db upgrade
$ python database_init.py
$ exit
```
-----------------
### Content Service
```bash
$ cd content
$ docker-compose build
$ docker-compose up
```
```bash
# new terminal
$ docker-compose exec backend sh
# in docker container bash
$ python manage.py makemigrations
$ python manage.py migrate
```
### Endpoints
- Catalog
  - List 
    * http://localhost:8001/catalog/list

- Content
  - List 
    * (GET) http://localhost:8000/api/contents
  - Create 
    * (POST) http://localhost:8000/api/contents
      
      * Body Params: {
       "name":"Name",
       "description":"Descrip",
       "catalog_id":1
}


  - Delete
    * (DELETE) http://localhost:8000/api/contents/<string:id> 
  - Update
    * (PUT) http://localhost:8000/api/contents/<string:id>

### Tests
  
```bash
$ cd content
$ docker-compose up
$ docker-compose exec backend sh
$ python manage.py test
```