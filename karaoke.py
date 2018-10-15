#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler


if __name__ == "__main__":

    try:
        file = sys.argv[1]
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(file))
        lista = cHandler.get_tags()

        exit = ""
        for elemento in lista:
            nombre = elemento[0]
            atributo = elemento[1]
            exit += '\n' + nombre + '\t'
            for valor in atributo:
                if atributo[valor] != '':
                    exit += valor + '="' + atributo[valor] + '"' + '\t'
        print (exit)

        file = file.replace('.smil', '.json')
        with open (file, 'w') as jsonsalida:
            json.dump(lista, jsonsalida, indent=3)

    except IndexError:
        sys.exit('Usage python3 karaoke.p file.smil')
