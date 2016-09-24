#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]

IgnoreAutodep = True

def setup():
    shelltools.system("wget wget https://raw.githubusercontent.com/solus-project/3rd-party/master/network/web/browser/tor-browser/files/tor-browser.desktop")

def install():
    pisitools.insinto("/opt/tor-browser/", "Browser/*")
    pisitools.insinto("/usr/share/applications/", "tor-browser.desktop")
