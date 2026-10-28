
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'BillSplitter source code is ready for CI.'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r backend/requirements.txt'
            }
        }

        stage('Build Application') {
            steps {
                bat 'python -m compileall -q backend'
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
            echo 'BillSplitter CI pipeline failed. Check the Console Output.'
        }
    }
}
