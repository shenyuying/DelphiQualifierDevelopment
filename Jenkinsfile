pipeline {
  agent any
  stages {
    stage('Precheck') {
      steps {
        sh '''echo "Hello World!"
echo $PATH'''
      }
    }
    stage('Preparation') {
      steps {
        git(poll: true, url: 'https://github.com/shenyuying/DelphiQualifierDevelopment.git', branch: 'master')
      }
    }
    stage('deployLeopard1') {
      steps {
        sh 'echo "Deployment"'
      }
    }
    stage('Verification') {
      steps {
        sh 'echo "python"'
        sh 'python ./verification.py'
      }
    }
    stage('final check') {
      steps {
        sh 'pwd'
      }
    }
  }
}