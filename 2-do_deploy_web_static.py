#!/usr/bin/python3
"""
 Fabric script (based on the file 1-pack_web_static.py)
 that distributes an archive to your web servers,
 using the function do_deploy.
"""
from fabric.api import env
from fabric.operations import run, put, sudo
import os
env.hosts = ['35.229.26.94', '184.72.156.146']


def do_deploy(archive_path):
    """
        Function to deploy the Web Static on the server
    """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        filename = archive_path.split("/")[-1]
        path = "/data/web_static/releases"
        put("{}".format(archive_path), "/tmp/{}"
            .format(filename))
        foldername = filename.split(".")
        run("sudo mkdir -p {}/{}/"
            .format(path, foldername[0]))
        newfile = '.'.join(foldername)
        run("sudo tar -xzf /tmp/{} -C {}/{}/"
            .format(newfile, path, foldername[0]))
        run("sudo rm /tmp/{}"
            .format(filename))
        run("sudo mv {}/{}/web_static/* {}/{}/"
            .format(path, foldername[0], path, foldername[0]))
        run("sudo rm -rf {}/{}/web_static"
            .format(path, foldername[0]))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf {}/{} /data/web_static/current"
            .format(path, foldername[0]))
        return True
    except:
        return False
