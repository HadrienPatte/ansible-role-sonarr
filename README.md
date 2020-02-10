# Ansible Role: Sonarr

[![Build Status](https://travis-ci.com/HadrienPatte/ansible-role-sonarr.svg?branch=master)](https://travis-ci.com/HadrienPatte/ansible-role-sonarr)

An Ansible Role that installs Sonarr v3 on Debian.

## Requirements

None.

## Role Variables

* `sonarr_user`: name of the system user that runs sonarr, defaults to `sonarr`
* `sonarr_group`: group of the system user that runs sonarr. Any media files
  created by Sonarr will be writeable by this group. It's advisable to keep the
  group the same between download client, Sonarr and media centers. Defaults to
  `sonarr`

# Dependencies

None.

# Example Playbook

```yaml
- name: Install Sonarr v3.
  hosts: all
  roles:
    - hadrienpatte.sonarr
```

## License

MIT

## Author Information

Hadrien Patte [![PGP 0xFB500BB0](https://peegeepee.com/badge/orange/FB500BB0.svg)](https://peegeepee.com/FB500BB0)
