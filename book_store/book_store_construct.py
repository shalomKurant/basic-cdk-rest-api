from constructs import Construct
from aws_cdk import (
    aws_apigateway,
    aws_lambda,
    CfnOutput,
)
from aws_cdk.aws_lambda_python_alpha import PythonLayerVersion
import re
import os
import shutil


class BookStoreConstruct(Construct):
    def __init__(self, scope: Construct, construct_id: str):
        super().__init__(scope, construct_id)
        self.rest_api_name = "BookStoreApi"

        runtime = aws_lambda.Runtime.PYTHON_3_11

        layer_folder = create_cdk_layer_folder("BookStoreLayer", "requirements.txt")

        layer = PythonLayerVersion(
            self,
            "BookStoreLayer",
            layer_version_name=construct_id,
            entry=layer_folder,
            compatible_runtimes=[runtime],
        )
        books_base_lambda = aws_lambda.Function(
            self,
            'BooksBaseLambda',
            runtime=runtime,
            code=aws_lambda.Code.from_asset('./api'),
            handler='http_creator.handler',
        )

        books_base_lambda.add_layers(layer)

        api = aws_apigateway.LambdaRestApi(
            self,
            'book-store-api-gateway',
            rest_api_name=self.rest_api_name,
            handler=books_base_lambda,
        )
        output_name = f"{self.rest_api_name}GatewayURL"
        CfnOutput(scope, id=output_name, value=api.url).override_logical_id(output_name)



BUILD_FOLDER = ".build"
ROOT_DIR = "ROOT_DIR"

def create_cdk_build_folder(cdk_build_folder: str) -> None:
    os.makedirs(cdk_build_folder, exist_ok=True)


def _create_resource_build_folder(resource_name: str) -> str:
    build_folder = os.path.join(get_root_dir(), BUILD_FOLDER)
    create_cdk_build_folder(build_folder)
    resource_folder = os.path.join(build_folder, to_snake(resource_name))
    os.makedirs(resource_folder, exist_ok=True)
    return resource_folder


def create_cdk_lambdas_folder(lambda_name: str, root_handler_path: str) -> str:
    lambda_folder = _create_resource_build_folder(lambda_name)
    build_folder_with_root = os.path.join(lambda_folder, os.path.basename(root_handler_path))
    handler_path_from_root = os.path.join(get_root_dir(), root_handler_path)
    shutil.copytree(handler_path_from_root, build_folder_with_root, dirs_exist_ok=True)
    return lambda_folder


def create_cdk_layer_folder(layer_name: str, path_to_requirements: str) -> str:
    layer_folder = _create_resource_build_folder(layer_name)
    shutil.copyfile(path_to_requirements, os.path.join(layer_folder, "requirements.txt"))
    return layer_folder


def get_root_dir() -> str:
    return _get_environment_variable(ROOT_DIR)


def _get_environment_variable(name: str) -> str:
    try:
        return "cdk_first_try"
        return os.environ[name]
    except KeyError:
        raise KeyError(f"{name} is not set! Please deploy using the deploy.py script!") from None


def to_snake(string: str) -> str:
    string = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", string)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", string).lower().replace("-", "_")
