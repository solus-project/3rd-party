#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Version =  get.srcVERSION()

def install():
    shutil.rmtree("pycharm-community-%s/jre" % Version)
    pisitools.insinto("/opt/pycharm-ce", "pycharm-community-%s/*" % Version)
    pisitools.dosym("/opt/pycharm-ce/bin/pycharm.sh", "/usr/bin/pycharm-ce")
