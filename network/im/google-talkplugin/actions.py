#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

Suffix = "-1"

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf google-talkplugin_%s%s_amd64.deb" % (get.srcVERSION(), Suffix))
    shelltools.system("tar xvf data.tar.*")

def install():
    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")
