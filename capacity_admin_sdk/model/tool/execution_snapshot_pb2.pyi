# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from capacity_admin_sdk.model.tool.callback_pb2 import (
    Callback as capacity_admin_sdk___model___tool___callback_pb2___Callback,
)

from capacity_admin_sdk.model.tool.extra_info_pb2 import (
    ExtraInfo as capacity_admin_sdk___model___tool___extra_info_pb2___ExtraInfo,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
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


class ExecutionSnapshot(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Targets(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        targetId = ... # type: typing___Text

        def __init__(self,
            *,
            targetId : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ExecutionSnapshot.Targets: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExecutionSnapshot.Targets: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"targetId",b"targetId"]) -> None: ...

    class Actions(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class Param(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            cmd = ... # type: typing___Text
            scriptType = ... # type: typing___Text
            parser = ... # type: typing___Text
            param = ... # type: typing___Text
            execUser = ... # type: typing___Text
            timeout = ... # type: builtin___int

            def __init__(self,
                *,
                cmd : typing___Optional[typing___Text] = None,
                scriptType : typing___Optional[typing___Text] = None,
                parser : typing___Optional[typing___Text] = None,
                param : typing___Optional[typing___Text] = None,
                execUser : typing___Optional[typing___Text] = None,
                timeout : typing___Optional[builtin___int] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> ExecutionSnapshot.Actions.Param: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExecutionSnapshot.Actions.Param: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"cmd",b"cmd",u"execUser",b"execUser",u"param",b"param",u"parser",b"parser",u"scriptType",b"scriptType",u"timeout",b"timeout"]) -> None: ...

        name = ... # type: typing___Text
        type = ... # type: typing___Text
        action = ... # type: typing___Text

        @property
        def param(self) -> ExecutionSnapshot.Actions.Param: ...

        def __init__(self,
            *,
            name : typing___Optional[typing___Text] = None,
            type : typing___Optional[typing___Text] = None,
            action : typing___Optional[typing___Text] = None,
            param : typing___Optional[ExecutionSnapshot.Actions.Param] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ExecutionSnapshot.Actions: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExecutionSnapshot.Actions: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"param",b"param"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"action",b"action",u"name",b"name",u"param",b"param",u"type",b"type"]) -> None: ...

    name = ... # type: typing___Text
    type = ... # type: typing___Text
    operation = ... # type: typing___Text
    packageId = ... # type: typing___Text
    versionId = ... # type: typing___Text
    needNotify = ... # type: typing___Text

    @property
    def targets(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ExecutionSnapshot.Targets]: ...

    @property
    def actions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ExecutionSnapshot.Actions]: ...

    @property
    def callback(self) -> capacity_admin_sdk___model___tool___callback_pb2___Callback: ...

    @property
    def extraInfo(self) -> capacity_admin_sdk___model___tool___extra_info_pb2___ExtraInfo: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        type : typing___Optional[typing___Text] = None,
        operation : typing___Optional[typing___Text] = None,
        packageId : typing___Optional[typing___Text] = None,
        versionId : typing___Optional[typing___Text] = None,
        targets : typing___Optional[typing___Iterable[ExecutionSnapshot.Targets]] = None,
        actions : typing___Optional[typing___Iterable[ExecutionSnapshot.Actions]] = None,
        callback : typing___Optional[capacity_admin_sdk___model___tool___callback_pb2___Callback] = None,
        extraInfo : typing___Optional[capacity_admin_sdk___model___tool___extra_info_pb2___ExtraInfo] = None,
        needNotify : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ExecutionSnapshot: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ExecutionSnapshot: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"callback",b"callback",u"extraInfo",b"extraInfo"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"actions",b"actions",u"callback",b"callback",u"extraInfo",b"extraInfo",u"name",b"name",u"needNotify",b"needNotify",u"operation",b"operation",u"packageId",b"packageId",u"targets",b"targets",u"type",b"type",u"versionId",b"versionId"]) -> None: ...
