# COM S 579 RAG

## About

This RAG (Retrieval-Augmented Generation) project uses the LlamaIndex pipeline paired
with [Pinecone](https://www.pinecone.io/) as a vector database. The frontend is built
using [Gradio](https://www.gradio.app/). The pipeline, vector DB, and UI library were all randomly assigned to students.
This project is written entirely in Python.

## Set Up Project

These instructions assume you already have python 3 and pip installed, and know how to use them.

1. Clone or download this repository.
2. Set up a python venv and make sure you are using it (not required, but can help prevent issues later).
3. Install the required packages by running the following command in the root directory of the project:

```
pip3 install -r requirements.txt
```

4. Set up a Pinecone account and create a new index.

    1. Set the name to whatever you want - just take note of it for later.
    2. Under "Configure your Index", click "Setup by model" and select "text-embedding-ada-002", then "Set
       Configuration".
    3. Under "Capacity Mode", select "Serverless". Select a provider and environment that works best for you.
    4. Click "Create Index" in the bottom right corner.
    5. Click "Connect" in the top right corner and un-hide the API key by clicking the eye icon. Take note of this key.

5. Set up an OpenAI account and create a new API key with "All" permissions. Take note of this key.
6. Modify `env_template.py` and fill in your two API keys and index name from above. Rename this file to `env.py`.

The project should then be ready to run.

Here is a video demonstration of this process:

https://github.com/jeremynoesen/ComS579/assets/46114593/8bca86ad-3f2c-477b-991a-1d1ebd3fd474

## Upload To Pinecone

To upload data to the Pinecone index, you will need a PDF file with the data you would like to include. You can then run
the following command, replacing `<file.pdf>` with the path to the file you would like to upload:

```
python3 upload.py <file.pdf>
```

Here is a video demonstration of this process:

https://github.com/jeremynoesen/ComS579/assets/46114593/ae5867c1-07e8-4c2e-ac4e-2d7984aa9c5e
