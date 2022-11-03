from xmljson import badgerfish as bf
from defusedxml.ElementTree import fromstring
from collections import OrderedDict
import defusedxml.ElementTree as ET
import json

bf = bf(dict_type = OrderedDict)

def check_format(file):
    #check if the file is correctly formatted
    try:
        tree = ET.parse(file)
        tree.getroot() == "DATA_EXPORT"
        tree.getroot()[2].tag == "ADDRESS"
        #check if third child's child is named "ROOF"
        return True
    except ET.ParseError:
        # if the file is not well-formed, print that is not well-formed
        print(file + " is not well-formed")
        return False



#define a function to convert xml to json
def xml_to_json(file):
# if the file is well-formed...
    if check_format(file):
    # get file name   
        name = str.split(file, ".")[-2]
        # open the XML file, convert to json and dump into a new file
        with open(file, "r") as input:
            jsonOut = bf.data(fromstring(input.read()))
            with open(name + ".json","w+") as newFile:
                json.dump(jsonOut, newFile, ensure_ascii=False)
                



def main():
    file=input("Iveskite failo pavadinima arba kelia iki jo: ")
    xml_to_json(file)

if __name__ == '__main__':
    main()