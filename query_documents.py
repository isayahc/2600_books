import argparse
import os
from llama_index import StorageContext, load_index_from_storage
from dotenv import load_dotenv
from llama_index import VectorStoreIndex, SimpleDirectoryReader

def query_data(query: str):
    """Query to a vector database
    
    ## argument
    Return: return_description
    """
    
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    # load index
    index = load_index_from_storage(storage_context)

    query_engine = index.as_query_engine()
    user_query = query_engine.query(query)
    user_query = user_query.response
    print(user_query)
    return user_query
    # x = 0

def main():
    parser = argparse.ArgumentParser(description='Query a vector database.')
    parser.add_argument('query', type=str, help='Query to be executed')

    args = parser.parse_args()
    query_data(args.query)

if __name__ == "__main__":
    main()
