#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

WorkDir = "."

def install():
    pisitools.insinto("/usr/bin", "usr/bin/flash-player-properties")
    pisitools.insinto("/usr/share/applications", "usr/share/applications/flash-player-properties.desktop")
    pisitools.insinto("/usr/lib/mozilla/plugins", "libflashplayer.so")

    for i in ["16", "22", "24", "32", "48"]:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" % (i,i), "usr/share/icons/hicolor/%sx%s/apps/flash-player-properties.png" % (i,i))
