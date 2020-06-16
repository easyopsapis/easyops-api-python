# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class Repository(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    repo_name = ... # type: typing___Text
    repo_id = ... # type: builtin___int
    name_with_namespace = ... # type: typing___Text
    path_with_namespace = ... # type: typing___Text
    git_ssh_url = ... # type: typing___Text
    git_http_url = ... # type: typing___Text
    link = ... # type: typing___Text
    default_branch = ... # type: typing___Text

    def __init__(self,
        *,
        repo_name : typing___Optional[typing___Text] = None,
        repo_id : typing___Optional[builtin___int] = None,
        name_with_namespace : typing___Optional[typing___Text] = None,
        path_with_namespace : typing___Optional[typing___Text] = None,
        git_ssh_url : typing___Optional[typing___Text] = None,
        git_http_url : typing___Optional[typing___Text] = None,
        link : typing___Optional[typing___Text] = None,
        default_branch : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Repository: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Repository: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"default_branch",b"default_branch",u"git_http_url",b"git_http_url",u"git_ssh_url",b"git_ssh_url",u"link",b"link",u"name_with_namespace",b"name_with_namespace",u"path_with_namespace",b"path_with_namespace",u"repo_id",b"repo_id",u"repo_name",b"repo_name"]) -> None: ...
