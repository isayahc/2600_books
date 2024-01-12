import os
from llama_index import StorageContext, load_index_from_storage
from dotenv import load_dotenv
from llama_index import VectorStoreIndex, SimpleDirectoryReader



def query_data(query:str):
    """Query to a vector database
    
    ## argument
    Return: return_description
    """
    
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    # load index
    index = load_index_from_storage(storage_context)

    query_engine = index.as_query_engine()
    query_engine.query(query)