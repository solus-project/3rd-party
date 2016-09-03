#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."


def install():
    shutil.rmtree("DataGrip-2016.2.2/jre")
    pisitools.insinto("/opt/datagrip", "DataGrip-2016.2.2/*")
    pisitools.dosym("/opt/datagrip/bin/datagrip.sh", "/usr/bin/datagrip")