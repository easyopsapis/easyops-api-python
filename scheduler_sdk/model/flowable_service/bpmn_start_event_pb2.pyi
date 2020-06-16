# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from scheduler_sdk.model.flowable_service.bpmn_links_pb2 import (
    BPMNLinks as scheduler_sdk___model___flowable_service___bpmn_links_pb2___BPMNLinks,
)

from typing import (
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


class BPMNStartEvent(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id = ... # type: typing___Text

    @property
    def links(self) -> scheduler_sdk___model___flowable_service___bpmn_links_pb2___BPMNLinks: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        links : typing___Optional[scheduler_sdk___model___flowable_service___bpmn_links_pb2___BPMNLinks] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> BPMNStartEvent: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> BPMNStartEvent: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"links",b"links"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"links",b"links"]) -> None: ...
