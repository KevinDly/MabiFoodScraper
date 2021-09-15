# MabiFoodScraper
This program is designed to extract data on Mabinogi food from the Mabinogi wiki. At current, it is not fully functional; however, it is able to read singular foods from the wiki. It is recommended to use the list of foods (located [here](https://wiki.mabinogiworld.com/view/Category:Food)) to choose from.

## Usage
```
py scrapeFood.py [Mabinogi Wiki Link] [Food Table Index]
```
This command will print out the food into a dict format onto the command line. 


For instance, if you would like to retrieve the entry 'Basil' from the list of vegetables, you would use the link [https://wiki.mabinogiworld.com/view/Vegetables]() and for the Food Table Index, would input 0, as it is the 0th table on that page. An example is provided below with usage and output.
```
py scrapeFood.py https://wiki.mabinogiworld.com/view/Vegetables 0

{'Name': 'Basil', 'NPC Resale Value': '4 G', 'Method': 'Purchased', 'Edible': 'No', 'Hunger Restored': '-', 'Cooking EXP': '?', 'Purchase Location': 'Caitin / Shena / Effie (8g) / Flying Food Truck (8g)', 'Other Locations': '{{{Location}}}'}
```

## Planned Features
The full version of this will allow you to use multiple links at the same time, and will export all the data as json files that may be used in other programs.

Thanks to the [Mabinogi Wiki](https://wiki.mabinogiworld.com/view/Wiki_Home) for all the information on Mabinogi food.