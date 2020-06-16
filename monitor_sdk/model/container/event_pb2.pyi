# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from monitor_sdk.model.container.metadata_pb2 import (
    Metadata as monitor_sdk___model___container___metadata_pb2___Metadata,
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


class Event(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class InvolvedObject(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        kind = ... # type: typing___Text
        namespace = ... # type: typing___Text
        name = ... # type: typing___Text
        uid = ... # type: typing___Text
        apiVersion = ... # type: typing___Text
        resourceVersion = ... # type: typing___Text
        fieldPath = ... # type: typing___Text

        def __init__(self,
            *,
            kind : typing___Optional[typing___Text] = None,
            namespace : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            uid : typing___Optional[typing___Text] = None,
            apiVersion : typing___Optional[typing___Text] = None,
            resourceVersion : typing___Optional[typing___Text] = None,
            fieldPath : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Event.InvolvedObject: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Event.InvolvedObject: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"apiVersion",b"apiVersion",u"fieldPath",b"fieldPath",u"kind",b"kind",u"name",b"name",u"namespace",b"namespace",u"resourceVersion",b"resourceVersion",u"uid",b"uid"]) -> None: ...

    class Source(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        component = ... # type: typing___Text
        host = ... # type: typing___Text

        def __init__(self,
            *,
            component : typing___Optional[typing___Text] = None,
            host : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Event.Source: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Event.Source: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"component",b"component",u"host",b"host"]) -> None: ...

    class Series(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        count = ... # type: builtin___int
        lastObservedTime = ... # type: typing___Text

        def __init__(self,
            *,
            count : typing___Optional[builtin___int] = None,
            lastObservedTime : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Event.Series: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Event.Series: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"count",b"count",u"lastObservedTime",b"lastObservedTime"]) -> None: ...

    reason = ... # type: typing___Text
    message = ... # type: typing___Text
    firstTimestamp = ... # type: typing___Text
    lastTimestamp = ... # type: typing___Text
    count = ... # type: builtin___int
    type = ... # type: typing___Text
    eventTime = ... # type: typing___Text
    action = ... # type: typing___Text
    reportingComponent = ... # type: typing___Text
    reportingInstance = ... # type: typing___Text

    @property
    def metadata(self) -> monitor_sdk___model___container___metadata_pb2___Metadata: ...

    @property
    def involvedObject(self) -> Event.InvolvedObject: ...

    @property
    def source(self) -> Event.Source: ...

    @property
    def series(self) -> Event.Series: ...

    def __init__(self,
        *,
        metadata : typing___Optional[monitor_sdk___model___container___metadata_pb2___Metadata] = None,
        involvedObject : typing___Optional[Event.InvolvedObject] = None,
        reason : typing___Optional[typing___Text] = None,
        message : typing___Optional[typing___Text] = None,
        source : typing___Optional[Event.Source] = None,
        firstTimestamp : typing___Optional[typing___Text] = None,
        lastTimestamp : typing___Optional[typing___Text] = None,
        count : typing___Optional[builtin___int] = None,
        type : typing___Optional[typing___Text] = None,
        eventTime : typing___Optional[typing___Text] = None,
        series : typing___Optional[Event.Series] = None,
        action : typing___Optional[typing___Text] = None,
        reportingComponent : typing___Optional[typing___Text] = None,
        reportingInstance : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Event: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Event: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"involvedObject",b"involvedObject",u"metadata",b"metadata",u"series",b"series",u"source",b"source"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"action",b"action",u"count",b"count",u"eventTime",b"eventTime",u"firstTimestamp",b"firstTimestamp",u"involvedObject",b"involvedObject",u"lastTimestamp",b"lastTimestamp",u"message",b"message",u"metadata",b"metadata",u"reason",b"reason",u"reportingComponent",b"reportingComponent",u"reportingInstance",b"reportingInstance",u"series",b"series",u"source",b"source",u"type",b"type"]) -> None: ...
