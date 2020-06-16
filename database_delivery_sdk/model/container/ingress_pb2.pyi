# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from database_delivery_sdk.model.container.ingress_backend_pb2 import (
    IngressBackend as database_delivery_sdk___model___container___ingress_backend_pb2___IngressBackend,
)

from database_delivery_sdk.model.container.ingress_rule_pb2 import (
    IngressRule as database_delivery_sdk___model___container___ingress_rule_pb2___IngressRule,
)

from database_delivery_sdk.model.container.ingress_tls_pb2 import (
    IngressTLS as database_delivery_sdk___model___container___ingress_tls_pb2___IngressTLS,
)

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


class Ingress(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    instanceId = ... # type: typing___Text
    kind = ... # type: typing___Text
    namespace = ... # type: typing___Text
    resourceName = ... # type: typing___Text
    displayName = ... # type: typing___Text
    description = ... # type: typing___Text
    address = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    ctime = ... # type: typing___Text
    creator = ... # type: typing___Text

    @property
    def annotations(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def backend(self) -> database_delivery_sdk___model___container___ingress_backend_pb2___IngressBackend: ...

    @property
    def rules(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[database_delivery_sdk___model___container___ingress_rule_pb2___IngressRule]: ...

    @property
    def tls(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[database_delivery_sdk___model___container___ingress_tls_pb2___IngressTLS]: ...

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        kind : typing___Optional[typing___Text] = None,
        namespace : typing___Optional[typing___Text] = None,
        resourceName : typing___Optional[typing___Text] = None,
        displayName : typing___Optional[typing___Text] = None,
        description : typing___Optional[typing___Text] = None,
        annotations : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        address : typing___Optional[typing___Iterable[typing___Text]] = None,
        backend : typing___Optional[database_delivery_sdk___model___container___ingress_backend_pb2___IngressBackend] = None,
        rules : typing___Optional[typing___Iterable[database_delivery_sdk___model___container___ingress_rule_pb2___IngressRule]] = None,
        tls : typing___Optional[typing___Iterable[database_delivery_sdk___model___container___ingress_tls_pb2___IngressTLS]] = None,
        ctime : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Ingress: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Ingress: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"annotations",b"annotations",u"backend",b"backend"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"address",b"address",u"annotations",b"annotations",u"backend",b"backend",u"creator",b"creator",u"ctime",b"ctime",u"description",b"description",u"displayName",b"displayName",u"instanceId",b"instanceId",u"kind",b"kind",u"namespace",b"namespace",u"resourceName",b"resourceName",u"rules",b"rules",u"tls",b"tls"]) -> None: ...
