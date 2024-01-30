import docker

# Connect to the Docker daemon
client = docker.from_env()

# Start OpenDaylight containers
client.containers.run('opendaylight/odl:latest', detach=True, ports={'6653/tcp': 6653})

# Start other containers as needed

print("Containers started successfully")
