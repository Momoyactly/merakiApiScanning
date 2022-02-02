# Meraki Scanning API
## Intro

## Docker Build
for **ARM** use image **python:slim-buster**
## Docker Run
## Unittesting
## Warning Meraki Api Scanning wrong config
![Config in meraki dashboard](images/exampleConfigMeraki.png)

# Grafana-Postgres Integration
``` sql
SELECT * FROM pg_catalog.pg_tables
WHERE schemaname != 'information_schema' AND
schemaname != 'pg_catalog';
```
### TO DO
- Update README
- Include the db as a datasoruce in Grafana container
- Automatize the cert creation & renewal (including the certbot in the image of ngnix)
- Try changing the db from postgres to mongo, for better performance 
- Add dashbords in grafana as an data analysis example
- Create views in D3 