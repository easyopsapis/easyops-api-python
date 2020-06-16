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

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)

from user_service_sdk.model.topboard.sprint_pb2 import (
    Sprint as user_service_sdk___model___topboard___sprint_pb2___Sprint,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class Product(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text
    instanceId = ... # type: typing___Text
    title = ... # type: typing___Text
    description = ... # type: typing___Text

    @property
    def sprints(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[user_service_sdk___model___topboard___sprint_pb2___Sprint]: ...

    def __init__(self,
        *,
        sprints : typing___Optional[typing___Iterable[user_service_sdk___model___topboard___sprint_pb2___Sprint]] = None,
        name : typing___Optional[typing___Text] = None,
        instanceId : typing___Optional[typing___Text] = None,
        title : typing___Optional[typing___Text] = None,
        description : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Product: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Product: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"description",b"description",u"instanceId",b"instanceId",u"name",b"name",u"sprints",b"sprints",u"title",b"title"]) -> None: ...
