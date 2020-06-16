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

from notify_sdk.model.cmdb.cluster_info_pb2 import (
    ClusterInfo as notify_sdk___model___cmdb___cluster_info_pb2___ClusterInfo,
)

from notify_sdk.model.easy_flow.deploy_package_result_pb2 import (
    DeployPackageResult as notify_sdk___model___easy_flow___deploy_package_result_pb2___DeployPackageResult,
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


class TargetResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    targetId = ... # type: typing___Text
    targetName = ... # type: typing___Text
    code = ... # type: builtin___int
    msg = ... # type: typing___Text
    status = ... # type: typing___Text

    @property
    def cluster(self) -> notify_sdk___model___cmdb___cluster_info_pb2___ClusterInfo: ...

    @property
    def packageStatus(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[notify_sdk___model___easy_flow___deploy_package_result_pb2___DeployPackageResult]: ...

    def __init__(self,
        *,
        targetId : typing___Optional[typing___Text] = None,
        targetName : typing___Optional[typing___Text] = None,
        cluster : typing___Optional[notify_sdk___model___cmdb___cluster_info_pb2___ClusterInfo] = None,
        code : typing___Optional[builtin___int] = None,
        msg : typing___Optional[typing___Text] = None,
        status : typing___Optional[typing___Text] = None,
        packageStatus : typing___Optional[typing___Iterable[notify_sdk___model___easy_flow___deploy_package_result_pb2___DeployPackageResult]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TargetResult: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TargetResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"cluster",b"cluster"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"cluster",b"cluster",u"code",b"code",u"msg",b"msg",u"packageStatus",b"packageStatus",u"status",b"status",u"targetId",b"targetId",u"targetName",b"targetName"]) -> None: ...
