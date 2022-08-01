# write a python gui program to capitalize the text inputted into a text box
# add text box, capitalize button
# when capitalize button is pressed. text in text box is capitalized
# use gtk

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk # noqa


class capText(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Capitalize Text")

        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.entry1 = Gtk.Entry()
        self.entry1.set_text("enter text here")
        self.grid.attach(self.entry1, 0, 0, 1, 1)
        self.entry1.connect("activate", self.cap_text)

        self.button1 = Gtk.Button(label="Capitalize")
        self.button1.connect("clicked", self.cap_text)
        self.grid.attach(self.button1, 1, 0, 1, 1)

    def cap_text(self, widget):
        t = self.entry1.get_text()
        t = t.upper()
        self.entry1.set_text(t)


win = capText()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
