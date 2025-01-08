from llama_index.llms.openai import OpenAI
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import VectorStoreIndex
import llama_index
import os
from dotenv import load_dotenv

load_dotenv()

def main(url: str)->None:
    document=SimpleWebPageReader(html_to_text=True).load_data(urls=[url])
    
    