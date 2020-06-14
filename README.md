# awsLambda-python-CF
A sample project that shows the code example for AWS Lambda Function being coupled with Cloud Formation

This project is a sample application which shows how to use cloudFormation stack to create the Lambda Function when being using by code pipeline.
There are four file here as 
* lambda_function
* buildspec.yml
* CFnServiceRole.json
* samTemplate.yaml

# lambda_function
In _lambda_function_ file, the actual code of the lambda function is being defined.
The function imports _boto3_ library which helps us to connect and get resources of other AWS resources. In the code below, boto3 is being used to connect with ECS and from there we change the desire count of our service.

> NB. This project won't help you create a ECS cluster and its respective service and tasks.

# buildspec.yml
In our case the _buildspec.yml_ file is pretty simple. Since the project will be run by _Code Pipeline_ and which will trigger the _Cloud Formation_, so our buildspec.yml file also points to _Code Pipeline's_ template file names as _samTemplate.yaml_. 
In this buildspec file, you need to put your respective S3 bucket name where this code(the python code with the CFn template and alongside it's generated output file) will be zipped.

# CFnServiceRole.json
Before you create a Cloud Formation, we need some policies attached and for that, go to IAM and create a Role named 'CloudFormation-Lambda-ServiceRole' with role as 'AWSLambdaExecute' and save it. 
Again go to the IAM roles and search the role that has been just created and edit it to add inline policy and paste the role there.

> NB. XXX_XXX replace this part with your account id.

# samTemplate.yaml
This file describe the process how things works behind the scene. It first says it will work on AWS::Serverless::Function and we define the other resources as the handler and runtime and memory size along with timeout and other properties.
