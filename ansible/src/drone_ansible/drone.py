import os
import shlex
import subprocess


def cmd(command):
    args = shlex.split(command)
    output = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=None, check=False)
    print(str(output.stdout, encoding='utf-8'))
    if output.returncode:
        print('Exiting')
        exit(output.returncode)


def settings():
    envs = os.environ.items()
    if os.environ.get('DEBUG', '').lower() == 'true':
        print(envs)
    return dict([(k.replace('PLUGIN_', '').lower(), v) for k, v in envs if k.startswith('PLUGIN_')])
