#!/usr/bin/python2 -tt
# -*- coding: utf-8 -*-

import os
import ConfigParser
from StringIO import StringIO

from gi.repository import Gtk, Gdk
from gi.repository import GLib

GLADE_FILE = os.path.join(os.path.dirname(__file__), 'choose_btn.glade')

class ChooseBtnExample(object):
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(GLADE_FILE)
        self.main_win = self.builder.get_object("main_window")
        self.main_handlers = {
            "on_main_window_delete_event": self.delete_event,
            "on_btn_browse_clicked": self.btn_browse_click,
            "on_fedora_release_changed": self.fedora_release_changed,
            "on_list_versions_cursor_changed": self.list_view_cursor_changed,
        }
        self.builder.connect_signals(self.main_handlers)
        self.text_entry = self.builder.get_object('directory_entry')
        self.combo_box = self.builder.get_object('fedora_release')
        self.listview = self.builder.get_object('list_versions')
        self.label_release = self.builder.get_object('label_fedora_release')
        self.text_view = self.builder.get_object('build_view')
        self.store = Gtk.ListStore(str)
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Available versions", renderer, markup=0, text=0)
        column.set_sort_column_id(0)
        self.listview.append_column(column)
        self.listview.set_model(self.store)
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
        git_config = os.path.join(text, '.git', 'config')
        if not os.path.exists(git_config):
            print 'This is not Git repository'
            self.label_release.set_text("")
            self.store.clean()
        else:
            versions = self._parse_git_config_file(git_config)
            print (versions)
            for version in sorted(versions):
                self.store.append([version])
            self.label_release.set_text(sorted(versions)[0])

    def fedora_release_changed(self, widget):
        version = self.combo_box.get_active_text()
        print(version)

    def _parse_git_config_file(self, git_config):
        data = StringIO('\n'.join(line.strip() for line in open(git_config, 'r')))
        config = ConfigParser.SafeConfigParser()
        config.readfp(data)
        releases = []
        tag = 'branch'
        for section in config.sections():
            if section.startswith(tag):
                releases.append(section.replace(tag, '').replace('"', '').strip())
        return releases

    def list_view_cursor_changed(self, listview):
        model, listiter = listview.get_selection().get_selected()
        if listiter is not None:
            text = model[listiter][0]
            print ('changed row: %s' % text)
            self.label_release.set_text(text)
            text_buffer = self.text_view.get_buffer()
            text_buffer.insert_at_cursor(text + '\n')


if __name__ == "__main__":
    hw = ChooseBtnExample()
    #hw.run()
