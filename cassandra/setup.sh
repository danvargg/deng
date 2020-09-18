# Install java
sudo apt install openjdk-8-jdk -y
java -version

# Add the GPG keys
wget -q -O - https://www.apache.org/dist/cassandra/KEYS | sudo apt-key add -

# Add and enable the Apache Cassandra repository
sudo sh -c 'echo "deb http://www.apache.org/dist/cassandra/debian 311x main" > /etc/apt/sources.list.d/cassandra.list'

# Get the latest package from the repository
sudo apt update

# Install Apache Cassandra
sudo apt install cassandra -y

# Verify the Apache Cassandra service is installed and running
systemctl status cassandra

# Configuring Apache Cassandra
/etc/cassandra/cassandra.yaml
# cluster_name: your preferred cluster name
# seeds: set of IP address of nodes separated by a comma
# storage_port: the data storage port, must be allowed in the firewall
# listen_address: sets the port where Apache Cassandra should listen
# native_transport_port: port for clients to connect with Cassandra, must also be allowed in the firewall

# Testing Apache Cassandra
nodetool status

# Cassandra command line
cqlsh