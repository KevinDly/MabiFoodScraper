import requests, sys, re, json, os, argparse
from bs4 import BeautifulSoup
from wikiScrapers import scrapeFoodTable
recipeKey = 'Recipe'

def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        #raise argparse.ArgumentTypeError("readable_dir:{path} is not a valid path")
        os.makedirs(path)
        return path

def writeJSON(path, filename, tableDict):
    with open(os.path.join(path, filename), 'w') as file:
        file.write(json.dumps(tableDict, indent=4))
    
def main():
    parser = argparse.ArgumentParser(description='Scrape Mabinogi wiki food tables')
    subparsers = parser.add_subparsers(help='Scrape a single table from the wiki')
    
    parser_single = subparsers.add_parser('singleScrape', help='Allows you to obtain a single table from the wiki.')
    parser_single.add_argument('link', help='A link to a url containing one or more Mabinogi wiki food tables.')
    parser_single.add_argument('-i', type=int, help='The index of the table, default 0', default=0)
    
    parser_multi = subparsers.add_parser('multiScrape', help='Allows you to obtain tables from multiple links')
    parser_multi.add_argument('list', type=argparse.FileType('r'), help='Path to a file containing a list of Mabinogi wiki URLs')
    parser_multi.add_argument('-o', type=dir_path, help='Path to a folder to write the files out to.')
    
    args = vars(parser.parse_args())
    
    if 'link' in args:
        URL = args['link']
        index = args['i']
            
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        tables = soup.find_all("table", class_="prettytable")
        if(index >= len(tables)):
            print('Chosen index {} is too large, there are only {} tables on this page.'.format(index, len(tables)))
            return
        tableDict = scrapeFoodTable(tables[index], recipeKey)
        print(json.dumps(tableDict, indent=4))
    elif 'list' in args:
        groupToFood = {}
        file = args['list']
        count = 1
        for line in file:
            url = line.strip()
            group = url.rsplit('/')[-1]
            foodList = {'foods':[]}
            try:
                page = requests.get(url)
                soup = BeautifulSoup(page.content, "html.parser")
                tables = soup.find_all("table", class_="prettytable")
                for table in tables:
                    tableDict = scrapeFoodTable(table, recipeKey)
                    #print(json.dumps(tableDict, indent=4))
                    foodList['foods'].append(tableDict)
                    groupToFood.update({tableDict['Name']: group})
                    
                if args['o'] != None:
                    writeJSON(args['o'], group + '.JSON', foodList)
                    count = count + 1
                else:
                    print(json.dumps(foodList, indent=4))
                
            except requests.exceptions.MissingSchema as exception:
                print("Incorrect URL:", url)
                
        if args['o'] != None:
            writeJSON(args['o'], 'groupToFood' + '.JSON', groupToFood)
            print('Wrote {} files to {}'.format(count, args['o']))
        else:
            print(groupToFood)
    else:
        print('Please use the -h command for help.')
main()