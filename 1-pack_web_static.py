#!/usr/bin/python3
"""
The 1-pack_web_static module
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from os.path import isfile
import datetime
import os
from fabric.api import local


def do_pack():
    """
    generate a .tgz archive from web_static with do_pack
    """
    now = datetime.datetime.now()
    archive = 'web_static_' + str(now.year) + str(now.month) +
    str(now.day) + str(now.hour) + str(now.minute) + str(now.second) + '.tgz'

    if os.path.isdir("versions") is False:
        local('mkdir -p versions')

    local("tar -cvzf versions/{} web_static".format(archive))
    if (isfile('version/{}'.format(archive))):
        return ('version/{}'.format(archive))
    else:
        return None
