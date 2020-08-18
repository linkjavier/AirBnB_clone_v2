#!/usr/bin/python3
"""
 Fabric script (based on the file 1-pack_web_static.py)
 that distributes an archive to your web servers,
 using the function do_deploy.
"""
from fabric.api import *
from fabric.operations import run, put
import os
env.hosts = ['35.229.26.94', '184.72.156.146']


def do_deploy(filepath):
    """
        Function to deploy the Web Static on the server
    """
    if os.path.isfile(filepath) is False:
        return False
    try:
        filename = filepath.split("/")[-1]
        path = "/data/web_static/releases"
        put("{}".format(filepath), "/tmp/{}".format(filename))
        foldername = filename.split(".")
        run("mkdir -p {}/{}/".format(path, foldername[0]))
        newfile = '.'.join(foldername)
        run("tar -xzf /tmp/{} -C {}/{}/"
            .format(newfile, path, foldername[0]))
        run("rm /tmp/{}".format(filename))
        run("mv {}/{}/web_static/* {}/{}/"
            .format(path, foldername[0], path, foldername[0]))
        run("rm -rf {}/{}/web_static".format(path, foldername[0]))
        run("rm -rf /data/web_static/current")
        run("ln -sf {}/{} /data/web_static/current"
            .format(path, foldername[0]))
        return True
    except:
        return False
