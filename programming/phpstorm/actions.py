#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Version = get.srcVERSION()

def install():
    shutil.rmtree("PhpStorm-%s/jre" % Version)
    pisitools.insinto("/opt/phpstorm", "PhpStorm-%s/*" % Version)
    pisitools.dosym("/opt/phpstorm/bin/phpstorm.sh", "/usr/bin/phpstorm")
