# Hacker News Generator

```shell
# Fetch data
bq query --format csv --use_legacy_sql=false 'SELECT title FROM `bigquery-public-data.hacker_news.stories` where score > 100' > hn_title.csv
```

```shell
# Dev locally
pip install -r requirements.txt
./venv/bin/functions-framework --target title_bot --debug
```

```shell
# Deploy
gcloud run deploy --allow-unauthenticated --source=.
```
