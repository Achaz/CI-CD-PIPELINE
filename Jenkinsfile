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

        stage('Clone Gitops Repo Feature Branch') {          

            steps {
                sh 'rm -R CI-CD-PIPELINE'
                sh 'git clone -b main https://github.com/Achaz/CI-CD-PIPELINE.git'
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

        stage('Update Deployment Manifest') {

            steps {

                dir("CI-CD-PIPELINE") {
                    sh 'BUILD_NUMBER=${BUILD_NUMBER}'
                    sh 'sed -i "s/{{BUILD_NUMBER}}/$BUILD_NUMBER/g" argocd/deployments.yml'

                }
            }

        }  

        stage ('Updating the Deployment File') {

            environment {
                GIT_REPO_NAME = "CI-CD-PIPELINE"
                GIT_USER_NAME = "Achaz"
                GITHUB_TOKEN = credentials('GITHUB_TOKEN')
                
            }

            
            steps {

                withCredentials([gitUsernamePassword(credentialsId: 'github', gitToolName: 'Default')]){

                    dir("CI-CD-PIPELINE"){

                        sh '''                    
                        
                            git config  user.email "jtugume123@gmail.com"
                            git config  user.name "Achaz"
                            git remote set-url origin https://$GITHUB_TOKEN@github.com/Achaz/CI-CD-PIPELINE.git
                            git add -A
                            BUILD_NUMBER=${BUILD_NUMBER}
                            git commit -am "updated the image ${BUILD_NUMBER}" || true
                            git push origin main                            
                        
                        '''

                    }
                    
                }

            }

        }
               
    }
    
}


