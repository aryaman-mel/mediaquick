pipeline {
  agent any
  environment {
    DOCKER_IMAGE = 'docker.io/aryaman124/mediquick'
  }
  options { timestamps() }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Test') {
      steps {
        sh '''
          python3 -m venv .venv
          . .venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
          # (No pytest yet; project has no tests. Add later if you want.)
          # sanity: check Flask can import
          python - <<'PY'
import importlib
importlib.import_module("app")
print("import OK")
PY
        '''
      }
    }

    stage('Docker Build') {
      steps {
        sh '''
          docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} .
          docker tag ${DOCKER_IMAGE}:${BUILD_NUMBER} ${DOCKER_IMAGE}:latest
        '''
      }
    }

    stage('Push Image') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', passwordVariable: 'DH_PASS', usernameVariable: 'DH_USER')]) {
          sh '''
            echo "$DH_PASS" | docker login -u "$DH_USER" --password-stdin
            docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}
            docker push ${DOCKER_IMAGE}:latest
          '''
        }
      }
    }
  }

  post {
    always {
      // if you later produce coverage.xml, this will archive it
      archiveArtifacts artifacts: 'coverage.xml', allowEmptyArchive: true
      sh 'docker logout || true'
    }
  }
}
