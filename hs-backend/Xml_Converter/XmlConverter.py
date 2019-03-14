import json


class XmlConverter(object):
    wortschatz = {}
    anzahl_dokumente = 0

    def __init__(self, newspaper_page, name, print_space_element, xmlns):
        self.Newspaper_Page = newspaper_page
        self.Xmlns = xmlns
        self.name = name
        self.get_content(print_space_element)
        self.export_json()

    def get_content(self, element):
        if element.tag == self.Xmlns + 'String':
            wort = element.get('CONTENT')
            if wort in self.wortschatz:
                self.wortschatz[wort] = self.wortschatz[wort] + 1
            else:
                self.wortschatz[wort] = 1
            self.Newspaper_Page.Text[-1][-1].append(wort)
        else:
            if self.Newspaper_Page.Text != '':
                if element.tag == self.Xmlns + 'TextBlock':
                    self.Newspaper_Page.Text.append([])
                elif element.tag == self.Xmlns + 'TextLine':
                    self.Newspaper_Page.Text[-1].append([])
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
        if data.get('Text') != []:
            self.anzahl_dokumente = self.anzahl_dokumente + 1
            with open('./Data/Text/' + self.name + '.json', 'w') as outfile:
                json.dump(data, outfile, indent=4, ensure_ascii=False)

