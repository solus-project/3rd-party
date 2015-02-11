#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/usr"]
IgnoreAutodep = True

Version = get.srcVERSION()

def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf opera-stable_%s_amd64.deb" % Version)
    shelltools.system("tar xvf data.tar.xz")

def install():
    # root owns sandbox as it is setuid
    shelltools.system("chown root:root usr/lib/x86_64-linux-gnu/opera/opera_sandbox")
    # ensure setuid
    shelltools.system("chmod 4755 usr/lib/x86_64-linux-gnu/opera/opera_sandbox")
    pisitools.insinto("/", "usr")

    # Because ew.
    pisitools.move("%s/usr/lib/x86_64-linux-gnu/*" % get.installDIR(), "%s/usr/lib" % get.installDIR())
    pisitools.removeDir("/usr/lib/x86_64-linux-gnu")
    pisitools.removeDir("/usr/share/lintian")

    pisitools.remove("/usr/bin/opera")
    pisitools.dosym("/usr/lib/opera/opera", "/usr/bin/opera")
