#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools


NoStrip = ["/"]
IgnoreAutodep = True

def setup():
	shelltools.system("mv getbuild* spideroakone.deb")
	shelltools.system("pwd")
	shelltools.system("ar xf spideroakone.deb")
	shelltools.system("tar xf data.tar.gz")


def install():
    pisitools.insinto("/", "etc")
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "opt")
