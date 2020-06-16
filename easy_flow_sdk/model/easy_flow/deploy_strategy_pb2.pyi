# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from easy_flow_sdk.model.cmdb.cluster_info_pb2 import (
    ClusterInfo as easy_flow_sdk___model___cmdb___cluster_info_pb2___ClusterInfo,
)

from easy_flow_sdk.model.easy_flow.deploy_target_pb2 import (
    DeployTarget as easy_flow_sdk___model___easy_flow___deploy_target_pb2___DeployTarget,
)

from easy_flow_sdk.model.easy_flow.target_info_pb2 import (
    TargetInfo as easy_flow_sdk___model___easy_flow___target_info_pb2___TargetInfo,
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


class DeployStrategy(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class App(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        name = ... # type: typing___Text
        appId = ... # type: typing___Text

        def __init__(self,
            *,
            name : typing___Optional[typing___Text] = None,
            appId : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> DeployStrategy.App: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DeployStrategy.App: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"appId",b"appId",u"name",b"name"]) -> None: ...

    class BatchStrategy(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class AutoBatch(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            batchNum = ... # type: builtin___int
            batchInterval = ... # type: builtin___int
            failedStop = ... # type: builtin___bool

            def __init__(self,
                *,
                batchNum : typing___Optional[builtin___int] = None,
                batchInterval : typing___Optional[builtin___int] = None,
                failedStop : typing___Optional[builtin___bool] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> DeployStrategy.BatchStrategy.AutoBatch: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DeployStrategy.BatchStrategy.AutoBatch: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"batchInterval",b"batchInterval",u"batchNum",b"batchNum",u"failedStop",b"failedStop"]) -> None: ...

        class ManualBatch(google___protobuf___message___Message):
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
                    def FromString(cls, s: builtin___bytes) -> DeployStrategy.BatchStrategy.ManualBatch.Batches: ...
                else:
                    @classmethod
                    def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DeployStrategy.BatchStrategy.ManualBatch.Batches: ...
                def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                def ClearField(self, field_name: typing_extensions___Literal[u"targets",b"targets"]) -> None: ...

            batchNum = ... # type: builtin___int
            batchInterval = ... # type: builtin___int
            failedStop = ... # type: builtin___bool

            @property
            def batches(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[DeployStrategy.BatchStrategy.ManualBatch.Batches]: ...

            def __init__(self,
                *,
                batches : typing___Optional[typing___Iterable[DeployStrategy.BatchStrategy.ManualBatch.Batches]] = None,
                batchNum : typing___Optional[builtin___int] = None,
                batchInterval : typing___Optional[builtin___int] = None,
                failedStop : typing___Optional[builtin___bool] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> DeployStrategy.BatchStrategy.ManualBatch: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DeployStrategy.BatchStrategy.ManualBatch: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"batchInterval",b"batchInterval",u"batchNum",b"batchNum",u"batches",b"batches",u"failedStop",b"failedStop"]) -> None: ...

        type = ... # type: typing___Text

        @property
        def autoBatch(self) -> DeployStrategy.BatchStrategy.AutoBatch: ...

        @property
        def manualBatch(self) -> DeployStrategy.BatchStrategy.ManualBatch: ...

        def __init__(self,
            *,
            autoBatch : typing___Optional[DeployStrategy.BatchStrategy.AutoBatch] = None,
            manualBatch : typing___Optional[DeployStrategy.BatchStrategy.ManualBatch] = None,
            type : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> DeployStrategy.BatchStrategy: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DeployStrategy.BatchStrategy: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"autoBatch",b"autoBatch",u"manualBatch",b"manualBatch"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"autoBatch",b"autoBatch",u"manualBatch",b"manualBatch",u"type",b"type"]) -> None: ...

    class PackageList(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        packageName = ... # type: typing___Text
        targetVersion = ... # type: typing___Text
        preStop = ... # type: builtin___bool
        postRestart = ... # type: builtin___bool
        autoStart = ... # type: builtin___bool
        userCheck = ... # type: builtin___bool
        fullUpdate = ... # type: builtin___bool
        packageId = ... # type: typing___Text
        installPath = ... # type: typing___Text
        type = ... # type: builtin___int
        platform = ... # type: typing___Text

        @property
        def cluster(self) -> easy_flow_sdk___model___cmdb___cluster_info_pb2___ClusterInfo: ...

        def __init__(self,
            *,
            packageName : typing___Optional[typing___Text] = None,
            cluster : typing___Optional[easy_flow_sdk___model___cmdb___cluster_info_pb2___ClusterInfo] = None,
            targetVersion : typing___Optional[typing___Text] = None,
            preStop : typing___Optional[builtin___bool] = None,
            postRestart : typing___Optional[builtin___bool] = None,
            autoStart : typing___Optional[builtin___bool] = None,
            userCheck : typing___Optional[builtin___bool] = None,
            fullUpdate : typing___Optional[builtin___bool] = None,
            packageId : typing___Optional[typing___Text] = None,
            installPath : typing___Optional[typing___Text] = None,
            type : typing___Optional[builtin___int] = None,
            platform : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> DeployStrategy.PackageList: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DeployStrategy.PackageList: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"cluster",b"cluster"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"autoStart",b"autoStart",u"cluster",b"cluster",u"fullUpdate",b"fullUpdate",u"installPath",b"installPath",u"packageId",b"packageId",u"packageName",b"packageName",u"platform",b"platform",u"postRestart",b"postRestart",u"preStop",b"preStop",u"targetVersion",b"targetVersion",u"type",b"type",u"userCheck",b"userCheck"]) -> None: ...

    class Status(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        outOfDate = ... # type: builtin___bool

        def __init__(self,
            *,
            outOfDate : typing___Optional[builtin___bool] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> DeployStrategy.Status: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DeployStrategy.Status: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"outOfDate",b"outOfDate"]) -> None: ...

    id = ... # type: typing___Text
    name = ... # type: typing___Text
    apiVersion = ... # type: typing___Text
    org = ... # type: builtin___int
    type = ... # type: typing___Text
    scope = ... # type: typing___Text
    clusterEnvironment = ... # type: typing___Text
    clusterType = ... # type: typing___Text

    @property
    def app(self) -> DeployStrategy.App: ...

    @property
    def batchStrategy(self) -> DeployStrategy.BatchStrategy: ...

    @property
    def clusters(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[easy_flow_sdk___model___cmdb___cluster_info_pb2___ClusterInfo]: ...

    @property
    def targetList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[easy_flow_sdk___model___easy_flow___target_info_pb2___TargetInfo]: ...

    @property
    def packageList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[DeployStrategy.PackageList]: ...

    @property
    def status(self) -> DeployStrategy.Status: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        apiVersion : typing___Optional[typing___Text] = None,
        org : typing___Optional[builtin___int] = None,
        app : typing___Optional[DeployStrategy.App] = None,
        type : typing___Optional[typing___Text] = None,
        batchStrategy : typing___Optional[DeployStrategy.BatchStrategy] = None,
        scope : typing___Optional[typing___Text] = None,
        clusters : typing___Optional[typing___Iterable[easy_flow_sdk___model___cmdb___cluster_info_pb2___ClusterInfo]] = None,
        targetList : typing___Optional[typing___Iterable[easy_flow_sdk___model___easy_flow___target_info_pb2___TargetInfo]] = None,
        clusterEnvironment : typing___Optional[typing___Text] = None,
        clusterType : typing___Optional[typing___Text] = None,
        packageList : typing___Optional[typing___Iterable[DeployStrategy.PackageList]] = None,
        status : typing___Optional[DeployStrategy.Status] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> DeployStrategy: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DeployStrategy: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"app",b"app",u"batchStrategy",b"batchStrategy",u"status",b"status"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"apiVersion",b"apiVersion",u"app",b"app",u"batchStrategy",b"batchStrategy",u"clusterEnvironment",b"clusterEnvironment",u"clusterType",b"clusterType",u"clusters",b"clusters",u"id",b"id",u"name",b"name",u"org",b"org",u"packageList",b"packageList",u"scope",b"scope",u"status",b"status",u"targetList",b"targetList",u"type",b"type"]) -> None: ...
