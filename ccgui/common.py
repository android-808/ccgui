import os
import pkg_resources

def get_version():
    """
    Returns the program version from the egg metadata

    :returns: the version of Deluge
    :rtype: string

    """
    return pkg_resources.require("ccgui")[0].version

def get_image(filename):
    return resource("ccgui", os.path.join("data","pixmaps",filename))

def resource(module, path):
    return pkg_resources.require("ccgui>=%s" % get_version())[0].get_resource_filename(
        pkg_resources._manager, os.path.join(*(module.split('.')+[path]))
    )
