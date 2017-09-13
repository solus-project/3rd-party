#!/usr/bin/python

from pisi.actionsapi import pisitools, shelltools


def setup():
    shelltools.system("ar xf unity-editor-5.5.0f3+20161125_amd64.deb")
    shelltools.system("tar xf data.tar.gz")


def install():
    shelltools.system("chmod 4755 opt/Unity/Editor/chrome-sandbox")
    pisitools.insinto("/opt/unity-editor", "opt/Unity/*")
    pisitools.insinto("/usr/share/icons", "usr/share/icons/*")
    pisitools.dosym("/opt/unity-editor/Editor/Unity", "/usr/bin/unity-editor")