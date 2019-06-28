# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from model.pipeline.pipeline_pb2 import (
    Pipeline as model___pipeline___pipeline_pb2___Pipeline,
)

from model.pipeline.project_pb2 import (
    Project as model___pipeline___project_pb2___Project,
)

from model.pipeline.provider_pb2 import (
    Provider as model___pipeline___provider_pb2___Provider,
)

from model.pipeline.trigger_pb2 import (
    Trigger as model___pipeline___trigger_pb2___Trigger,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class GetTriggerDetailRequest(google___protobuf___message___Message):
    id = ... # type: typing___Text

    def __init__(self,
        id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetTriggerDetailRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"id"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"id"]) -> None: ...

class GetTriggerDetailResponse(google___protobuf___message___Message):

    @property
    def trigger(self) -> model___pipeline___trigger_pb2___Trigger: ...

    @property
    def project(self) -> model___pipeline___project_pb2___Project: ...

    @property
    def provider(self) -> model___pipeline___provider_pb2___Provider: ...

    @property
    def pipeline(self) -> model___pipeline___pipeline_pb2___Pipeline: ...

    def __init__(self,
        trigger : typing___Optional[model___pipeline___trigger_pb2___Trigger] = None,
        project : typing___Optional[model___pipeline___project_pb2___Project] = None,
        provider : typing___Optional[model___pipeline___provider_pb2___Provider] = None,
        pipeline : typing___Optional[model___pipeline___pipeline_pb2___Pipeline] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetTriggerDetailResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"pipeline",u"project",u"provider",u"trigger"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"pipeline",u"project",u"provider",u"trigger"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"pipeline",b"pipeline",u"project",b"project",u"provider",b"provider",u"trigger",b"trigger"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"pipeline",b"project",b"provider",b"trigger"]) -> None: ...

class GetTriggerDetailResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> GetTriggerDetailResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[GetTriggerDetailResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetTriggerDetailResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...