#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
import os.path


def do_pack():
    ''' script that generates a .tgz archive from content
    of the web_static dir'''

    date = datetime.today()

    ftgz = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        date.year, date.month, date.day, date.hour, date.minute, date.second)

    if os.path.isdir("versions") is False:
        if local("sudo mkdir -p versions").failed is True:
            return None

    if local("tar -czvf {} web_static".format(ftgz)).failed is True:
        return None
    return ftgz
