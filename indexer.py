from elasticsearch import Elasticsearch, helpers
import json

es = Elasticsearch(["http://localhost:9200"])

def bulk_index(docs, index_name="search_index"):
    actions = [
        { "_index": index_name, "_source": doc }
        for doc in docs
    ]
    helpers.bulk(es, actions)
    print(f"Indexed {len(docs)} documents into {index_name}")

if __name__ == "__main__":
    bulk_index([{"title": "DevOps Handbook", "category": "Tech"}])
