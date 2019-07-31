# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from model.inspection.collector_pb2 import (
    InspectionCollector as model___inspection___collector_pb2___InspectionCollector,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class UpdateCollectorRequest(google___protobuf___message___Message):
    class Args(google___protobuf___message___Message):
        key = ... # type: typing___Text
        alias = ... # type: typing___Text
        type = ... # type: typing___Text
        require = ... # type: bool

        def __init__(self,
            key : typing___Optional[typing___Text] = None,
            alias : typing___Optional[typing___Text] = None,
            type : typing___Optional[typing___Text] = None,
            require : typing___Optional[bool] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> UpdateCollectorRequest.Args: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"alias",u"key",u"require",u"type"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"alias",b"key",b"require",b"type"]) -> None: ...

    pluginId = ... # type: typing___Text
    collectorId = ... # type: typing___Text
    name = ... # type: typing___Text
    content = ... # type: typing___Text
    script = ... # type: typing___Text

    @property
    def args(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[UpdateCollectorRequest.Args]: ...

    def __init__(self,
        pluginId : typing___Optional[typing___Text] = None,
        collectorId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        content : typing___Optional[typing___Text] = None,
        script : typing___Optional[typing___Text] = None,
        args : typing___Optional[typing___Iterable[UpdateCollectorRequest.Args]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> UpdateCollectorRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"args",u"collectorId",u"content",u"name",u"pluginId",u"script"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"args",b"collectorId",b"content",b"name",b"pluginId",b"script"]) -> None: ...

class UpdateCollectorResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> model___inspection___collector_pb2___InspectionCollector: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[model___inspection___collector_pb2___InspectionCollector] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> UpdateCollectorResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...
