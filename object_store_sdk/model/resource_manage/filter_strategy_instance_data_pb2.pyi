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

from google.protobuf.struct_pb2 import (
    Struct as google___protobuf___struct_pb2___Struct,
)

from object_store_sdk.model.resource_manage.filter_condition_group_pb2 import (
    FilterConditionGroup as object_store_sdk___model___resource_manage___filter_condition_group_pb2___FilterConditionGroup,
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


class FilterStrategyInstanceData(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id = ... # type: typing___Text
    strategyInstanceId = ... # type: typing___Text

    @property
    def data(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def filter(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[object_store_sdk___model___resource_manage___filter_condition_group_pb2___FilterConditionGroup]: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        strategyInstanceId : typing___Optional[typing___Text] = None,
        data : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        filter : typing___Optional[typing___Iterable[object_store_sdk___model___resource_manage___filter_condition_group_pb2___FilterConditionGroup]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FilterStrategyInstanceData: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FilterStrategyInstanceData: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"data",b"data",u"filter",b"filter",u"id",b"id",u"strategyInstanceId",b"strategyInstanceId"]) -> None: ...
