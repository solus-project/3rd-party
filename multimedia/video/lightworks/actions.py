#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr", "/lib"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf lwks-%s-amd64.deb" % Version)
    shelltools.system("tar xf data.tar.xz")
    shelltools.system("ar xf libcg_*_amd64.deb")
    shelltools.system("tar xf data.tar.xz")
    shelltools.system("ar xf libcggl_*_amd64.deb")
    shelltools.system("tar xf data.tar.xz")

    # Port library location
    shelltools.system("mkdir usr/lib64")
    shelltools.system("mv usr/lib/x86_64-linux-gnu/* usr/lib64")
    

def install():
    pisitools.insinto("/", "usr")
    pisitools.insinto("/", "lib")
    pisitools.removeDir("/usr/share/lintian")
    pisitools.removeDir("/usr/lib/x86_64-linux-gnu")
    
