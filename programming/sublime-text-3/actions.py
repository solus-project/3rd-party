#!/usr/bin/python

from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/opt/sublime_text", "sublime_text")
    pisitools.insinto("/opt/sublime_text", "crash_reporter")
    pisitools.insinto("/opt/sublime_text", "plugin_host")
    pisitools.insinto("/opt/sublime_text", "python3.3.zip")
    pisitools.insinto("/opt/sublime_text", "*.py")
    pisitools.insinto("/opt/sublime_text", "Packages")

    pisitools.insinto("/usr/share/applications", "sublime_text.desktop")

    for i in ["16", "32", "48", "128", "256"]:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" % (i,i), "Icon/%sx%s/" % (i,i), "sublime-text.png")

    pisitools.dosym("/opt/sublime_text/sublime_text", "/usr/bin/sublime_text")
