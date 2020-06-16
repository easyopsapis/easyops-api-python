# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from container_sdk.model.container.cluster_pb2 import (
    Cluster as container_sdk___model___container___cluster_pb2___Cluster,
)

from container_sdk.model.container.namespace_pb2 import (
    Namespace as container_sdk___model___container___namespace_pb2___Namespace,
)

from container_sdk.model.container.secret_pb2 import (
    Secret as container_sdk___model___container___secret_pb2___Secret,
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


class GetRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    instanceId = ... # type: typing___Text

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"instanceId",b"instanceId"]) -> None: ...

class GetResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def secret(self) -> container_sdk___model___container___secret_pb2___Secret: ...

    @property
    def namespace(self) -> container_sdk___model___container___namespace_pb2___Namespace: ...

    @property
    def cluster(self) -> container_sdk___model___container___cluster_pb2___Cluster: ...

    def __init__(self,
        *,
        secret : typing___Optional[container_sdk___model___container___secret_pb2___Secret] = None,
        namespace : typing___Optional[container_sdk___model___container___namespace_pb2___Namespace] = None,
        cluster : typing___Optional[container_sdk___model___container___cluster_pb2___Cluster] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"cluster",b"cluster",u"namespace",b"namespace",u"secret",b"secret"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"cluster",b"cluster",u"namespace",b"namespace",u"secret",b"secret"]) -> None: ...

class GetResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> GetResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[GetResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
