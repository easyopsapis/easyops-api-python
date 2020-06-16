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


class GetDeployTaskV1Request(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    cmdTaskId = ... # type: typing___Text

    def __init__(self,
        *,
        cmdTaskId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetDeployTaskV1Request: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetDeployTaskV1Request: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"cmdTaskId",b"cmdTaskId"]) -> None: ...

class GetDeployTaskV1Response(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class DeployList(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        agentId = ... # type: typing___Text
        ip = ... # type: typing___Text
        deployPath = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
        agentPluginId = ... # type: typing___Text
        agentPluginName = ... # type: typing___Text
        preVersionName = ... # type: typing___Text
        pluginVersionName = ... # type: typing___Text
        status = ... # type: typing___Text

        def __init__(self,
            *,
            agentId : typing___Optional[typing___Text] = None,
            ip : typing___Optional[typing___Text] = None,
            deployPath : typing___Optional[typing___Iterable[typing___Text]] = None,
            agentPluginId : typing___Optional[typing___Text] = None,
            agentPluginName : typing___Optional[typing___Text] = None,
            preVersionName : typing___Optional[typing___Text] = None,
            pluginVersionName : typing___Optional[typing___Text] = None,
            status : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> GetDeployTaskV1Response.DeployList: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetDeployTaskV1Response.DeployList: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"agentId",b"agentId",u"agentPluginId",b"agentPluginId",u"agentPluginName",b"agentPluginName",u"deployPath",b"deployPath",u"ip",b"ip",u"pluginVersionName",b"pluginVersionName",u"preVersionName",b"preVersionName",u"status",b"status"]) -> None: ...

    targetId = ... # type: typing___Text
    targetName = ... # type: typing___Text
    creator = ... # type: typing___Text
    status = ... # type: typing___Text
    ctime = ... # type: builtin___int
    etime = ... # type: builtin___int

    @property
    def deployList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[GetDeployTaskV1Response.DeployList]: ...

    def __init__(self,
        *,
        targetId : typing___Optional[typing___Text] = None,
        targetName : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        status : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[builtin___int] = None,
        etime : typing___Optional[builtin___int] = None,
        deployList : typing___Optional[typing___Iterable[GetDeployTaskV1Response.DeployList]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetDeployTaskV1Response: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetDeployTaskV1Response: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"creator",b"creator",u"ctime",b"ctime",u"deployList",b"deployList",u"etime",b"etime",u"status",b"status",u"targetId",b"targetId",u"targetName",b"targetName"]) -> None: ...

class GetDeployTaskV1ResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> GetDeployTaskV1Response: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[GetDeployTaskV1Response] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetDeployTaskV1ResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetDeployTaskV1ResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
