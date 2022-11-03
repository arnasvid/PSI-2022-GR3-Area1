from xmljson import badgerfish as bf
from defusedxml.ElementTree import fromstring
from collections import OrderedDict
import defusedxml.ElementTree as ET
import json


class CheckFormatResponse:
    def __init__(self, success, tree):
        self.success = success
        self.tree = tree


def check_format(file):
    # check if the file is correctly formatted
    try:
        tree = ET.parse(file)
        tree.getroot() == "DATA_EXPORT"
        tree.getroot()[2].tag == "ADDRESS"
        # check if third child's child is named "ROOF"
        return CheckFormatResponse(True, tree)
    except ET.ParseError:
        # if the file is not well-formed, print that is not well-formed
        print(file + " is not well-formed")
        return CheckFormatResponse(False, None)


# define a function to convert xml to json
def xml_to_json(file):
    # if the file is well-formed...
    response = check_format(file)

    if (response.success and response.tree):
        # print(response.success, response.tree)
        # transfer "FACE" child to json
        # print("root: ")
        # print(response.tree.getroot())
        # print("3 child: ")
        faces = response.tree.getroot()[3][0]
        # print(structure)
        ##roof_1 = structure[0]
        # print(roof_1)

        ##faces = roof_1[0]
        for face in faces:
            polygon = face[0]
            polygon.attrib['id'] = 1
            print(polygon.attrib.get('id'))
        # get file name
        name = str.split(file, ".")[-2]
        # open the XML file, convert to json and dump into a new file
        with open(file, "rt") as input:

            text = input.read()
            first, main = text.split("<FACES>")
            main_final, last = main.split("</FACES>")

            final = "<FACES>" + main_final + "</FACES>"
            print(final)
            # print(final_final)
            # print(last)

            jsonOut = bf.data(fromstring(final))
            with open(name + ".json", "w+") as newFile:
                json.dump(jsonOut, newFile, ensure_ascii=False)


def main():
    file = input("Iveskite failo pavadinima arba kelia iki jo: ")
    xml_to_json(file)


if __name__ == '__main__':
    main()
