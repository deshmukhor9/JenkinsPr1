pipeline{
    agent any
    environment{
        python = 'C:\\Users\\deshm\\AppData\\Local\\Programs\\Python\\Python313'
    }
    stages{
        stage('Checkout code'){
            steps{
                checkout scm
            }
        }
        stage('Extract data'){
            steps{
                bat '${env.python} extract.py'
            }
        }
    }
    
}
