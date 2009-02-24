#!/usr/bin/env python

import gtk

class Systray:

	kietol = None

	def __init__(self, kietol):
		self.kietol = kietol
		staticon = gtk.StatusIcon()
		staticon.set_from_pixbuf(self.kietol.getIcon())
		staticon.set_blinking(False)
		staticon.set_visible(False)
		staticon.connect("activate", self.hide)
		self.staticon = staticon
		
	def show(self, widget, event):
		self.kietol.window.hide_all()
		self.staticon.set_tooltip(self.kietol.window.get_title())
		self.staticon.set_visible(True)
		
	def hide(self, event):
		self.kietol.window.show_all()
		self.kietol.window.move(self.kietol.prefs.getInt("x"), self.kietol.prefs.getInt("y"))
		self.kietol.window.resize(self.kietol.prefs.getInt("width"), self.kietol.prefs.getInt("height"))
		self.staticon.set_visible(False)
		
	def refresh(self, progress):
		self.staticon.set_tooltip(self.kietol.window.get_title() + " (" + progress + ")")

