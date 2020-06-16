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


class Switch(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    instanceId = ... # type: typing___Text
    name = ... # type: typing___Text
    ip = ... # type: typing___Text
    status = ... # type: typing___Text
    type = ... # type: typing___Text
    _startU = ... # type: builtin___int
    _occupiedU = ... # type: builtin___int
    memo = ... # type: typing___Text
    propertyid = ... # type: typing___Text
    ctime = ... # type: typing___Text
    creator = ... # type: typing___Text
    product = ... # type: typing___Text
    customer = ... # type: typing___Text
    isSinglePower = ... # type: builtin___bool

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        ip : typing___Optional[typing___Text] = None,
        status : typing___Optional[typing___Text] = None,
        type : typing___Optional[typing___Text] = None,
        _startU : typing___Optional[builtin___int] = None,
        _occupiedU : typing___Optional[builtin___int] = None,
        memo : typing___Optional[typing___Text] = None,
        propertyid : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        product : typing___Optional[typing___Text] = None,
        customer : typing___Optional[typing___Text] = None,
        isSinglePower : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Switch: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Switch: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"_occupiedU",b"_occupiedU",u"_startU",b"_startU",u"creator",b"creator",u"ctime",b"ctime",u"customer",b"customer",u"instanceId",b"instanceId",u"ip",b"ip",u"isSinglePower",b"isSinglePower",u"memo",b"memo",u"name",b"name",u"product",b"product",u"propertyid",b"propertyid",u"status",b"status",u"type",b"type"]) -> None: ...
