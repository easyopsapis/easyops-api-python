# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from model.easy_command.task_detail_pb2 import (
    TaskDetail as model___easy_command___task_detail_pb2___TaskDetail,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class LiquibaseTaskCallbackRequest(google___protobuf___message___Message):

    @property
    def command(self) -> model___easy_command___task_detail_pb2___TaskDetail: ...

    def __init__(self,
        command : typing___Optional[model___easy_command___task_detail_pb2___TaskDetail] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> LiquibaseTaskCallbackRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"command"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"command"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"command",b"command"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"command"]) -> None: ...

class LiquibaseTaskCallbackResponse(google___protobuf___message___Message):
    status = ... # type: typing___Text

    def __init__(self,
        status : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> LiquibaseTaskCallbackResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"status"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"status"]) -> None: ...

class LiquibaseTaskCallbackResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> LiquibaseTaskCallbackResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[LiquibaseTaskCallbackResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> LiquibaseTaskCallbackResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...
