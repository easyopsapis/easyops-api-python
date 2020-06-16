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

from state_workflow_sdk.model.resource_manage.filter_condition_pb2 import (
    FilterCondition as state_workflow_sdk___model___resource_manage___filter_condition_pb2___FilterCondition,
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


class FilterConditionGroup(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text

    @property
    def conditionList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[state_workflow_sdk___model___resource_manage___filter_condition_pb2___FilterCondition]: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        conditionList : typing___Optional[typing___Iterable[state_workflow_sdk___model___resource_manage___filter_condition_pb2___FilterCondition]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FilterConditionGroup: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FilterConditionGroup: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"conditionList",b"conditionList",u"name",b"name"]) -> None: ...
