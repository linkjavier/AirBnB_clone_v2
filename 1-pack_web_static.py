#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
        Function that save the Web_proyect in a .tgz file
        with actual date on name.
    """
    now = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    filename = "versions/web_static_{}.tgz".format(now)
    try:
        local("mkdir -p ./versions")
        local("tar --create --verbose -z --file={} ./web_static"
              .format(filename))
        return filename
    except:
        return None
