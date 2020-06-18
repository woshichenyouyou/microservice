path=$(dirname "$PWD")

docker run -d --name jenkins_01 -p 8081:8080 -v $path/jenkins:/var/jenkins_home jenkins/jenkins:lts
