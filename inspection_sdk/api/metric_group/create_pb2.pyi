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

from inspection_sdk.model.inspection.dim_pb2 import (
    InspectionDim as inspection_sdk___model___inspection___dim_pb2___InspectionDim,
)

from inspection_sdk.model.inspection.metric_group_pb2 import (
    InspectionMetricGroup as inspection_sdk___model___inspection___metric_group_pb2___InspectionMetricGroup,
)

from inspection_sdk.model.inspection.val_pb2 import (
    InspectionVal as inspection_sdk___model___inspection___val_pb2___InspectionVal,
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


class CreateMetricGroupRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    pluginId = ... # type: typing___Text
    id = ... # type: typing___Text
    name = ... # type: typing___Text
    memo = ... # type: typing___Text
    category = ... # type: typing___Text

    @property
    def dims(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[inspection_sdk___model___inspection___dim_pb2___InspectionDim]: ...

    @property
    def vals(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[inspection_sdk___model___inspection___val_pb2___InspectionVal]: ...

    def __init__(self,
        *,
        pluginId : typing___Optional[typing___Text] = None,
        id : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        memo : typing___Optional[typing___Text] = None,
        dims : typing___Optional[typing___Iterable[inspection_sdk___model___inspection___dim_pb2___InspectionDim]] = None,
        category : typing___Optional[typing___Text] = None,
        vals : typing___Optional[typing___Iterable[inspection_sdk___model___inspection___val_pb2___InspectionVal]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateMetricGroupRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateMetricGroupRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"category",b"category",u"dims",b"dims",u"id",b"id",u"memo",b"memo",u"name",b"name",u"pluginId",b"pluginId",u"vals",b"vals"]) -> None: ...

class CreateMetricGroupResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> inspection_sdk___model___inspection___metric_group_pb2___InspectionMetricGroup: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[inspection_sdk___model___inspection___metric_group_pb2___InspectionMetricGroup] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateMetricGroupResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateMetricGroupResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
