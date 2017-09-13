#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Version =  get.srcVERSION()

def install():
    shutil.rmtree("clion-%s/jre64" % Version)
    pisitools.insinto("/opt/clion", "clion-%s/*" % Version)
    pisitools.dosym("/opt/clion/bin/clion.sh", "/usr/bin/clion")
