#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

def setup():
    shelltools.system("pwd")
    shelltools.system("tar xvf code-stable-vscode-amd64.deb.tar.xz")
    shelltools.system("install -dm755 opt/vscode-ms/")
    shelltools.system("install -dm755 usr/bin")
    shelltools.system("install -dm755 usr/share/pixmaps/")
    shelltools.system("mv VSCode-linux-x64/* opt/vscode-ms/")
    shelltools.system("wget https://raw.githubusercontent.com/solus-project/3rd-party/master/programming/vscode-ms/extras/vscode.desktop")
    shelltools.system("install -Dm644 vscode.desktop usr/share/applications/vscode.desktop")
    shelltools.system("cp opt/vscode-ms/resources/app/resources/linux/code.png usr/share/pixmaps/code.png")
def install():
    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")
