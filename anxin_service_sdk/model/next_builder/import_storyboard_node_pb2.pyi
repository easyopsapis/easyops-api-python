# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from anxin_service_sdk.model.next_builder.storyboard_brick_pb2 import (
    StoryboardBrick as anxin_service_sdk___model___next_builder___storyboard_brick_pb2___StoryboardBrick,
)

from anxin_service_sdk.model.next_builder.storyboard_route_pb2 import (
    StoryboardRoute as anxin_service_sdk___model___next_builder___storyboard_route_pb2___StoryboardRoute,
)

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


class ImportStoryboardNode(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Project(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        instanceId = ... # type: typing___Text

        def __init__(self,
            *,
            instanceId : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ImportStoryboardNode.Project: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ImportStoryboardNode.Project: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"instanceId",b"instanceId"]) -> None: ...

    class Parent(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        id = ... # type: typing___Text

        def __init__(self,
            *,
            id : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ImportStoryboardNode.Parent: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ImportStoryboardNode.Parent: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id"]) -> None: ...

    id = ... # type: typing___Text
    alias = ... # type: typing___Text
    appId = ... # type: typing___Text
    mountPoint = ... # type: typing___Text
    sort = ... # type: builtin___int
    type = ... # type: typing___Text

    @property
    def project(self) -> ImportStoryboardNode.Project: ...

    @property
    def parent(self) -> ImportStoryboardNode.Parent: ...

    @property
    def brick(self) -> anxin_service_sdk___model___next_builder___storyboard_brick_pb2___StoryboardBrick: ...

    @property
    def route(self) -> anxin_service_sdk___model___next_builder___storyboard_route_pb2___StoryboardRoute: ...

    def __init__(self,
        *,
        project : typing___Optional[ImportStoryboardNode.Project] = None,
        parent : typing___Optional[ImportStoryboardNode.Parent] = None,
        id : typing___Optional[typing___Text] = None,
        alias : typing___Optional[typing___Text] = None,
        appId : typing___Optional[typing___Text] = None,
        mountPoint : typing___Optional[typing___Text] = None,
        sort : typing___Optional[builtin___int] = None,
        type : typing___Optional[typing___Text] = None,
        brick : typing___Optional[anxin_service_sdk___model___next_builder___storyboard_brick_pb2___StoryboardBrick] = None,
        route : typing___Optional[anxin_service_sdk___model___next_builder___storyboard_route_pb2___StoryboardRoute] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ImportStoryboardNode: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ImportStoryboardNode: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"brick",b"brick",u"parent",b"parent",u"project",b"project",u"route",b"route"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"alias",b"alias",u"appId",b"appId",u"brick",b"brick",u"id",b"id",u"mountPoint",b"mountPoint",u"parent",b"parent",u"project",b"project",u"route",b"route",u"sort",b"sort",u"type",b"type"]) -> None: ...
