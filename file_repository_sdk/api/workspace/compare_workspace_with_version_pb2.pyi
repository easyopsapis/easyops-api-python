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


class CompareWorkspaceWithVersionRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    packageId = ... # type: typing___Text
    versionId = ... # type: typing___Text

    def __init__(self,
        *,
        packageId : typing___Optional[typing___Text] = None,
        versionId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CompareWorkspaceWithVersionRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CompareWorkspaceWithVersionRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"packageId",b"packageId",u"versionId",b"versionId"]) -> None: ...

class CompareWorkspaceWithVersionResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Detail(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        op = ... # type: typing___Text
        file = ... # type: typing___Text
        type = ... # type: typing___Text
        perm = ... # type: typing___Text
        newMd5 = ... # type: typing___Text
        oldMd5 = ... # type: typing___Text
        oldSize = ... # type: builtin___int
        newSize = ... # type: builtin___int
        encoding = ... # type: typing___Text

        def __init__(self,
            *,
            op : typing___Optional[typing___Text] = None,
            file : typing___Optional[typing___Text] = None,
            type : typing___Optional[typing___Text] = None,
            perm : typing___Optional[typing___Text] = None,
            newMd5 : typing___Optional[typing___Text] = None,
            oldMd5 : typing___Optional[typing___Text] = None,
            oldSize : typing___Optional[builtin___int] = None,
            newSize : typing___Optional[builtin___int] = None,
            encoding : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> CompareWorkspaceWithVersionResponse.Detail: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CompareWorkspaceWithVersionResponse.Detail: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"encoding",b"encoding",u"file",b"file",u"newMd5",b"newMd5",u"newSize",b"newSize",u"oldMd5",b"oldMd5",u"oldSize",b"oldSize",u"op",b"op",u"perm",b"perm",u"type",b"type"]) -> None: ...

    fromVersion = ... # type: typing___Text
    toVersion = ... # type: typing___Text

    @property
    def detail(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CompareWorkspaceWithVersionResponse.Detail]: ...

    def __init__(self,
        *,
        fromVersion : typing___Optional[typing___Text] = None,
        toVersion : typing___Optional[typing___Text] = None,
        detail : typing___Optional[typing___Iterable[CompareWorkspaceWithVersionResponse.Detail]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CompareWorkspaceWithVersionResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CompareWorkspaceWithVersionResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"detail",b"detail",u"fromVersion",b"fromVersion",u"toVersion",b"toVersion"]) -> None: ...

class CompareWorkspaceWithVersionResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> CompareWorkspaceWithVersionResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[CompareWorkspaceWithVersionResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CompareWorkspaceWithVersionResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CompareWorkspaceWithVersionResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
