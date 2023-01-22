import streamlit as st
import pickle
from pathlib import Path
import requests
import time
from bs4 import BeautifulSoup
from googlesearch import search
import streamlit_authenticator as stauth

# --- USER AUTH ---

names = ["Ilya", "Tanya"]
usernames = ["ilya", "tanya"]

# --- LOAD HESHED PASS ---

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
                                    "Scrapy", "aaaaad", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

# --- MESSAGES ---

if authentication_status == False:
    st.error("Usrename/Passwords is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:


# --- APP ---

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

 def write_to_file(link):
     with open("links.txt", "a") as file:
         file.write(link + "\n")
         st.write("Link successfully saved.")

 st.title("Google Search Scraper")
 query = st.text_input("Enter a query")
 if st.button("Search", key = "search"):
     results = google_search(query)
     time.sleep(600)
     st.write("Results:", key = "res")
     for result in results:
         description = get_description(result)
         st.write("- " + result + " - " + description)
         if st.button("Save link", key='save'):
             write_to_file(result)

 with open('results.txt', 'a') as file:
        file.write(query + '\n')
        results = google_search(query)
        for result in results:
            file.write(result + '\n')
