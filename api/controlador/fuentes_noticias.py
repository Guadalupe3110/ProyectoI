from modelo.fuentes_noticias import CL_FuentesNoticiasDB
from modelo.db_roles import CL_RolesDB
import xml.etree.ElementTree as ET
import xmltodict
import requests

class CL_FuentesNoticias:

    def xml(self):

        xml= xmltodict.parse(requests.get('https://www.lanacion.com.ar/arcio/rss/').text)
        print(xml['rss']['channel']['item'][0]['category'])
        #print(xml['rss'])
        return xml
