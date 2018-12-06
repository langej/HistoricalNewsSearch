import os
import pathlib
from xml.etree import ElementTree as EleTree
from NewspaperPage import NewspaperPage
from XmlConverter import XmlConverter

dir_root = './1930/'
dir_names = os.listdir(dir_root)
if '.DS_Store' in dir_names: dir_names.remove('.DS_Store')
pathlib.Path('./Data/').mkdir(exist_ok=True)

for dir_name in dir_names:
    filenames = os.listdir(dir_root + dir_name + '/alto/')
    for filename in filenames:
        filename_split = filename.split('_')
        newspaper_page = NewspaperPage(year=filename_split[3][0:4], month=filename_split[3][4:6],
                                       day=filename_split[3][6:], newspaper_number=filename_split[5],
                                       issue=filename_split[4], page_number=filename_split[7][:3],
                                       edition=filename_split[6])
        tree = EleTree.parse(dir_root + dir_name + '/alto/' + filename)
        root = tree.getroot()
        xmlns = '{http://www.loc.gov/standards/alto/ns-v2#}'
        print_space_element = root.find(xmlns + 'Layout/' + xmlns + 'Page/' + xmlns + 'PrintSpace')
        xml_converter = XmlConverter(newspaper_page=newspaper_page, print_space_element=print_space_element,
                                     xmlns=xmlns)