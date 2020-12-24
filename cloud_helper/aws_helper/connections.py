import os
import boto3


def aws_local_url():
    """
    Looks for the AWS local Environment proxy address
    """
    if os.environ.get("AWS_LOCAL_PROXY"):
        return os.environ.get("AWS_LOCAL_PROXY")
    else:
        return None


def client(service_name, *args, **kwargs):
    """
    Create a wrapper client by name using the boto3.client.

    See: py:meth:`boto3.client`.
    """
    client = boto3.client(
        service_name, endpoint_url=aws_local_url(), *args, **kwargs)
    return client


class Session(boto3.session.Session):
    """
    Same as boto3.resource 
    With added benifit of referring to Local AWS proxy URL
    """

    def __init__(self, *args, **kwargs):
        super(Session, self).__init__(*args, **kwargs)

    def client(self, service_name, *args, **kwargs):
        return super(Session, self).client(service_name, endpoint_url=aws_local_url())

    def resource(self, *args, **kwargs):
        return super(Session, self).resource(endpoint_url=aws_local_url())


def resource(service_name, *args, **kwargs):
    """
    Same as boto3.resource 
    With added benifit of referring to Local AWS proxy URL
    """
    return boto3.resource(
        service_name, endpoint_url=aws_local_url(), *args, **kwargs)
