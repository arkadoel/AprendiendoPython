import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        grid = Gtk.Grid()
        self.add(grid)

        self.set_border_width(10)
        self.set_title("Ventana 2")
        self.set_default_size(500,500)
        self.connect("destroy", Gtk.main_quit)

if __name__ == '__main__':
    win = MyWindow()
    win.show_all()
    Gtk.main()