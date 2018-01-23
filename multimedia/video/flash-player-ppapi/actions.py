#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

WorkDir = "."

def install():
    pisitools.insinto("/opt/google/chrome/PepperFlash", "libpepflashplayer.so")
