pipeline {
    agent any

    environment {
        COMPOSE_FILE = 'docker-compose.yml' // Define el archivo docker-compose a usar
    }

    stages {
        stage('Checkout') {
            steps {
                // Clona el repositorio de GitHub
                git branch: 'main', url: 'https://github.com/DiegoMarcel0/CRUD-Jefatura' 
            }
        }

        stage('Install Dependencies') {
            steps {
                // Instala dependencias del requirements.txt en un contenedor temporal
                bat 'docker run --rm -v $PWD:/app -w /app python:3.10 pip install -r requirements.txt'

            }
        }

        stage('Build and Start Services') {
            steps {
                // Construye y levanta los contenedores definidos en docker-compose.yml
                bat 'docker-compose up -d --build'
            }
        }

        stage('Run Application') {
            steps {
                echo 'La aplicación Django debería estar en ejecución en el contenedor ComisariaApp'
            }
        }

        stage('Check Docker Images') {
            steps {
                bat 'docker images'
            }
        }

    }

     /*post {
        always {
            // Detener y limpiar los contenedores al final del pipeline
            sh 'docker-compose down'
        }
    }*/
}