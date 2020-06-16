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

from msgsender_sdk.model.inspection.arg_pb2 import (
    InspectionArg as msgsender_sdk___model___inspection___arg_pb2___InspectionArg,
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


class InspectionCollector(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id = ... # type: typing___Text
    name = ... # type: typing___Text
    content = ... # type: typing___Text
    script = ... # type: typing___Text

    @property
    def args(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[msgsender_sdk___model___inspection___arg_pb2___InspectionArg]: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        content : typing___Optional[typing___Text] = None,
        script : typing___Optional[typing___Text] = None,
        args : typing___Optional[typing___Iterable[msgsender_sdk___model___inspection___arg_pb2___InspectionArg]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> InspectionCollector: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> InspectionCollector: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"args",b"args",u"content",b"content",u"id",b"id",u"name",b"name",u"script",b"script"]) -> None: ...
