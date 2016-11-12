#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools

def setup():
    shelltools.system("unzip platform-tools_r%s-linux.zip" % (get.srcVERSION()))

def install():
    pisitools.insinto("/usr/bin/", "platform-tools/adb")
    pisitools.insinto("/usr/bin/", "platform-tools/fastboot")
