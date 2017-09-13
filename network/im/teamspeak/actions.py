#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("sed -i -e 's|^MS_PrintLicense$||g' TeamSpeak3-Client-linux_amd64-%s.run" % Version)
    shelltools.system("bash ./TeamSpeak3-Client-linux_amd64-%s.run --target opt/teamspeak3" % Version)

def install():
    pisitools.insinto("/", "opt")
    pisitools.dosym("/opt/teamspeak3/ts3client_runscript.sh", "/usr/bin/ts3client_linux_amd64")
