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
    Value as google___protobuf___struct_pb2___Value,
)

from tool_sdk.model.cmdb.object_attr_value_struct_pb2 import (
    ObjectAttrValueStruct as tool_sdk___model___cmdb___object_attr_value_struct_pb2___ObjectAttrValueStruct,
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


class ObjectAttrValue(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    type = ... # type: typing___Text
    default_type = ... # type: typing___Text
    mode = ... # type: typing___Text
    prefix = ... # type: typing___Text
    start_value = ... # type: builtin___int
    series_number_length = ... # type: builtin___int

    @property
    def regex(self) -> google___protobuf___struct_pb2___Value: ...

    @property
    def default(self) -> google___protobuf___struct_pb2___Value: ...

    @property
    def struct_define(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[tool_sdk___model___cmdb___object_attr_value_struct_pb2___ObjectAttrValueStruct]: ...

    def __init__(self,
        *,
        type : typing___Optional[typing___Text] = None,
        regex : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        default_type : typing___Optional[typing___Text] = None,
        default : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        struct_define : typing___Optional[typing___Iterable[tool_sdk___model___cmdb___object_attr_value_struct_pb2___ObjectAttrValueStruct]] = None,
        mode : typing___Optional[typing___Text] = None,
        prefix : typing___Optional[typing___Text] = None,
        start_value : typing___Optional[builtin___int] = None,
        series_number_length : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ObjectAttrValue: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ObjectAttrValue: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"default",b"default",u"regex",b"regex"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"default",b"default",u"default_type",b"default_type",u"mode",b"mode",u"prefix",b"prefix",u"regex",b"regex",u"series_number_length",b"series_number_length",u"start_value",b"start_value",u"struct_define",b"struct_define",u"type",b"type"]) -> None: ...
