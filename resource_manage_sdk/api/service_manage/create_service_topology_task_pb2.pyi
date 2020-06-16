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


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class CreateServiceTopologyTaskRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Switch(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        connectNode2Service = ... # type: builtin___bool
        disconnectNode2Service = ... # type: builtin___bool
        connectService2Service = ... # type: builtin___bool
        disconnectService2Service = ... # type: builtin___bool

        def __init__(self,
            *,
            connectNode2Service : typing___Optional[builtin___bool] = None,
            disconnectNode2Service : typing___Optional[builtin___bool] = None,
            connectService2Service : typing___Optional[builtin___bool] = None,
            disconnectService2Service : typing___Optional[builtin___bool] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> CreateServiceTopologyTaskRequest.Switch: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateServiceTopologyTaskRequest.Switch: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"connectNode2Service",b"connectNode2Service",u"connectService2Service",b"connectService2Service",u"disconnectNode2Service",b"disconnectNode2Service",u"disconnectService2Service",b"disconnectService2Service"]) -> None: ...

    command = ... # type: typing___Text

    @property
    def switch(self) -> CreateServiceTopologyTaskRequest.Switch: ...

    def __init__(self,
        *,
        command : typing___Optional[typing___Text] = None,
        switch : typing___Optional[CreateServiceTopologyTaskRequest.Switch] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateServiceTopologyTaskRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateServiceTopologyTaskRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"switch",b"switch"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"command",b"command",u"switch",b"switch"]) -> None: ...

class CreateServiceTopologyTaskResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    task = ... # type: typing___Text
    status = ... # type: typing___Text

    def __init__(self,
        *,
        task : typing___Optional[typing___Text] = None,
        status : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateServiceTopologyTaskResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateServiceTopologyTaskResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"status",b"status",u"task",b"task"]) -> None: ...

class CreateServiceTopologyTaskResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> CreateServiceTopologyTaskResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[CreateServiceTopologyTaskResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateServiceTopologyTaskResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateServiceTopologyTaskResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
