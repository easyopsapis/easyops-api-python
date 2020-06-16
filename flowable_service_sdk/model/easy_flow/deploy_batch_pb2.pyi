# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from flowable_service_sdk.model.easy_flow.deploy_target_pb2 import (
    DeployTarget as flowable_service_sdk___model___easy_flow___deploy_target_pb2___DeployTarget,
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


class DeployBatch(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Batches(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def targets(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[flowable_service_sdk___model___easy_flow___deploy_target_pb2___DeployTarget]: ...

        def __init__(self,
            *,
            targets : typing___Optional[typing___Iterable[flowable_service_sdk___model___easy_flow___deploy_target_pb2___DeployTarget]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> DeployBatch.Batches: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DeployBatch.Batches: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"targets",b"targets"]) -> None: ...

    type = ... # type: typing___Text
    batchNum = ... # type: builtin___int
    batchInterval = ... # type: builtin___int
    failedStop = ... # type: builtin___bool

    @property
    def batches(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[DeployBatch.Batches]: ...

    def __init__(self,
        *,
        type : typing___Optional[typing___Text] = None,
        batchNum : typing___Optional[builtin___int] = None,
        batchInterval : typing___Optional[builtin___int] = None,
        batches : typing___Optional[typing___Iterable[DeployBatch.Batches]] = None,
        failedStop : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> DeployBatch: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DeployBatch: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"batchInterval",b"batchInterval",u"batchNum",b"batchNum",u"batches",b"batches",u"failedStop",b"failedStop",u"type",b"type"]) -> None: ...
