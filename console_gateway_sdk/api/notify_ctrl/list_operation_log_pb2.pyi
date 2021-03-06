# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from console_gateway_sdk.model.notify.operation_log_pb2 import (
    OperationLog as console_gateway_sdk___model___notify___operation_log_pb2___OperationLog,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
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


class ListOperationLogRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    object_id = ... # type: typing___Text
    instance_id = ... # type: typing___Text
    range = ... # type: typing___Text
    st = ... # type: typing___Text
    et = ... # type: typing___Text
    include_notifier = ... # type: builtin___bool
    app_id = ... # type: typing___Text
    target_id = ... # type: typing___Text
    event_id = ... # type: typing___Text
    parent_event_id = ... # type: typing___Text
    event = ... # type: typing___Text
    exclude_event = ... # type: typing___Text
    system = ... # type: typing___Text
    page = ... # type: builtin___int
    pageSize = ... # type: builtin___int
    status = ... # type: typing___Text
    device_id = ... # type: typing___Text
    operator = ... # type: typing___Text
    user = ... # type: typing___Text
    with_children = ... # type: builtin___bool
    exclude_system = ... # type: typing___Text
    without_total = ... # type: typing___Text
    ctime_order = ... # type: typing___Text
    query = ... # type: typing___Text
    topic = ... # type: typing___Text
    app_name = ... # type: typing___Text
    business = ... # type: typing___Text
    start_time = ... # type: typing___Text
    end_time = ... # type: typing___Text

    def __init__(self,
        *,
        object_id : typing___Optional[typing___Text] = None,
        instance_id : typing___Optional[typing___Text] = None,
        range : typing___Optional[typing___Text] = None,
        st : typing___Optional[typing___Text] = None,
        et : typing___Optional[typing___Text] = None,
        include_notifier : typing___Optional[builtin___bool] = None,
        app_id : typing___Optional[typing___Text] = None,
        target_id : typing___Optional[typing___Text] = None,
        event_id : typing___Optional[typing___Text] = None,
        parent_event_id : typing___Optional[typing___Text] = None,
        event : typing___Optional[typing___Text] = None,
        exclude_event : typing___Optional[typing___Text] = None,
        system : typing___Optional[typing___Text] = None,
        page : typing___Optional[builtin___int] = None,
        pageSize : typing___Optional[builtin___int] = None,
        status : typing___Optional[typing___Text] = None,
        device_id : typing___Optional[typing___Text] = None,
        operator : typing___Optional[typing___Text] = None,
        user : typing___Optional[typing___Text] = None,
        with_children : typing___Optional[builtin___bool] = None,
        exclude_system : typing___Optional[typing___Text] = None,
        without_total : typing___Optional[typing___Text] = None,
        ctime_order : typing___Optional[typing___Text] = None,
        query : typing___Optional[typing___Text] = None,
        topic : typing___Optional[typing___Text] = None,
        app_name : typing___Optional[typing___Text] = None,
        business : typing___Optional[typing___Text] = None,
        start_time : typing___Optional[typing___Text] = None,
        end_time : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListOperationLogRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListOperationLogRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"app_id",b"app_id",u"app_name",b"app_name",u"business",b"business",u"ctime_order",b"ctime_order",u"device_id",b"device_id",u"end_time",b"end_time",u"et",b"et",u"event",b"event",u"event_id",b"event_id",u"exclude_event",b"exclude_event",u"exclude_system",b"exclude_system",u"include_notifier",b"include_notifier",u"instance_id",b"instance_id",u"object_id",b"object_id",u"operator",b"operator",u"page",b"page",u"pageSize",b"pageSize",u"parent_event_id",b"parent_event_id",u"query",b"query",u"range",b"range",u"st",b"st",u"start_time",b"start_time",u"status",b"status",u"system",b"system",u"target_id",b"target_id",u"topic",b"topic",u"user",b"user",u"with_children",b"with_children",u"without_total",b"without_total"]) -> None: ...

class ListOperationLogResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    page = ... # type: builtin___int
    pageSize = ... # type: builtin___int
    total = ... # type: builtin___int

    @property
    def list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[console_gateway_sdk___model___notify___operation_log_pb2___OperationLog]: ...

    def __init__(self,
        *,
        page : typing___Optional[builtin___int] = None,
        pageSize : typing___Optional[builtin___int] = None,
        total : typing___Optional[builtin___int] = None,
        list : typing___Optional[typing___Iterable[console_gateway_sdk___model___notify___operation_log_pb2___OperationLog]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListOperationLogResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListOperationLogResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"list",b"list",u"page",b"page",u"pageSize",b"pageSize",u"total",b"total"]) -> None: ...

class ListOperationLogResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> ListOperationLogResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[ListOperationLogResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListOperationLogResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListOperationLogResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
