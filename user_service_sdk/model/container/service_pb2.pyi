# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.struct_pb2 import (
    Struct as google___protobuf___struct_pb2___Struct,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)

from user_service_sdk.model.container.loadbalancer_status_pb2 import (
    LoadBalancerStatus as user_service_sdk___model___container___loadbalancer_status_pb2___LoadBalancerStatus,
)

from user_service_sdk.model.container.service_spec_pb2 import (
    ServiceSpec as user_service_sdk___model___container___service_spec_pb2___ServiceSpec,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class Service(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Status(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def loadBalancer(self) -> user_service_sdk___model___container___loadbalancer_status_pb2___LoadBalancerStatus: ...

        def __init__(self,
            *,
            loadBalancer : typing___Optional[user_service_sdk___model___container___loadbalancer_status_pb2___LoadBalancerStatus] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Service.Status: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Service.Status: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"loadBalancer",b"loadBalancer"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"loadBalancer",b"loadBalancer"]) -> None: ...

    instanceId = ... # type: typing___Text
    kind = ... # type: typing___Text
    name = ... # type: typing___Text
    namespace = ... # type: typing___Text
    resourceName = ... # type: typing___Text
    resourceSpec = ... # type: typing___Text
    creationTimestamp = ... # type: typing___Text
    creator = ... # type: typing___Text

    @property
    def annotations(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def labels(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def spec(self) -> user_service_sdk___model___container___service_spec_pb2___ServiceSpec: ...

    @property
    def status(self) -> Service.Status: ...

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        kind : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        namespace : typing___Optional[typing___Text] = None,
        resourceName : typing___Optional[typing___Text] = None,
        annotations : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        labels : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        spec : typing___Optional[user_service_sdk___model___container___service_spec_pb2___ServiceSpec] = None,
        resourceSpec : typing___Optional[typing___Text] = None,
        status : typing___Optional[Service.Status] = None,
        creationTimestamp : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Service: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Service: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"annotations",b"annotations",u"labels",b"labels",u"spec",b"spec",u"status",b"status"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"annotations",b"annotations",u"creationTimestamp",b"creationTimestamp",u"creator",b"creator",u"instanceId",b"instanceId",u"kind",b"kind",u"labels",b"labels",u"name",b"name",u"namespace",b"namespace",u"resourceName",b"resourceName",u"resourceSpec",b"resourceSpec",u"spec",b"spec",u"status",b"status"]) -> None: ...
