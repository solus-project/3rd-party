#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

def setup():
    shelltools.system("tar xvf flash_player_ppapi_linux.x86_64.tar.gz")

def install():
    pisitools.insinto("/opt/google/chrome/PepperFlash", "libpepflashplayer.so")
