# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from database_delivery_sdk.model.container.http_ingress_path_pb2 import (
    HTTPIngressPath as database_delivery_sdk___model___container___http_ingress_path_pb2___HTTPIngressPath,
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


class IngressRule(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Http(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def paths(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[database_delivery_sdk___model___container___http_ingress_path_pb2___HTTPIngressPath]: ...

        def __init__(self,
            *,
            paths : typing___Optional[typing___Iterable[database_delivery_sdk___model___container___http_ingress_path_pb2___HTTPIngressPath]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> IngressRule.Http: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> IngressRule.Http: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"paths",b"paths"]) -> None: ...

    host = ... # type: typing___Text

    @property
    def http(self) -> IngressRule.Http: ...

    def __init__(self,
        *,
        host : typing___Optional[typing___Text] = None,
        http : typing___Optional[IngressRule.Http] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> IngressRule: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> IngressRule: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"http",b"http"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"host",b"host",u"http",b"http"]) -> None: ...