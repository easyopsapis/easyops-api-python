# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from assets_inventory_sdk.model.inspection.condition_pb2 import (
    InspectionCondition as assets_inventory_sdk___model___inspection___condition_pb2___InspectionCondition,
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


class InspectionVal(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id = ... # type: typing___Text
    name = ... # type: typing___Text
    memo = ... # type: typing___Text
    type = ... # type: typing___Text
    unit = ... # type: typing___Text
    weight = ... # type: builtin___int

    @property
    def conditions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[assets_inventory_sdk___model___inspection___condition_pb2___InspectionCondition]: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        memo : typing___Optional[typing___Text] = None,
        type : typing___Optional[typing___Text] = None,
        unit : typing___Optional[typing___Text] = None,
        weight : typing___Optional[builtin___int] = None,
        conditions : typing___Optional[typing___Iterable[assets_inventory_sdk___model___inspection___condition_pb2___InspectionCondition]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> InspectionVal: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> InspectionVal: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"conditions",b"conditions",u"id",b"id",u"memo",b"memo",u"name",b"name",u"type",b"type",u"unit",b"unit",u"weight",b"weight"]) -> None: ...
