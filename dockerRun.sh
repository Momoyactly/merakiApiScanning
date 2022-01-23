docker stop testFlask 
docker rm testFlask
docker run --name testFlask -d -p 80:5000 flask-docker