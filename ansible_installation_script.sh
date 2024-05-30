sudo apt install pipx
pipx install --include-deps ansible
pipx install ansible-core

pipx upgrade --include-injected ansible
pipx inject ansible argcomplete
pipx inject --include-apps ansible argcomplete
#Installing Ansible
python3 -m pip install --user ansible
python3 -m pip install --user ansible-core
python3 -m pip install --user ansible-core==2.12.3