Drone plugins
=============

[![Build Status](https://drone.b7w.me/api/badges/b7w/drone-plugins/status.svg)](https://drone.b7w.me/b7w/drone-plugins)


Build
-----

```shell script
poetry install --extras docker-compose --extras ansible
```


Ansible playbook
----------------

Build: `docker build -t drone/ansible --build-arg HANDLER=ansible .`       
Run: `docker run --rm -v/home/user/playbook.yml:/playbook.yml:ro -ePLUGIN_VAULT_PASSWORD=root -ePLUGIN_PRIVATE_KEY="$(< ~/.ssh/id_rsa)" -ePLUGIN_PLAYBOOK=/playbook.yml drone/ansible:latest`       



Docker compose
--------------

Allow execute `docker-compose up -d` on remote server over ssh 

Build: `docker build -t drone/dc --build-arg HANDLER=docker-compose .`       
Run: `docker run --rm -v/home/user/docker-compose.yml:/docker-compose.yml:ro -ePLUGIN_HOST=root@example.com -ePLUGIN_KEY="$(< ~/.ssh/id_rsa)" -ePLUGIN_PROJECT=example -ePLUGIN_FILE=/docker-compose.yml registry.b7w.me/b7w/drone-plugin/docker-compose:latest`       




About
-----

Assistant is open source project, released by MIT license.


Look, feel, be happy :-)
