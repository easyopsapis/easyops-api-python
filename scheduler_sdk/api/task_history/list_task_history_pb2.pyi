# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class ListHistoryRequest(google___protobuf___message___Message):
    page = ... # type: int
    page_size = ... # type: int
    __select__ = ... # type: typing___Text
    __sortby__ = ... # type: typing___Text
    src_id = ... # type: typing___Text
    id = ... # type: typing___Text
    task_id = ... # type: typing___Text

    def __init__(self,
        page : typing___Optional[int] = None,
        page_size : typing___Optional[int] = None,
        __select__ : typing___Optional[typing___Text] = None,
        __sortby__ : typing___Optional[typing___Text] = None,
        src_id : typing___Optional[typing___Text] = None,
        id : typing___Optional[typing___Text] = None,
        task_id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListHistoryRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"__select__",u"__sortby__",u"id",u"page",u"page_size",u"src_id",u"task_id"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"__select__",b"__sortby__",b"id",b"page",b"page_size",b"src_id",b"task_id"]) -> None: ...

class ListHistoryResponse(google___protobuf___message___Message):
    class Annotations(google___protobuf___message___Message):
        appId = ... # type: typing___Text

        def __init__(self,
            appId : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ListHistoryResponse.Annotations: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"appId"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"appId"]) -> None: ...

    name = ... # type: typing___Text
    total_time = ... # type: int
    code = ... # type: int
    msg = ... # type: typing___Text
    id = ... # type: typing___Text
    start_time = ... # type: typing___Text
    user = ... # type: typing___Text
    end_time = ... # type: typing___Text
    org = ... # type: int
    src_id = ... # type: typing___Text
    task_id = ... # type: typing___Text
    job_type = ... # type: typing___Text
    tool_exec_id = ... # type: typing___Text
    total_status = ... # type: typing___Text

    @property
    def annotations(self) -> ListHistoryResponse.Annotations: ...

    def __init__(self,
        name : typing___Optional[typing___Text] = None,
        total_time : typing___Optional[int] = None,
        code : typing___Optional[int] = None,
        msg : typing___Optional[typing___Text] = None,
        id : typing___Optional[typing___Text] = None,
        start_time : typing___Optional[typing___Text] = None,
        user : typing___Optional[typing___Text] = None,
        end_time : typing___Optional[typing___Text] = None,
        org : typing___Optional[int] = None,
        src_id : typing___Optional[typing___Text] = None,
        task_id : typing___Optional[typing___Text] = None,
        job_type : typing___Optional[typing___Text] = None,
        tool_exec_id : typing___Optional[typing___Text] = None,
        total_status : typing___Optional[typing___Text] = None,
        annotations : typing___Optional[ListHistoryResponse.Annotations] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListHistoryResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"annotations"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"annotations",u"code",u"end_time",u"id",u"job_type",u"msg",u"name",u"org",u"src_id",u"start_time",u"task_id",u"tool_exec_id",u"total_status",u"total_time",u"user"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"annotations",b"annotations"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"annotations",b"code",b"end_time",b"id",b"job_type",b"msg",b"name",b"org",b"src_id",b"start_time",b"task_id",b"tool_exec_id",b"total_status",b"total_time",b"user"]) -> None: ...

class ListHistoryResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> ListHistoryResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[ListHistoryResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListHistoryResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...
