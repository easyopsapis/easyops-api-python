# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
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
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class InspectionCollector(google___protobuf___message___Message):
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
        def FromString(cls, s: bytes) -> InspectionCollector.Args: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"alias",u"key",u"require",u"type"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"alias",b"key",b"require",b"type"]) -> None: ...

    id = ... # type: typing___Text
    name = ... # type: typing___Text
    content = ... # type: typing___Text
    script = ... # type: typing___Text

    @property
    def args(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[InspectionCollector.Args]: ...

    def __init__(self,
        id : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        content : typing___Optional[typing___Text] = None,
        script : typing___Optional[typing___Text] = None,
        args : typing___Optional[typing___Iterable[InspectionCollector.Args]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> InspectionCollector: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"args",u"content",u"id",u"name",u"script"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"args",b"content",b"id",b"name",b"script"]) -> None: ...