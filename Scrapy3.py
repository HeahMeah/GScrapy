import streamlit as st
import requests
from bs4 import BeautifulSoup
from googlesearch import search

def google_search(query):
    urls = []
    for url in search(query, num_results=10):
        urls.append(url)
    return urls

def get_description(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    description = soup.find('meta', attrs={'name': 'description'})
    if description:
        return description['content']
    else:
        return 'No description available.'

st.title("Google Search Scraper")
query = st.text_input("Enter a query")
if st.button("Search"):
    results = google_search(query)
    st.write("Results:")
    for result in results:
        description = get_description(result)
        st.write("- " + result + " - " + description)
