from llama_index.llms import OpenAI
from llama_index.readers import SimpleWebPageReader
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import VectorStoreIndex
import os
from dotenv import load_dotenv
load_dotenv()

def main(doc: str) -> None:
    documents = SimpleDirectoryReader(url).load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    response  = query_engine.query("What is CNN?")
    print(response)

if __name__ == "__main__":
    main(doc="C:\Users\Subhranil\Desktop\llamaindex\data")
