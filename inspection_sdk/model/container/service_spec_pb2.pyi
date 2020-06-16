# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.struct_pb2 import (
    Struct as google___protobuf___struct_pb2___Struct,
)

from inspection_sdk.model.container.service_port_pb2 import (
    ServicePort as inspection_sdk___model___container___service_port_pb2___ServicePort,
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


class ServiceSpec(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    type = ... # type: typing___Text
    clusterIP = ... # type: typing___Text
    loadBalancerIP = ... # type: typing___Text
    externalIPs = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    externalName = ... # type: typing___Text
    sessionAffinity = ... # type: typing___Text

    @property
    def selector(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def ports(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[inspection_sdk___model___container___service_port_pb2___ServicePort]: ...

    def __init__(self,
        *,
        type : typing___Optional[typing___Text] = None,
        clusterIP : typing___Optional[typing___Text] = None,
        loadBalancerIP : typing___Optional[typing___Text] = None,
        externalIPs : typing___Optional[typing___Iterable[typing___Text]] = None,
        externalName : typing___Optional[typing___Text] = None,
        sessionAffinity : typing___Optional[typing___Text] = None,
        selector : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        ports : typing___Optional[typing___Iterable[inspection_sdk___model___container___service_port_pb2___ServicePort]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ServiceSpec: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ServiceSpec: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"selector",b"selector"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"clusterIP",b"clusterIP",u"externalIPs",b"externalIPs",u"externalName",b"externalName",u"loadBalancerIP",b"loadBalancerIP",u"ports",b"ports",u"selector",b"selector",u"sessionAffinity",b"sessionAffinity",u"type",b"type"]) -> None: ...