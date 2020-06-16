# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.struct_pb2 import (
    Value as google___protobuf___struct_pb2___Value,
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


class ServicePort(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text
    port = ... # type: builtin___int
    protocol = ... # type: typing___Text
    nodePort = ... # type: builtin___int

    @property
    def targetPort(self) -> google___protobuf___struct_pb2___Value: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        port : typing___Optional[builtin___int] = None,
        protocol : typing___Optional[typing___Text] = None,
        targetPort : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        nodePort : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ServicePort: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ServicePort: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"targetPort",b"targetPort"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name",u"nodePort",b"nodePort",u"port",b"port",u"protocol",b"protocol",u"targetPort",b"targetPort"]) -> None: ...