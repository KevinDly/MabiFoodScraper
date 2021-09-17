# MabiFoodScraper
This program is designed to extract data on Mabinogi food from the Mabinogi wiki. At current, it is not fully functional; however, it is able to read singular foods from the wiki. Additionally, it is also able to read full pages of food at a time. It is recommended to use the list of foods (located [here](https://wiki.mabinogiworld.com/view/Category:Food)) to choose from.

## Usage

This program makes usage of the argparse Python library, as such you may use the following command to see command usage.

```
py scrapeFood.py -h
```

There are two included programs within this program: **singleScrape** and **multiScrape**.

### singleScrape
This command will allow you to pick a food table from a Mabinogi wiki link. The default is the first table available; however, any table may be chosen.

The command for singleScrape is as follows:
```
py scrapeFood.py singleScrape [-h] [-i I] link
```
The positional argument, link, is the link to the page, such as [this one](https://wiki.mabinogiworld.com/view/Baking_List). This is required.

The optimal argument, -i, is the index of the table you wish to choose, 0 indexed. The default for this optional argument is 0. 

The output will print out the table requested in JSON format.

### multiScrape
This command will allow you to pick from multiple URLs, and print or write out all tables from each URL into a file or the command line. Additionally, a mapping will be made from each food to the corresponding link, and if an output folder is chosen, will be written to groupToFood.json.

The command for multiScrape is as follows:
```
py scrapeFood.py multiScrape [-h] [-o O] list
```
The positional argument, list, is the file path to a list of one or multiple Mabinogi wiki URL(s). The file format should look similar to below:
```
https://wiki.mabinogiworld.com/view/Baking_List
https://wiki.mabinogiworld.com/view/Boiling_List
https://wiki.mabinogiworld.com/view/Simmering_List
```
The optional argument, -o, is a path to a folder you wish the JSONs to be written to. If this argument is not supplied, all JSON information will be printed onto the command line. If the folder does not exist, the folder will be created before writing.

For example, if we decide to put the links above into a file called urls.txt, and wish to write to a folder called jsons, we would have the following command
```
py scrapeFood.py multiScrape ./urls.txt ./jsons/
```
This would then create four files, Baking_List.JSON, Boiling_List.JSON, Simmering_List.JSON, and groupToFood.JSON within a folder called jsons. The first three files would contain the tables in JSON format of their respective links, and the fourth would be a JSON list with food mapped to their respective file.

## Planned Features
All currently planned features are finished!

Thanks to the [Mabinogi Wiki](https://wiki.mabinogiworld.com/view/Wiki_Home) for all the information on Mabinogi food.