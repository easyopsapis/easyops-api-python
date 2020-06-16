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

from state_workflow_sdk.model.cmdb.cluster_info_pb2 import (
    ClusterInfo as state_workflow_sdk___model___cmdb___cluster_info_pb2___ClusterInfo,
)

from state_workflow_sdk.model.easy_flow.version_info_pb2 import (
    VersionInfo as state_workflow_sdk___model___easy_flow___version_info_pb2___VersionInfo,
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


class TargetInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class InstanceInfo(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        versionName = ... # type: typing___Text
        packageId = ... # type: typing___Text
        installPath = ... # type: typing___Text
        versionId = ... # type: typing___Text

        @property
        def versionInfo(self) -> state_workflow_sdk___model___easy_flow___version_info_pb2___VersionInfo: ...

        def __init__(self,
            *,
            versionName : typing___Optional[typing___Text] = None,
            versionInfo : typing___Optional[state_workflow_sdk___model___easy_flow___version_info_pb2___VersionInfo] = None,
            packageId : typing___Optional[typing___Text] = None,
            installPath : typing___Optional[typing___Text] = None,
            versionId : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> TargetInfo.InstanceInfo: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TargetInfo.InstanceInfo: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"versionInfo",b"versionInfo"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"installPath",b"installPath",u"packageId",b"packageId",u"versionId",b"versionId",u"versionInfo",b"versionInfo",u"versionName",b"versionName"]) -> None: ...

    class OperationInfo(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        operation = ... # type: typing___Text
        installPath = ... # type: typing___Text
        packageId = ... # type: typing___Text

        @property
        def versionToInfo(self) -> state_workflow_sdk___model___easy_flow___version_info_pb2___VersionInfo: ...

        @property
        def versionFromInfo(self) -> state_workflow_sdk___model___easy_flow___version_info_pb2___VersionInfo: ...

        def __init__(self,
            *,
            operation : typing___Optional[typing___Text] = None,
            versionToInfo : typing___Optional[state_workflow_sdk___model___easy_flow___version_info_pb2___VersionInfo] = None,
            versionFromInfo : typing___Optional[state_workflow_sdk___model___easy_flow___version_info_pb2___VersionInfo] = None,
            installPath : typing___Optional[typing___Text] = None,
            packageId : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> TargetInfo.OperationInfo: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TargetInfo.OperationInfo: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"versionFromInfo",b"versionFromInfo",u"versionToInfo",b"versionToInfo"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"installPath",b"installPath",u"operation",b"operation",u"packageId",b"packageId",u"versionFromInfo",b"versionFromInfo",u"versionToInfo",b"versionToInfo"]) -> None: ...

    targetId = ... # type: typing___Text
    targetName = ... # type: typing___Text
    instanceId = ... # type: typing___Text

    @property
    def cluster(self) -> state_workflow_sdk___model___cmdb___cluster_info_pb2___ClusterInfo: ...

    @property
    def instanceInfo(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[TargetInfo.InstanceInfo]: ...

    @property
    def operationInfo(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[TargetInfo.OperationInfo]: ...

    def __init__(self,
        *,
        targetId : typing___Optional[typing___Text] = None,
        targetName : typing___Optional[typing___Text] = None,
        instanceId : typing___Optional[typing___Text] = None,
        cluster : typing___Optional[state_workflow_sdk___model___cmdb___cluster_info_pb2___ClusterInfo] = None,
        instanceInfo : typing___Optional[typing___Iterable[TargetInfo.InstanceInfo]] = None,
        operationInfo : typing___Optional[typing___Iterable[TargetInfo.OperationInfo]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TargetInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TargetInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"cluster",b"cluster"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"cluster",b"cluster",u"instanceId",b"instanceId",u"instanceInfo",b"instanceInfo",u"operationInfo",b"operationInfo",u"targetId",b"targetId",u"targetName",b"targetName"]) -> None: ...
