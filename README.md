# python-web-bottle-api-postgres-raw-sql-pop

## Description
Simple web app that serves an api
for a bottle project.

Uses sqlalchemy query a table `pop` using raw sql.

Remotely tested with *testify*.

## Tech stack
- python
  - bottle
  - sqlalchemy
  - testify
  - response
- postgres

## Docker stack
- python:latest
- postgres:alpine

## To run
`sudo ./install.sh -u`
- Get all pops: http://localhost/pop
  - Schema id, name, and color
- CRUD opperations
  - Create: curl -i -X PUT localhost/pop/<id>
  - Read: http://localhost/pop/<id>
  - Update: curl -i -X POST localhost/pop/<id>/<name>/<color>
  - Delete: curl -i -X DELETE localhost/pop/<id>

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credit
[Bottle sqlalchemy setup](https://github.com/iurisilvio/bottle-sqlalchemy/blob/master/examples/basic.py)
