import shutil


def cmd_exists(cmd):
    """Check if required commands is installed"""
    return shutil.which(cmd) is not None
