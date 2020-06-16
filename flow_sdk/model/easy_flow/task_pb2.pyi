# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from flow_sdk.model.easy_flow.deploy_target_pb2 import (
    DeployTarget as flow_sdk___model___easy_flow___deploy_target_pb2___DeployTarget,
)

from flow_sdk.model.easy_flow.package_info_pb2 import (
    PackageInfo as flow_sdk___model___easy_flow___package_info_pb2___PackageInfo,
)

from flow_sdk.model.easy_flow.target_info_pb2 import (
    TargetInfo as flow_sdk___model___easy_flow___target_info_pb2___TargetInfo,
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

from google.protobuf.struct_pb2 import (
    Struct as google___protobuf___struct_pb2___Struct,
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


class Task(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
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
                    def FromString(cls, s: builtin___bytes) -> Task.ConfigList.Configs.Items: ...
                else:
                    @classmethod
                    def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Task.ConfigList.Configs.Items: ...
                def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name",u"path",b"path"]) -> None: ...

            packageId = ... # type: typing___Text
            installPath = ... # type: typing___Text

            @property
            def items(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Task.ConfigList.Configs.Items]: ...

            def __init__(self,
                *,
                packageId : typing___Optional[typing___Text] = None,
                items : typing___Optional[typing___Iterable[Task.ConfigList.Configs.Items]] = None,
                installPath : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> Task.ConfigList.Configs: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Task.ConfigList.Configs: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"installPath",b"installPath",u"items",b"items",u"packageId",b"packageId"]) -> None: ...

        hosts = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

        @property
        def configs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Task.ConfigList.Configs]: ...

        def __init__(self,
            *,
            hosts : typing___Optional[typing___Iterable[typing___Text]] = None,
            configs : typing___Optional[typing___Iterable[Task.ConfigList.Configs]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Task.ConfigList: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Task.ConfigList: ...
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
                    def FromString(cls, s: builtin___bytes) -> Task.ConfigDiff.Detail.Items: ...
                else:
                    @classmethod
                    def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Task.ConfigDiff.Detail.Items: ...
                def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                def ClearField(self, field_name: typing_extensions___Literal[u"newName",b"newName",u"oldName",b"oldName",u"path",b"path"]) -> None: ...

            packageId = ... # type: typing___Text
            installPath = ... # type: typing___Text

            @property
            def items(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Task.ConfigDiff.Detail.Items]: ...

            def __init__(self,
                *,
                items : typing___Optional[typing___Iterable[Task.ConfigDiff.Detail.Items]] = None,
                packageId : typing___Optional[typing___Text] = None,
                installPath : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> Task.ConfigDiff.Detail: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Task.ConfigDiff.Detail: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"installPath",b"installPath",u"items",b"items",u"packageId",b"packageId"]) -> None: ...

        hosts = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

        @property
        def detail(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Task.ConfigDiff.Detail]: ...

        def __init__(self,
            *,
            hosts : typing___Optional[typing___Iterable[typing___Text]] = None,
            detail : typing___Optional[typing___Iterable[Task.ConfigDiff.Detail]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Task.ConfigDiff: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Task.ConfigDiff: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"detail",b"detail",u"hosts",b"hosts"]) -> None: ...

    class Batches(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def targets(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[flow_sdk___model___easy_flow___deploy_target_pb2___DeployTarget]: ...

        def __init__(self,
            *,
            targets : typing___Optional[typing___Iterable[flow_sdk___model___easy_flow___deploy_target_pb2___DeployTarget]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Task.Batches: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Task.Batches: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"targets",b"targets"]) -> None: ...

    appId = ... # type: typing___Text
    appName = ... # type: typing___Text
    clusterId = ... # type: typing___Text
    clusterType = ... # type: typing___Text
    operator = ... # type: typing___Text
    org = ... # type: builtin___int
    taskTimeStamp = ... # type: typing___Text
    configVersion = ... # type: typing___Text
    configPackageId = ... # type: typing___Text
    needNotify = ... # type: builtin___bool
    batchNum = ... # type: builtin___int
    batchInterval = ... # type: builtin___int
    failedStop = ... # type: builtin___bool

    @property
    def targetList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[flow_sdk___model___easy_flow___target_info_pb2___TargetInfo]: ...

    @property
    def packageList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[flow_sdk___model___easy_flow___package_info_pb2___PackageInfo]: ...

    @property
    def configList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Task.ConfigList]: ...

    @property
    def labels(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def configDiff(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Task.ConfigDiff]: ...

    @property
    def batches(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Task.Batches]: ...

    def __init__(self,
        *,
        appId : typing___Optional[typing___Text] = None,
        appName : typing___Optional[typing___Text] = None,
        clusterId : typing___Optional[typing___Text] = None,
        clusterType : typing___Optional[typing___Text] = None,
        operator : typing___Optional[typing___Text] = None,
        org : typing___Optional[builtin___int] = None,
        targetList : typing___Optional[typing___Iterable[flow_sdk___model___easy_flow___target_info_pb2___TargetInfo]] = None,
        packageList : typing___Optional[typing___Iterable[flow_sdk___model___easy_flow___package_info_pb2___PackageInfo]] = None,
        configList : typing___Optional[typing___Iterable[Task.ConfigList]] = None,
        taskTimeStamp : typing___Optional[typing___Text] = None,
        configVersion : typing___Optional[typing___Text] = None,
        configPackageId : typing___Optional[typing___Text] = None,
        labels : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        configDiff : typing___Optional[typing___Iterable[Task.ConfigDiff]] = None,
        needNotify : typing___Optional[builtin___bool] = None,
        batchNum : typing___Optional[builtin___int] = None,
        batchInterval : typing___Optional[builtin___int] = None,
        batches : typing___Optional[typing___Iterable[Task.Batches]] = None,
        failedStop : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Task: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Task: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"labels",b"labels"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"appId",b"appId",u"appName",b"appName",u"batchInterval",b"batchInterval",u"batchNum",b"batchNum",u"batches",b"batches",u"clusterId",b"clusterId",u"clusterType",b"clusterType",u"configDiff",b"configDiff",u"configList",b"configList",u"configPackageId",b"configPackageId",u"configVersion",b"configVersion",u"failedStop",b"failedStop",u"labels",b"labels",u"needNotify",b"needNotify",u"operator",b"operator",u"org",b"org",u"packageList",b"packageList",u"targetList",b"targetList",u"taskTimeStamp",b"taskTimeStamp"]) -> None: ...
