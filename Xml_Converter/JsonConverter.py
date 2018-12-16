from os import listdir
from os.path import isfile, join
from xml.dom import minidom
import json

# Hier den Pfad zu den Dateien
path = "/home/jon/Downloads/Data/Data/"

files = [f for f in listdir(path) if isfile(join(path, f))]


def convert_to_json():
    for file in files:
        try:
            content = minidom.parse(path + file)
            year = content.getElementsByTagName('Year')[0].firstChild.nodeValue
            month = content.getElementsByTagName('Month')[0].firstChild.nodeValue
            day = content.getElementsByTagName('Day')[0].firstChild.nodeValue
            newspaper_number = content.getElementsByTagName('NewspaperNumber')[0].firstChild.nodeValue
            page_number = content.getElementsByTagName('PageNumber')[0].firstChild.nodeValue
            edition = content.getElementsByTagName('Edition')[0].firstChild.nodeValue
            issue = content.getElementsByTagName('Issue')[0].firstChild.nodeValue
            if content.getElementsByTagName('Text')[0].firstChild != None:
                text = content.getElementsByTagName('Text')[0].firstChild.nodeValue
            else:
                text = ""

            jayson = {
                "year": year,
                "month": month,
                "day": day,
                "newspaperNumber": newspaper_number,
                "pageNumber": page_number,
                "edition": edition,
                "issue": issue,
                "text": text
            }

            with open(path+file+".json", "w") as write_file:
                json.dump(jayson, write_file)

        except Exception as ex:
            print(ex)
            print(file)



if __name__ == "__main__":
    convert_to_json()
