# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
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


class CapacityTask(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    instanceId = ... # type: typing___Text
    name = ... # type: typing___Text
    hosts = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    suspectedIdleHosts = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    idleHosts = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    nonIdleHosts = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    status = ... # type: typing___Text
    endTime = ... # type: typing___Text
    hitRate = ... # type: builtin___float
    ctime = ... # type: typing___Text
    creator = ... # type: typing___Text
    execId = ... # type: typing___Text
    normalHosts = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    abnormalHosts = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        hosts : typing___Optional[typing___Iterable[typing___Text]] = None,
        suspectedIdleHosts : typing___Optional[typing___Iterable[typing___Text]] = None,
        idleHosts : typing___Optional[typing___Iterable[typing___Text]] = None,
        nonIdleHosts : typing___Optional[typing___Iterable[typing___Text]] = None,
        status : typing___Optional[typing___Text] = None,
        endTime : typing___Optional[typing___Text] = None,
        hitRate : typing___Optional[builtin___float] = None,
        ctime : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        execId : typing___Optional[typing___Text] = None,
        normalHosts : typing___Optional[typing___Iterable[typing___Text]] = None,
        abnormalHosts : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CapacityTask: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CapacityTask: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"abnormalHosts",b"abnormalHosts",u"creator",b"creator",u"ctime",b"ctime",u"endTime",b"endTime",u"execId",b"execId",u"hitRate",b"hitRate",u"hosts",b"hosts",u"idleHosts",b"idleHosts",u"instanceId",b"instanceId",u"name",b"name",u"nonIdleHosts",b"nonIdleHosts",u"normalHosts",b"normalHosts",u"status",b"status",u"suspectedIdleHosts",b"suspectedIdleHosts"]) -> None: ...
