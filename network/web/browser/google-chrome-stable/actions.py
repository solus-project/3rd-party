#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf google-chrome-stable_current_amd64.deb")
    shelltools.system("tar xvf data.tar.xz")

def install():
    # root owns sandbox as it is setuid
    shelltools.system("chown root:root opt/google/chrome/chrome-sandbox")
    # ensure setuid
    shelltools.system("chmod 4755 opt/google/chrome/chrome-sandbox")
    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")
