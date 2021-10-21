#Check for commandline arguments
import re
def scrapeFoodTable(table, recipeKey):
    #Locate the tbody of the table
    tbody = table.find('tbody')
    
    #List out all trs in the tbody.
    trList = tbody.find_all('tr', recursive=False)
    
    tableDict = {}
    currHead = [];
    
    #Some recipes dont conform to the the normal recipe structure.
    recipeIgnore = ["Wheat Flour"]
    
    #Iterate through each tr looking for th and td.
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
                        
                #If the list of table headers are longer than the list of data, have to make the first head a key value for the rest of the dict.
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
    #TODO: Update this so that recipes may also work for the "Number Food" format
    if tableDict['Name'] not in recipeIgnore:
        if recipeKey in tableDict:
            #split string if it has a /
            recipeList = [r.strip() for r in tableDict[recipeKey].split('/')]
            finalList = []
            for recipe in recipeList:
                ingredientList = [i.strip() for i in recipe.split(') ')]
                #print(ingredientList)
                splitList = [s.split('(') for s in ingredientList]
                for i in range(len(splitList)):
                    tuple = splitList[i]
                    tuple[0] = tuple[0].strip()
                    tuple[1] = re.sub("[^0-9]", "", tuple[1])
                    splitList[i] = tuple
                finalList.append(splitList)
                
                #split inner strings even further by splitting '('
                #Turn percentages into raw numbers.
            tableDict['Recipe'] = finalList
    
    return tableDict