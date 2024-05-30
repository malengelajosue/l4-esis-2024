sudo ip tuntap add mode tap tap0
sudo ip addr add 10.10.10.10/24 dev tap0
sudo ip link set dev tap0 up