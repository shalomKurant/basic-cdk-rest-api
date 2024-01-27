from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_stepfunctions,
    aws_apigateway,
    aws_lambda,
    aws_dynamodb,
    RemovalPolicy
)
from constructs import Construct

from book_store.book_store_construct import BookStoreConstruct


class BookStoreStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        BookStoreConstruct(self, "BookStoreConstruct")