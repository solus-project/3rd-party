#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

def setup():
    shelltools.system("tar xvf Popcorn-Time-%s-Linux-64.tar.xz" % (get.srcVERSION()))

def install():
    pisitools.insinto("/opt/popcorn-time", "*")
    pisitools.dosym("/opt/popcorn-time/Popcorn-Time", "/usr/bin/Popcorn-Time")
