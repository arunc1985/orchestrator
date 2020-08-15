

echo "\n"
echo "Delete Processes and Images .."
docker rmi -f $(docker images -qa) && docker rm -f $(docker ps -qa)
docker rmi -f py-app-mongo:release-v1

echo "docker pull mongo"
docker pull mongo

echo "Run mongo container"
docker run -d -p 27017:27017 --name mongodb mongo

echo "docker logs mongodb"
docker logs mongodb

echo "Create a base-image for Python Centos (Refer file dockerfile-bases) and build the image"
docker build -t py-centos:bases -f dockerfile-bases .

echo "Create a image for python image which will use base image as py-centos:bases built in previous step"

docker rmi -f py-app-mongo:release-v1

echo "\n\n"
echo "Build Python App Image"
docker build -t py-app-mongo:release-v1 -f dockerfile .

echo "\n\n"
docker rm -f flaskpy3-mongo

echo "docker images "
docker images

echo "\n\n"
echo "Run the Python App"

docker run -d --name flaskpy3-mongo -v /c/Users/arunkuch/Documents/Programs/dockers/exercise006/application:/tests -e FLASKHOSTNAME='0.0.0.0' -e FLASKPORT=4500 -p 4500:4500 py-app-mongo:release-v1

echo "logs flaskpy3-mongo"
docker logs flaskpy3-mongo

docker ps 



docker network disconnect python-app-mongo mongodb
docker network disconnect python-app-mongo flaskpy3-mongo

docker network rm python-app-mongo


docker network create python-app-mongo
docker network connect python-app-mongo mongodb
docker network connect python-app-mongo flaskpy3-mongo
docker network ls


curl -XGET http://localhost:4500/hello_mongo/

