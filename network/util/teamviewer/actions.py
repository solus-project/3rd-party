#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

Version = get.srcVERSION()
WorkDir = "."
NoStrip = ["/opt/teamviewer/tv_bin/wine/drive_c/TeamViewer/tvwine.dll.so"]
IgnoreAutodep = True

def build():
    shelltools.system("pwd")
    shelltools.system("ar xf teamviewer_%s_i386.deb" % Version)
    shelltools.system("tar xf data.tar.bz2")

def install():
    pisitools.insinto("/opt/", "./opt/*")
    pisitools.insinto("/etc/systemd/system", "./opt/teamviewer/tv_bin/script/teamviewerd.service")
    
    #necessary symlinks
    pisitools.dosym("/opt/teamviewer/tv_bin/script/teamviewer", "usr/bin/teamviewer")
    pisitools.dosym("/opt/teamviewer/tv_bin/desktop/com.teamviewer.TeamViewer.desktop", "/usr/share/applications/teamviewer-teamviewer12.desktop")
    pisitools.dosym("/etc/systemd/system/teamviewerd.service", "/etc/systemd/system/multi-user.target.wants/teamviewerd.service")    
    pisitools.dosym("/opt/teamviewer/tv_bin/desktop/teamviewer.png", "/usr/share/pixmaps/teamviewer.png")

    shelltools.chmod("%s/opt/teamviewer/doc/*" % get.installDIR(),0755)
    shelltools.chmod("%s/opt/teamviewer/tv_bin/*" % get.installDIR(),0755)
