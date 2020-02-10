import os

import testinfra.utils.ansible_runner

import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
    ('apt-transport-https'),
    ('sonarr'),
])
def test_package_is_installed(host, name):
    package = host.package(name)
    assert package.is_installed
