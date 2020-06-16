# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from influxdb_service_sdk.model.cmdb.user_pb2 import (
    User as influxdb_service_sdk___model___cmdb___user_pb2___User,
)

from influxdb_service_sdk.model.topboard.issue_basic_pb2 import (
    IssueBasic as influxdb_service_sdk___model___topboard___issue_basic_pb2___IssueBasic,
)

from typing import (
    Iterable as typing___Iterable,
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


class Comment(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text
    instanceId = ... # type: typing___Text
    ctime = ... # type: typing___Text
    body = ... # type: typing___Text
    parentId = ... # type: typing___Text

    @property
    def issue(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[influxdb_service_sdk___model___topboard___issue_basic_pb2___IssueBasic]: ...

    @property
    def author(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[influxdb_service_sdk___model___cmdb___user_pb2___User]: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        instanceId : typing___Optional[typing___Text] = None,
        issue : typing___Optional[typing___Iterable[influxdb_service_sdk___model___topboard___issue_basic_pb2___IssueBasic]] = None,
        ctime : typing___Optional[typing___Text] = None,
        body : typing___Optional[typing___Text] = None,
        parentId : typing___Optional[typing___Text] = None,
        author : typing___Optional[typing___Iterable[influxdb_service_sdk___model___cmdb___user_pb2___User]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Comment: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Comment: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"author",b"author",u"body",b"body",u"ctime",b"ctime",u"instanceId",b"instanceId",u"issue",b"issue",u"name",b"name",u"parentId",b"parentId"]) -> None: ...
