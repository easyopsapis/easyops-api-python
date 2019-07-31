# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from model.cmdb_extend.app_pipeline_pb2 import (
    AppPipeline as model___cmdb_extend___app_pipeline_pb2___AppPipeline,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class GetPipelineRequest(google___protobuf___message___Message):
    appId = ... # type: typing___Text
    flowId = ... # type: typing___Text

    def __init__(self,
        appId : typing___Optional[typing___Text] = None,
        flowId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetPipelineRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"appId",u"flowId"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"appId",b"flowId"]) -> None: ...

class GetPipelineResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> model___cmdb_extend___app_pipeline_pb2___AppPipeline: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[model___cmdb_extend___app_pipeline_pb2___AppPipeline] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetPipelineResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...
