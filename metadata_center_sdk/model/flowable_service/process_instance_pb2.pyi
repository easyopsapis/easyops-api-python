# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
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


class ProcessInstance(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    instanceId = ... # type: typing___Text
    flowableInstanceId = ... # type: typing___Text
    name = ... # type: typing___Text
    creator = ... # type: typing___Text
    ctime = ... # type: typing___Text
    etime = ... # type: typing___Text
    status = ... # type: typing___Text
    stepIdList = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    stopAt = ... # type: typing___Text
    isSuspended = ... # type: builtin___bool
    isCancelled = ... # type: builtin___bool

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        flowableInstanceId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[typing___Text] = None,
        etime : typing___Optional[typing___Text] = None,
        status : typing___Optional[typing___Text] = None,
        stepIdList : typing___Optional[typing___Iterable[typing___Text]] = None,
        stopAt : typing___Optional[typing___Text] = None,
        isSuspended : typing___Optional[builtin___bool] = None,
        isCancelled : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ProcessInstance: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ProcessInstance: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"creator",b"creator",u"ctime",b"ctime",u"etime",b"etime",u"flowableInstanceId",b"flowableInstanceId",u"instanceId",b"instanceId",u"isCancelled",b"isCancelled",u"isSuspended",b"isSuspended",u"name",b"name",u"status",b"status",u"stepIdList",b"stepIdList",u"stopAt",b"stopAt"]) -> None: ...
