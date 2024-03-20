"""
This module is used to upload data to Pinecone for indexing. The code was written based on this tutorial:
https://github.com/pinecone-io/examples/blob/master/learn/generation/llama-index/using-llamaindex-with-pinecone.ipynb
"""

import re
import sys
import env
from pathlib import Path
from llama_index.readers import PDFReader
from llama_index.node_parser import SemanticSplitterNodeParser
from llama_index.embeddings import OpenAIEmbedding
from llama_index.ingestion import IngestionPipeline
from pinecone.grpc import PineconeGRPC
from llama_index.vector_stores import PineconeVectorStore

# Args parsing
if len(sys.argv) != 2:
    print("Usage: python upload.py <file_path>")
    sys.exit(1)
if not Path(sys.argv[1]).exists():
    print(f"File {sys.argv[1]} does not exist")
    sys.exit(1)

# model used for node parsing and vectorization
embed_model = OpenAIEmbedding(api_key=env.OPENAI_API_KEY)

# Initialize Pinecone
pc = PineconeGRPC(api_key=env.PINECONE_API_KEY)
pinecone_index = pc.Index(env.INDEX_NAME)
vector_store = PineconeVectorStore(pinecone_index=pinecone_index)

# Define pipeline
pipeline = IngestionPipeline(
    transformations=[
        SemanticSplitterNodeParser(
            buffer_size=1,
            breakpoint_percentile_threshold=95,
            embed_model=embed_model,
        ),
        embed_model,
    ],
    vector_store=vector_store
)

# Load the PDF file
documents = PDFReader().load_data(file=Path(sys.argv[1]))

# Clean the text data
for doc in documents:

    # Fix hyphenated words broken by newline
    doc.text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', doc.text)

    # Fix improperly spaced hyphenated words and normalize whitespace
    doc.text = re.sub(r'(\w)\s*-\s*(\w)', r'\1-\2', doc.text)
    doc.text = re.sub(r'\s+', ' ', doc.text)

# Run the pipeline
pipeline.run(documents=documents)
