#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-

__author__      = "Fer D. Minguela"
__copyright__   = "Copyright 2019, Fernando D. Minguela"
__credits__     = ["Fer D. Minguela"]
__license__     = "GPL"
__version__     = "0.0.1"
__maintainer__  = "Fer D. Minguela"
__email__       = "fer.d.minguela@gmail.com"
__status__      = "Develop"
__app_name__    = "PyRegius"
__date__        = "22-Abr-2019" #inicio del proyecto

'''Para instalar ver si hay los paquetes python3.5 y python3-pip
despues installar /usr/bin/pip3 install pyobject

apt install python3-pip python3-gi python3-docutils gir1.2-gtksource-3.0 \
            gir1.2-webkit2-4.0 gir1.2-gtkspell3-3.0
            
Para GtkSource ver https://github.com/ondratu/formiko/blob/master/formiko/sourceview.py

Si la linea from gi.repository import Gtk no es reconocido, Dar alt+enter 
en Gtk y 'Generate stubs for binary module'

Python Regius es un futuro IDE para python
'''

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GtkSource', '3.0')
gi.require_version('GtkSpell', '3.0')
gi.require_version('Pango', '1.0')
from gi.repository.Pango import FontDescription
from gi.repository import Gtk, Pango, GtkSource
from gi.repository.GtkSource import LanguageManager, DrawSpacesFlags

EXAMPLE_TEXT = """import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def main():
    win = Gtk.Window()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == '__main__':
    main()
"""

class MainWindow(Gtk.Window):
    DEFAULT_WIDTH = 950
    DEFAULT_HEIGHT= 700

    default_manager = LanguageManager.get_default()
    LANGS = {
        '.rst': default_manager.get_language('rst'),
        '.md': default_manager.get_language('markdown'),
        '.html': default_manager.get_language('html'),
        '.htm': default_manager.get_language('html'),
        '.json': default_manager.get_language('json'),
        '.py': default_manager.get_language('python')
    }

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.set_border_width(5) #padding controles
        self.set_title(__app_name__ + " " + __version__)
        self.set_default_size(self.DEFAULT_WIDTH,self.DEFAULT_HEIGHT)

        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.generate_textview()

    def set_white_chars(self, white_chars):
        '''
        Pone puntos en los espacios en blanco
        :param white_chars:
        :return:
        '''
        if white_chars:
            self.textview.set_draw_spaces(DrawSpacesFlags.ALL)
        else:
            self.textview.set_draw_spaces(0)

    def set_text_wrapping(self, text_wrapping):
        '''
        Tipo de salto de linea
        :param text_wrapping:
        :return:
        '''
        if text_wrapping:
            self.textview.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)
        else:
            self.textview.set_wrap_mode(Gtk.WrapMode.NONE)

    def set_spaces_instead_of_tabs(self, use_spaces):
        '''
        Poner espacios en vez de tabulaciones
        :param use_spaces:
        :return:
        '''
        self.source_view.set_insert_spaces_instead_of_tabs(use_spaces)
        self.source_view.set_smart_backspace(use_spaces)

    def do_file_type(self, ext):
        language = self.LANGS.get(ext, self.LANGS['.rst'])
        if self.textbuffer.get_language() != language:
            self.textbuffer.set_language(language)

    def generate_textview(self):
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        self.grid.attach(scrolledwindow, 0, 1, 3, 1)

        self.textview = GtkSource.View()
        self.textview.override_font(FontDescription.from_string('Monospace'))
        self.textview.set_show_line_numbers(True)
        self.textview.set_auto_indent(True)
        self.textview.set_tab_width(4)
        #self.textview.set_show_right_margin(True) #muy python
        self.textview.set_highlight_current_line(True)
        self.set_text_wrapping(True)
        #self.set_white_chars(True) #pone los puntos en los espacios

        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.new_with_language(self.LANGS['.%s' % 'py'])
        self.textbuffer.set_text(EXAMPLE_TEXT)
        self.do_file_type('.py')
        scrolledwindow.add(self.textview)

        self.tag_bold = self.textbuffer.create_tag("bold",
            weight=Pango.Weight.BOLD)
        self.tag_italic = self.textbuffer.create_tag("italic",
            style=Pango.Style.ITALIC)
        self.tag_underline = self.textbuffer.create_tag("underline",
            underline=Pango.Underline.SINGLE)
        self.tag_found = self.textbuffer.create_tag("found",
            background="yellow")

if __name__ == '__main__':
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.set_position(Gtk.WindowPosition.CENTER)
    win.show_all()
    Gtk.main()

