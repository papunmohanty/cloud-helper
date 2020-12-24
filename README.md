# Cloud Helper

The Cloud Helper is a basic wrapper over various cloud libraries
for different cloud providers. Which is a single point to connect
various cloud vendors and perform operations to the respective
cloud services.

## Installation

You can install the Cloud Helper from
[PyPI](https://pypi.org/project/cloud-helper/):

    pip install cloud-helper

The Cloud Helper is supported on Python 3.6 and above.

## How to use

One of the very reaason to create the library is to have a single
library which provides facilities of connecting to various cloud providers
and perform various operations.
Another reason is a way to run your application and decide whether the
application should connect to local cloud environment running in a
Docker container or to an original cloud service, with just a simple
environment variable set prior to run your application.

This powerfull feature will allow you to decide to run your application
in local docker environment or in a production environment **without changing
your code**.

### Example:

Install a local AWS environment.

Localstack is one of the great tool,
which can be install by using the following command:

```sh
$ pip install localstack
```

**NOTE -** make sure you have **Docker** installed before running localstack command

spin-up your localstack environment using Docker

```sh
$ localstack start
```

Localstack exposes a proxy URL:

    http://localhost:4566

Setup an environment variable using the above proxy url:

```sh
export AWS_LOCAL_PROXY=http://localhost:4566
```

Now you can use the code from this library
without passing any endpoint proxy url:

```py
from cloud_helper.aws_helper.connections import client

s3_client = client("s3")
```

```py
from cloud_helper.aws_helper.connections import resource

s3_resource = resource("s3")
```

```py
from cloud_helper.aws_helper.connections import Session

session = Session()
```

## Please Note

This library is under progress.

I as an author, will add different features in near future.

## License & copyright

Licensed under the [MIT License](LICENSE)
