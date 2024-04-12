__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer


# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv('neural_network_patent_query.csv')
    st.write('Data loaded')
    return preprocess_data(df)

# Preprocess the data
def preprocess_data(df):
    # Preprocess the data
    dfs = df.sort_values(by='patent_number', ascending=True)
    dfs.set_index('patent_number', inplace=True)
    desired_columns = ['patent_title', 'patent_abstract', 'patent_date']
    dfs = dfs[desired_columns]
    dfs.loc[:, 'patent_title'] = dfs['patent_title'].str.lower()
    dfs.loc[:, 'patent_abstract'] = dfs['patent_abstract'].str.lower()
    dfs['text'] = "The title of the patent is " + dfs['patent_title'] + ' and its abstract is ' + dfs['patent_abstract'] + ' dated ' + dfs['patent_date']
    docs = dfs['text'].tolist()
    ids = [str(x) for x in dfs.index.tolist()]
    st.write('Data Preprocessed')
    return docs, ids

# Initialize the Chroma client and collection
@st.cache_resource
def initialize_chroma(docs,ids):
    client = chromadb.Client()
    collection = client.get_or_create_collection("patents")
    collection.add(documents=docs, ids=ids)
    st.write('Client and Collection Created')
    return client, collection

# Add documents to the collection
#def add_documents(collection, docs, ids):
#   collection.add(documents=docs, ids=ids)

# Query the collection
def query_collection(collection, query):
    results = collection.query(query_texts=[query], n_results=1)
    return results['documents']

def main():
    st.title("Semantic Search with Chroma DB on Patents Dataset")

    # Load the data
    docs, ids = load_data()
    #st.write('Data Loaded')    

    # Initialize the Chroma client and collection
    client, collection = initialize_chroma(docs,ids)
    #st.write('Collection Created')

    # Get user input for the query
    query = st.text_input("Enter your query:")

    if query:
        # Query the collection
        results = query_collection(collection, query)

        # Display the results
        st.write(results)  # Display the document text
    else:
        st.write("Please enter a query to search the patent collection.")

if __name__ == "__main__":
    main()