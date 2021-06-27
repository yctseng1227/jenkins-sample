pipeline {
    environment {
        REGISTRY_CREDENTIAL = "harbor-credential"
    }

    agent any
    stages {
        stage("Setup") {
            steps {
                sh "docker version"
                script {
                    DOCKER_REG = "registry.eevee.tw/lab"
                    IMAGE_NAME = "app/yctseng"
                }
            }   
        }
        stage("Build Docker Image") {
            steps {
                dir("simple-flask") {
                    script {
                        ImageName = "${DOCKER_REG}/${IMAGE_NAME}"
                        DockerImage = docker.build(ImageName)
                    }
                }
            }   
        }
        stage("Test Docker Image") {
            steps {
                sh "docker run --rm ${DOCKER_REG}/${IMAGE_NAME} flask test"
            }   
        }
        stage("Push Docker Image") {
            steps {
                script {
                    docker.withRegistry("https://${DOCKER_REG}", REGISTRY_CREDENTIAL) {
                        DockerImage.push("latest")
                    }
                }
                echo "Remove unused images"
                sh "docker rmi ${DOCKER_REG}/${IMAGE_NAME}"
            }
        }
    }
}
