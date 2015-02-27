Med Hub Installer
=================

[Vagrant][] and [ansible][] scripts to setup and run a VM hosting all components of Med-Hub:

- [medication-service][], port 8000 -> 18000
- [medication-app][], port 80 -> 10080
- MongoDB Backend, on port 27017

This will install _lighttpd_, configured to proxy requests on both ports through _supervisor_ to the _gunicorn_ ports the apps are running on.

Installing
----------

1. Install Vagrant and ansible
2. Install vagrant plugins:

        vagrant plugin install vagrant-vbguest

3. Install ansible galaxy items:

        ansible-galaxy install Stouts.mongodb

4. Clone this repo:

        git clone --recursive https://github.com/chb/med-hub-installer
        cd med-hub-installer

5. Since our app repos are private, we need a deployment key, one for each:
    - Create a new SSH key - without setting a passphrase - into a local file named `deploy_key.app` and `deploy_key.service` using `ssh-keygen`
    - Add these keys to the repo's "Deployment Keys" on GitHub

6. Adjust `settings.yml` to your liking
7. Adjust `config.service.py` and `config.app.py` to your liking
8. Get the VM configured and running:

        vagrant up

9. On your host machine you can now connect to the VM's hosted app at [http://192.168.88.22]() (or the URL you have configured).

[vagrant]: http://www.vagrantup.com/downloads
[ansible]: http://docs.ansible.com
[app]: https://github.com/chb/clinical-trials-app
[medication-service]: https://github.com/chb/medication-service/
[medication-app]: https://github.com/chb/medication-app
