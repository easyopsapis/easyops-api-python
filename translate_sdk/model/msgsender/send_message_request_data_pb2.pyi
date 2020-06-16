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

from translate_sdk.model.msgsender.message_receiver_pb2 import (
    MessageReceiver as translate_sdk___model___msgsender___message_receiver_pb2___MessageReceiver,
)

from translate_sdk.model.msgsender.messsage_data_pb2 import (
    MessageData as translate_sdk___model___msgsender___messsage_data_pb2___MessageData,
)

from typing import (
    Iterable as typing___Iterable,
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


class SendMessageRequestData(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def receivers(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[translate_sdk___model___msgsender___message_receiver_pb2___MessageReceiver]: ...

    @property
    def msg_data(self) -> translate_sdk___model___msgsender___messsage_data_pb2___MessageData: ...

    def __init__(self,
        *,
        receivers : typing___Optional[typing___Iterable[translate_sdk___model___msgsender___message_receiver_pb2___MessageReceiver]] = None,
        msg_data : typing___Optional[translate_sdk___model___msgsender___messsage_data_pb2___MessageData] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SendMessageRequestData: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SendMessageRequestData: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"msg_data",b"msg_data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"msg_data",b"msg_data",u"receivers",b"receivers"]) -> None: ...
