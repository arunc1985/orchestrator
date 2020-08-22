
echo "git pull origin dockers"
git pull origin dockers

echo "\n"
echo "Delete Processes and Images .."
docker rm -f $(docker ps -qa) && docker rmi -f $(docker images -qa)

echo "docker pull mongo - Pull mongo image from dockerhub repo"
docker pull mongo

echo "Run mongo container"
# docker run -d (as daemon) -p 27017:27017(port map) --name mongodb(cont name) mongo(image name)
docker run -d -p 27017:27017 --name mongodb mongo

echo "docker logs mongodb"
docker logs mongodb

echo "Create a base-image for Python Centos (Refer file dockerfile-bases) and build the image"
docker build -t py-centos:bases -f dockerfile-bases .

echo "Create a image for python image which will use base image as py-centos:bases built in previous step"
echo "\n\n"
echo "Build Python App Image"
docker build -t py-app-mongo:release-v1 -f dockerfile .

echo "list all docker images "
docker images

echo "\n\n"
echo "Run the Python App"

# Create a mount between host and container
# /root/orchestrator/containers/dockers/exercise006/application/:/tests
# the tests dir inside container will have contents of the host's application dir
# Whatever file you change in application dir, it will reflect inside the container
docker run -d --name flaskpy3-mongo \
	-v /root/orchestrator/containers/dockers/exercise006/application/:/tests \
	-e FLASKHOSTNAME='0.0.0.0' \
	-e FLASKPORT=4500 \
	-p 4500:4500 \
	py-app-mongo:release-v1

echo "logs flaskpy3-mongo"
docker logs flaskpy3-mongo

docker ps 


echo "Create a network named python-app-mongo "
# Disconnect container from network
docker network disconnect python-app-mongo mongodb
docker network disconnect python-app-mongo flaskpy3-mongo
# Delete the network
docker network rm network-python-mongo

echo "Connect mongo and python app containers to network named python-app-mongo "

# Create a new network 
docker network create network-python-mongo
# docker network create <<network-name>>
# Add python-app container and mongodb container to the above network "network-python-mongo"
# Before adding containers to network they must be in running state...
# Any n.o. containers can be connected to a network..
# Syntax : docker network connect <<network-name>> <<container-name>>/<<container-id>>
docker network connect network-python-mongo mongodb
docker network connect network-python-mongo flaskpy3-mongo
# List all the available networks
docker network ls

echo "Do a Curl and test data"
curl -XGET http://localhost:4500/hello_mongo/

