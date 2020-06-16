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

from monitor_sdk.model.next_builder.micro_app_project_pb2 import (
    MicroAppProject as monitor_sdk___model___next_builder___micro_app_project_pb2___MicroAppProject,
)

from monitor_sdk.model.next_builder.storyboard_brick_pb2 import (
    StoryboardBrick as monitor_sdk___model___next_builder___storyboard_brick_pb2___StoryboardBrick,
)

from monitor_sdk.model.next_builder.storyboard_route_pb2 import (
    StoryboardRoute as monitor_sdk___model___next_builder___storyboard_route_pb2___StoryboardRoute,
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


class StoryboardNode(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    instanceId = ... # type: typing___Text
    alias = ... # type: typing___Text
    appId = ... # type: typing___Text
    id = ... # type: typing___Text
    mountPoint = ... # type: typing___Text
    sort = ... # type: builtin___int
    type = ... # type: typing___Text

    @property
    def brick(self) -> monitor_sdk___model___next_builder___storyboard_brick_pb2___StoryboardBrick: ...

    @property
    def route(self) -> monitor_sdk___model___next_builder___storyboard_route_pb2___StoryboardRoute: ...

    @property
    def project(self) -> monitor_sdk___model___next_builder___micro_app_project_pb2___MicroAppProject: ...

    @property
    def parent(self) -> StoryboardNode: ...

    @property
    def children(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[StoryboardNode]: ...

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        alias : typing___Optional[typing___Text] = None,
        appId : typing___Optional[typing___Text] = None,
        id : typing___Optional[typing___Text] = None,
        mountPoint : typing___Optional[typing___Text] = None,
        sort : typing___Optional[builtin___int] = None,
        type : typing___Optional[typing___Text] = None,
        brick : typing___Optional[monitor_sdk___model___next_builder___storyboard_brick_pb2___StoryboardBrick] = None,
        route : typing___Optional[monitor_sdk___model___next_builder___storyboard_route_pb2___StoryboardRoute] = None,
        project : typing___Optional[monitor_sdk___model___next_builder___micro_app_project_pb2___MicroAppProject] = None,
        parent : typing___Optional[StoryboardNode] = None,
        children : typing___Optional[typing___Iterable[StoryboardNode]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> StoryboardNode: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StoryboardNode: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"brick",b"brick",u"parent",b"parent",u"project",b"project",u"route",b"route"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"alias",b"alias",u"appId",b"appId",u"brick",b"brick",u"children",b"children",u"id",b"id",u"instanceId",b"instanceId",u"mountPoint",b"mountPoint",u"parent",b"parent",u"project",b"project",u"route",b"route",u"sort",b"sort",u"type",b"type"]) -> None: ...
