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


class PatchManagerHost(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class InstalledPatch(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        articleId = ... # type: typing___Text
        installedTime = ... # type: typing___Text

        def __init__(self,
            *,
            articleId : typing___Optional[typing___Text] = None,
            installedTime : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> PatchManagerHost.InstalledPatch: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> PatchManagerHost.InstalledPatch: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"articleId",b"articleId",u"installedTime",b"installedTime"]) -> None: ...

    instanceId = ... # type: typing___Text
    hostname = ... # type: typing___Text
    ip = ... # type: typing___Text
    _agentStatus = ... # type: typing___Text
    _environment = ... # type: typing___Text
    osSystem = ... # type: typing___Text
    osArchitecture = ... # type: typing___Text
    osVersion = ... # type: typing___Text
    osRelease = ... # type: typing___Text
    requireReboot = ... # type: builtin___bool
    lastStartTime = ... # type: builtin___int
    lastInstallPatchTime = ... # type: builtin___int

    @property
    def installedPatch(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[PatchManagerHost.InstalledPatch]: ...

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        hostname : typing___Optional[typing___Text] = None,
        ip : typing___Optional[typing___Text] = None,
        _agentStatus : typing___Optional[typing___Text] = None,
        _environment : typing___Optional[typing___Text] = None,
        osSystem : typing___Optional[typing___Text] = None,
        osArchitecture : typing___Optional[typing___Text] = None,
        osVersion : typing___Optional[typing___Text] = None,
        osRelease : typing___Optional[typing___Text] = None,
        requireReboot : typing___Optional[builtin___bool] = None,
        lastStartTime : typing___Optional[builtin___int] = None,
        lastInstallPatchTime : typing___Optional[builtin___int] = None,
        installedPatch : typing___Optional[typing___Iterable[PatchManagerHost.InstalledPatch]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> PatchManagerHost: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> PatchManagerHost: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"_agentStatus",b"_agentStatus",u"_environment",b"_environment",u"hostname",b"hostname",u"installedPatch",b"installedPatch",u"instanceId",b"instanceId",u"ip",b"ip",u"lastInstallPatchTime",b"lastInstallPatchTime",u"lastStartTime",b"lastStartTime",u"osArchitecture",b"osArchitecture",u"osRelease",b"osRelease",u"osSystem",b"osSystem",u"osVersion",b"osVersion",u"requireReboot",b"requireReboot"]) -> None: ...
