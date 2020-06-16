# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from agent_admin_sdk.model.monitor.alert_event_pb2 import (
    AlertEvent as agent_admin_sdk___model___monitor___alert_event_pb2___AlertEvent,
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


class AlertRange(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    org = ... # type: builtin___int
    key = ... # type: typing___Text
    alert_begin_time = ... # type: builtin___int

    @property
    def first_alert(self) -> agent_admin_sdk___model___monitor___alert_event_pb2___AlertEvent: ...

    def __init__(self,
        *,
        org : typing___Optional[builtin___int] = None,
        key : typing___Optional[typing___Text] = None,
        first_alert : typing___Optional[agent_admin_sdk___model___monitor___alert_event_pb2___AlertEvent] = None,
        alert_begin_time : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> AlertRange: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AlertRange: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"first_alert",b"first_alert"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"alert_begin_time",b"alert_begin_time",u"first_alert",b"first_alert",u"key",b"key",u"org",b"org"]) -> None: ...
