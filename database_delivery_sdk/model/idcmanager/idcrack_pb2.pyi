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


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class IDCRack(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Layout(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        instanceId = ... # type: typing___Text
        type = ... # type: typing___Text
        startU = ... # type: builtin___int
        occupiedU = ... # type: builtin___int

        def __init__(self,
            *,
            instanceId : typing___Optional[typing___Text] = None,
            type : typing___Optional[typing___Text] = None,
            startU : typing___Optional[builtin___int] = None,
            occupiedU : typing___Optional[builtin___int] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> IDCRack.Layout: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> IDCRack.Layout: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"instanceId",b"instanceId",u"occupiedU",b"occupiedU",u"startU",b"startU",u"type",b"type"]) -> None: ...

    instanceId = ... # type: typing___Text
    name = ... # type: typing___Text
    code = ... # type: typing___Text
    status = ... # type: typing___Text
    type = ... # type: typing___Text
    unum = ... # type: builtin___int
    freeUnum = ... # type: builtin___int
    memo = ... # type: typing___Text
    ctime = ... # type: typing___Text
    creator = ... # type: typing___Text

    @property
    def layout(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[IDCRack.Layout]: ...

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        code : typing___Optional[typing___Text] = None,
        status : typing___Optional[typing___Text] = None,
        type : typing___Optional[typing___Text] = None,
        unum : typing___Optional[builtin___int] = None,
        freeUnum : typing___Optional[builtin___int] = None,
        memo : typing___Optional[typing___Text] = None,
        layout : typing___Optional[typing___Iterable[IDCRack.Layout]] = None,
        ctime : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> IDCRack: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> IDCRack: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"creator",b"creator",u"ctime",b"ctime",u"freeUnum",b"freeUnum",u"instanceId",b"instanceId",u"layout",b"layout",u"memo",b"memo",u"name",b"name",u"status",b"status",u"type",b"type",u"unum",b"unum"]) -> None: ...
