# Serverless Application Model (SAM) Tips

Due to this template quite pre-defined for easy to used but it might not applicable for all usecased below will explain how sam work and how to config each path

## Pre-require

- Connect with AWS Account for deploy from local

```bash
brew install aws-sam-cli
```

## About Project

The project is Boilerplate working with aws-sam-cli for template and deployment process empower by github actions already intregate the following coponents

- [CI/CD for Lambda work with AWS Sam](https://aws.amazon.com/blogs/compute/introducing-aws-sam-pipelines-automatically-generate-deployment-pipelines-for-serverless-applications/)

## Quick Start

Run from your development Machine

```bash
## Build Template before apply
sam build -t template-local.yaml
## Invoke event to your lambda locally
## if you dont have one run sam local generate-event and save to files
sam local invoke -e events/event.json
## More Detail 
sam local -h
```

### Work API Locally

```bash
sam local start-api
curl http://localhost:3000/
```

The SAM CLI reads the application template to determine the API's routes and the functions that they invoke. The `Events` property on each function's definition includes the route and method for each path. [more-info](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-start-api.html)

```yaml
      Events:
        HelloWorld:
          Type: Api
          Properties:
            Path: /hello
            Method: get
```

### Deploy from Local

Deployment from local using template-{env} This case using template `SIT` Env, Auth with your AWS Account before run

```bash
## Build Template before apply
sam build -t template-sit.yaml
## Deploy Lambda from Builded template
sam deploy --config-env sit --stack-name my-sam-test 
##  Cleanup Resource
sam delete --stack-name my-sam-test  
## OR you using sync from local and auto deploy to sit env by run
sam sync --stack-name <your-stack-name> # see at workflow stack-name variable
```

### Useful link Component Project

- [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)
- [SAM-Template](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification.html)
- [AWS-CLI-SAM-TEMPLATE](https://github.com/aws/aws-sam-cli-app-templates)
