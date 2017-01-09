# sass-app


## running tests
`docker-compose exec website py.test snakeeyes/tests`

## running tests with coverage
`docker-compose exec website py.test --cov-report term-missing --cov snakeeyes`

## running static analysis tool
`docker-compose exec website flake8 . --exclude __init__.py`