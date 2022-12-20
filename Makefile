# Runs the docker image to test locally
run:
	docker ps --filter name=rigel* --filter status=running -aq | xargs docker stop
	docker build --progress=plain . -t rigel
	docker run -d -it --rm --gpus all -p 7070:7070 rigel

# Uploads the latest image to Cloud Run
push:
	gcloud builds submit --tag gcr.io/gpt-3-for-web/rigel-v1

# Deploys the latest image to Cloud Run
deploy:
	gcloud run deploy rigel-v1 --image gcr.io/gpt-3-for-web/rigel-v1 --platform managed --region us-central1 --allow-unauthenticated --memory 32Gi --cpu 8

%:
	@:

.PHONY: run, push, deploy