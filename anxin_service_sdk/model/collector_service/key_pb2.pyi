# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
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


class CollectorKey(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class TagDefine(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        name = ... # type: typing___Text
        default = ... # type: typing___Text
        readOnly = ... # type: builtin___bool

        def __init__(self,
            *,
            name : typing___Optional[typing___Text] = None,
            default : typing___Optional[typing___Text] = None,
            readOnly : typing___Optional[builtin___bool] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> CollectorKey.TagDefine: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CollectorKey.TagDefine: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"default",b"default",u"name",b"name",u"readOnly",b"readOnly"]) -> None: ...

    class ParamDefine(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        name = ... # type: typing___Text
        valueType = ... # type: typing___Text
        default = ... # type: typing___Text
        readOnly = ... # type: builtin___bool

        def __init__(self,
            *,
            name : typing___Optional[typing___Text] = None,
            valueType : typing___Optional[typing___Text] = None,
            default : typing___Optional[typing___Text] = None,
            readOnly : typing___Optional[builtin___bool] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> CollectorKey.ParamDefine: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CollectorKey.ParamDefine: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"default",b"default",u"name",b"name",u"readOnly",b"readOnly",u"valueType",b"valueType"]) -> None: ...

    name = ... # type: typing___Text
    keyName = ... # type: typing___Text
    labels = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    keyId = ... # type: typing___Text
    version = ... # type: builtin___int
    key = ... # type: typing___Text
    metricType = ... # type: typing___Text
    dataType = ... # type: typing___Text
    agentType = ... # type: typing___Text
    help = ... # type: typing___Text
    unit = ... # type: typing___Text
    metricVersion = ... # type: builtin___int

    @property
    def tagDefine(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CollectorKey.TagDefine]: ...

    @property
    def paramDefine(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CollectorKey.ParamDefine]: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        keyName : typing___Optional[typing___Text] = None,
        labels : typing___Optional[typing___Iterable[typing___Text]] = None,
        keyId : typing___Optional[typing___Text] = None,
        version : typing___Optional[builtin___int] = None,
        key : typing___Optional[typing___Text] = None,
        metricType : typing___Optional[typing___Text] = None,
        dataType : typing___Optional[typing___Text] = None,
        agentType : typing___Optional[typing___Text] = None,
        tagDefine : typing___Optional[typing___Iterable[CollectorKey.TagDefine]] = None,
        paramDefine : typing___Optional[typing___Iterable[CollectorKey.ParamDefine]] = None,
        help : typing___Optional[typing___Text] = None,
        unit : typing___Optional[typing___Text] = None,
        metricVersion : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CollectorKey: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CollectorKey: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"agentType",b"agentType",u"dataType",b"dataType",u"help",b"help",u"key",b"key",u"keyId",b"keyId",u"keyName",b"keyName",u"labels",b"labels",u"metricType",b"metricType",u"metricVersion",b"metricVersion",u"name",b"name",u"paramDefine",b"paramDefine",u"tagDefine",b"tagDefine",u"unit",b"unit",u"version",b"version"]) -> None: ...