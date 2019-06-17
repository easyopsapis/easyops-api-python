# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from model.cmdb.fail_instance_pb2 import (
    FailInstance as model___cmdb___fail_instance_pb2___FailInstance,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class DeleteInstanceBatchRequest(google___protobuf___message___Message):
    objectId = ... # type: typing___Text
    instanceIds = ... # type: typing___Text

    def __init__(self,
        objectId : typing___Optional[typing___Text] = None,
        instanceIds : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DeleteInstanceBatchRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"instanceIds",u"objectId"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"instanceIds",b"objectId"]) -> None: ...

class DeleteInstanceBatchResponse(google___protobuf___message___Message):

    @property
    def deleteFailedInstances(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[model___cmdb___fail_instance_pb2___FailInstance]: ...

    def __init__(self,
        deleteFailedInstances : typing___Optional[typing___Iterable[model___cmdb___fail_instance_pb2___FailInstance]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DeleteInstanceBatchResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"deleteFailedInstances"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"deleteFailedInstances"]) -> None: ...

class DeleteInstanceBatchResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> DeleteInstanceBatchResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[DeleteInstanceBatchResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DeleteInstanceBatchResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...