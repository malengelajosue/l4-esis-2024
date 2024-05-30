sudo apt-get remove --purge openssh-server  libssh-dev
sudo apt-get install openssh-server libssh-dev build-essential

git clone https://github.com/ansible/pylibssh.git
cd pylibssh
pip install tox --break-system-packages
tox -e build-dists



docker run nginx
docker run ubuntu
docker run alpine

sudo groupadd docker
sudo usermod -aG docker $USER