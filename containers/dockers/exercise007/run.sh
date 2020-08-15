
docker rmi -f volumes-tests-flask:v1

docker build -t volumes-tests-flask:v1 -f dockerfile .

docker rm -f flaskpy3

docker run -d -v /root/orchestrator/containers/dockers/exercise007/application/:/tests --name flaskpy3 -e FLASKHOSTNAME='0.0.0.0' -e FLASKPORT=5500 -e CODER='By Arun!' -p 5500:5500 volumes-tests-flask:v1


curl -XGET http://localhost:5500/welcome/Arun/Chandramouli


docker tag volumes-tests-flask:v1 jupiter19/jupiter19:volumes-tests-flask:v1
docker push jupiter19/jupiter19
