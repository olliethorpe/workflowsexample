import aws_cdk as core
import aws_cdk.assertions as assertions

from ba_cloud_academy_github_cdk_olliethorpe.ba_cloud_academy_github_cdk_olliethorpe_stack import BaCloudAcademyGithubCdkOlliethorpeStack

# example tests. To run these tests, uncomment this file along with the example
# resource in ba_cloud_academy_github_cdk_olliethorpe/ba_cloud_academy_github_cdk_olliethorpe_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = BaCloudAcademyGithubCdkOlliethorpeStack(app, "ba-cloud-academy-github-cdk-olliethorpe")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
