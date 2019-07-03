# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
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
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class InstalledMicroApp(google___protobuf___message___Message):
    class Icons(google___protobuf___message___Message):
        large = ... # type: typing___Text

        def __init__(self,
            large : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> InstalledMicroApp.Icons: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"large"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"large"]) -> None: ...

    name = ... # type: typing___Text
    appId = ... # type: typing___Text
    storyboard = ... # type: typing___Text
    tags = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    currentVersion = ... # type: typing___Text
    installStatus = ... # type: typing___Text

    @property
    def icons(self) -> InstalledMicroApp.Icons: ...

    def __init__(self,
        name : typing___Optional[typing___Text] = None,
        appId : typing___Optional[typing___Text] = None,
        icons : typing___Optional[InstalledMicroApp.Icons] = None,
        storyboard : typing___Optional[typing___Text] = None,
        tags : typing___Optional[typing___Iterable[typing___Text]] = None,
        currentVersion : typing___Optional[typing___Text] = None,
        installStatus : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> InstalledMicroApp: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"icons"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"appId",u"currentVersion",u"icons",u"installStatus",u"name",u"storyboard",u"tags"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"icons",b"icons"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"appId",b"currentVersion",b"icons",b"installStatus",b"name",b"storyboard",b"tags"]) -> None: ...