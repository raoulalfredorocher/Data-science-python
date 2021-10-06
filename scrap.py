#IMPORT
from bs4 import BeautifulSoup
import requests

#VARIABILI#
html_str = ""
#example = : "https://www.polimi.it/studenti-iscritti/"



try:
    html = input('Inserisci il nome del sito internet: ')
except:
    print("aggiuntere http:// o https:// davanti all\'url")

#html = "http://www.lesisterepedagogico.it"
html_doc = requests.get(html)

html_str = BeautifulSoup(html_doc.text, 'html.parser')


Html_file= open("jhonny.html","w")
Html_file.write(str(html_str))
Html_file.close() 