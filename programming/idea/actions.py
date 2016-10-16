#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."


def install():
    shutil.rmtree("idea-IU-162.2032.8/jre")
    pisitools.insinto("/opt/idea", "idea-IU-162.2032.8/*")
    pisitools.dosym("/opt/idea/bin/idea.sh", "/usr/bin/idea")