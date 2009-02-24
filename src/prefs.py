#!/usr/bin/env python

import os, ConfigParser

PREFSFILE = os.path.expanduser("~/.kietol/preferences")

#
#  Implements storage and retrieval of GMP preferences.
#
class Prefs:
	
	kietol, parser = None, None
	
	defaults = { 
		"x" : "50",
		"y" : "50",
		"width" : "380",
		"height" : "100", 
		"continuous" : "True",
		"random" : "False",
		"repeat" : "False",
		"path" : os.path.expanduser("~/"),
		"sort" : "0"
	}
	
	#
	#  Instantiates a new Prefs with the options from STORE.
	#
	def __init__(self, kietol):
		
		self.kietol = kietol
		
		self.parser = ConfigParser.SafeConfigParser(self.defaults)
		
		try:
			self.parser.read([PREFSFILE,])
		except StandardError:
			return
		
	#
	#  A convenience method for retrieving an option.
	#
	def get(self, option):
		return self.parser.get("DEFAULT", option)
		
	#
	#  A convenience method for retrieving an integer option.
	#
	def getInt(self, option):
		return int(self.parser.get("DEFAULT", option))
		
	#
	#  A convenience method for retrieving a boolean option.
	#
	def getBool(self, option):
		return self.parser.get("DEFAULT", option) == "True"
		
	#
	#  A convenience method for setting an option.
	#
	def set(self, option, value):
		self.parser.set("DEFAULT", option, value) 
		
	#
	#  Writes prefs to the specified file, defaulting to PREFSFILE.
	#
	def save(self, prefsFile=PREFSFILE):
		
		x, y = self.kietol.window.get_position()
		
		if x > 0 or y > 0:  #gtk gives 0,0 quite often
			self.set("x", str(x))
			self.set("y", str(y))
		
		rect = self.kietol.window.get_allocation()
		self.set("width", str(rect.width))
		self.set("height", str(rect.height))
		
		self.set("continuous", str(self.kietol.playlist.continuous))
		self.set("random", str(self.kietol.playlist.random))
		self.set("repeat", str(self.kietol.playlist.repeat))
		
		self.set("path", self.kietol.menu.path)
		self.set("sort", str(self.kietol.menu.sort))
		
		try:
			self.parser.write(open(prefsFile, "w"))
		except StandardError:
			return
			
# End of file
