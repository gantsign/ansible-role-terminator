Ansible Role: Terminator
========================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-terminator.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-terminator)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.terminator-blue.svg)](https://galaxy.ansible.com/gantsign/terminator)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-terminator/master/LICENSE)

Ansible role for installing the [Terminator](https://launchpad.net/terminator/)
terminal emulator.

Requirements
------------

* Ansible >= 2.5

* Ubuntu

    * Xenial (16.04)
    * Bionic (18.04)
    * Note: other Ubuntu versions may work but have not been tested.

Role Variables
--------------

None

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
     - role: gantsign.terminator
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
