from elasticsearch import Elasticsearch

es = Elasticsearch(["http://localhost:9200"])

data = [
    {"brand": "Fender", "model": "Stratocaster", "price": 1200, "stock": 10, "tags": ["electric", "guitar"]},
    {"brand": "Gibson", "model": "Les Paul", "price": 2500, "stock": 5, "tags": ["electric", "guitar"]},
    {"brand": "Yamaha", "model": "FG800", "price": 500, "stock": 15, "tags": ["acoustic", "guitar"]},
]

for i, item in enumerate(data):
    es.index(index="guitar_shop", id=i, body=item)

print("Data inserted successfully!")
