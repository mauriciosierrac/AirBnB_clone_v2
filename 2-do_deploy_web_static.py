#!/usr/bin/python3

from fabric.api import run
from fabric.api import put
from fabric.api import env
import os.path


env.hosts = ['34.75.52.228', '18.212.233.99']


def do_deploy(archive_path):
    ''' this method distributes an archive to your web servers'''

    if os.path.isfile(archive_path) is False:
        return False

    filel = archive_path.split('/')[-1]
    files = filel.split('.')[0]

    if put(archive_path, '/tmp/{}'.format(filel)).failed is True:
        return False

    if run('tar xzvf /tmp/{} -C /data/web_static/releases/{}/'.format(filel, files)).failed is True:
        return False

    if run('rm /tmp/{}'.format(filel)).failed is True:
        return False

    if run('rm -f /data/web_static/current').failed is True:
        return False

    if run('ln -sf /data/web_static/releases/{} /data/web_static/releases/current').failed is True:
        return False
    return True
