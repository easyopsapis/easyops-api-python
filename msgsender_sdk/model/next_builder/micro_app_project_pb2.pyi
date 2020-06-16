# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
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


class MicroAppProject(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class DevelopmentEnv(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        openApiIP = ... # type: typing___Text
        accessKey = ... # type: typing___Text
        secretKey = ... # type: typing___Text

        def __init__(self,
            *,
            openApiIP : typing___Optional[typing___Text] = None,
            accessKey : typing___Optional[typing___Text] = None,
            secretKey : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> MicroAppProject.DevelopmentEnv: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> MicroAppProject.DevelopmentEnv: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"accessKey",b"accessKey",u"openApiIP",b"openApiIP",u"secretKey",b"secretKey"]) -> None: ...

    class AppSetting(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        name = ... # type: typing___Text
        homepage = ... # type: typing___Text

        def __init__(self,
            *,
            name : typing___Optional[typing___Text] = None,
            homepage : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> MicroAppProject.AppSetting: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> MicroAppProject.AppSetting: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"homepage",b"homepage",u"name",b"name"]) -> None: ...

    projectId = ... # type: typing___Text
    name = ... # type: typing___Text
    appId = ... # type: typing___Text
    models = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    type = ... # type: typing___Text

    @property
    def developmentEnv(self) -> MicroAppProject.DevelopmentEnv: ...

    @property
    def appSetting(self) -> MicroAppProject.AppSetting: ...

    def __init__(self,
        *,
        projectId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        appId : typing___Optional[typing___Text] = None,
        models : typing___Optional[typing___Iterable[typing___Text]] = None,
        developmentEnv : typing___Optional[MicroAppProject.DevelopmentEnv] = None,
        appSetting : typing___Optional[MicroAppProject.AppSetting] = None,
        type : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MicroAppProject: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> MicroAppProject: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"appSetting",b"appSetting",u"developmentEnv",b"developmentEnv"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"appId",b"appId",u"appSetting",b"appSetting",u"developmentEnv",b"developmentEnv",u"models",b"models",u"name",b"name",u"projectId",b"projectId",u"type",b"type"]) -> None: ...