# erlang_kerl

Role to install kerl - tool for Erlang/OTP version management


## Requirements

- Ansible >= 2.7

###### Additional required packages

 - Ubuntu: 'build-essential', 'autoconf', 'libncurses5-dev', 'openssl', 'libssl-dev', 'fop', 'xsltproc', 'unixodbc-dev', 'git', 'make', 'automake', 'gcc'
 - CentOS: 'openssl-devel', 'automake', 'autoconf', 'ncurses-devel', 'gcc', 'perl', 'fop'

### Supported platforms

```yml
- EL
  - 7
- Ubuntu
  - bionic
  - xenial
```

## Default role variables

| Name | Description | Type | Default | Required |
| -----| ----------- | :--: | :------:| :------: |
| erlang_kerl__repo_url | URL path to the repo | string | `https://raw.githubusercontent.com/kerl/kerl/master/kerl` | True |
| erlang_kerl__repo_dest | Absolute path of where to download the file to | string | `/usr/bin/kerl` | True |
| erlang_kerl__build_version | Version of erlang to be installed | string | `example_overide` | True |
| erlang_kerl__build_dir | Path to the Erlang installation directory | string | `/usr/local/erlang` | True |
| erlang_kerl__build_path | Absolute path where erlang will be installed | string | `{{ erlang_kerl__build_dir }}/{{ erlang_kerl__build_version }}` | True |

**All default variables are described in [defaults/main.yml](defaults/main.yml) file.**

## Example Playbook

```yaml
    - hosts: all
      become: true
      roles:
        - role: zerodowntime.erlang_kerl
```

## License

[Apache License 2.0](LICENSE)

## Support

ZeroDowntime Team <support@zdt.io>

For more information about the project, please visit <https://www.zdt.io/building-blocks/>.
