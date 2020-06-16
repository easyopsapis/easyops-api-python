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


class DeploymentStrategy(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class RollingUpdate(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def maxSurge(self) -> google___protobuf___struct_pb2___Value: ...

        @property
        def maxUnavailable(self) -> google___protobuf___struct_pb2___Value: ...

        def __init__(self,
            *,
            maxSurge : typing___Optional[google___protobuf___struct_pb2___Value] = None,
            maxUnavailable : typing___Optional[google___protobuf___struct_pb2___Value] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> DeploymentStrategy.RollingUpdate: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DeploymentStrategy.RollingUpdate: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"maxSurge",b"maxSurge",u"maxUnavailable",b"maxUnavailable"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"maxSurge",b"maxSurge",u"maxUnavailable",b"maxUnavailable"]) -> None: ...

    type = ... # type: typing___Text

    @property
    def rollingUpdate(self) -> DeploymentStrategy.RollingUpdate: ...

    def __init__(self,
        *,
        type : typing___Optional[typing___Text] = None,
        rollingUpdate : typing___Optional[DeploymentStrategy.RollingUpdate] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> DeploymentStrategy: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DeploymentStrategy: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"rollingUpdate",b"rollingUpdate"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"rollingUpdate",b"rollingUpdate",u"type",b"type"]) -> None: ...
