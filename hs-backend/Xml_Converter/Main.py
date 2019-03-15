import os
import pathlib
from xml.etree import ElementTree as EleTree
from NewspaperPage import NewspaperPage
from XmlConverter import XmlConverter
from pgmagick import Image

wortschatz = {}
anzahl_dokumente = 0


def merge_dic(dic):
    for key in dic:
        if key in wortschatz:
            wortschatz[key] = wortschatz[key] + dic[key]
        else:
            wortschatz[key] = dic[key]


def get_text_statistics():
    wörter = 0
    wörter_1000 = 0
    wörter_1 = 0
    for wort in wortschatz:
        if wortschatz[wort] > 1000:
            wörter_1000 = wörter_1000 + 1
            wörter = wörter + wortschatz[wort]
        elif wortschatz[wort] == 1:
            wörter_1 = wörter_1 + 1
            wörter = wörter + wortschatz[wort]
        else:
            wörter = wörter + wortschatz[wort]
    print(wortschatz)
    print('Total documents: ' + str(anzahl_dokumente))
    print('Total word occurrences: ' + str(wörter))
    print('Vocabulary size: ' + str(len(wortschatz)))
    print('Words occurring > 1000 times: ' + str(wörter_1000))
    print('Words occurring once: ' + str(wörter_1) + '\n')


dir_Daten = './Daten/'
dir_Jahre = os.listdir(dir_Daten)
if '.DS_Store' in dir_Jahre: dir_Jahre.remove('.DS_Store')
pathlib.Path('./Data').mkdir(exist_ok=True)
pathlib.Path('./Data/Text').mkdir(exist_ok=True)
pathlib.Path('./Data/View').mkdir(exist_ok=True)
for dir_Jahr in dir_Jahre:
    dir_root = dir_Daten + dir_Jahr + '/'
    dir_names = os.listdir(dir_root)
    if '.DS_Store' in dir_names: dir_names.remove('.DS_Store')
    for dir_name in dir_names:
        filenames = os.listdir(dir_root + dir_name + '/alto/')
        for filename in filenames:
            filename_split = filename.split('_')
            newspaper_page = NewspaperPage(year=filename_split[3][0:4], month=filename_split[3][4:6],
                                        day=filename_split[3][6:], newspaper_number=filename_split[5],
                                        issue=filename_split[4], page_number=filename_split[7][:3],
                                        edition=filename_split[6])
            view_path = dir_root + dir_name + '/viewing/' + filename.replace('xml', 'jp2')
            name = newspaper_page.Year + '_' + newspaper_page.Month + '_' \
                   + newspaper_page.Day + '_' + newspaper_page.Newspaper_Number + '_' \
                   + newspaper_page.Edition + '_' + newspaper_page.Page_Number
            img = Image(view_path)
            img.write('./Data/View/' + name + '.jpeg')
            tree = EleTree.parse(dir_root + dir_name + '/alto/' + filename)
            root = tree.getroot()
            xmlns = '{http://www.loc.gov/standards/alto/ns-v2#}'
            print_space_element = root.find(xmlns + 'Layout/' + xmlns + 'Page/' + xmlns + 'PrintSpace')
            xml_converter = XmlConverter(newspaper_page=newspaper_page, name=name,
                                         print_space_element=print_space_element, xmlns=xmlns)
            anzahl_dokumente += xml_converter.anzahl_dokumente
            merge_dic(xml_converter.wortschatz)
            if anzahl_dokumente == 4532:
                break
        if anzahl_dokumente == 4532:
            break
    if anzahl_dokumente == 4532:
        break
get_text_statistics()
