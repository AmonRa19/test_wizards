Data pipeline:
zips.json (http://media.mongodb.org/zips.json)
data.json -> (import) -> mongodb
mongodb -> (flask) -> HTTP
HTTP -> (d3.js) -> chart
