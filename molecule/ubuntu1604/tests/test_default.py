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
