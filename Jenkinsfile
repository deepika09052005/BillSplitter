
pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\kassl\\AppData\\Local\\Python\\bin\\python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'BillSplitter source code checked out from GitHub.'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"%PYTHON%" -m pip install -r backend\\requirements.txt'
            }
        }

        stage('Build Application') {
            steps {
                bat '"%PYTHON%" -m compileall -q backend'
                echo 'BillSplitter backend build completed.'
            }
        }

        stage('Verify Project Files') {
            steps {
                bat 'dir backend'
                bat 'dir frontend'
                echo 'Project files verified successfully.'
            }
        }
    }

    post {
        success {
            echo 'BillSplitter CI pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}
