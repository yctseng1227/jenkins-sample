pipeline {
    environment {
        imagename = "registry.macacahub.tw/lab/yctseng-app"
        registryCredential = 'harbor-credential'
        dockerImage = ''
    }
    agent any
    stages {
        stage('Setup') {
            steps{
                dir('simple-flask'){
                    sh 'pwd'
                }
            }
        }
        stage('Build') {
            steps{
                dir('simple-flask'){
                    sh 'pwd'
                    script{
                        dockerImage = docker.build(imagename)
                    }
                    
                }
            }   
        }
        stage('Deploy Image') {
            steps{
                script {
                    docker.withRegistry( 'https://registry.macacahub.tw/', registryCredential ) {
                        dockerImage.push("$BUILD_NUMBER")
                        dockerImage.push('latest')
                    }
                }
            }
        }
        stage('Remove Unused docker image') {
            steps{
                sh "docker rmi $imagename:$BUILD_NUMBER"
                sh "docker rmi $imagename:latest"
            }
        }
        /*
        stage('Test') {
            steps{
                dir('simple-flask'){
                    sh 'pwd'
                    script{
                        docker.image(dockerImage).withRun(){
                            sh 'docker run -d --rm -p 8888:80'
                            sh 'curl 127.0.0.1:8888'
                        }
                    }
                }
            }
        }
        */
    }
}
