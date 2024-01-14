import os
from llama_index import StorageContext, load_index_from_storage
from dotenv import load_dotenv
from llama_index import VectorStoreIndex, SimpleDirectoryReader

load_dotenv()


os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
LIBRARY_DIRECTORY = os.getenv('LIBRARY_DIRECTORY')


documents = SimpleDirectoryReader(LIBRARY_DIRECTORY).load_data()
index = VectorStoreIndex.from_documents(documents)

index.storage_context.persist()

# rebuild storage context
# storage_context = StorageContext.from_defaults(persist_dir="./storage")
# load index
# index = load_index_from_storage(storage_context)

# query_engine = index.as_query_engine()
# query_engine.query("YOUR_QUESTION")
