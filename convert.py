import json, copy

def convertToTree(json):
    jsonList = []
    if 'Recipe' in json:
        for recipe in json['Recipe']:
            newJson = {}
            newJson['name'] = json['Name']
            newJson['attributes'] = copy.deepcopy(json)
            newJson['children'] = [e[0] for e in recipe]
            newJson['attributes']['recipePercents'] = [e[1] for e in recipe]
            newJson['attributes'].pop('Recipe', None)
            newJson['attributes'].pop('Name', None)
            jsonList.append(newJson)
    else:
            newJson = {}
            newJson['name'] = json['Name']
            newJson['attributes'] = json
            newJson['attributes'].pop('Name', None)
            jsonList.append(newJson)
    return jsonList