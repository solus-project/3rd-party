#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Version =  get.srcVERSION()

def install():
    shutil.rmtree("DataGrip-%s/jre64" % Version)
    pisitools.insinto("/opt/datagrip", "DataGrip-%s/*" % Version)
    pisitools.dosym("/opt/datagrip/bin/datagrip.sh", "/usr/bin/datagrip")
