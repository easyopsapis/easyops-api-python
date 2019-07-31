# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.struct_pb2 import (
    Struct as google___protobuf___struct_pb2___Struct,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class PermissionResource(google___protobuf___message___Message):
    name = ... # type: typing___Text
    system = ... # type: typing___Text

    @property
    def condition(self) -> google___protobuf___struct_pb2___Struct: ...

    def __init__(self,
        name : typing___Optional[typing___Text] = None,
        system : typing___Optional[typing___Text] = None,
        condition : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PermissionResource: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"condition"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"condition",u"name",u"system"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"condition",b"condition"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"condition",b"name",b"system"]) -> None: ...
