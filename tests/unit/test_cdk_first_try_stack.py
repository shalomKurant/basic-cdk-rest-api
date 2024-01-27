import aws_cdk as core
import aws_cdk.assertions as assertions

from book_store.book_store_stack import BookStoreStack

# example tests. To run these tests, uncomment this file along with the example
# resource in book_store/book_store_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = BookStoreStack(app, "cdk-first-try")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
