# Pymp Makefile

PYTHON=/usr/bin/python
PREFIX=/usr
DESTDIR=
KIETOL_HOME=$(PREFIX)/lib/kietol

all: clean
	cd src && $(PYTHON) ./build.py && rm -f ./build.pyc
	sed -e "s|PYTHON=.*|PYTHON=$(PYTHON)|" \
		  -e "s|KIETOL_HOME=.*|KIETOL_HOME=$(KIETOL_HOME)|" \
		  src/kietol.sh > src/kietol

install: all	
	install -d $(DESTDIR)/$(KIETOL_HOME)
	install -m 0644 src/*.pyc $(DESTDIR)/$(KIETOL_HOME)
	
	install -d $(DESTDIR)/$(PREFIX)/share/{applications,pixmaps}
	install -m 0644 src/kietol.desktop $(DESTDIR)/$(PREFIX)/share/applications
	install -m 0644 src/*.png $(DESTDIR)/$(PREFIX)/share/pixmaps
	
	install -d $(DESTDIR)/$(PREFIX)/bin
	install -m 0755 src/kietol $(DESTDIR)/$(PREFIX)/bin
	
clean:
	rm -f src/*.pyc src/kietol
	
#End of file
