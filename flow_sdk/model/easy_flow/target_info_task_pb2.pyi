# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from model.cmdb.cluster_info_pb2 import (
    ClusterInfo as model___cmdb___cluster_info_pb2___ClusterInfo,
)

from model.file_repository.diff_pb2 import (
    Diff as model___file_repository___diff_pb2___Diff,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class TaskTargetInfo(google___protobuf___message___Message):
    class InstanceInfo(google___protobuf___message___Message):
        versionName = ... # type: typing___Text
        packageId = ... # type: typing___Text
        installPath = ... # type: typing___Text
        versionId = ... # type: typing___Text

        def __init__(self,
            versionName : typing___Optional[typing___Text] = None,
            packageId : typing___Optional[typing___Text] = None,
            installPath : typing___Optional[typing___Text] = None,
            versionId : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> TaskTargetInfo.InstanceInfo: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"installPath",u"packageId",u"versionId",u"versionName"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"installPath",b"packageId",b"versionId",b"versionName"]) -> None: ...

    class VersionInfo(google___protobuf___message___Message):
        class SourceDecode(google___protobuf___message___Message):
            ensName = ... # type: typing___Text
            host = ... # type: typing___Text
            type = ... # type: typing___Text
            ip = ... # type: typing___Text
            port = ... # type: int

            def __init__(self,
                ensName : typing___Optional[typing___Text] = None,
                host : typing___Optional[typing___Text] = None,
                type : typing___Optional[typing___Text] = None,
                ip : typing___Optional[typing___Text] = None,
                port : typing___Optional[int] = None,
                ) -> None: ...
            @classmethod
            def FromString(cls, s: bytes) -> TaskTargetInfo.VersionInfo.SourceDecode: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            if sys.version_info >= (3,):
                def ClearField(self, field_name: typing_extensions___Literal[u"ensName",u"host",u"ip",u"port",u"type"]) -> None: ...
            else:
                def ClearField(self, field_name: typing_extensions___Literal[b"ensName",b"host",b"ip",b"port",b"type"]) -> None: ...

        source = ... # type: typing___Text
        name = ... # type: typing___Text
        versionId = ... # type: typing___Text
        packageId = ... # type: typing___Text
        org = ... # type: int
        creator = ... # type: typing___Text
        memo = ... # type: typing___Text
        ctime = ... # type: typing___Text
        mtime = ... # type: typing___Text
        sign = ... # type: typing___Text
        sourceType = ... # type: typing___Text
        conf = ... # type: typing___Text
        env_type = ... # type: int

        @property
        def sourceDecode(self) -> TaskTargetInfo.VersionInfo.SourceDecode: ...

        @property
        def diff(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[model___file_repository___diff_pb2___Diff]: ...

        def __init__(self,
            sourceDecode : typing___Optional[TaskTargetInfo.VersionInfo.SourceDecode] = None,
            source : typing___Optional[typing___Text] = None,
            diff : typing___Optional[typing___Iterable[model___file_repository___diff_pb2___Diff]] = None,
            name : typing___Optional[typing___Text] = None,
            versionId : typing___Optional[typing___Text] = None,
            packageId : typing___Optional[typing___Text] = None,
            org : typing___Optional[int] = None,
            creator : typing___Optional[typing___Text] = None,
            memo : typing___Optional[typing___Text] = None,
            ctime : typing___Optional[typing___Text] = None,
            mtime : typing___Optional[typing___Text] = None,
            sign : typing___Optional[typing___Text] = None,
            sourceType : typing___Optional[typing___Text] = None,
            conf : typing___Optional[typing___Text] = None,
            env_type : typing___Optional[int] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> TaskTargetInfo.VersionInfo: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"sourceDecode"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"conf",u"creator",u"ctime",u"diff",u"env_type",u"memo",u"mtime",u"name",u"org",u"packageId",u"sign",u"source",u"sourceDecode",u"sourceType",u"versionId"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"sourceDecode",b"sourceDecode"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[b"conf",b"creator",b"ctime",b"diff",b"env_type",b"memo",b"mtime",b"name",b"org",b"packageId",b"sign",b"source",b"sourceDecode",b"sourceType",b"versionId"]) -> None: ...

    targetId = ... # type: typing___Text
    targetName = ... # type: typing___Text
    instanceId = ... # type: typing___Text

    @property
    def cluster(self) -> model___cmdb___cluster_info_pb2___ClusterInfo: ...

    @property
    def instanceInfo(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[TaskTargetInfo.InstanceInfo]: ...

    @property
    def versionInfo(self) -> TaskTargetInfo.VersionInfo: ...

    def __init__(self,
        targetId : typing___Optional[typing___Text] = None,
        targetName : typing___Optional[typing___Text] = None,
        instanceId : typing___Optional[typing___Text] = None,
        cluster : typing___Optional[model___cmdb___cluster_info_pb2___ClusterInfo] = None,
        instanceInfo : typing___Optional[typing___Iterable[TaskTargetInfo.InstanceInfo]] = None,
        versionInfo : typing___Optional[TaskTargetInfo.VersionInfo] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> TaskTargetInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"cluster",u"versionInfo"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"cluster",u"instanceId",u"instanceInfo",u"targetId",u"targetName",u"versionInfo"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"cluster",b"cluster",u"versionInfo",b"versionInfo"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"cluster",b"instanceId",b"instanceInfo",b"targetId",b"targetName",b"versionInfo"]) -> None: ...