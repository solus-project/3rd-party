#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt", "/usr"]
IgnoreAutodep = True

# Should not change.
Suffix = "-1"

def setup():
    shelltools.system("pwd")
    shelltools.system("tar xf code-stable-code_1.5.2-1473686317_amd64.tar.gz")
    shelltools.system("install -dm755 opt/vscode-ms/")
    shelltools.system("install -dm755 usr/share/pixmaps/")
    shelltools.system("mv VSCode-linux-x64/* opt/vscode-ms/")
    shelltools.system("wget https://raw.githubusercontent.com/solus-project/3rd-party/master/programming/vscode-ms/extras/vscode.desktop")
    shelltools.system("install -Dm644 vscode.desktop usr/share/applications/vscode.desktop")
    shelltools.system("cp opt/vscode-ms/resources/app/resources/linux/code.png usr/share/pixmaps/code.png")
def install():
    pisitools.insinto("/", "opt")
    pisitools.insinto("/", "usr")
    pisitools.dosym("/opt/vscode-ms/bin/code", "/usr/bin/code")
