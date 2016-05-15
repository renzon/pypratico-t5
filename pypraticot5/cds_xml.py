import requests
import xmltodict


def buscar_cds():
    response = requests.get('http://www.w3schools.com/xml/cd_catalog.xml')
    xml = response.text
    dct = xmltodict.parse(xml)
    cds = dct['CATALOG']['CD']
    return [c['TITLE'] for c in cds]


if __name__ == '__main__':
    print(buscar_cds())
