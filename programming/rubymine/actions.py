#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Version =  get.srcVERSION()

def install():
    shutil.rmtree("RubyMine-%s/jre" % Version)
    pisitools.insinto("/opt/rubymine", "RubyMine-%s/*" % Version)
    pisitools.dosym("/opt/rubymine/bin/rubymine.sh", "/usr/bin/rubymine")