pipeline {
    agent any

    stages {
        stage('Start Containers') {
            steps {
                sh 'python3 scripts/start_containers.py'
            }
        }
        stage('Setup SDN Topology') {
            steps {
                sh 'python3 scripts/setup_sdn_topology.py'
            }
        }
        stage('Connectivity Test') {
            steps {
                sh 'python3 tests/connectivity_test.py'
            }
        }
    }
}
