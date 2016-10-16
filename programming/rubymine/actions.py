#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."


def install():
    shutil.rmtree("RubyMine-2016.2.4/jre")
    pisitools.insinto("/opt/rubymine", "RubyMine-2016.2.4/*")
    pisitools.dosym("/opt/rubymine/bin/rubymine.sh", "/usr/bin/rubymine")