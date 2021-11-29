
# Library to work with APIs
from bs4 import BeautifulSoup 
import requests

def fnc_teste():
    print("Hi, i´m a function.")

# Funtion to return all adrress basead in CEP\n",
def fnc_GetCEP(strCEP):
    page = requests.get("https://viacep.com.br/ws/{}/json/".format(strCEP))
    return page.json()

# Function to replace caracters
def fnc_AdjustCepBody(strCEP):
    # Local variables
    strCEP = strCEP.replace("-","")
    strCEP = strCEP.replace(".","")
    return strCEP