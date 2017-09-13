#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Version =  get.srcVERSION()

def install():
    shutil.rmtree("Rider-%s/jre64" % Version)
    pisitools.insinto("/opt/rider", "Rider-%s/*" % Version)
    pisitools.dosym("/opt/rider/bin/rider.sh", "/usr/bin/rider")