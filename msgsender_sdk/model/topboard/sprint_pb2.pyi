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

from msgsender_sdk.model.topboard.issue_basic_pb2 import (
    IssueBasic as msgsender_sdk___model___topboard___issue_basic_pb2___IssueBasic,
)

from msgsender_sdk.model.topboard.product_basic_pb2 import (
    ProductBasic as msgsender_sdk___model___topboard___product_basic_pb2___ProductBasic,
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


class Sprint(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text
    instanceId = ... # type: typing___Text
    title = ... # type: typing___Text
    status = ... # type: typing___Text
    goal = ... # type: typing___Text
    startTime = ... # type: typing___Text
    endTime = ... # type: typing___Text

    @property
    def product(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[msgsender_sdk___model___topboard___product_basic_pb2___ProductBasic]: ...

    @property
    def issues(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[msgsender_sdk___model___topboard___issue_basic_pb2___IssueBasic]: ...

    def __init__(self,
        *,
        product : typing___Optional[typing___Iterable[msgsender_sdk___model___topboard___product_basic_pb2___ProductBasic]] = None,
        issues : typing___Optional[typing___Iterable[msgsender_sdk___model___topboard___issue_basic_pb2___IssueBasic]] = None,
        name : typing___Optional[typing___Text] = None,
        instanceId : typing___Optional[typing___Text] = None,
        title : typing___Optional[typing___Text] = None,
        status : typing___Optional[typing___Text] = None,
        goal : typing___Optional[typing___Text] = None,
        startTime : typing___Optional[typing___Text] = None,
        endTime : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Sprint: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Sprint: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"endTime",b"endTime",u"goal",b"goal",u"instanceId",b"instanceId",u"issues",b"issues",u"name",b"name",u"product",b"product",u"startTime",b"startTime",u"status",b"status",u"title",b"title"]) -> None: ...
