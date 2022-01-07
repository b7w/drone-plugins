from drone_ansible.common import create_known_hosts, create_ssh_key, create_tmp_file
from drone_ansible.drone import cmd, settings


def ansible(setting: dict):
    private_key = setting['private_key'].strip()
    vault_password = setting['vault_password'].strip()
    inventory = setting['inventory'].strip()
    limit = setting.get('limit', '').strip()
    playbook = setting['playbook'].strip()

    create_ssh_key(private_key)
    vault_password_file = create_tmp_file(vault_password)
    limit_hosts = f'--limit={limit}' if limit else ''

    print('Running drone_ansible-playbook...')
    cmd(f'ansible-playbook'
        f' --inventory={inventory}'
        f' --vault-password-file={vault_password_file}'
        f' {limit_hosts}'
        f' {playbook}')
    print('Done')


def docker_compose(setting: dict):
    host = setting.get('host', '').strip()
    key = setting.get('key', '').strip()
    project = setting['project'].strip()
    file = setting['file'].strip()
    scale = setting.get('scale', '').strip()
    p_scale = f'--scale {scale}' if scale else ''

    create_ssh_key(key)
    create_known_hosts(host)

    print('Running docker-compose...')
    cmd(f'docker-compose --project-name={project} --file={file} --host=ssh://{host} up -d {p_scale}')
    print('Done')


def main():
    ansible(settings())


if __name__ == '__main__':
    main()
