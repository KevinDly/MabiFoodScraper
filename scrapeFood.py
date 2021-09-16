import requests, sys, re, json, os.path
from bs4 import BeautifulSoup
from wikiParsers import parseFoodTable
recipeKey = 'Recipe'

def main():
    if (len(sys.argv) == 3):
        URL = sys.argv[1]
        index = int(sys.argv[2])
            
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        tables = soup.find_all("table", class_="prettytable")
        tableDict = parseFoodTable(tables[index], recipeKey)
        print(json.dumps(tableDict, indent=4))
    else:
        urlListFile = sys.argv[1]
        if not os.path.exists(urlListFile):
            print("Invalid filepath:", urlListFile)
        else:
            file = open(urlListFile, 'r')
            for line in file:
                url = line.strip()
                try:
                    page = requests.get(url)
                    soup = BeautifulSoup(page.content, "html.parser")
                    tables = soup.find_all("table", class_="prettytable")
                    for table in tables:
                        tableDict = parseFoodTable(table, recipeKey)
                        print(json.dumps(tableDict, indent=4))
                except requests.exceptions.MissingSchema as exception:
                    print("Incorrect URL:", url)
                    
main()