import os
import sys


def cmd(command):
    code = os.system(command)
    if code != 0:
        sys.exit(code)


def settings():
    envs = os.environ.items()
    return dict([(k.replace('DRONE_', '').lower(), v) for k, v in envs if k.startswith('DRONE')])
