# MabiFoodScraper
This program is designed to extract data on Mabinogi food from the Mabinogi wiki. At current, it is not fully functional; however, it is able to read singular foods from the wiki. Additionally, it is also able to read full pages of food at a time. It is recommended to use the list of foods (located [here](https://wiki.mabinogiworld.com/view/Category:Food)) to choose from.

## Usage

#### Grabbing One Table
```
py scrapeFood.py [Mabinogi Wiki Link] [Food Table Index]
```
This command will print out the food into a dict format onto the command line. 

For instance, if you would like to retrieve the entry 'Basil' from the list of vegetables, you would use the link [https://wiki.mabinogiworld.com/view/Vegetables]() and for the Food Table Index, would input 0, as it is the 0th table on that page. An example is provided below with usage and output.
```
py scrapeFood.py https://wiki.mabinogiworld.com/view/Vegetables 0

{'Name': 'Basil', 'NPC Resale Value': '4 G', 'Method': 'Purchased', 'Edible': 'No', 'Hunger Restored': '-', 'Cooking EXP': '?', 'Purchase Location': 'Caitin / Shena / Effie (8g) / Flying Food Truck (8g)', 'Other Locations': '{{{Location}}}'}
```

#### Grabbing All Tables on Multiple URLs
```
py scrapeFood.py [Path to List of URLs]
```
This will allow you to grab all the tables from multiple URLs at one time.
The file must have one URL per each line, much like the following:

```
https://wiki.mabinogiworld.com/view/Deep-frying_List
https://wiki.mabinogiworld.com/view/Baking_List
https://wiki.mabinogiworld.com/view/Kneading_List
```

As an example, say the above is in a text file called **mabiURLs** in the same directory as scrapeFood.py, you would format the command as follows:
```
py scrapeFood.py ./mabiURLs
```

The above will then return all tables from all 3 links.
## Planned Features
The full version will allow you to export all information as JSON files. In addition each food will be mapped to their corresponding food group in a separate file.

Thanks to the [Mabinogi Wiki](https://wiki.mabinogiworld.com/view/Wiki_Home) for all the information on Mabinogi food.