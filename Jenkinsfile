pipeline {
  agent any
  stages {
    stage('Precheck') {
      steps {
        sh '''echo "Hello World!"
echo $PATH'''
        sh 'python ./precheck.py'
      }
    }
    stage('Preparation') {
      steps {
        git(poll: true, url: 'https://github.com/shenyuying/DelphiQualifierDevelopment.git', branch: 'master')
      }
    }
    stage('deployLeopard1') {
      steps {
        sh 'echo "Deployment1"'
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