# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from model.ops_automation.job_tasks_pb2 import (
    JobTasks as model___ops_automation___job_tasks_pb2___JobTasks,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class ListJobTasksRequest(google___protobuf___message___Message):
    page = ... # type: int
    pageSize = ... # type: int
    taskId = ... # type: typing___Text
    execUser = ... # type: typing___Text
    jobId = ... # type: typing___Text
    trigger = ... # type: typing___Text
    resourceType = ... # type: typing___Text
    status = ... # type: typing___Text
    startTime = ... # type: typing___Text
    endTime = ... # type: typing___Text

    def __init__(self,
        page : typing___Optional[int] = None,
        pageSize : typing___Optional[int] = None,
        taskId : typing___Optional[typing___Text] = None,
        execUser : typing___Optional[typing___Text] = None,
        jobId : typing___Optional[typing___Text] = None,
        trigger : typing___Optional[typing___Text] = None,
        resourceType : typing___Optional[typing___Text] = None,
        status : typing___Optional[typing___Text] = None,
        startTime : typing___Optional[typing___Text] = None,
        endTime : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListJobTasksRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"endTime",u"execUser",u"jobId",u"page",u"pageSize",u"resourceType",u"startTime",u"status",u"taskId",u"trigger"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"endTime",b"execUser",b"jobId",b"page",b"pageSize",b"resourceType",b"startTime",b"status",b"taskId",b"trigger"]) -> None: ...

class ListJobTasksResponse(google___protobuf___message___Message):
    page = ... # type: int
    page_size = ... # type: int
    total = ... # type: int

    @property
    def list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[model___ops_automation___job_tasks_pb2___JobTasks]: ...

    def __init__(self,
        page : typing___Optional[int] = None,
        page_size : typing___Optional[int] = None,
        total : typing___Optional[int] = None,
        list : typing___Optional[typing___Iterable[model___ops_automation___job_tasks_pb2___JobTasks]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListJobTasksResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"list",u"page",u"page_size",u"total"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"list",b"page",b"page_size",b"total"]) -> None: ...

class ListJobTasksResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> ListJobTasksResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[ListJobTasksResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListJobTasksResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...
