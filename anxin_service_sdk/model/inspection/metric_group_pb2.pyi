# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from anxin_service_sdk.model.inspection.dim_pb2 import (
    InspectionDim as anxin_service_sdk___model___inspection___dim_pb2___InspectionDim,
)

from anxin_service_sdk.model.inspection.val_pb2 import (
    InspectionVal as anxin_service_sdk___model___inspection___val_pb2___InspectionVal,
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


class InspectionMetricGroup(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id = ... # type: typing___Text
    name = ... # type: typing___Text
    category = ... # type: typing___Text
    memo = ... # type: typing___Text

    @property
    def dims(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[anxin_service_sdk___model___inspection___dim_pb2___InspectionDim]: ...

    @property
    def vals(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[anxin_service_sdk___model___inspection___val_pb2___InspectionVal]: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        category : typing___Optional[typing___Text] = None,
        dims : typing___Optional[typing___Iterable[anxin_service_sdk___model___inspection___dim_pb2___InspectionDim]] = None,
        vals : typing___Optional[typing___Iterable[anxin_service_sdk___model___inspection___val_pb2___InspectionVal]] = None,
        memo : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> InspectionMetricGroup: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> InspectionMetricGroup: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"category",b"category",u"dims",b"dims",u"id",b"id",u"memo",b"memo",u"name",b"name",u"vals",b"vals"]) -> None: ...
