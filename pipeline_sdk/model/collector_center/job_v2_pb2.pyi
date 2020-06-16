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

from google.protobuf.struct_pb2 import (
    Value as google___protobuf___struct_pb2___Value,
)

from pipeline_sdk.model.collector_center.script_pb2 import (
    Script as pipeline_sdk___model___collector_center___script_pb2___Script,
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


class CollJobV2(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Target(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class AgentHost(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            instanceId = ... # type: typing___Text
            ip = ... # type: typing___Text
            uuid = ... # type: typing___Text

            def __init__(self,
                *,
                instanceId : typing___Optional[typing___Text] = None,
                ip : typing___Optional[typing___Text] = None,
                uuid : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> CollJobV2.Target.AgentHost: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CollJobV2.Target.AgentHost: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"instanceId",b"instanceId",u"ip",b"ip",u"uuid",b"uuid"]) -> None: ...

        id = ... # type: typing___Text

        @property
        def agentHost(self) -> CollJobV2.Target.AgentHost: ...

        def __init__(self,
            *,
            id : typing___Optional[typing___Text] = None,
            agentHost : typing___Optional[CollJobV2.Target.AgentHost] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> CollJobV2.Target: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CollJobV2.Target: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"agentHost",b"agentHost"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"agentHost",b"agentHost",u"id",b"id"]) -> None: ...

    id = ... # type: typing___Text
    interval = ... # type: builtin___int
    timeout = ... # type: builtin___int
    timeRange = ... # type: typing___Text
    jobFilePath = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    version = ... # type: typing___Text
    name = ... # type: typing___Text
    dataId = ... # type: builtin___int
    fun = ... # type: typing___Text
    clazzId = ... # type: typing___Text
    clazzName = ... # type: typing___Text
    configId = ... # type: typing___Text
    requiredFields = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    cacheTtl = ... # type: builtin___int
    ignoreInvalid = ... # type: builtin___bool
    labels = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    disabled = ... # type: builtin___bool
    org = ... # type: builtin___int
    creator = ... # type: typing___Text
    modifier = ... # type: typing___Text
    ctime = ... # type: builtin___int
    mtime = ... # type: builtin___int
    objectId = ... # type: typing___Text
    instanceId = ... # type: typing___Text

    @property
    def target(self) -> CollJobV2.Target: ...

    @property
    def script(self) -> pipeline_sdk___model___collector_center___script_pb2___Script: ...

    @property
    def env(self) -> google___protobuf___struct_pb2___Value: ...

    @property
    def kwargs(self) -> google___protobuf___struct_pb2___Value: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        interval : typing___Optional[builtin___int] = None,
        timeout : typing___Optional[builtin___int] = None,
        timeRange : typing___Optional[typing___Text] = None,
        jobFilePath : typing___Optional[typing___Iterable[typing___Text]] = None,
        version : typing___Optional[typing___Text] = None,
        target : typing___Optional[CollJobV2.Target] = None,
        name : typing___Optional[typing___Text] = None,
        script : typing___Optional[pipeline_sdk___model___collector_center___script_pb2___Script] = None,
        dataId : typing___Optional[builtin___int] = None,
        env : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        kwargs : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        fun : typing___Optional[typing___Text] = None,
        clazzId : typing___Optional[typing___Text] = None,
        clazzName : typing___Optional[typing___Text] = None,
        configId : typing___Optional[typing___Text] = None,
        requiredFields : typing___Optional[typing___Iterable[typing___Text]] = None,
        cacheTtl : typing___Optional[builtin___int] = None,
        ignoreInvalid : typing___Optional[builtin___bool] = None,
        labels : typing___Optional[typing___Iterable[typing___Text]] = None,
        disabled : typing___Optional[builtin___bool] = None,
        org : typing___Optional[builtin___int] = None,
        creator : typing___Optional[typing___Text] = None,
        modifier : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[builtin___int] = None,
        mtime : typing___Optional[builtin___int] = None,
        objectId : typing___Optional[typing___Text] = None,
        instanceId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CollJobV2: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CollJobV2: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"env",b"env",u"kwargs",b"kwargs",u"script",b"script",u"target",b"target"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"cacheTtl",b"cacheTtl",u"clazzId",b"clazzId",u"clazzName",b"clazzName",u"configId",b"configId",u"creator",b"creator",u"ctime",b"ctime",u"dataId",b"dataId",u"disabled",b"disabled",u"env",b"env",u"fun",b"fun",u"id",b"id",u"ignoreInvalid",b"ignoreInvalid",u"instanceId",b"instanceId",u"interval",b"interval",u"jobFilePath",b"jobFilePath",u"kwargs",b"kwargs",u"labels",b"labels",u"modifier",b"modifier",u"mtime",b"mtime",u"name",b"name",u"objectId",b"objectId",u"org",b"org",u"requiredFields",b"requiredFields",u"script",b"script",u"target",b"target",u"timeRange",b"timeRange",u"timeout",b"timeout",u"version",b"version"]) -> None: ...