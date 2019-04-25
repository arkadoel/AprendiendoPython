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
            
Para GtkSource ver 
https://github.com/ondratu/formiko/blob/master/formiko/sourceview.py

Si la linea from gi.repository import Gtk no es reconocido, Dar alt+enter 
en Gtk y 'Generate stubs for binary module'

Python Regius es un futuro IDE para python
De momento es una prueba de diseño y funcionalidades, a modo de experimiento
'''

import gi
import os
from subprocess import *
gi.require_version('Gtk', '3.0')
gi.require_version('GtkSource', '3.0')
gi.require_version('GtkSpell', '3.0')
gi.require_version('Pango', '1.0')
from gi.repository.Pango import FontDescription
from gi.repository import Gtk, Pango, GtkSource, Gdk
from gi.repository.GtkSource import LanguageManager, DrawSpacesFlags, StyleSchemeManager

EXAMPLE_TEXT = """
#fragmento de codigo de ejemplo
import threading
import time
from Constantes import const
import sys, os, subprocess
from datos.TablaAlerta import tbAlertas

try:
    import winsound
except:
    print('Sistema no windows, no se encuentra la libreria winSound')


class MirarHora(threading.Thread):

    ESPERA = 10     #segundos de espera entre iteracciones
    PASADAS = 1     #recarga el listado de tareas cada X pasadas de reloj

    def __init__(self, target=None, group=None, name=None, verbose=None, args=None, kwargs=None, daemon=None):
        '''
        Inicializacion del hilo, por si queremos pasarle datos
        :param target:
        :param group:
        :param name:
        :param verbose:
        :param args:
        :param kwargs:
        :return:
        '''
        threading.Thread.__init__(self, group=group, target=target,name=name, daemon=daemon)
        self.args = args
        self.kwargs = kwargs
        self.alertaActual = None
        return

    def run(self):
        print('Argumentos pasados al demonio: ', self.kwargs)
        seguir = True
        #obtener lista de tareas para hoy
        self.listaTareas = self.kwargs
        i=0

        while seguir:
            if i>self.PASADAS:
                self.listaTareas = tbAlertas().listarHorasAlertasHoy()
                self.alertaActual = None


            horaActual = const.getHora()

            for key, value in self.listaTareas.items():
                if horaActual == value[0]:
                    print('toca sonar', value[0])
                    if self.alertaActual is not None:
                        if self.alertaActual != key:
                            #la alerta no ha sido notificada, la hacemos sonar
                            self.hacerProcesos(hora=value[0], texto=value[1], comando=value[2])
                        else:
                            print('La alerta ya fue notificada, no sonara')
                    else:
                        self.hacerProcesos(hora=value[0], texto=value[1], comando=value[2])
                        self.alertaActual = key
                else:
                    print('.', end=' ')

            #hereda el error de no limpiar el buffer del lenguaje C --> LOL
            sys.stdout.flush()

            time.sleep(self.ESPERA)

            i +=1
        #finWhile

        print('Finalizado el daemon reloj')


    def hacerProcesos(self, hora=None, texto=None, comando=None):
        '''
        Lanza los eventos que haya que hacer en ese momento
        :return:
        '''

        const.SYSTRAY.showMessage(hora, texto)

        if comando is not None:
            strEjecuta = comando
            print(strEjecuta)
            subprocess.call(strEjecuta, shell=True)

        #repetimos tres veces el sonido
        for i in range(0, 3):

            if os.name == 'nt':
                #windows
                winsound.PlaySound(const.SONIDO, winsound.SND_FILENAME)
            elif os.name== 'posix':
                #linux
                comando = 'aplay ' + const.SONIDO
                os.system(comando)



"""

class MainWindow(Gtk.Window):
    DEFAULT_WIDTH = 950
    DEFAULT_HEIGHT= 700
    PYTHON_BIN ='/usr/bin/python3.5'

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

        self.workingFile = None
        self.init_ui()

    def init_ui(self):

        self.set_border_width(5) #padding controles
        self.set_title(__app_name__ + " " + __version__)
        self.set_default_size(self.DEFAULT_WIDTH,self.DEFAULT_HEIGHT)

        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.generate_toolbar()
        self.generate_textview()
        #self.generate_console()

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

    def generate_console(self):
        scrolled_window1 = Gtk.ScrolledWindow()
        scrolled_window1.set_border_width(2)
        self.grid.attach(scrolled_window1, 0, 2, 3, 1)
        # we scroll only if needed
        scrolled_window1.set_policy(
            Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

        # a text buffer (stores text)
        self.bufferConsola = Gtk.TextBuffer()

        # a textview (displays the buffer)
        self.txtConsola = Gtk.TextView(buffer=self.bufferConsola)
        # textview is scrolled
        scrolled_window1.add(self.txtConsola)
        # wrap the text, if needed, breaking lines in between words
        self.txtConsola.set_wrap_mode(Gtk.WrapMode.WORD)

        self.bufferConsola.set_text('>')

        self.txtConsola.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse( "#014276" ));
        tag = self.bufferConsola.create_tag()
        tag.set_property("foreground",'yellow')
        start = self.bufferConsola.get_start_iter()
        end = self.bufferConsola.get_end_iter()
        self.bufferConsola.apply_tag(tag, start, end)
        self.fontConsola = FontDescription.from_string('Monospace')
        self.fontConsola.set_size(8 * 1000)
        self.txtConsola.override_font(self.fontConsola)




    def generate_textview(self):
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        self.grid.attach(scrolledwindow, 0, 1, 3, 1)

        self.textview = GtkSource.View()
        self.font = FontDescription.from_string('Monospace')
        self.font.set_size(12*1000)
        self.textview.override_font(self.font)
        self.textview.set_show_line_numbers(True)
        self.textview.set_auto_indent(True)
        self.textview.set_tab_width(4)
        #self.textview.set_show_right_margin(True) #muy python
        self.textview.set_highlight_current_line(True)
        self.set_text_wrapping(False)
        #self.set_white_chars(True) #pone los puntos en los espacios

        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.new_with_language(self.LANGS['.%s' % 'py'])
        self.textbuffer.set_text('')
        self.workingFile = None
        self.do_file_type('.py')
        #/usr/share/gtksourceview-3.0/styles/
        #mas temas en https://wiki.gnome.org/Projects/GtkSourceView/StyleSchemes
        style_scheme = GtkSource.StyleSchemeManager.get_default().get_scheme('oblivion')
        #style_scheme = GtkSource.StyleSchemeManager.get_default().get_scheme('tango')
        self.textbuffer.set_style_scheme(style_scheme)

        scrolledwindow.add(self.textview)

        self.tag_bold = self.textbuffer.create_tag("bold",
            weight=Pango.Weight.BOLD)
        self.tag_italic = self.textbuffer.create_tag("italic",
            style=Pango.Style.ITALIC)
        self.tag_underline = self.textbuffer.create_tag("underline",
            underline=Pango.Underline.SINGLE)
        self.tag_found = self.textbuffer.create_tag("found",
            background="yellow")

        #scroll zoom raton
        self.textview.connect('scroll-event', self.on_scroll)
        self.connect("key-press-event", self.key_press_event)

    def generate_toolbar(self):
        toolbar = Gtk.Toolbar()
        self.grid.attach(toolbar, 0, 0, 3, 1)

        btnNew  = Gtk.ToolButton()
        btnNew.set_icon_name("document-new")
        btnOpen = Gtk.ToolButton()
        btnOpen.set_icon_name("folder-open")
        btnSave = Gtk.ToolButton()
        btnSave.set_icon_name("media-floppy")
        btnUndo = Gtk.ToolButton()
        btnUndo.set_icon_name("edit-undo")
        btnRedo = Gtk.ToolButton()
        btnRedo.set_icon_name("edit-redo")
        btnZoomIn = Gtk.ToolButton()
        btnZoomIn.set_icon_name("zoom-in")
        btnZoomOut = Gtk.ToolButton()
        btnZoomOut.set_icon_name("zoom-out")
        btnCompileRun = Gtk.ToolButton()
        btnCompileRun.set_icon_name("media-playback-start")

        toolbar.insert(btnNew, 1)
        toolbar.insert(btnOpen, 2)
        toolbar.insert(btnSave, 3)
        toolbar.insert(Gtk.SeparatorToolItem(), 4)
        toolbar.insert(btnUndo, 5)
        toolbar.insert(btnRedo, 6)
        toolbar.insert(Gtk.SeparatorToolItem(), 7)
        toolbar.insert(btnZoomIn, 8)
        toolbar.insert(btnZoomOut, 9)
        toolbar.insert(Gtk.SeparatorToolItem(), 10)
        toolbar.insert(btnCompileRun, 11)

        btnZoomIn.connect("clicked", self.btnZoomIn_click)
        btnZoomOut.connect("clicked", self.btnZoomOut_click)
        btnOpen.connect("clicked", self.open_dialog_load_file)
        btnSave.connect("clicked", self.save_dialog)
        btnUndo.connect("clicked", self.btn_undo_click)
        btnRedo.connect("clicked", self.btn_redo_click)
        btnCompileRun.connect("clicked", self.btn_compile_run_click)

    def key_press_event(self, widget, event):
        keyval_name = Gdk.keyval_name(event.keyval)
        ctrl = (event.state & Gdk.ModifierType.CONTROL_MASK)
        if ctrl and keyval_name == 'y':
            if self.textbuffer.can_redo():
                self.textbuffer.do_redo(self.textbuffer)
        elif ctrl and keyval_name == 'z':
            if self.textbuffer.can_undo():
                self.textbuffer.do_undo(self.textbuffer)

    def btn_redo_click(self, widget):
        if self.textbuffer.can_redo():
            self.textbuffer.do_redo(self.textbuffer)

    def btn_undo_click(self, widget):
        if self.textbuffer.can_undo():
            self.textbuffer.do_undo(self.textbuffer)

    def btn_compile_run_click(self, widget):
        if self.workingFile is None or self.workingFile is  '':
            self.save_dialog(widget)

        self.save_to_file(self.workingFile)
        comando =  self.PYTHON_BIN + " " + self.workingFile
        print('xfce4-terminal  -x %s' % comando)

        os.system('xfce4-terminal  -x %s -T "PyRegius"' % comando)

    def open_dialog_load_file(self, widget):

        dialog = Gtk.FileChooserDialog("Abrir ...", None,
                                       Gtk.FileChooserAction.OPEN,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                        Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            selected_file = dialog.get_filename()
            print (selected_file)
            self.Cargar_fichero(selected_file)
        elif response == Gtk.ResponseType.CANCEL:
            selected_file = ""
        dialog.destroy()

        return selected_file

    def save_dialog(self, widget):
        if(self.workingFile is None or self.workingFile == '' ):
            dialog = Gtk.FileChooserDialog("Guardar ...", None,
                                           Gtk.FileChooserAction.SAVE,
                                           (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                            Gtk.STOCK_SAVE, Gtk.ResponseType.ACCEPT))

            self.add_filters(dialog)
            response = dialog.run()

            Gtk.FileChooser.set_do_overwrite_confirmation(dialog, True)

            if response == Gtk.ResponseType.ACCEPT:
                selected_file = Gtk.FileChooser.get_filename(dialog)
                print('guardar en ', selected_file)
                self.save_to_file(selected_file)
            else:
                print('No guardar')

            dialog.destroy()
        else:

            if(self.textbuffer.get_modified() is True):
                print('guardar modificacion en ', self.workingFile)
                self.save_to_file(self.workingFile)
            else:
                print('sin modificacion en ', self.workingFile)

    def save_to_file(self, filename):
        '''
        Guardado de archivo
        :param filename:
        :return:
        '''
        start_iter = self.textbuffer.get_start_iter()
        end_iter = self.textbuffer.get_end_iter()
        text = self.textbuffer.get_text(start_iter, end_iter, True)

        with open(filename, 'w', encoding="utf-8") as src:
            # python version 3.x
            src.write(text)
            src.close()
        self.textbuffer.set_modified(False)
        self.workingFile = filename

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        filter_py.add_pattern(".py")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

    def Cargar_fichero(self, selected_file):
        filename, file_extension = os.path.splitext(selected_file)
        texto = self.Read_file_to_end(selected_file)
        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.new_with_language(self.LANGS['.%s' % 'py'])
        self.textbuffer.set_text(texto)
        self.do_file_type(file_extension)
        self.workingFile = selected_file
        self.textbuffer.set_modified(False)

    def Read_file_to_end(self, ruta):
        with open(ruta, 'r') as f:
            texto = f.read()
            f.close()
        return texto

    def btnZoomIn_click(self, widget):
        self.zoom_in()

    def zoom_in(self):
        print('zoom in ')
        newSize = self.font.get_size() + (2*1000)
        self.font.set_size(newSize)# if newSize < 99000 else 20000)
        self.textview.override_font(self.font)

    def btnZoomOut_click(self, widget):
        self.zoom_out()

    def zoom_out(self):
        print('zoom out')
        newSize = self.font.get_size() - (2*1000)
        self.font.set_size(newSize if newSize>2000 else 3000)
        self.textview.override_font(self.font)

    def on_scroll(self, widget, event):
        """ handles on scroll event"""
        # Handles zoom in / zoom out on Ctrl+mouse wheel
        accel_mask = Gtk.accelerator_get_default_mod_mask()
        if event.state & accel_mask == Gdk.ModifierType.CONTROL_MASK:
            direction = event.get_scroll_deltas()[2]
            print(event.get_scroll_deltas())
            if direction >0:  # scrolling down -> zoom out
                self.zoom_out()
            else:
                self.zoom_in()


if __name__ == '__main__':
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.set_position(Gtk.WindowPosition.CENTER)
    win.show_all()
    Gtk.main()

