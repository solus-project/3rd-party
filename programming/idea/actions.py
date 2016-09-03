#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."


def install():
    shutil.rmtree("idea-IU-162.1812.17/jre")
    pisitools.insinto("/opt/idea", "idea-IU-162.1812.17/*")
    pisitools.dosym("/opt/idea/bin/idea.sh", "/usr/bin/idea")