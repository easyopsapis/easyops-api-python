# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
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

from webshell_sdk.model.container.ingress_backend_pb2 import (
    IngressBackend as webshell_sdk___model___container___ingress_backend_pb2___IngressBackend,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class HTTPIngressPath(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    path = ... # type: typing___Text

    @property
    def backend(self) -> webshell_sdk___model___container___ingress_backend_pb2___IngressBackend: ...

    def __init__(self,
        *,
        path : typing___Optional[typing___Text] = None,
        backend : typing___Optional[webshell_sdk___model___container___ingress_backend_pb2___IngressBackend] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> HTTPIngressPath: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> HTTPIngressPath: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"backend",b"backend"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"backend",b"backend",u"path",b"path"]) -> None: ...
