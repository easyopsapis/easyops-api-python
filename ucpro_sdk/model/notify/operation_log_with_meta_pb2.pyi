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

from ucpro_sdk.model.notify.operation_log_pb2 import (
    OperationLog as ucpro_sdk___model___notify___operation_log_pb2___OperationLog,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class OperationLogWithMeta(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    system = ... # type: typing___Text
    topic = ... # type: typing___Text

    @property
    def data(self) -> ucpro_sdk___model___notify___operation_log_pb2___OperationLog: ...

    def __init__(self,
        *,
        system : typing___Optional[typing___Text] = None,
        topic : typing___Optional[typing___Text] = None,
        data : typing___Optional[ucpro_sdk___model___notify___operation_log_pb2___OperationLog] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> OperationLogWithMeta: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> OperationLogWithMeta: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"data",b"data",u"system",b"system",u"topic",b"topic"]) -> None: ...
