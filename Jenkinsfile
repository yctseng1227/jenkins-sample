pipeline {
    environment {
        REGISTRY_CREDENTIAL = 'harbor-credential'
        dockerImage = ''
    }
    parameters{
        string (name: 'DOCKER_REG', defaultValue: 'registry.eevee.tw/lab',  description: 'Docker registry')
        string (name: 'IMAGE_NAME', defaultValue: 'app/yctseng',  description: 'Image name')
    }

    agent any
    stages {
        stage('Setup') {
            steps{
                sh 'docker version'
            }
        }
        stage('Build') {
            steps{
                dir('simple-flask'){
                    script{
                        ImageName = "${DOCKER_REG}/${IMAGE_NAME}"
                        dockerImage = docker.build(ImageName)
                    }
                }
            }   
        }
        stage('Test') {
            steps{
                sh "docker run --rm ${IMAGE_NAME} flask test"
            }   
        }
        stage('Deploy') {
            steps{
                script {
                    docker.withRegistry( "https://${DOCKER_REG}", REGISTRY_CREDENTIAL ) {
                        //dockerImage.push("$BUILD_NUMBER")
                        dockerImage.push("latest")
                    }
                }
                echo "Remove unused images"
                //sh "docker rmi $imagename:$BUILD_NUMBER"
                sh "docker rmi ${IMAGE_NAME}"
            }
        }
    }
}
