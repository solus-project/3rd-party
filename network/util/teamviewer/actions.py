#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import get, pisitools, shelltools

Version = get.srcVERSION()
WorkDir = "."
IgnoreAutodep = True

def build():
    shelltools.system("pwd")
    shelltools.system("ar xf teamviewer_%s_amd64.deb" % Version)
    shelltools.system("tar xf data.tar.xz")

def install():
    pisitools.insinto("/opt/", "./opt/*")
    pisitools.insinto("/etc/systemd/system", "./opt/teamviewer/tv_bin/script/teamviewerd.service")
    
    #necessary symlinks
    pisitools.dosym("/opt/teamviewer/tv_bin/script/teamviewer", "/usr/bin/teamviewer")
    pisitools.dosym("/opt/teamviewer/tv_bin/desktop/com.teamviewer.TeamViewer.desktop", "/usr/share/applications/teamviewer-teamviewer.desktop")
    pisitools.dosym("/etc/systemd/system/teamviewerd.service", "/etc/systemd/system/multi-user.target.wants/teamviewerd.service")    
    pisitools.dosym("/opt/teamviewer/tv_bin/desktop/teamviewer.png", "/usr/share/pixmaps/teamviewer.png")

    pisitools.dodir("/etc/teamviewer")
    pisitools.dodir("/var/log/teamviewer13")

    shelltools.chmod("%s/opt/teamviewer/doc/*" % get.installDIR(),0755)
    shelltools.chmod("%s/opt/teamviewer/tv_bin/*" % get.installDIR(),0755)
    
    # shelltools.system("systemctl start teamviewerd.service")
