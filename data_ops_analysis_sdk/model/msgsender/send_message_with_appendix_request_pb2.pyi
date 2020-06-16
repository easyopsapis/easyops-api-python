# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from data_ops_analysis_sdk.model.msgsender.send_message_request_data_pb2 import (
    SendMessageRequestData as data_ops_analysis_sdk___model___msgsender___send_message_request_data_pb2___SendMessageRequestData,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
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


class SendMessageWithAppendixRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def data(self) -> data_ops_analysis_sdk___model___msgsender___send_message_request_data_pb2___SendMessageRequestData: ...

    def __init__(self,
        *,
        data : typing___Optional[data_ops_analysis_sdk___model___msgsender___send_message_request_data_pb2___SendMessageRequestData] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SendMessageWithAppendixRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SendMessageWithAppendixRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> None: ...
