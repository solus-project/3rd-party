#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

import shutil


NoStrip = ["/"]
IgnoreAutodep = True

def setup():
	#shutil.move('getbuild?platform=ubuntu&arch=x86_64', 'spideroakone.deb')
	#print "Successfully renamed."
	shelltools.system("mv getbuild* spideroakone.deb")
	shelltools.system("pwd")
	shelltools.system("ar xf spideroakone.deb")
	shelltools.system("tar xf data.tar.gz")
	

def install():
    pisitools.insinto("/", "etc")
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "opt")
