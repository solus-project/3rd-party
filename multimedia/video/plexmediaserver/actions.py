#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/"]
IgnoreAutodep = True

def setup():
    shelltools.system("ar xf plexmediaserver_%s-*_amd64.deb" % (get.srcVERSION()))
    shelltools.system("tar xvf data.tar.*")

def install():
    # root owns sandbox as it is setuid
    pisitools.insinto("/", "etc")
    pisitools.insinto("/", "usr")
    pisitools.insinto("/usr/lib/sysusers.d/plexmediaserver.conf", "files/plexmediaserver.conf")
    pisitools.insinto("/usr/lib/sysusers.d/plexmediaserver.conf", "files/plexmediaserver.conf")
