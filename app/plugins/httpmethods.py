from typing import Union, Literalf
from enum import Enum


class HttpMethod(Enum):
    get = ("get", "GET")
    post = ("post", "POST")
    put = ("put", "PUT")
    delete = ("delete", "DELETE")
    patch = ("patch", "PATCH")
    head = ("head", "HEAD")
    options = ("options", "OPTIONS")
    trace = ("trace", "TRACE")
