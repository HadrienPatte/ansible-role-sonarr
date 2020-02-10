import os

import testinfra.utils.ansible_runner

import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_group(host):
    group = host.group('sonarr')
    assert group.exists


def test_user(host):
    user = host.user('sonarr')
    assert user.name == 'sonarr'
    assert user.group == 'sonarr'


@pytest.mark.parametrize('name', [
    ('apt-transport-https'),
    ('sonarr'),
    ('nginx'),
])
def test_package_is_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize('name', [
    ('sonarr'),
    ('nginx'),
])
def test_service_is_running(host, name):
    service = host.service(name)
    assert service.is_running


@pytest.mark.parametrize('name', [
    ('sonarr'),
    ('nginx'),
])
def test_service_is_enabled(host, name):
    service = host.service(name)
    assert service.is_enabled


@pytest.mark.parametrize('port', [
    ('8989'),
    ('80'),
    ('443'),
])
def test_socket(host, port):
    assert host.socket('tcp://0.0.0.0:' + port).is_listening
