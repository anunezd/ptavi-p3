#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import urllib.request
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

        salida = ""
        for elemento in lista:
            nombre = elemento[0]
            etiqueta = elemento[1]
            salida += '\n' + nombre + '\t'
            for atributo in etiqueta:
                if etiqueta[atributo] != '':
                    salida += atributo + '="' + etiqueta[atributo] + '"' + '\t'
        print (salida)

        file = file.replace('.smil', '.json')
        with open (file, 'w') as jsonsalida:
            json.dump(lista, jsonsalida, indent=3)

        for elemento in lista:
            etiqueta = elemento [1]
            for atributo in etiqueta:
                if atributo == 'src':
                    if etiqueta[atributo].startswith('http://'):
                        url = etiqueta[atributo]
                        file = url.split('/')[-1]
                        urllib.request.urlretrieve(url,file)
                        etiqueta[atributo] = file

    except IndexError:
        sys.exit('Usage python3 karaoke.p file.smil')
