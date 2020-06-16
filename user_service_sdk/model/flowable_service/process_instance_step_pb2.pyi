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

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)

from user_service_sdk.model.flowable_service.process_variable_pb2 import (
    ProcessVariable as user_service_sdk___model___flowable_service___process_variable_pb2___ProcessVariable,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class ProcessInstanceStep(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    instanceId = ... # type: typing___Text
    userTaskId = ... # type: typing___Text
    flowableTaskId = ... # type: typing___Text
    creator = ... # type: typing___Text
    ctime = ... # type: typing___Text
    etime = ... # type: typing___Text
    operator = ... # type: typing___Text
    status = ... # type: typing___Text
    otime = ... # type: typing___Text
    action = ... # type: typing___Text
    memo = ... # type: typing___Text
    formHeaderData = ... # type: typing___Text
    formBodyData = ... # type: typing___Text

    @property
    def variables(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[user_service_sdk___model___flowable_service___process_variable_pb2___ProcessVariable]: ...

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        userTaskId : typing___Optional[typing___Text] = None,
        flowableTaskId : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[typing___Text] = None,
        etime : typing___Optional[typing___Text] = None,
        operator : typing___Optional[typing___Text] = None,
        status : typing___Optional[typing___Text] = None,
        otime : typing___Optional[typing___Text] = None,
        action : typing___Optional[typing___Text] = None,
        memo : typing___Optional[typing___Text] = None,
        variables : typing___Optional[typing___Iterable[user_service_sdk___model___flowable_service___process_variable_pb2___ProcessVariable]] = None,
        formHeaderData : typing___Optional[typing___Text] = None,
        formBodyData : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ProcessInstanceStep: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ProcessInstanceStep: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"action",b"action",u"creator",b"creator",u"ctime",b"ctime",u"etime",b"etime",u"flowableTaskId",b"flowableTaskId",u"formBodyData",b"formBodyData",u"formHeaderData",b"formHeaderData",u"instanceId",b"instanceId",u"memo",b"memo",u"operator",b"operator",u"otime",b"otime",u"status",b"status",u"userTaskId",b"userTaskId",u"variables",b"variables"]) -> None: ...
