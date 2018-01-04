import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('file', [
    '/etc/default/docker',
    '/lib/systemd/system/docker.service'
])
def test_hosts_file(host, file):
    f = host.file(file)

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize('name', [
    'docker-ce'
])
def test_package(host, name):
    pkg = host.package(name)
    assert pkg.is_installed


@pytest.mark.parametrize('name', [
    'docker'
])
def test_service(host, name):
    service = host.service(name)
    assert service.is_enabled
#    assert service.is_running
