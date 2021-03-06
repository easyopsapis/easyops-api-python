# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
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


class Probe(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Exec(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        command = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

        def __init__(self,
            *,
            command : typing___Optional[typing___Iterable[typing___Text]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Probe.Exec: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Probe.Exec: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"command",b"command"]) -> None: ...

    class HttpGet(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class HttpHeaders(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            name = ... # type: typing___Text
            value = ... # type: typing___Text

            def __init__(self,
                *,
                name : typing___Optional[typing___Text] = None,
                value : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> Probe.HttpGet.HttpHeaders: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Probe.HttpGet.HttpHeaders: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name",u"value",b"value"]) -> None: ...

        path = ... # type: typing___Text
        port = ... # type: builtin___int
        host = ... # type: typing___Text
        schema = ... # type: typing___Text

        @property
        def httpHeaders(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Probe.HttpGet.HttpHeaders]: ...

        def __init__(self,
            *,
            path : typing___Optional[typing___Text] = None,
            port : typing___Optional[builtin___int] = None,
            host : typing___Optional[typing___Text] = None,
            schema : typing___Optional[typing___Text] = None,
            httpHeaders : typing___Optional[typing___Iterable[Probe.HttpGet.HttpHeaders]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Probe.HttpGet: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Probe.HttpGet: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"host",b"host",u"httpHeaders",b"httpHeaders",u"path",b"path",u"port",b"port",u"schema",b"schema"]) -> None: ...

    class TcpSocket(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        port = ... # type: builtin___int
        host = ... # type: typing___Text

        def __init__(self,
            *,
            port : typing___Optional[builtin___int] = None,
            host : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Probe.TcpSocket: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Probe.TcpSocket: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"host",b"host",u"port",b"port"]) -> None: ...

    type = ... # type: typing___Text
    initialDelaySeconds = ... # type: builtin___int
    timeoutSeconds = ... # type: builtin___int
    periodSeconds = ... # type: builtin___int
    successThreshold = ... # type: builtin___int
    failureThreshold = ... # type: builtin___int

    @property
    def exec(self) -> Probe.Exec: ...

    @property
    def httpGet(self) -> Probe.HttpGet: ...

    @property
    def tcpSocket(self) -> Probe.TcpSocket: ...

    def __init__(self,
        *,
        type : typing___Optional[typing___Text] = None,
        exec : typing___Optional[Probe.Exec] = None,
        httpGet : typing___Optional[Probe.HttpGet] = None,
        tcpSocket : typing___Optional[Probe.TcpSocket] = None,
        initialDelaySeconds : typing___Optional[builtin___int] = None,
        timeoutSeconds : typing___Optional[builtin___int] = None,
        periodSeconds : typing___Optional[builtin___int] = None,
        successThreshold : typing___Optional[builtin___int] = None,
        failureThreshold : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Probe: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Probe: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"exec",b"exec",u"httpGet",b"httpGet",u"tcpSocket",b"tcpSocket"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"exec",b"exec",u"failureThreshold",b"failureThreshold",u"httpGet",b"httpGet",u"initialDelaySeconds",b"initialDelaySeconds",u"periodSeconds",b"periodSeconds",u"successThreshold",b"successThreshold",u"tcpSocket",b"tcpSocket",u"timeoutSeconds",b"timeoutSeconds",u"type",b"type"]) -> None: ...
