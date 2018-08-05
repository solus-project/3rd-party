#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."


def install():
    shutil.rmtree("WebStorm-173.4674.32/jre64")
    pisitools.insinto("/opt/webstorm", "WebStorm-173.4674.32/*")
    pisitools.dosym("/opt/webstorm/bin/webstorm.sh", "/usr/bin/webstorm")
