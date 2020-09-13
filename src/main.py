import os
from pathlib import Path

from drone import cmd, settings


def docker_compose(setting: dict):
    print(f'Setting: {setting}')
    host = setting.get('host', '').strip()
    key = setting.get('key', '').strip()
    project = setting['project'].strip()
    file = setting['file'].strip()
    scale = setting.get('scale', '').strip()
    p_scale = f'--scale {scale}' if scale else ''

    print('Creating ssh folder...')
    ssh_folder = Path(Path.home(), '.ssh')
    ssh_folder.mkdir()

    print('Adding key...')
    key_file = Path(ssh_folder, 'id_rsa')
    key_file.write_text(key)

    print('Adding host to known_hosts...')
    ssh_folder.chmod(700)
    _, address = host.split('@')
    cmd(f'ssh-keyscan {address} >> ~/.ssh/known_hosts')

    print('Running docker-compose...')
    cmd(f'docker-compose --project-name={project} --file={file} --host=ssh://{host} up -d {p_scale}')
    print('Done')


def main(name):
    handlers = {'docker-compose': docker_compose}
    fn = handlers[name]
    fn(settings())


if __name__ == '__main__':
    main(os.environ['HANDLER_FN'])
