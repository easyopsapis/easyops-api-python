# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from easy_flow_sdk.model.cmdb.cluster_info_pb2 import (
    ClusterInfo as easy_flow_sdk___model___cmdb___cluster_info_pb2___ClusterInfo,
)

from easy_flow_sdk.model.easy_flow.deploy_label_pb2 import (
    DeployLabel as easy_flow_sdk___model___easy_flow___deploy_label_pb2___DeployLabel,
)

from easy_flow_sdk.model.easy_flow.deploy_target_pb2 import (
    DeployTarget as easy_flow_sdk___model___easy_flow___deploy_target_pb2___DeployTarget,
)

from easy_flow_sdk.model.easy_flow.package_info_pb2 import (
    PackageInfo as easy_flow_sdk___model___easy_flow___package_info_pb2___PackageInfo,
)

from easy_flow_sdk.model.easy_flow.target_info_pb2 import (
    TargetInfo as easy_flow_sdk___model___easy_flow___target_info_pb2___TargetInfo,
)

from easy_flow_sdk.model.easy_flow.version_info_pb2 import (
    VersionInfo as easy_flow_sdk___model___easy_flow___version_info_pb2___VersionInfo,
)

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


class CreateRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Batches(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def targets(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[easy_flow_sdk___model___easy_flow___deploy_target_pb2___DeployTarget]: ...

        def __init__(self,
            *,
            targets : typing___Optional[typing___Iterable[easy_flow_sdk___model___easy_flow___deploy_target_pb2___DeployTarget]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> CreateRequest.Batches: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateRequest.Batches: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"targets",b"targets"]) -> None: ...

    class InstanceInfo(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        versionName = ... # type: typing___Text
        packageId = ... # type: typing___Text
        installPath = ... # type: typing___Text
        versionId = ... # type: typing___Text

        @property
        def versionInfo(self) -> easy_flow_sdk___model___easy_flow___version_info_pb2___VersionInfo: ...

        def __init__(self,
            *,
            versionName : typing___Optional[typing___Text] = None,
            versionInfo : typing___Optional[easy_flow_sdk___model___easy_flow___version_info_pb2___VersionInfo] = None,
            packageId : typing___Optional[typing___Text] = None,
            installPath : typing___Optional[typing___Text] = None,
            versionId : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> CreateRequest.InstanceInfo: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateRequest.InstanceInfo: ...
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
        def versionToInfo(self) -> easy_flow_sdk___model___easy_flow___version_info_pb2___VersionInfo: ...

        @property
        def versionFromInfo(self) -> easy_flow_sdk___model___easy_flow___version_info_pb2___VersionInfo: ...

        def __init__(self,
            *,
            operation : typing___Optional[typing___Text] = None,
            versionToInfo : typing___Optional[easy_flow_sdk___model___easy_flow___version_info_pb2___VersionInfo] = None,
            versionFromInfo : typing___Optional[easy_flow_sdk___model___easy_flow___version_info_pb2___VersionInfo] = None,
            installPath : typing___Optional[typing___Text] = None,
            packageId : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> CreateRequest.OperationInfo: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateRequest.OperationInfo: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"versionFromInfo",b"versionFromInfo",u"versionToInfo",b"versionToInfo"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"installPath",b"installPath",u"operation",b"operation",u"packageId",b"packageId",u"versionFromInfo",b"versionFromInfo",u"versionToInfo",b"versionToInfo"]) -> None: ...

    class ConfigList(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class Configs(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            class Items(google___protobuf___message___Message):
                DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
                name = ... # type: typing___Text
                path = ... # type: typing___Text

                def __init__(self,
                    *,
                    name : typing___Optional[typing___Text] = None,
                    path : typing___Optional[typing___Text] = None,
                    ) -> None: ...
                if sys.version_info >= (3,):
                    @classmethod
                    def FromString(cls, s: builtin___bytes) -> CreateRequest.ConfigList.Configs.Items: ...
                else:
                    @classmethod
                    def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateRequest.ConfigList.Configs.Items: ...
                def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name",u"path",b"path"]) -> None: ...

            packageId = ... # type: typing___Text
            installPath = ... # type: typing___Text

            @property
            def items(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CreateRequest.ConfigList.Configs.Items]: ...

            def __init__(self,
                *,
                packageId : typing___Optional[typing___Text] = None,
                items : typing___Optional[typing___Iterable[CreateRequest.ConfigList.Configs.Items]] = None,
                installPath : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> CreateRequest.ConfigList.Configs: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateRequest.ConfigList.Configs: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"installPath",b"installPath",u"items",b"items",u"packageId",b"packageId"]) -> None: ...

        hosts = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

        @property
        def configs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CreateRequest.ConfigList.Configs]: ...

        def __init__(self,
            *,
            hosts : typing___Optional[typing___Iterable[typing___Text]] = None,
            configs : typing___Optional[typing___Iterable[CreateRequest.ConfigList.Configs]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> CreateRequest.ConfigList: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateRequest.ConfigList: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"configs",b"configs",u"hosts",b"hosts"]) -> None: ...

    class ConfigDiff(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class Detail(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            class Items(google___protobuf___message___Message):
                DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
                path = ... # type: typing___Text
                newName = ... # type: typing___Text
                oldName = ... # type: typing___Text

                def __init__(self,
                    *,
                    path : typing___Optional[typing___Text] = None,
                    newName : typing___Optional[typing___Text] = None,
                    oldName : typing___Optional[typing___Text] = None,
                    ) -> None: ...
                if sys.version_info >= (3,):
                    @classmethod
                    def FromString(cls, s: builtin___bytes) -> CreateRequest.ConfigDiff.Detail.Items: ...
                else:
                    @classmethod
                    def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateRequest.ConfigDiff.Detail.Items: ...
                def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                def ClearField(self, field_name: typing_extensions___Literal[u"newName",b"newName",u"oldName",b"oldName",u"path",b"path"]) -> None: ...

            packageId = ... # type: typing___Text
            installPath = ... # type: typing___Text

            @property
            def items(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CreateRequest.ConfigDiff.Detail.Items]: ...

            def __init__(self,
                *,
                items : typing___Optional[typing___Iterable[CreateRequest.ConfigDiff.Detail.Items]] = None,
                packageId : typing___Optional[typing___Text] = None,
                installPath : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> CreateRequest.ConfigDiff.Detail: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateRequest.ConfigDiff.Detail: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"installPath",b"installPath",u"items",b"items",u"packageId",b"packageId"]) -> None: ...

        hosts = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

        @property
        def detail(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CreateRequest.ConfigDiff.Detail]: ...

        def __init__(self,
            *,
            hosts : typing___Optional[typing___Iterable[typing___Text]] = None,
            detail : typing___Optional[typing___Iterable[CreateRequest.ConfigDiff.Detail]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> CreateRequest.ConfigDiff: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateRequest.ConfigDiff: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"detail",b"detail",u"hosts",b"hosts"]) -> None: ...

    needNotify = ... # type: builtin___bool
    appId = ... # type: typing___Text
    appName = ... # type: typing___Text
    clusterId = ... # type: typing___Text
    clusterType = ... # type: typing___Text
    batchNum = ... # type: builtin___int
    batchInterval = ... # type: builtin___int
    failedStop = ... # type: builtin___bool
    targetId = ... # type: typing___Text
    targetName = ... # type: typing___Text
    instanceId = ... # type: typing___Text
    configPackageId = ... # type: typing___Text

    @property
    def labels(self) -> easy_flow_sdk___model___easy_flow___deploy_label_pb2___DeployLabel: ...

    @property
    def batches(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CreateRequest.Batches]: ...

    @property
    def cluster(self) -> easy_flow_sdk___model___cmdb___cluster_info_pb2___ClusterInfo: ...

    @property
    def instanceInfo(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CreateRequest.InstanceInfo]: ...

    @property
    def operationInfo(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CreateRequest.OperationInfo]: ...

    @property
    def targetList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[easy_flow_sdk___model___easy_flow___target_info_pb2___TargetInfo]: ...

    @property
    def packageList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[easy_flow_sdk___model___easy_flow___package_info_pb2___PackageInfo]: ...

    @property
    def configList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CreateRequest.ConfigList]: ...

    @property
    def configDiff(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CreateRequest.ConfigDiff]: ...

    def __init__(self,
        *,
        needNotify : typing___Optional[builtin___bool] = None,
        labels : typing___Optional[easy_flow_sdk___model___easy_flow___deploy_label_pb2___DeployLabel] = None,
        appId : typing___Optional[typing___Text] = None,
        appName : typing___Optional[typing___Text] = None,
        clusterId : typing___Optional[typing___Text] = None,
        clusterType : typing___Optional[typing___Text] = None,
        batchNum : typing___Optional[builtin___int] = None,
        batchInterval : typing___Optional[builtin___int] = None,
        batches : typing___Optional[typing___Iterable[CreateRequest.Batches]] = None,
        failedStop : typing___Optional[builtin___bool] = None,
        targetId : typing___Optional[typing___Text] = None,
        targetName : typing___Optional[typing___Text] = None,
        instanceId : typing___Optional[typing___Text] = None,
        cluster : typing___Optional[easy_flow_sdk___model___cmdb___cluster_info_pb2___ClusterInfo] = None,
        instanceInfo : typing___Optional[typing___Iterable[CreateRequest.InstanceInfo]] = None,
        operationInfo : typing___Optional[typing___Iterable[CreateRequest.OperationInfo]] = None,
        targetList : typing___Optional[typing___Iterable[easy_flow_sdk___model___easy_flow___target_info_pb2___TargetInfo]] = None,
        packageList : typing___Optional[typing___Iterable[easy_flow_sdk___model___easy_flow___package_info_pb2___PackageInfo]] = None,
        configList : typing___Optional[typing___Iterable[CreateRequest.ConfigList]] = None,
        configPackageId : typing___Optional[typing___Text] = None,
        configDiff : typing___Optional[typing___Iterable[CreateRequest.ConfigDiff]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"cluster",b"cluster",u"labels",b"labels"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"appId",b"appId",u"appName",b"appName",u"batchInterval",b"batchInterval",u"batchNum",b"batchNum",u"batches",b"batches",u"cluster",b"cluster",u"clusterId",b"clusterId",u"clusterType",b"clusterType",u"configDiff",b"configDiff",u"configList",b"configList",u"configPackageId",b"configPackageId",u"failedStop",b"failedStop",u"instanceId",b"instanceId",u"instanceInfo",b"instanceInfo",u"labels",b"labels",u"needNotify",b"needNotify",u"operationInfo",b"operationInfo",u"packageList",b"packageList",u"targetId",b"targetId",u"targetList",b"targetList",u"targetName",b"targetName"]) -> None: ...

class CreateResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Data(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        taskId = ... # type: typing___Text

        def __init__(self,
            *,
            taskId : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> CreateResponse.Data: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateResponse.Data: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"taskId",b"taskId"]) -> None: ...

    code = ... # type: builtin___int
    msg = ... # type: typing___Text

    @property
    def data(self) -> CreateResponse.Data: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        msg : typing___Optional[typing___Text] = None,
        data : typing___Optional[CreateResponse.Data] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"data",b"data",u"msg",b"msg"]) -> None: ...

class CreateResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> CreateResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[CreateResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
