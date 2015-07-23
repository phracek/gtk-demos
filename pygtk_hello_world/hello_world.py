#!/usr/bin/python2 -tt
# -*- coding: utf-8 -*-

import os

from gi.repository import Gtk, Gdk
from gi.repository import GLib

GLADE_FILE = os.path.join(os.path.dirname(__file__), 'hello_world.glade')

class HelloWorld(object):
    def __init__(self):
        pass

    def run(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(GLADE_FILE)
        self.main_win = self.builder.get_object("main_window")
        self.main_handlers = {
            "on_main_window_delete_event": self.delete_event,
        }
        self.builder.connect_signals(self.main_handlers)
        self.main_win.show_all()
        Gtk.main()

    def delete_event(self, widget, event, data=None):
        Gtk.main_quit()

if __name__ == "__main__":
    hw = HelloWorld()
    hw.run()
