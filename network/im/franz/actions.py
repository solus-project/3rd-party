#!/usr/bin/python

# Created for Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

def setup():
    shelltools.system("pwd")
    shelltools.system("mkdir franz")
    shelltools.system("tar xvf Franz-linux-x64-%s.tgz -C franz" % (get.srcVERSION()))
    shelltools.system("wget https://raw.githubusercontent.com/meetfranz/franz-pkgbuild/master/franz.sh")
    shelltools.system("wget https://raw.githubusercontent.com/meetfranz/franz-pkgbuild/master/franz.desktop")
    shelltools.system("wget https://raw.githubusercontent.com/meetfranz/franz-pkgbuild/master/franz.png")
    shelltools.system("install -Dm755 franz.sh usr/bin/franz")
    shelltools.system("install -Dm644 franz.desktop usr/share/applications/franz.desktop")
    shelltools.system("install -Dm644 franz.png usr/share/pixmaps/franz.png")

def install():
    pisitools.insinto("/", "usr")
    pisitools.insinto("/opt/", "franz")
