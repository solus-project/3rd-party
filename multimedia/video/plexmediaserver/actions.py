#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/"]
KeepSpecial = ["python"]
IgnoreAutodep = True

def setup():
    shelltools.system("ar xf plexmediaserver_%s-*_amd64.deb" % get.srcVERSION())
    shelltools.system("tar xvf data.tar.*")
    shelltools.system("sed -i 's/x-www-browser/xdg-open/' usr/share/applications/plexmediamanager.desktop")
    shelltools.system("wget https://raw.githubusercontent.com/solus-project/3rd-party/master/multimedia/video/plexmediaserver/files/plexmediaserver.conf")

    shelltools.system("wget https://raw.githubusercontent.com/solus-project/3rd-party/master/multimedia/video/plexmediaserver/files/plexmediaserver.tmpfile")
    shelltools.system("mkdir tmp")
    shelltools.system("mv plexmediaserver.tmpfile tmp/plexmediaserver.conf")

    shelltools.system("wget https://raw.githubusercontent.com/solus-project/3rd-party/master/multimedia/video/plexmediaserver/files/plexmediaserver.service")

def install():
    pisitools.insinto("/opt", "usr/lib/plexmediaserver")
    pisitools.insinto("/usr/lib64/sysusers.d", "plexmediaserver.conf")
    pisitools.insinto("/usr/lib64/tmpfiles.d", "tmp/plexmediaserver.conf")
    pisitools.insinto("/usr/lib64/systemd/system", "plexmediaserver.service")
    pisitools.insinto("/usr", "usr/share")
