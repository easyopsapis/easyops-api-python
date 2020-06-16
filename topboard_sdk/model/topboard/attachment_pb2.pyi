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

from topboard_sdk.model.topboard.issue_basic_pb2 import (
    IssueBasic as topboard_sdk___model___topboard___issue_basic_pb2___IssueBasic,
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


class Attachment(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text
    instanceId = ... # type: typing___Text
    type = ... # type: typing___Text
    filename = ... # type: typing___Text
    size = ... # type: typing___Text
    fileToConvert = ... # type: typing___Text

    @property
    def issue(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[topboard_sdk___model___topboard___issue_basic_pb2___IssueBasic]: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        instanceId : typing___Optional[typing___Text] = None,
        type : typing___Optional[typing___Text] = None,
        filename : typing___Optional[typing___Text] = None,
        size : typing___Optional[typing___Text] = None,
        fileToConvert : typing___Optional[typing___Text] = None,
        issue : typing___Optional[typing___Iterable[topboard_sdk___model___topboard___issue_basic_pb2___IssueBasic]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Attachment: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Attachment: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"fileToConvert",b"fileToConvert",u"filename",b"filename",u"instanceId",b"instanceId",u"issue",b"issue",u"name",b"name",u"size",b"size",u"type",b"type"]) -> None: ...
