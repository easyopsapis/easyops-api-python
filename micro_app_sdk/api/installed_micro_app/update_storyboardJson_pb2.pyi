# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from micro_app_sdk.model.micro_app.installed_micro_app_pb2 import (
    InstalledMicroApp as micro_app_sdk___model___micro_app___installed_micro_app_pb2___InstalledMicroApp,
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


class UpdateInstalledMicroAppStoryboardJsonRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class MicroApp(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        storyboardJson = ... # type: typing___Text

        def __init__(self,
            *,
            storyboardJson : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> UpdateInstalledMicroAppStoryboardJsonRequest.MicroApp: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UpdateInstalledMicroAppStoryboardJsonRequest.MicroApp: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"storyboardJson",b"storyboardJson"]) -> None: ...

    app_id = ... # type: typing___Text

    @property
    def micro_app(self) -> UpdateInstalledMicroAppStoryboardJsonRequest.MicroApp: ...

    def __init__(self,
        *,
        app_id : typing___Optional[typing___Text] = None,
        micro_app : typing___Optional[UpdateInstalledMicroAppStoryboardJsonRequest.MicroApp] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UpdateInstalledMicroAppStoryboardJsonRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UpdateInstalledMicroAppStoryboardJsonRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"micro_app",b"micro_app"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"app_id",b"app_id",u"micro_app",b"micro_app"]) -> None: ...

class UpdateInstalledMicroAppStoryboardJsonResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> micro_app_sdk___model___micro_app___installed_micro_app_pb2___InstalledMicroApp: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[micro_app_sdk___model___micro_app___installed_micro_app_pb2___InstalledMicroApp] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UpdateInstalledMicroAppStoryboardJsonResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UpdateInstalledMicroAppStoryboardJsonResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
