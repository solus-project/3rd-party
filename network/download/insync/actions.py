#!/usr/bin/python

# Created For Solus Operating System

from pisi.actionsapi import pisitools, shelltools, get

NoStrip = ["/etc", "/usr"]


def setup():
    shelltools.system("ar xf insync_{}-trusty_amd64.deb".format(get.srcVERSION()) )
    shelltools.system("tar xvf data.tar.gz")

    # enable status indicators the in nautilus file manager; requires the package
    #    nautilus-python to be installed (should be installed automatically as
    #    a dependency from pspec.xml)
    shelltools.system("ar xf insync-nautilus_{}-precise_all.deb".format(get.srcVERSION() ) )
    shelltools.system("tar xvf data.tar.gz")

    # a similar package exists for the caja file manager but requires python-caja
    #    to be packaged for Solus first

def install():
    pisitools.insinto("/", "etc")
    pisitools.insinto("/", "usr")
