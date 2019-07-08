# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from model.msgsender.message_receiver_pb2 import (
    MessageReceiver as model___msgsender___message_receiver_pb2___MessageReceiver,
)

from model.msgsender.messsage_data_pb2 import (
    MessageData as model___msgsender___messsage_data_pb2___MessageData,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class SendMessageRequestData(google___protobuf___message___Message):

    @property
    def receivers(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[model___msgsender___message_receiver_pb2___MessageReceiver]: ...

    @property
    def msg_data(self) -> model___msgsender___messsage_data_pb2___MessageData: ...

    def __init__(self,
        receivers : typing___Optional[typing___Iterable[model___msgsender___message_receiver_pb2___MessageReceiver]] = None,
        msg_data : typing___Optional[model___msgsender___messsage_data_pb2___MessageData] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SendMessageRequestData: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"msg_data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"msg_data",u"receivers"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"msg_data",b"msg_data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"msg_data",b"receivers"]) -> None: ...