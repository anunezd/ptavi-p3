#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import urllib.request
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler


class KaraokeLocal:

    def __init__(self, file):
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(file))
        self.lista = cHandler.get_tags()

    def __str__(self):
        salida = ""
        for elemento in self.lista:
            nombre = elemento[0]
            etiqueta = elemento[1]
            salida += '\n' + nombre + '\t'
            for atributo in etiqueta:
                if etiqueta[atributo] != '':
                    salida += atributo + '="' + etiqueta[atributo] + '"' + '\t'
        return (salida)

    def to_json(self, filesmil, filejson=''):
        if filejson == '':
            filejson = filesmil.replace('.smil', '.json')
        with open(filejson, 'w') as jsonfile:
            json.dump(self.lista, jsonfile, indent=3)

    def do_local(self):
        for elemento in self.lista:
            etiqueta = elemento[1]
            for atributo in etiqueta:
                if atributo == 'src':
                    if etiqueta[atributo].startswith('http://'):
                        url = etiqueta[atributo]
                        arch = url.split('/')[-1]
                        urllib.request.urlretrieve(url, arch)
                        etiqueta[atributo] = arch


if __name__ == "__main__":

    try:
        file = sys.argv[1]
    except IndexError:
        sys.exit('Usage python3 karaoke.p file.smil')

    karaoke = KaraokeLocal(file)
    print(karaoke)
    karaoke.to_json(file)
    karaoke.do_local()
    karaoke.to_json(file, 'local.json')
    print(karaoke)
