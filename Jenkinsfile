pipeline {
    environment {
        REGISTRY_CREDENTIAL = "harbor-credential"
        dockerImage = ""
    }

    agent any
    stages {
        stage("Setup") {
            steps{
                sh "docker version"
                script {
                    DOCKER_REG = "registry.eevee.tw/lab"
                    IMAGE_NAME = "app/yctseng"
                }
            }   
        }
        stage("Build Docker Image") {
            steps{
                dir("simple-flask"){
                    script{
                        ImageName = "${IMAGE_NAME}"
                        dockerImage = docker.build(ImageName)
                    }
                }
            }   
        }
        stage("Test") {
            steps{
                sh "docker run --rm ${IMAGE_NAME} flask test"
            }   
        }
        stage("Push Docker Image") {
            steps{
                script {
                    docker.withRegistry( "https://${DOCKER_REG}", REGISTRY_CREDENTIAL ) {
                        dockerImage.push("latest")
                    }
                }
                echo "Remove unused images"
                sh "docker rmi ${IMAGE_NAME}"
            }
        }
    }
}
