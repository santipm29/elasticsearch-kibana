# Kibana and Elasticsearch with docker-compose

```console
docker-compose up
```
## open kibana 
http://localhost:5601/app/kibana

## create index
method http put --> http://localhost:9200/indexname
```javascript
{
    "settings" : {
        "index" : {
            "number_of_shards" : 1, 
            "number_of_replicas" : 1 
        }
    }
}
```
