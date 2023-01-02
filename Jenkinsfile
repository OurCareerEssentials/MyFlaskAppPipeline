pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                //checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/OurCareerEssentials/MyFlaskAppPipeline.git']]])
                //git branch: 'main', url: 'https://github.com/OurCareerEssentials/MyFlaskAppPipeline.git'                                                
                sh 'pip3 install -r requirements.txt'
                sh 'sudo docker-compose build'
                sh 'sudo docker-compose up -d'
            }
        }
        stage('Test') { 
            steps {
                sh 'pytest test_unit_app.py'
                sh 'pytest test_integration_app.py' 
                sh 'pytest test_functional_app.py' 
                sh 'selenium functional_selenium.py' 
                sh 'sudo docker-compose down'
            }
        }
        stage('Release') { 
            steps {
                sh 'sudo docker tag flaskapp_app:latest ourcareeressentials/flaskapp-deployment'
                sh 'sudo docker push ourcareeressentials/flaskapp-deployment'
            }
        }
        stage('Deploy') { 
            steps {
                sh 'kubectl delete deploy flaskapp-deployment'
                sh 'kubectl apply -f mysql-deployment.yaml'
                sh 'kubectl apply -f deployment.yaml'
            }
        }
    }
}