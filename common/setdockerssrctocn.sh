#!/bin/bash
cat>/etc/docker/daemon.json<<EOF
{
  "registry-mirrors": ["https://registry.docker-cn.com"]
}
EOF
systemctl restart docker
