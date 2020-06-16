# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from console_gateway_sdk.model.easy_flow.deploy_label_pb2 import (
    DeployLabel as console_gateway_sdk___model___easy_flow___deploy_label_pb2___DeployLabel,
)

from console_gateway_sdk.model.easy_flow.target_result_pb2 import (
    TargetResult as console_gateway_sdk___model___easy_flow___target_result_pb2___TargetResult,
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


class DeployRet(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
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
                    def FromString(cls, s: builtin___bytes) -> DeployRet.ConfigDiff.Detail.Items: ...
                else:
                    @classmethod
                    def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DeployRet.ConfigDiff.Detail.Items: ...
                def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                def ClearField(self, field_name: typing_extensions___Literal[u"newName",b"newName",u"oldName",b"oldName",u"path",b"path"]) -> None: ...

            packageId = ... # type: typing___Text
            installPath = ... # type: typing___Text

            @property
            def items(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[DeployRet.ConfigDiff.Detail.Items]: ...

            def __init__(self,
                *,
                items : typing___Optional[typing___Iterable[DeployRet.ConfigDiff.Detail.Items]] = None,
                packageId : typing___Optional[typing___Text] = None,
                installPath : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> DeployRet.ConfigDiff.Detail: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DeployRet.ConfigDiff.Detail: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"installPath",b"installPath",u"items",b"items",u"packageId",b"packageId"]) -> None: ...

        hosts = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

        @property
        def detail(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[DeployRet.ConfigDiff.Detail]: ...

        def __init__(self,
            *,
            hosts : typing___Optional[typing___Iterable[typing___Text]] = None,
            detail : typing___Optional[typing___Iterable[DeployRet.ConfigDiff.Detail]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> DeployRet.ConfigDiff: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DeployRet.ConfigDiff: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"detail",b"detail",u"hosts",b"hosts"]) -> None: ...

    taskId = ... # type: typing___Text
    appId = ... # type: typing___Text
    appName = ... # type: typing___Text
    operator = ... # type: typing___Text
    org = ... # type: builtin___int
    batchNum = ... # type: builtin___int
    batchInterval = ... # type: builtin___int
    failedStop = ... # type: builtin___bool
    status = ... # type: typing___Text
    code = ... # type: builtin___int
    usedTime = ... # type: builtin___int
    startTime = ... # type: typing___Text
    endTime = ... # type: typing___Text
    clusterId = ... # type: typing___Text
    configPackageId = ... # type: typing___Text

    @property
    def targetList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[console_gateway_sdk___model___easy_flow___target_result_pb2___TargetResult]: ...

    @property
    def labels(self) -> console_gateway_sdk___model___easy_flow___deploy_label_pb2___DeployLabel: ...

    @property
    def configDiff(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[DeployRet.ConfigDiff]: ...

    def __init__(self,
        *,
        taskId : typing___Optional[typing___Text] = None,
        appId : typing___Optional[typing___Text] = None,
        appName : typing___Optional[typing___Text] = None,
        operator : typing___Optional[typing___Text] = None,
        org : typing___Optional[builtin___int] = None,
        targetList : typing___Optional[typing___Iterable[console_gateway_sdk___model___easy_flow___target_result_pb2___TargetResult]] = None,
        batchNum : typing___Optional[builtin___int] = None,
        batchInterval : typing___Optional[builtin___int] = None,
        failedStop : typing___Optional[builtin___bool] = None,
        status : typing___Optional[typing___Text] = None,
        code : typing___Optional[builtin___int] = None,
        usedTime : typing___Optional[builtin___int] = None,
        startTime : typing___Optional[typing___Text] = None,
        endTime : typing___Optional[typing___Text] = None,
        clusterId : typing___Optional[typing___Text] = None,
        configPackageId : typing___Optional[typing___Text] = None,
        labels : typing___Optional[console_gateway_sdk___model___easy_flow___deploy_label_pb2___DeployLabel] = None,
        configDiff : typing___Optional[typing___Iterable[DeployRet.ConfigDiff]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> DeployRet: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DeployRet: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"labels",b"labels"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"appId",b"appId",u"appName",b"appName",u"batchInterval",b"batchInterval",u"batchNum",b"batchNum",u"clusterId",b"clusterId",u"code",b"code",u"configDiff",b"configDiff",u"configPackageId",b"configPackageId",u"endTime",b"endTime",u"failedStop",b"failedStop",u"labels",b"labels",u"operator",b"operator",u"org",b"org",u"startTime",b"startTime",u"status",b"status",u"targetList",b"targetList",u"taskId",b"taskId",u"usedTime",b"usedTime"]) -> None: ...
