# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
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


class HistoryExportExcelRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    object_id = ... # type: typing___Text
    instanceId = ... # type: typing___Text
    operator = ... # type: typing___Text
    event = ... # type: typing___Text
    exclude_event = ... # type: typing___Text
    parent_event_id = ... # type: typing___Text
    range = ... # type: typing___Text
    st = ... # type: typing___Text
    et = ... # type: typing___Text
    with_children = ... # type: builtin___bool
    is_next = ... # type: builtin___bool

    def __init__(self,
        *,
        object_id : typing___Optional[typing___Text] = None,
        instanceId : typing___Optional[typing___Text] = None,
        operator : typing___Optional[typing___Text] = None,
        event : typing___Optional[typing___Text] = None,
        exclude_event : typing___Optional[typing___Text] = None,
        parent_event_id : typing___Optional[typing___Text] = None,
        range : typing___Optional[typing___Text] = None,
        st : typing___Optional[typing___Text] = None,
        et : typing___Optional[typing___Text] = None,
        with_children : typing___Optional[builtin___bool] = None,
        is_next : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> HistoryExportExcelRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> HistoryExportExcelRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"et",b"et",u"event",b"event",u"exclude_event",b"exclude_event",u"instanceId",b"instanceId",u"is_next",b"is_next",u"object_id",b"object_id",u"operator",b"operator",u"parent_event_id",b"parent_event_id",u"range",b"range",u"st",b"st",u"with_children",b"with_children"]) -> None: ...