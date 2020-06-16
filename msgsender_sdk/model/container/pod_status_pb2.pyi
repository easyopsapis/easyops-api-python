# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from msgsender_sdk.model.container.container_status_pb2 import (
    ContainerStatus as msgsender_sdk___model___container___container_status_pb2___ContainerStatus,
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


class PodStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    phase = ... # type: typing___Text
    message = ... # type: typing___Text
    hostIP = ... # type: typing___Text
    podIP = ... # type: typing___Text

    @property
    def initContainerStatuses(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[msgsender_sdk___model___container___container_status_pb2___ContainerStatus]: ...

    @property
    def containerStatuses(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[msgsender_sdk___model___container___container_status_pb2___ContainerStatus]: ...

    def __init__(self,
        *,
        phase : typing___Optional[typing___Text] = None,
        message : typing___Optional[typing___Text] = None,
        initContainerStatuses : typing___Optional[typing___Iterable[msgsender_sdk___model___container___container_status_pb2___ContainerStatus]] = None,
        containerStatuses : typing___Optional[typing___Iterable[msgsender_sdk___model___container___container_status_pb2___ContainerStatus]] = None,
        hostIP : typing___Optional[typing___Text] = None,
        podIP : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> PodStatus: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> PodStatus: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"containerStatuses",b"containerStatuses",u"hostIP",b"hostIP",u"initContainerStatuses",b"initContainerStatuses",u"message",b"message",u"phase",b"phase",u"podIP",b"podIP"]) -> None: ...
