#!/usr/bin/python3
"""
the 3-deploy_web_static.py module
Fabric script (based on the file 2-do_deploy_web_static.py) that
creates and distributes an archive to  web servers,
using the function deploy
"""
import datetime
import os
from os.path import isfile
from fabric.api import put, run, env, local
env.hosts = ['35.227.98.159', '104.196.65.233']


def do_pack():
    """
    generate a .tgz archive from web_static with do_pack
    """
    now = datetime.datetime.now()
    archive = 'web_static_' + str(now.year) + str(now.month) +\
        str(now.day) + str(now.hour) + str(now.minute) +\
        str(now.second) + '.tgz'

    if os.path.isdir("versions") is False:
        local('mkdir -p versions')

    local("tar -cvzf versions/{} web_static".format(archive))
    if (isfile('version/{}'.format(archive))):
        return ('version/{}'.format(archive))
    else:
        return None


def do_deploy(archive_path):
    """distributes an archive to web servers using do_deploy func
    """
    if (isfile(archive_path)) is False:
        return False

    noex = archive_path.split('/')[1].split('.')[0]
    ex = archive_path.split('/')[1]
    re = put(archive_path, "/tmp/")
    if re.failed:
        return False
    re = run('mkdir -p /data/web_static/releases/{}/'.format(noex))
    if re.failed:
        return False
    re = run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
        ex, noex))
    if re.failed:
        return False
    re = run('rm /tmp/{}.tgz'.format(noex))
    if re.failed:
        return False
    re = run('mv /data/web_static/releases/{}/web_static/* \
/data/web_static/releases/{}/'.format(noex, noex))
    if re.failed:
        return False
    re = run('rm -rf /data/web_static/releases/{}/web_static'.format(noex))
    if re.failed:
        return False
    re = run('rm -rf /data/web_static/current')
    if re.failed:
        return False
    re = run('ln -s /data/web_static/releases/{}/\
            /data/web_static/current'.format(noex))
    if re.failed:
        return False
    print("New version deployed")
    return True


def deploy():
    """creates and distributes an archive to your web servers, using
    the function deploy
    """
    path = do_pack()
    if not path:
        return False
    re = do_deploy(path)
    return re
