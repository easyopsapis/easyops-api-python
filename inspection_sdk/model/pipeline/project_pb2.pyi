# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class Project(google___protobuf___message___Message):
    class Variables(google___protobuf___message___Message):
        key = ... # type: typing___Text
        value = ... # type: typing___Text

        def __init__(self,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> Project.Variables: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"key",b"value"]) -> None: ...

    id = ... # type: typing___Text
    name = ... # type: typing___Text
    favorite = ... # type: typing___Text
    tags = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    creator = ... # type: typing___Text
    ctime = ... # type: typing___Text
    mtime = ... # type: typing___Text
    repo_name = ... # type: typing___Text
    repo_id = ... # type: int
    name_with_namespace = ... # type: typing___Text
    path_with_namespace = ... # type: typing___Text
    git_ssh_url = ... # type: typing___Text
    git_http_url = ... # type: typing___Text
    link = ... # type: typing___Text
    default_branch = ... # type: typing___Text

    @property
    def variables(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Project.Variables]: ...

    def __init__(self,
        id : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        favorite : typing___Optional[typing___Text] = None,
        tags : typing___Optional[typing___Iterable[typing___Text]] = None,
        variables : typing___Optional[typing___Iterable[Project.Variables]] = None,
        creator : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[typing___Text] = None,
        mtime : typing___Optional[typing___Text] = None,
        repo_name : typing___Optional[typing___Text] = None,
        repo_id : typing___Optional[int] = None,
        name_with_namespace : typing___Optional[typing___Text] = None,
        path_with_namespace : typing___Optional[typing___Text] = None,
        git_ssh_url : typing___Optional[typing___Text] = None,
        git_http_url : typing___Optional[typing___Text] = None,
        link : typing___Optional[typing___Text] = None,
        default_branch : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Project: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"creator",u"ctime",u"default_branch",u"favorite",u"git_http_url",u"git_ssh_url",u"id",u"link",u"mtime",u"name",u"name_with_namespace",u"path_with_namespace",u"repo_id",u"repo_name",u"tags",u"variables"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"creator",b"ctime",b"default_branch",b"favorite",b"git_http_url",b"git_ssh_url",b"id",b"link",b"mtime",b"name",b"name_with_namespace",b"path_with_namespace",b"repo_id",b"repo_name",b"tags",b"variables"]) -> None: ...