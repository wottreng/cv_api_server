pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'wottreng/object-detection'
        DOCKER_TAG = "${BUILD_NUMBER}"
        DOCKER_LATEST = 'latest'
        DOCKER_REGISTRY_CREDENTIALS = 'docker-hub-credentials'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build image with build number tag
                    def image = docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")

                    // Tag the same image as latest
                    sh "docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:${DOCKER_LATEST}"
                }
            }
        }

        stage('Test Container') {
            steps {
                script {
                    // Test the container by running basic checks
                    docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").inside('-u root') {
                        // Check Python version
                        sh 'python --version'

                        // Validate the main application file exists
                        sh 'ls -la main.py'

                        // Run a syntax check on the main application
                        sh 'python -m py_compile main.py'
                    }
                }
            }
        }
    }

    post {
        always {
            // Clean up Docker images to save disk space
            script {
                sh "docker rmi ${DOCKER_IMAGE}:${DOCKER_TAG} || true"
                sh "docker rmi ${DOCKER_IMAGE}:${DOCKER_LATEST} || true"

                // Clean up dangling images
                sh 'docker image prune -f || true'
            }
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
