#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools


NoStrip = ["/"]
IgnoreAutodep = True

def setup():
	shelltools.system("ar xf SpiderOakONE_*.deb")
	shelltools.system("tar xf data.tar.gz")
	shelltools.system("rm -r etc/apt")


def install():
    pisitools.insinto("/", "etc")
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "opt")
