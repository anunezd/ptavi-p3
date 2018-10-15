#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler


class MiKaraoke:

    def __init__(self,file):
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(file))
        self.lista = cHandler.get_tags()

    def __str__(self):
        exit = ""
        for elemento in self.lista:
            nombre = elemento[0]
            atributo = elemento[1]
            exit += '\n' + nombre + '\t'
            for valor in atributo:
                if atributo[valor] != '':
                    exit += valor + '="' + atributo[valor] + '"' + '\t'
        return exit

    def to_json(self, filesmil, filejson=''):
        if filejson == '':
            filejson = filesmil.replace('.smil', '.json')
        with open (filejson, 'w') as jsonfile:
            json.dump(self.lista, jsonfile, indent=3)


if __name__ == "__main__":

    try:
        file = sys.argv[1]
    except IndexError:
        sys.exit('Usage python3 karaoke.p file.smil')
    karaoke = MiKaraoke(file)
    print(karaoke)
    karaoke.to_json(file)
