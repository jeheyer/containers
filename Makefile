CLOUD_RUN_REGION := us-central1

include Makefile.env

all: gcp_setup app_engine cloud_build cloud_run_deploy
cloud-run: gcp-setup cloud-build cloud-run-deploy
docker: docker-build docker-push

gcp-setup:
	gcloud config set project $(PROJECT_ID)

app-engine:
	cd $(SERVICE_NAME)
	gcloud app deploy

cloud-build:
	cp requirements.txt $(SERVICE_NAME)/
	gcloud builds submit --tag gcr.io/$(PROJECT_ID)/$(SERVICE_NAME) $(SERVICE_NAME)

cloud-run-deploy:
	gcloud config set run/region $(CLOUD_RUN_REGION)
	gcloud run deploy $(SERVICE_NAME) --image gcr.io/$(PROJECT_ID)/$(SERVICE_NAME) --allow-unauthenticated

docker-build:
	cp requirements.txt $(SERVICE_NAME)/
	docker build -t $(DOCKER_NAMESPACE)/$(SERVICE_NAME) $(SERVICE_NAME)

docker-push:
	docker push $(DOCKER_NAMESPACE)/$(SERVICE_NAME)

docker-save:
	docker save $(DOCKER_NAMESPACE)/$(SERVICE_NAME):latest | gzip > $(SERVICE_NAME).tgz
