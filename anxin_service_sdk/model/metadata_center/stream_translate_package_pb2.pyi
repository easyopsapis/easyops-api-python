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


class StreamTranslatePackage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class MatchData(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class Resource(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            objectId = ... # type: typing___Text
            instances = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

            def __init__(self,
                *,
                objectId : typing___Optional[typing___Text] = None,
                instances : typing___Optional[typing___Iterable[typing___Text]] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> StreamTranslatePackage.MatchData.Resource: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StreamTranslatePackage.MatchData.Resource: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"instances",b"instances",u"objectId",b"objectId"]) -> None: ...

        class Tags(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            key = ... # type: typing___Text
            value = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

            def __init__(self,
                *,
                key : typing___Optional[typing___Text] = None,
                value : typing___Optional[typing___Iterable[typing___Text]] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> StreamTranslatePackage.MatchData.Tags: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StreamTranslatePackage.MatchData.Tags: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

        matchKey = ... # type: typing___Text

        @property
        def resource(self) -> StreamTranslatePackage.MatchData.Resource: ...

        @property
        def tags(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[StreamTranslatePackage.MatchData.Tags]: ...

        def __init__(self,
            *,
            matchKey : typing___Optional[typing___Text] = None,
            resource : typing___Optional[StreamTranslatePackage.MatchData.Resource] = None,
            tags : typing___Optional[typing___Iterable[StreamTranslatePackage.MatchData.Tags]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> StreamTranslatePackage.MatchData: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StreamTranslatePackage.MatchData: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"resource",b"resource"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"matchKey",b"matchKey",u"resource",b"resource",u"tags",b"tags"]) -> None: ...

    id = ... # type: typing___Text
    org = ... # type: builtin___int
    version = ... # type: builtin___int
    schemas = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    matchFields = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    @property
    def matchData(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[StreamTranslatePackage.MatchData]: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        org : typing___Optional[builtin___int] = None,
        version : typing___Optional[builtin___int] = None,
        schemas : typing___Optional[typing___Iterable[typing___Text]] = None,
        matchFields : typing___Optional[typing___Iterable[typing___Text]] = None,
        matchData : typing___Optional[typing___Iterable[StreamTranslatePackage.MatchData]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> StreamTranslatePackage: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StreamTranslatePackage: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"matchData",b"matchData",u"matchFields",b"matchFields",u"org",b"org",u"schemas",b"schemas",u"version",b"version"]) -> None: ...
