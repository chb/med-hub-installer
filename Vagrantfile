# -*- mode: ruby -*-

if (defined?(ip)).nil?
  IP_ADDRESS = "192.168.88.22"
end

Vagrant.configure(2) do |config|
  config.vm.hostname = "med-hub"
  config.vm.box = "ubuntu/trusty64"
  config.vm.network :private_network, :ip => IP_ADDRESS

  config.vm.provider :virtualbox do |v|
    v.name = "med-hub"
    v.memory = 2048
    v.cpus = 2
  end

  # use cachier plugin if available
  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :box
  end

  # play Ansible
  config.vm.provision :ansible do |ansible|
    ansible.playbook = "playbook.yml"
    #ansible.verbose = "vvv"
    ansible.extra_vars = {
      vagrant_host: IP_ADDRESS
    }
  end
end
