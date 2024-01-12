import os
from llama_index import StorageContext, load_index_from_storage
from dotenv import load_dotenv

load_dotenv()


os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("sample").load_data()
index = VectorStoreIndex.from_documents(documents)

index.storage_context.persist()

# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="./storage")
# load index
index = load_index_from_storage(storage_context)
