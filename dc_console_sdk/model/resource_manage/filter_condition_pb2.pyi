# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from dc_console_sdk.model.resource_manage.filter_data_source_pb2 import (
    FilterDataSource as dc_console_sdk___model___resource_manage___filter_data_source_pb2___FilterDataSource,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
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


class FilterCondition(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text
    compare = ... # type: typing___Text

    @property
    def left(self) -> dc_console_sdk___model___resource_manage___filter_data_source_pb2___FilterDataSource: ...

    @property
    def right(self) -> dc_console_sdk___model___resource_manage___filter_data_source_pb2___FilterDataSource: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        compare : typing___Optional[typing___Text] = None,
        left : typing___Optional[dc_console_sdk___model___resource_manage___filter_data_source_pb2___FilterDataSource] = None,
        right : typing___Optional[dc_console_sdk___model___resource_manage___filter_data_source_pb2___FilterDataSource] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FilterCondition: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FilterCondition: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"left",b"left",u"right",b"right"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"compare",b"compare",u"left",b"left",u"name",b"name",u"right",b"right"]) -> None: ...
