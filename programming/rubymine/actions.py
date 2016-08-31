#!/usr/bin/python

from pisi.actionsapi import pisitools
import shutil

WorkDir = "."


def install():
    shutil.rmtree("RubyMine-2016.2.2/jre")
    pisitools.insinto("/opt/rubymine", "RubyMine-2016.2.2/*")