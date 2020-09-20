import tempfile
from pathlib import Path

from drone_ansible.drone import cmd


def create_known_hosts(host):
    _, address = host.split('@')
    cmd(f'ssh-keyscan {address} >> ~/.ssh/known_hosts')


def create_ssh_key(key):
    print('Creating ssh folder...')
    ssh_folder = Path(Path.home(), '.ssh')
    ssh_folder.mkdir()
    ssh_folder.chmod(0o700)
    print('Adding private key...')
    key_file = Path(ssh_folder, 'id_rsa')
    key_file.write_text(key)
    key_file.chmod(0o600)


def create_tmp_file(content):
    with tempfile.NamedTemporaryFile(delete=False) as fp:
        fp.write(bytes(content, encoding='utf-8'))
        return fp.name
