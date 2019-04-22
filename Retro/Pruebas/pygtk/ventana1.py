#!/usr/bin/python3.5
__author__ = 'fer'
__version__ = '0.0.0.1'
'''
Para instalar ver si hay los paquetes python3.5 y python3-pip
despues installar /usr/bin/pip3 install pyobject

Si la linea from gi.repository import Gtk no es reconocido, Dar alt+enter 
en Gtk y 'Generate stubs for binary module'
'''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def main():
    win = Gtk.Window()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == '__main__':
    main()