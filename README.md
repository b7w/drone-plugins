Drone plugins
=============

[![Build Status](https://drone.b7w.me/api/badges/b7w/drone-plugins/status.svg)](https://drone.b7w.me/b7w/drone-plugins)


Build
----

`docker build -t drone/dc --build-arg HANDLER=docker-compose .`       


Test
----

`docker run --rm -v/home/user/docker-compose.yml:/docker-compose.yml:ro -eDRONE_HOST=root@example.com -eDRONE_KEY="$(< ~/.ssh/id_rsa)" -eDRONE_PROJECT=drone -eDRONE_FILE=/docker-compose.yml drone/dc:latest`       


About
-----

Assistant is open source project, released by MIT license.


Look, feel, be happy :-)
