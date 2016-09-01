#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."


def install():
    shutil.rmtree("clion-2016.2.1/jre")
    pisitools.insinto("/opt/clion", "clion-2016.2.1/*")
    pisitools.dosym("/opt/clion/bin/clion.sh", "/usr/bin/clion")