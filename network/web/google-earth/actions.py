#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import pisitools, shelltools, get

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def setup():
    shelltools.system("ar xf google-earth-pro-stable_%s_amd64.deb" % get.srcVERSION())
    shelltools.system("tar xvf data.tar.xz")
    shelltools.system("mv opt/google/earth/pro/google-earth-pro.desktop .")
    

def install():
    pisitools.insinto("/", "opt")
    pisitools.insinto("/usr", "usr/bin")
    pisitools.insinto("/usr/share/applications", "google-earth-pro.desktop")
    pisitools.dosym("ld-linux-x86-64.so.2", "/lib/ld-lsb-x86-64.so.3")
    
    for i in ["16", "22", "24", "32", "48", "64", "128", "256"]:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" % (i,i), "opt/google/earth/pro/product_logo_%s.png" % i, "google-earth-pro.png")
