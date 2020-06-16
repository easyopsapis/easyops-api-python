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


class Version(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text
    versionId = ... # type: typing___Text
    packageId = ... # type: typing___Text
    org = ... # type: builtin___int
    baseImageId = ... # type: typing___Text
    baseVersionName = ... # type: typing___Text
    creator = ... # type: typing___Text
    env_type = ... # type: builtin___int
    memo = ... # type: typing___Text
    ctime = ... # type: typing___Text
    mtime = ... # type: typing___Text
    sign = ... # type: typing___Text
    repoVersion = ... # type: typing___Text
    source = ... # type: typing___Text
    sourceType = ... # type: typing___Text
    workspaceBaseId = ... # type: typing___Text
    conf = ... # type: typing___Text

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        versionId : typing___Optional[typing___Text] = None,
        packageId : typing___Optional[typing___Text] = None,
        org : typing___Optional[builtin___int] = None,
        baseImageId : typing___Optional[typing___Text] = None,
        baseVersionName : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        env_type : typing___Optional[builtin___int] = None,
        memo : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[typing___Text] = None,
        mtime : typing___Optional[typing___Text] = None,
        sign : typing___Optional[typing___Text] = None,
        repoVersion : typing___Optional[typing___Text] = None,
        source : typing___Optional[typing___Text] = None,
        sourceType : typing___Optional[typing___Text] = None,
        workspaceBaseId : typing___Optional[typing___Text] = None,
        conf : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Version: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Version: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"baseImageId",b"baseImageId",u"baseVersionName",b"baseVersionName",u"conf",b"conf",u"creator",b"creator",u"ctime",b"ctime",u"env_type",b"env_type",u"memo",b"memo",u"mtime",b"mtime",u"name",b"name",u"org",b"org",u"packageId",b"packageId",u"repoVersion",b"repoVersion",u"sign",b"sign",u"source",b"source",u"sourceType",b"sourceType",u"versionId",b"versionId",u"workspaceBaseId",b"workspaceBaseId"]) -> None: ...