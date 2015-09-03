#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf google-chrome-unstable_%s%s_amd64.deb" % (get.srcVERSION(), Suffix))
    shelltools.system("tar xvf data.tar.xz")

def install():
    # root owns sandbox as it is setuid
    shelltools.system("chown root:root opt/google/chrome-unstable/chrome-sandbox")
    # ensure setuid
    shelltools.system("chmod 4755 opt/google/chrome-unstable/chrome-sandbox")
    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")
