#!/usr/bin/python2 -tt
# -*- coding: utf-8 -*-

import os

from gi.repository import Gtk, Gdk
from gi.repository import GLib

GLADE_FILE = os.path.join(os.path.dirname(__file__), 'directory_browse.glade')

class HelloWorld(object):
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(GLADE_FILE)
        self.main_win = self.builder.get_object("main_window")
        self.main_handlers = {
            "on_main_window_delete_event": self.delete_event,
            "on_btn_browse_clicked": self.btn_browse_click
        }
        self.builder.connect_signals(self.main_handlers)
        self.text_entry = self.builder.get_object('directory_entry')
        self.main_win.show_all()
        Gtk.main()

    def run(self):
        self.main_win.show_all()

    def delete_event(self, widget, event, data=None):
        Gtk.main_quit()

    def btn_browse_click(self, widget):
        print ('I have clicked')
        dialog = Gtk.FileChooserDialog("Please choose a folder", self.main_win,
                Gtk.FileChooserAction.SELECT_FOLDER,
                (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK)
        )
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print ('Select clicked')
            text = dialog.get_filename()
            self.text_entry.set_text(text)
        else:
            print ('Cancel clicked')
        dialog.destroy()

if __name__ == "__main__":
    hw = HelloWorld()
    #hw.run()
