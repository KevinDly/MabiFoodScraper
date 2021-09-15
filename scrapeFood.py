import requests
import sys
from bs4 import BeautifulSoup

dictHeaders = ['Gradual Stat Change', ]
URL = sys.argv[1]
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

tables = soup.find_all("table", class_="prettytable")

# for food in tables:
    # #headers = tables.find_all("th")
    # ##data = tables.find_all("td")
    # ##print(headers, end="\n"*2)
    # ##print(data, end="\n"*2)
    # for child in food.children:
        # print(child)
#tables[1].find('td', class_='image').decompose()
#body = tables[1].find('tbody')

#put below in a loop probably.
#TODO: Parse physical change, gradual stat change, etc

index = int(sys.argv[2])
#tables[index].find('td', class_='image').decompose()
tbody = tables[index].find('tbody')
trList = tbody.find_all('tr', recursive=False)

tableDict = {}
currHead = [];

for tr in trList:
    innerBody = tr.find('tbody')
    if innerBody:
        #If it is a complete table with th and td parse the entire table, otherwise only need an array of the td.
        if(tr.find_all('th')):
            head = innerBody.find_all('th')
            textHead = [h.text.strip() for h in head]
            data = innerBody.find_all('td')
            textData = [d.text.strip() for d in data]
            
            result = dict(zip(textHead, textData))
            tableDict.update(result)
        else:
            data = innerBody.find_all('td')
            textData = [d.text.strip() for d in data]
            physicalDict = {currHead[0]: textData}
            tableDict.update(physicalDict)
    else:
        #if it is a th add to thList otherwise tdList
        eleList = tr.find_all('th')
        if(eleList):
            headList = []
            for head in eleList:
                headList.append(head.text.strip())
            currHead = headList
        else:
            eleList = tr.find_all('td')
            dataList = []
            for data in eleList:
                    dataList.append(data.text.strip())
                    
            #If the list of table headers are longer than the list of data, have to make the first head a key value.
            if(len(currHead) != len(dataList)):
                key = headList.pop(0)
                statDict = dict(zip(currHead, dataList))
                keyToDict = {key: statDict}
                tableDict.update(keyToDict)
                currHead = []
            else:
                currDict = dict(zip(currHead, dataList))
                tableDict.update(currDict)
                currHead = []
            
            

#Modify the key:value pair "recipe" to have appropriate values.
#{Recipe: { Ingredients: [[], []], Percentages: [[], []]}}
if 'Recipe' in tableDict:
    #split string if it has a /
    recipeList = [r.strip() for r in tableDict['Recipe'].split('/')]
    for recipe in recipeList:
        ingredientList = [i.strip() for i in recipe.split(') ')]
        #print(ingredientList)
        #split inner strings even further by splitting '('
        #Turn percentages into raw numbers.

print(tableDict)
