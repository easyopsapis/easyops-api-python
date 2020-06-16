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

from webshell_sdk.model.container.container_state_pb2 import (
    ContainerState as webshell_sdk___model___container___container_state_pb2___ContainerState,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class ContainerStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text
    restartCount = ... # type: builtin___int
    image = ... # type: typing___Text

    @property
    def state(self) -> webshell_sdk___model___container___container_state_pb2___ContainerState: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        restartCount : typing___Optional[builtin___int] = None,
        state : typing___Optional[webshell_sdk___model___container___container_state_pb2___ContainerState] = None,
        image : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ContainerStatus: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ContainerStatus: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"state",b"state"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"image",b"image",u"name",b"name",u"restartCount",b"restartCount",u"state",b"state"]) -> None: ...
