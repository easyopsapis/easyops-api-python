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


class GetAppDependenciesRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    appId = ... # type: typing___Text

    def __init__(self,
        *,
        appId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetAppDependenciesRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetAppDependenciesRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"appId",b"appId"]) -> None: ...

class GetAppDependenciesResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Dependencies(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        packageName = ... # type: typing___Text
        constraint = ... # type: typing___Text
        currentVersion = ... # type: typing___Text
        meetConstraint = ... # type: builtin___bool

        def __init__(self,
            *,
            packageName : typing___Optional[typing___Text] = None,
            constraint : typing___Optional[typing___Text] = None,
            currentVersion : typing___Optional[typing___Text] = None,
            meetConstraint : typing___Optional[builtin___bool] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> GetAppDependenciesResponse.Dependencies: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetAppDependenciesResponse.Dependencies: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"constraint",b"constraint",u"currentVersion",b"currentVersion",u"meetConstraint",b"meetConstraint",u"packageName",b"packageName"]) -> None: ...


    @property
    def dependencies(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[GetAppDependenciesResponse.Dependencies]: ...

    def __init__(self,
        *,
        dependencies : typing___Optional[typing___Iterable[GetAppDependenciesResponse.Dependencies]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetAppDependenciesResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetAppDependenciesResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"dependencies",b"dependencies"]) -> None: ...

class GetAppDependenciesResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> GetAppDependenciesResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[GetAppDependenciesResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetAppDependenciesResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetAppDependenciesResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...