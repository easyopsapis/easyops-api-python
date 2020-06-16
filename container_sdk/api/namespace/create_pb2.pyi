# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from container_sdk.model.container.namespace_pb2 import (
    Namespace as container_sdk___model___container___namespace_pb2___Namespace,
)

from container_sdk.model.container.resource_quota_pb2 import (
    ResourceQuota as container_sdk___model___container___resource_quota_pb2___ResourceQuota,
)

from container_sdk.model.container.resource_requirements_pb2 import (
    ResourceRequirements as container_sdk___model___container___resource_requirements_pb2___ResourceRequirements,
)

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


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class CreateRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    clusterId = ... # type: typing___Text
    workspaceId = ... # type: typing___Text

    @property
    def namespace(self) -> container_sdk___model___container___namespace_pb2___Namespace: ...

    @property
    def namespaceQuota(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def containerDefaultLimit(self) -> container_sdk___model___container___resource_requirements_pb2___ResourceRequirements: ...

    def __init__(self,
        *,
        clusterId : typing___Optional[typing___Text] = None,
        workspaceId : typing___Optional[typing___Text] = None,
        namespace : typing___Optional[container_sdk___model___container___namespace_pb2___Namespace] = None,
        namespaceQuota : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        containerDefaultLimit : typing___Optional[container_sdk___model___container___resource_requirements_pb2___ResourceRequirements] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"containerDefaultLimit",b"containerDefaultLimit",u"namespace",b"namespace",u"namespaceQuota",b"namespaceQuota"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"clusterId",b"clusterId",u"containerDefaultLimit",b"containerDefaultLimit",u"namespace",b"namespace",u"namespaceQuota",b"namespaceQuota",u"workspaceId",b"workspaceId"]) -> None: ...

class CreateResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def namespace(self) -> container_sdk___model___container___namespace_pb2___Namespace: ...

    @property
    def namespaceQuota(self) -> container_sdk___model___container___resource_quota_pb2___ResourceQuota: ...

    @property
    def containerDefaultLimit(self) -> container_sdk___model___container___resource_requirements_pb2___ResourceRequirements: ...

    def __init__(self,
        *,
        namespace : typing___Optional[container_sdk___model___container___namespace_pb2___Namespace] = None,
        namespaceQuota : typing___Optional[container_sdk___model___container___resource_quota_pb2___ResourceQuota] = None,
        containerDefaultLimit : typing___Optional[container_sdk___model___container___resource_requirements_pb2___ResourceRequirements] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"containerDefaultLimit",b"containerDefaultLimit",u"namespace",b"namespace",u"namespaceQuota",b"namespaceQuota"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"containerDefaultLimit",b"containerDefaultLimit",u"namespace",b"namespace",u"namespaceQuota",b"namespaceQuota"]) -> None: ...

class CreateResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> CreateResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[CreateResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
