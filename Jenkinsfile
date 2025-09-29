pipeline {
  agent any
  options { timestamps() }
  stages {
    stage('Checkout'){ steps { checkout scm } }
    stage('Test'){
      steps {
        sh '''
          python -m venv .venv
          . .venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
          pytest -q --cov=app --cov-report xml:coverage.xml
        '''
      }
    }
    stage('Docker Build'){
      steps { sh 'docker build -t docker.io/<your-dh-user>/mediquick:${BUILD_NUMBER} .' }
    }
  }
  post {
    always { archiveArtifacts artifacts: 'coverage.xml', allowEmptyArchive: true }
  }
}
