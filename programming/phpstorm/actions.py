#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Build = "181.5281.19"

def install():
    shutil.rmtree("PhpStorm-%s/jre64" % Build)
    pisitools.insinto("/opt/phpstorm", "PhpStorm-%s/*" % Build)
    pisitools.dosym("/opt/phpstorm/bin/phpstorm.sh", "/usr/bin/phpstorm")
