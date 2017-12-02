#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."


def install():
    shutil.rmtree("WebStorm-173.3727.108/jre64")
    pisitools.insinto("/opt/webstorm", "WebStorm-173.3727.108/*")
    pisitools.dosym("/opt/webstorm/bin/webstorm.sh", "/usr/bin/webstorm")
