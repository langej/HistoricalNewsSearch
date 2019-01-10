import xml.etree.ElementTree as ET
from xml.dom import minidom
import json


class XmlConverter(object):

    def __init__(self, newspaper_page, print_space_element, xmlns):
        self.Newspaper_Page = newspaper_page
        self.Xmlns = xmlns
        self.get_content(print_space_element)
        self.export_json()

    def get_content(self, element):
        if element.tag == self.Xmlns + 'String':
            self.Newspaper_Page.Text = self.Newspaper_Page.Text + element.get('CONTENT') + ' '
        else:
            if self.Newspaper_Page.Text != '':
                if element.tag == self.Xmlns + 'ComposedBlock':
                    self.Newspaper_Page.Text = self.Newspaper_Page.Text + '\n \n \n'
                elif element.tag == self.Xmlns + 'TextBlock':
                    self.Newspaper_Page.Text = self.Newspaper_Page.Text + '\n \n'
                elif element.tag == self.Xmlns + 'TextLine':
                    self.Newspaper_Page.Text = self.Newspaper_Page.Text + '\n'
            for child in element:
                self.get_content(child)
        return True

    def export_json(self):
        data = {
            'Year': self.Newspaper_Page.Year,
            'Month': self.Newspaper_Page.Month,
            'Day': self.Newspaper_Page.Day,
            'NewspaperNumber': self.Newspaper_Page.Newspaper_Number,
            'PageNumber': self.Newspaper_Page.Page_Number,
            'Edition': self.Newspaper_Page.Edition,
            'Issue': self.Newspaper_Page.Issue,
            'Text': self.Newspaper_Page.Text
        }
        if data.get('Text') != '':
            with open('./Data/Text/' + self.Newspaper_Page.Newspaper_Number + '_' + self.Newspaper_Page.Edition
                            + '_' + self.Newspaper_Page.Page_Number + '.json', 'w') as outfile:
                json.dump(data, outfile, indent=4, ensure_ascii=False)

        """    
        def export_xml(self):
        page = ET.Element('Page')
        year = ET.SubElement(page, 'Year')
        year.text = self.Newspaper_Page.Year
        month = ET.SubElement(page, 'Month')
        month.text = self.Newspaper_Page.Month
        day = ET.SubElement(page, 'Day')
        day.text = self.Newspaper_Page.Day
        newspaper_number = ET.SubElement(page, 'NewspaperNumber')
        newspaper_number.text = self.Newspaper_Page.Newspaper_Number
        page_number = ET.SubElement(page, 'PageNumber')
        page_number.text = self.Newspaper_Page.Page_Number
        edition = ET.SubElement(page, 'Edition')
        edition.text = self.Newspaper_Page.Edition
        issue = ET.SubElement(page, 'Issue')
        issue.text = self.Newspaper_Page.Issue
        text = ET.SubElement(page, 'Text')
        text.text = self.Newspaper_Page.Text

        xml = minidom.parseString(ET.tostring(page, encoding="unicode"))
        xml_file = open('./Data/' + self.Newspaper_Page.Newspaper_Number + '_' + self.Newspaper_Page.Edition
                        + '_' + self.Newspaper_Page.Page_Number + '.xml', 'w')
        xml_file.write(xml.toprettyxml(indent="  "))
        xml_file.close()
        """

