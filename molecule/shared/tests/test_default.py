import os
import testinfra.utils.ansible_runner
import testinfra

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_kerl_is_installed(host):
    command = host.command("sudo kerl version")
    assert command.stdout.find("1.8.5") > -1, "no kerl installed"
