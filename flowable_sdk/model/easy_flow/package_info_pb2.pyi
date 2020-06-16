# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from flowable_sdk.model.cmdb.cluster_info_pb2 import (
    ClusterInfo as flowable_sdk___model___cmdb___cluster_info_pb2___ClusterInfo,
)

from flowable_sdk.model.easy_flow.version_info_pb2 import (
    VersionInfo as flowable_sdk___model___easy_flow___version_info_pb2___VersionInfo,
)

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


class PackageInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    packageName = ... # type: typing___Text
    versionName = ... # type: typing___Text
    preVersionId = ... # type: typing___Text
    preVersionName = ... # type: typing___Text
    preVersionEnvType = ... # type: builtin___int
    targetVersion = ... # type: typing___Text
    preStop = ... # type: builtin___bool
    postStart = ... # type: builtin___bool
    postRestart = ... # type: builtin___bool
    autoStart = ... # type: builtin___bool
    userCheck = ... # type: builtin___bool
    fullUpdate = ... # type: builtin___bool
    forceUpdate = ... # type: builtin___bool
    force = ... # type: builtin___bool
    forceInstall = ... # type: builtin___bool
    simulateInstall = ... # type: builtin___bool
    specialOp = ... # type: typing___Text
    fileOnly = ... # type: builtin___bool
    scriptOnly = ... # type: builtin___bool
    versionId = ... # type: typing___Text
    packageId = ... # type: typing___Text
    installPath = ... # type: typing___Text
    type = ... # type: builtin___int
    platform = ... # type: typing___Text

    @property
    def cluster(self) -> flowable_sdk___model___cmdb___cluster_info_pb2___ClusterInfo: ...

    @property
    def versionInfo(self) -> flowable_sdk___model___easy_flow___version_info_pb2___VersionInfo: ...

    def __init__(self,
        *,
        packageName : typing___Optional[typing___Text] = None,
        versionName : typing___Optional[typing___Text] = None,
        cluster : typing___Optional[flowable_sdk___model___cmdb___cluster_info_pb2___ClusterInfo] = None,
        preVersionId : typing___Optional[typing___Text] = None,
        preVersionName : typing___Optional[typing___Text] = None,
        preVersionEnvType : typing___Optional[builtin___int] = None,
        targetVersion : typing___Optional[typing___Text] = None,
        preStop : typing___Optional[builtin___bool] = None,
        postStart : typing___Optional[builtin___bool] = None,
        postRestart : typing___Optional[builtin___bool] = None,
        autoStart : typing___Optional[builtin___bool] = None,
        userCheck : typing___Optional[builtin___bool] = None,
        fullUpdate : typing___Optional[builtin___bool] = None,
        forceUpdate : typing___Optional[builtin___bool] = None,
        force : typing___Optional[builtin___bool] = None,
        forceInstall : typing___Optional[builtin___bool] = None,
        simulateInstall : typing___Optional[builtin___bool] = None,
        versionInfo : typing___Optional[flowable_sdk___model___easy_flow___version_info_pb2___VersionInfo] = None,
        specialOp : typing___Optional[typing___Text] = None,
        fileOnly : typing___Optional[builtin___bool] = None,
        scriptOnly : typing___Optional[builtin___bool] = None,
        versionId : typing___Optional[typing___Text] = None,
        packageId : typing___Optional[typing___Text] = None,
        installPath : typing___Optional[typing___Text] = None,
        type : typing___Optional[builtin___int] = None,
        platform : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> PackageInfo: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> PackageInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"cluster",b"cluster",u"versionInfo",b"versionInfo"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"autoStart",b"autoStart",u"cluster",b"cluster",u"fileOnly",b"fileOnly",u"force",b"force",u"forceInstall",b"forceInstall",u"forceUpdate",b"forceUpdate",u"fullUpdate",b"fullUpdate",u"installPath",b"installPath",u"packageId",b"packageId",u"packageName",b"packageName",u"platform",b"platform",u"postRestart",b"postRestart",u"postStart",b"postStart",u"preStop",b"preStop",u"preVersionEnvType",b"preVersionEnvType",u"preVersionId",b"preVersionId",u"preVersionName",b"preVersionName",u"scriptOnly",b"scriptOnly",u"simulateInstall",b"simulateInstall",u"specialOp",b"specialOp",u"targetVersion",b"targetVersion",u"type",b"type",u"userCheck",b"userCheck",u"versionId",b"versionId",u"versionInfo",b"versionInfo",u"versionName",b"versionName"]) -> None: ...
