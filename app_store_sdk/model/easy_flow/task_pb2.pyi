# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
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
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class Task(google___protobuf___message___Message):
    class ConfigList(google___protobuf___message___Message):
        class Configs(google___protobuf___message___Message):
            class Items(google___protobuf___message___Message):
                name = ... # type: typing___Text
                path = ... # type: typing___Text

                def __init__(self,
                    name : typing___Optional[typing___Text] = None,
                    path : typing___Optional[typing___Text] = None,
                    ) -> None: ...
                @classmethod
                def FromString(cls, s: bytes) -> Task.ConfigList.Configs.Items: ...
                def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                if sys.version_info >= (3,):
                    def ClearField(self, field_name: typing_extensions___Literal[u"name",u"path"]) -> None: ...
                else:
                    def ClearField(self, field_name: typing_extensions___Literal[b"name",b"path"]) -> None: ...

            packageId = ... # type: typing___Text

            @property
            def items(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Task.ConfigList.Configs.Items]: ...

            def __init__(self,
                packageId : typing___Optional[typing___Text] = None,
                items : typing___Optional[typing___Iterable[Task.ConfigList.Configs.Items]] = None,
                ) -> None: ...
            @classmethod
            def FromString(cls, s: bytes) -> Task.ConfigList.Configs: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            if sys.version_info >= (3,):
                def ClearField(self, field_name: typing_extensions___Literal[u"items",u"packageId"]) -> None: ...
            else:
                def ClearField(self, field_name: typing_extensions___Literal[b"items",b"packageId"]) -> None: ...

        hosts = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

        @property
        def configs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Task.ConfigList.Configs]: ...

        def __init__(self,
            hosts : typing___Optional[typing___Iterable[typing___Text]] = None,
            configs : typing___Optional[typing___Iterable[Task.ConfigList.Configs]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> Task.ConfigList: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"configs",u"hosts"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"configs",b"hosts"]) -> None: ...

    appId = ... # type: typing___Text
    appName = ... # type: typing___Text
    clusterId = ... # type: typing___Text
    clusterType = ... # type: typing___Text
    operator = ... # type: typing___Text
    org = ... # type: int
    taskTimeStamp = ... # type: typing___Text
    configVersion = ... # type: typing___Text
    configPackageId = ... # type: typing___Text
    configDiff = ... # type: typing___Text

    @property
    def configList(self) -> Task.ConfigList: ...

    @property
    def labels(self) -> google___protobuf___struct_pb2___Struct: ...

    def __init__(self,
        appId : typing___Optional[typing___Text] = None,
        appName : typing___Optional[typing___Text] = None,
        clusterId : typing___Optional[typing___Text] = None,
        clusterType : typing___Optional[typing___Text] = None,
        operator : typing___Optional[typing___Text] = None,
        org : typing___Optional[int] = None,
        configList : typing___Optional[Task.ConfigList] = None,
        taskTimeStamp : typing___Optional[typing___Text] = None,
        configVersion : typing___Optional[typing___Text] = None,
        configPackageId : typing___Optional[typing___Text] = None,
        labels : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        configDiff : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Task: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"configList",u"labels"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"appId",u"appName",u"clusterId",u"clusterType",u"configDiff",u"configList",u"configPackageId",u"configVersion",u"labels",u"operator",u"org",u"taskTimeStamp"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"configList",b"configList",u"labels",b"labels"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"appId",b"appName",b"clusterId",b"clusterType",b"configDiff",b"configList",b"configPackageId",b"configVersion",b"labels",b"operator",b"org",b"taskTimeStamp"]) -> None: ...