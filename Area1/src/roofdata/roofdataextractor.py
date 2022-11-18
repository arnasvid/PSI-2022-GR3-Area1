import extract_roof_data
import xml_to_json
import check_format


def main():
    
    file="src/XMLFiles/stogas.xml"
    print(check_format.cf(file))
    #print(xml_to_json.xtj(file))
    #extract_roof_data.erd(xml_to_json.xtj(file))
   
    


if __name__ == '__main__':
    main()
