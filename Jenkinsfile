pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Shridhar2602/SE_assignment'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x fibonacci.py"
                sh "./fibonacci.py"
            }
        }
        stage('Test Code Passed') {
            steps {
                sh "chmod u+x unit_test_1.py"
                sh "./unit_test_1.py"
            }
        }
        stage('Test Code Failed') {
            steps {
                sh "chmod u+x unit_test_2.py"
                sh "./unit_test_2.py"
            }
        }
    } 
}