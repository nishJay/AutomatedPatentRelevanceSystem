__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer


# Load the dataset
@st.cache_data
def load_data(query=None):
    df = pd.read_csv('neural_network_patent_query.csv')
    st.write('Data loaded')

    # Filter the dataset based on the query
    if query:
        df = df[df['patent_title'].str.contains(query, case=False)]

    # Preprocess the data
    dfs = df.sort_values(by='patent_number', ascending=True)
    dfs.set_index('patent_number', inplace=True)
    desired_columns = ['patent_title', 'patent_abstract', 'patent_date']
    dfs = dfs[desired_columns]
    dfs.loc[:, 'patent_title'] = dfs['patent_title'].str.lower()
    dfs.loc[:, 'patent_abstract'] = dfs['patent_abstract'].str.lower()
    df['patent_title'] = df['patent_title'].str.replace('The title of the patent is ', '', regex=True)
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

# Query the collection
def query_collection(collection, query):
    results = collection.query(query_texts=[query], n_results=8)
    return results['documents']

def extract_title(description):
    start_index = description.find("The title of the patent is ") + len("The title of the patent is ")
    end_index = description.find(" and its abstract is")
    return description[start_index:end_index]

def extract_abstract(description):
    start_index = description.find(" and its abstract is ") + len(" and its abstract is ")
    end_index = description.find(" dated")
    return description[start_index:end_index]

def extract_date(description):
    start_index = description.find("dated ") + len("dated ")

    return description[start_index:]



def main():
    st.title("Semantic Search with Chroma DB on Patents Dataset")

    # Add CSS style
    st.markdown("""
    <style>
    body {
    background-color: white;
    font-family: Arial, sans-serif;
    }
    h1 {
    color:  Olive;
    }
  .result {
    border: 3px OliveDrab;
    padding: 15px;
    margin-bottom: 10px;
    
    }
   .result-title {
    font-size: 25px;
    font-weight: bold;
    color: OliveDrab;
    }
   .result-description {
    margin-top: 10px;
    text-align: justify;
    }
   .result-date {
    margin-top: 5px;
    font-size: 14px;
    color: gray;
    }
    </style>
    """, unsafe_allow_html=True)

    # Get user input for the query
    query = st.text_input("Enter your query:")

    # Load the data
    docs, ids = load_data()

    # Initialize the Chroma client and collection
    client, collection = initialize_chroma(docs,ids)

    # Get user input for the query
    results = query_collection(collection, query)

    if query:
        # Query the collection
        results = query_collection(collection, query)

        if results:
            # Display the results
            #for result in results:
            for i, result in enumerate(results[:8]):
                #st.write(f"*Result {i + 1}:*")
                title1 = extract_title(result[0])
                title2 = extract_title(result[1])
                title3 = extract_title(result[2])
                title4 = extract_title(result[3])
                title5 = extract_title(result[4])
                title6 = extract_title(result[5])
                title7 = extract_title(result[6])
                title8 = extract_title(result[7])


                abstract1 = extract_abstract(result[0])
                abstract2 = extract_abstract(result[1])
                abstract3 = extract_abstract(result[2])
                abstract4 = extract_abstract(result[3])
                abstract5 = extract_abstract(result[4])
                abstract6 = extract_abstract(result[5])
                abstract7 = extract_abstract(result[6])
                abstract8 = extract_abstract(result[7])
                
                date1 = extract_date(result[0])
                date2 = extract_date(result[1])
                date3 = extract_date(result[2])
                date4 = extract_date(result[3])
                date5 = extract_date(result[4])
                date6 = extract_date(result[5])
                date7 = extract_date(result[6])
                date8 = extract_date(result[7])


                
                #st.write("Patent Title:", result['patent_title'])
                #st.write("Patent Abstract:", result['patent_abstract'])
                #st.write("Patent Date:", result['patent_date'])
                
                #st.write("Patent Description:", result[0] if len(result) > 0 else "N/A")
                #st.write("Patent Abstract:", result[1] if len(result) > 1 else "N/A")
                #st.write("Patent Date:", result[2] if len(result) > 2 else "N/A")
                #st.write("---")

                #title = result[0]  # Access title directly
                #abstract = result[1] if len(result) > 1 and result[1] != "" else "Not Available"
                #date = result[2] if len(result) > 2 else "N/A"

        # Display information separately
                #st.write("*Patent Description:*")
                #st.write(title)
                st.write("Result 1:")
                with st.expander("Patent Title: {}".format(title1)):
                    st.write("*Patent Description:*")
                    st.write("Abstract: {}".format(abstract1))
                    st.write("Dated: {}".format(date1))
                st.write("Result 2:")
                with st.expander("Patent Title: {}".format(title2)):
                    st.write("*Patent Description:*")
                    st.write("Abstract: {}".format(abstract2))
                    st.write("Dated: {}".format(date2))
                st.write("Result 3:")
                with st.expander("Patent Title: {}".format(title3)):
                    st.write("*Patent Description:*")
                    st.write("Abstract: {}".format(abstract3))
                    st.write("Dated: {}".format(date3))
                st.write("Result 4:")
                with st.expander("Patent Title: {}".format(title4)):
                    st.write("*Patent Description:*")
                    st.write("Abstract: {}".format(abstract4))
                    st.write("Dated: {}".format(date4))
                st.write("Result 5:")
                with st.expander("Patent Title: {}".format(title5)):
                    st.write("*Patent Description:*")
                    st.write("Abstract: {}".format(abstract5))
                    st.write("Dated: {}".format(date5))
                st.write("Result 6:")
                with st.expander("Patent Title: {}".format(title6)):
                    st.write("*Patent Description:*")
                    st.write("Abstract: {}".format(abstract6))
                    st.write("Dated: {}".format(date6))    
                st.write("Result 7:")
                with st.expander("Patent Title: {}".format(title7)):
                    st.write("*Patent Description:*")
                    st.write("Abstract: {}".format(abstract7))
                    st.write("Dated: {}".format(date7))    
                st.write("Result 8:")
                with st.expander("Patent Title: {}".format(title8)):
                    st.write("*Patent Description:*")
                    st.write("Abstract: {}".format(abstract8))
                    st.write("Dated: {}".format(date8))    
                    
                

                
                #st.write("Abstract: {}".format(abstract))
                
                
                #st.write("*Patent Abstract:*")
                #st.write(abstract)
                #st.write("*Patent Date:*")
                #st.write(date) 
           
                
        else:
            st.write("No results found for the query:", query)
    else:
        st.write("Please enter a query to search the patent collection.")

if __name__ == "__main__":
    main()
