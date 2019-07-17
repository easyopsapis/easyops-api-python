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

from model.easy_flow.deploy_package_result_pb2 import (
    DeployPackageResult as model___easy_flow___deploy_package_result_pb2___DeployPackageResult,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class TargetResult(google___protobuf___message___Message):
    targetId = ... # type: typing___Text
    targetName = ... # type: typing___Text
    code = ... # type: int
    msg = ... # type: typing___Text
    status = ... # type: typing___Text

    @property
    def cluster(self) -> model___cmdb___cluster_info_pb2___ClusterInfo: ...

    @property
    def packageStatus(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[model___easy_flow___deploy_package_result_pb2___DeployPackageResult]: ...

    def __init__(self,
        targetId : typing___Optional[typing___Text] = None,
        targetName : typing___Optional[typing___Text] = None,
        cluster : typing___Optional[model___cmdb___cluster_info_pb2___ClusterInfo] = None,
        code : typing___Optional[int] = None,
        msg : typing___Optional[typing___Text] = None,
        status : typing___Optional[typing___Text] = None,
        packageStatus : typing___Optional[typing___Iterable[model___easy_flow___deploy_package_result_pb2___DeployPackageResult]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> TargetResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"cluster"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"cluster",u"code",u"msg",u"packageStatus",u"status",u"targetId",u"targetName"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"cluster",b"cluster"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"cluster",b"code",b"msg",b"packageStatus",b"status",b"targetId",b"targetName"]) -> None: ...