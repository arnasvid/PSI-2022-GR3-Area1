from xmljson import badgerfish as bf
from defusedxml.ElementTree import fromstring
from collections import OrderedDict
import defusedxml.ElementTree as ET
import json

def check_format(file):
    # check if the file is correctly formatted
    try:
        tree = ET.parse(file)
        tree.getroot() == "DATA_EXPORT"
        tree.getroot()[2].tag == "ADDRESS"
        # check if third child's child is named "ROOF"
        return True
    except ET.ParseError:
        # if the file is not well-formed, print that is not well-formed
        print(file + " is not well-formed")
        return False


# define a function to convert xml to json
def xml_to_json(file):
    if check_format(file):
        with open(file, "r") as input:
            jsonOut = bf.data(fromstring(input.read()))
        return json.loads(json.dumps(jsonOut))

def extract_roof_data(data):
    print("extracting roof data")
 
    faces = data['DATA_EXPORT']['STRUCTURES']['ROOF']['FACES']
    lines = data['DATA_EXPORT']['STRUCTURES']['ROOF']['LINES']
    points = data['DATA_EXPORT']['STRUCTURES']['ROOF']['POINTS']

    final_string = ""
    for face in faces['FACE']:
        #We go through each face
        for path_line in face['POLYGON']['@path'].split(","):
            #We split  "(example) L44,L45,L46,L47" and we go through each of them
            for line in lines['LINE']:
                #einam per visus line'us ir ieskom sutampanciu
                # We go through each line and look for identical     
                if line['@id'] == path_line:
                    #If we find indetical ones
                    line_points = line['@path'].split(",")
                    #We split path of that line "(example)C25,C1", and we go through each of them
                    line_type = line['@type']
                    #We save type of that line
                    for point in points['POINT']:
                        #We go through all of points and find two that correspond to the points of the line
                        if point['@id'] == line_points[0]:
                            point1 = point['@data'].split(",")
                            # We take the coordinates of the first point, splitting it into three parts: x, y, z
                        if point['@id'] == line_points[1]:
                            point2 = point['@data'].split(",") 
                            # We take the coordinates of the second point, splitting it into three parts: x, y, z
                            


                    path_line_str = (" '" + path_line + "' : {'Type' : '"+ line_type + "','" + line_points[0] + "' : { 'X' : " + point1[0] + ","  
                    + "'Y' : " + point1[1] + "," + "'Z' : " + point1[2] + "},'" + line_points[1] + "' : { 'X' : " + point2[0] + ","  
                    + "'Y' : " + point2[1] + "," + "'Z' : " + point2[2] + "}" +  "},")
                    final_string = "".join([ final_string, path_line_str]) 
                    #We join all the strings into one, so it's easier to write to json
                    break
                            
                               
        final_string = "{" +final_string + "}"
         
        face['POLYGON']['@path'] = eval(final_string)
        final_string = ""
        #adding to json with eval function

    faces = data['DATA_EXPORT']['STRUCTURES']['ROOF']['FACES']
    with open("data" + ".json","w+") as newFile:
        json.dump(faces, newFile, ensure_ascii=True, indent=2, sort_keys=False)
   






def main():
    #file = input("Input the path to the file: ")
    file="Area1\src\XMLFIles\stogas.xml"
    extract_roof_data(xml_to_json(file))
    


if __name__ == '__main__':
    main()
