docker run -d --name jenkins_01 -p 8081:8080 -v /home/cyy/jenkins:/var/jenkins_home jenkins/jenkins:lts
docker exec -it b6df2b291d91 /bin/bash
