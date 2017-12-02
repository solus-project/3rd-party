#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."


def install():
    shutil.rmtree("PhpStorm-173.3727.138/jre64")
    pisitools.insinto("/opt/phpstorm", "PhpStorm-173.3727.138/*")
    pisitools.dosym("/opt/phpstorm/bin/phpstorm.sh", "/usr/bin/phpstorm")
