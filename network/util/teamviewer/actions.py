#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

WorkDir = "."
NoStrip = ["/opt/teamviewer/tv_bin/wine/drive_c/TeamViewer/tvwine.dll.so"]
IgnoreAutodep = True

def install():
    pisitools.insinto("/opt/teamviewer", "*")
    
    #necessary symlinks
    pisitools.dosym("/opt/teamviewer/tv_bin/script/teamviewer", "usr/bin/teamviewer")
    pisitools.dosym("/opt/teamviewer/logfiles", "var/log/teamviewer")
    pisitools.dosym("/opt/teamviewer/config", "etc/teamviewer")
    pisitools.dosym("/opt/teamviewer/tv_bin/desktop/teamviewer-teamviewer11.desktop", "/usr/share/applications/teamviewer-teamviewer11.desktop")
    pisitools.dosym("/etc/systemd/system/teamviewerd.service", "/etc/systemd/system/multi-user.target.wants/teamviewerd.service")
    pisitools.dosym("/opt/teamviewer/tv_bin/desktop/teamviewer.png", "/usr/share/pixmaps/teamviewer.png")

    shelltools.chmod("%s/opt/teamviewer/*" % get.installDIR(),0755)  
