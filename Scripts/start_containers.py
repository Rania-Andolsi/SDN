import docker

def start_containers():
    client = docker.from_env()

    try:
        # Démarrage des conteneurs SDN
        container_a = client.containers.run('opendaylight_controller_a', detach=True)
        container_b = client.containers.run('opendaylight_controller_b', detach=True)
        container_c = client.containers.run('opendaylight_controller_c', detach=True)

        print("Conteneurs SDN démarrés avec succès.")
    except docker.errors.APIError as e:
        print("Erreur lors du démarrage des conteneurs SDN :", str(e))

if __name__ == "__main__":
    start_containers()

