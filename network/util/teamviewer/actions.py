#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

NoStrip = ["/opt"]
IgnoreAutodep = True

def install():
    pisitools.insinto("/etc/systemd/system/", "tv_bin/script/teamviewerd.service")
    pisitools.dosym("/etc/systemd/system/teamviewerd.service", "/etc/systemd/system/multi-user.target.wants/teamviewerd.service")
    pisitools.dosym("/opt/teamviewer/tv_bin/desktop/teamviewer-teamviewer11.desktop", "/usr/share/applications/teamviewer-teamviewer11.desktop")
    pisitools.dosym("/opt/teamviewer/tv_bin/desktop/teamviewer.png", "/usr/share/pixmaps/teamviewer.png")
    pisitools.insinto("/opt/teamviewer", "*")
    shelltools.system("chmod -R o+w %s/opt/teamviewer/logfiles" %get.installDIR())
    shelltools.system("chmod -R o+w %s/opt/teamviewer/config" %get.installDIR())
    shelltools.system("chmod o+w %s/opt/teamviewer" %get.installDIR())
