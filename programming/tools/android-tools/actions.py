#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools

def setup():
    shelltools.system("unzip platform-tools_r25-linux.zip")

def install():
    pisitools.insinto("/usr/bin/", "platform-tools/adb")
    pisitools.insinto("/usr/bin/", "platform-tools/fastboot")
