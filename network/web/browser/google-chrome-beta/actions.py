#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf google-chrome-beta_%s%s_amd64.deb" % (get.srcVERSION(), Suffix))
    shelltools.system("tar xvf data.tar.xz")

def install():
    # root owns sandbox as it is setuid
    shelltools.system("chown root:root opt/google/chrome-beta/chrome-sandbox")
    # ensure setuid
    shelltools.system("chmod 4755 opt/google/chrome-beta/chrome-sandbox")

    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")

    for i in ["16", "22", "24", "32", "48", "64", "128", "256"]:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" % (i,i), "opt/google/chrome-beta/product_logo_%s_beta.png" % i, "google-chrome-beta.png")
