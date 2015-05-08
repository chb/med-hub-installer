Med Hub Installer
=================

[Vagrant][] and [ansible][] scripts to setup and run a VM hosting all components of Med-Hub:

- [medication-service][], port `8000` -> `18000`
- [medication-app][], port `80` -> `10080`
- MongoDB Backend, on port `27017`

This will install _lighttpd_, configured to proxy requests on both ports through _supervisor_ to the _gunicorn_ ports the apps are running on.

Installing
----------

1. Install Vagrant and ansible
2. Install vagrant plugins:

        vagrant plugin install vagrant-vbguest
        vagrant plugin install vagrant-proxyconf    # only if behind proxy

3. Install ansible galaxy items:

        ansible-galaxy install Stouts.mongodb

4. Clone this repo:

        git clone --recursive https://github.com/chb/med-hub-installer
        cd med-hub-installer

5. Since our app repos are private, we need a deployment key, one for each:
    - Create a new SSH key - without setting a passphrase - into a local file named `deploy_key.app` and `deploy_key.service` using `ssh-keygen`
    - Add these keys to the repo's "Deployment Keys" on GitHub

6. _Optionally_, if you're behind a proxy, add your proxy settings and make sure you installed the _proxyconf_ plugin in step 2:
    - In `Vagrantfile`, adjust `config.proxy.*`

7. Adjust `settings.yml` to your liking
8. Adjust `config.service.py` and `config.app.py` to your liking
9. Get the VM configured and running:

        vagrant up

10. On your host machine you can now connect to the VM's hosted app at [192.168.88.22](http://192.168.88.22) (or the URL you have configured in `Vagrantfile`).
11. The first time **medication-service** is installed, you will need to initialize its RxNorm database, see below.


RxNorm
------

Before any medication task works, the VM needs to have a local RxNorm database for _medication-service_.
The service repo contains a script that sets up a SQLite3 database and populates a MongoDB automatically.

1. Download the latest full RxNorm release [from NLM](http://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html) and place the ZIP in the installer's directory.
    This makes it available under `/vagrant` from inside the VM.
2. SSH into the VM:
    
        vagrant ssh
    
3. Copy (or move) the RxNorm ZIP into the service's root directory:
    
        sudo cp /vagrant/RxNorm_full_xxxxxxxx.zip /var/www/html/medication-service/
    
4. As the web user, activate the virtual environment and run the setup script.
    This will start the import into _SQLite_ and indexing, then produce mapping and fill the VM's _Mongo_ database, which will take a few minutes.

        cd /var/www/html/medication-service
        sudo -u www-data bash
        . env/bin/activate
        ./setup.sh
    
    > For whatever reason, the script would sometimes complain that I did not have `sqlite3` installed.
    > If this happens while it is in fact installed you will need to comment out the early exit in `medication-service/UMLS/databases/rxnorm.sh` line 18.

Digital Ocean
-------------

To provision a droplet, run the ansible playbook directly after creating a `hosts` file containing:

    [medhub]
    1.2.3.4 ansible_connection=ssh ansible_ssh_user=root

Now run with:

    $ ansible-playbook -i hosts playbook.yml

This assumes that you have setup your droplet to have your SSH key.


[vagrant]: http://www.vagrantup.com/downloads
[ansible]: http://docs.ansible.com
[app]: https://github.com/chb/clinical-trials-app
[medication-service]: https://github.com/chb/medication-service/
[medication-app]: https://github.com/chb/medication-app
