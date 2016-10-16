#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."


def install():
    shutil.rmtree("pycharm-2016.2.3/jre")
    pisitools.insinto("/opt/pycharm", "pycharm-2016.2.3/*")
    pisitools.dosym("/opt/pycharm/bin/pycharm.sh", "/usr/bin/pycharm")