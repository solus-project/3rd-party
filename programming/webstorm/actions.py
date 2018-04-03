#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."


def install():
    shutil.rmtree("WebStorm-181.4203.535/jre64")
    pisitools.insinto("/opt/webstorm", "WebStorm-181.4203.535/*")
    pisitools.dosym("/opt/webstorm/bin/webstorm.sh", "/usr/bin/webstorm")
