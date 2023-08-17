pipeline{

    agent any
    
    environment {
        AWS_ACCOUNT_ID="735873741347"
        AWS_DEFAULT_REGION="US-WEST-1"
        IMAGE_REPO_NAME="cicdpipeline"
        IMAGE_TAG="latest"
        REPOSITORY_URI= "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
    }

    stages{

        stage("Logging into AWS ECR"){

            steps{
                script {sh "aws ecr get-login-password --region us-west-1 | docker login --username AWS --password-stdin 735873741347.dkr.ecr.us-west-1.amazonaws.com"}
            }
            
        }

        stage("Cloning git"){

            steps{

                script {
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Achaz/CI-CD-PIPELINE.git']])
                }

            }
                           
        }

        stage ('Building Image'){

            steps {

                script {
                    dockerImage = docker.build "${IMAGE_REPO_NAME}:${IMAGE_TAG}"
                }

            }

        }

        stage ('Pushing to ECR') {

            steps {

                script{

                    docker.withRegistry('https://735873741347.dkr.ecr.us-west-1.amazonaws.com', 'ecr:us-west-1:aws-credentials') 
                    { 

                        dockerImage.push("${env.BUILD_NUMBER}")
                        dockerImage.push("latest")
                    
                    }
                }
            }
        }

        stage ('Updating the Deployment File') {

            environment {
                GIT_REPO_NAME = "CI-CD-PIPELINE"
                GIT_USER_NAME = "Achaz"
            }

            steps {

                withCredentials([string(credentialsId: 'github', variable: 'GITHUB_TOKEN')]){
                    sh '''
                    
                        git pull https://github.com/Achaz/CI-CD-PIPELINE.git
                        git config  user.email "jtugume123@gmail.com"
                        git config  user.name "Achaz"
                        BUILD_NUMBER=${BUILD_NUMBER}
                        sed -i "s/replaceImageTag/${BUILD_NUMBER}/g" CI-CD-Project/deployments.yml
                        git add ArgoCD/deployments.yml
                        git commit -m "updated the image ${BUILD_NUMBER}"
                        git push @github.com/${GIT_USER_NAME}/${GIT_REPO_NAME">@github.com/${GIT_USER_NAME}/${GIT_REPO_NAME">@github.com/${GIT_USER_NAME}/${GIT_REPO_NAME">https://${GITHUB_TOKEN}@github.com/${GIT_USER_NAME}/${GIT_REPO_NAME} HEAD:main
                        
                       
                    '''
                }

            }

        }
               
    }
    
}


