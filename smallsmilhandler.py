#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.root = {}
        self.region = {}
        self.img = {}
        self.audio = {}
        self.textstream = {}
        self.lista = []

    def startElement(self, name, attrs):

        if name == 'root-layout':
            # De esta manera tomamos los valores de los atributos
            self.root['width'] = attrs.get('width', "")
            self.root['height'] = attrs.get('height', "")
            self.root['background-color'] = attrs.get('background-color', "")
            self.lista.append([name, self.root])
        elif name == 'region':
            self.region['id'] = attrs.get('id', "")
            self.region['top'] = attrs.get('top', "")
            self.region['bottom'] = attrs.get('bottom', "")
            self.region['left'] = attrs.get('right', "")
            self.lista.append([name, self.region])
        elif name == 'img':
            self.img['src'] = attrs.get('src', "")
            self.img['region'] = attrs.get('region', "")
            self.img['begin'] = attrs.get('begin', "")
            self.img['dur'] = attrs.get('dur', "")
            self.lista.append([name, self.img])
        elif name == 'audio':
            self.audio['src'] = attrs.get('src', "")
            self.audio['begin'] = attrs.get('begin', "")
            self.audio['fur'] = attrs.get('dur', "")
            self.lista.append([name, self.audio])
        elif name == 'textstream':
            self.textstream['src'] = attrs.get('src', "")
            self.textstream['region'] = attrs.get('region', "")
            self.lista.append([name, self.textstream])

    def get_tags(self):
        return self.lista


if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
