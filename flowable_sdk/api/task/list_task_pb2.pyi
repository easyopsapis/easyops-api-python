# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from flowable_sdk.model.flowable.task_pb2 import (
    FlowableTask as flowable_sdk___model___flowable___task_pb2___FlowableTask,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
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


class ListTaskRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    start = ... # type: builtin___int
    size = ... # type: builtin___int
    name = ... # type: typing___Text
    nameLike = ... # type: typing___Text
    description = ... # type: typing___Text
    priority = ... # type: typing___Text
    assignee = ... # type: typing___Text
    assigneeLike = ... # type: typing___Text
    processInstanceId = ... # type: typing___Text
    XXX_RestFieldMask = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    def __init__(self,
        *,
        start : typing___Optional[builtin___int] = None,
        size : typing___Optional[builtin___int] = None,
        name : typing___Optional[typing___Text] = None,
        nameLike : typing___Optional[typing___Text] = None,
        description : typing___Optional[typing___Text] = None,
        priority : typing___Optional[typing___Text] = None,
        assignee : typing___Optional[typing___Text] = None,
        assigneeLike : typing___Optional[typing___Text] = None,
        processInstanceId : typing___Optional[typing___Text] = None,
        XXX_RestFieldMask : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListTaskRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListTaskRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"XXX_RestFieldMask",b"XXX_RestFieldMask",u"assignee",b"assignee",u"assigneeLike",b"assigneeLike",u"description",b"description",u"name",b"name",u"nameLike",b"nameLike",u"priority",b"priority",u"processInstanceId",b"processInstanceId",u"size",b"size",u"start",b"start"]) -> None: ...

class ListTaskResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    total = ... # type: builtin___int
    start = ... # type: builtin___int
    sort = ... # type: typing___Text
    order = ... # type: typing___Text
    size = ... # type: builtin___int

    @property
    def data(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[flowable_sdk___model___flowable___task_pb2___FlowableTask]: ...

    def __init__(self,
        *,
        data : typing___Optional[typing___Iterable[flowable_sdk___model___flowable___task_pb2___FlowableTask]] = None,
        total : typing___Optional[builtin___int] = None,
        start : typing___Optional[builtin___int] = None,
        sort : typing___Optional[typing___Text] = None,
        order : typing___Optional[typing___Text] = None,
        size : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListTaskResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListTaskResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"data",b"data",u"order",b"order",u"size",b"size",u"sort",b"sort",u"start",b"start",u"total",b"total"]) -> None: ...

class ListTaskResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> ListTaskResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[ListTaskResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListTaskResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListTaskResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
