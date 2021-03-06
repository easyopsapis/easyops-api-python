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

from staff_manage_sdk.model.topology.area_pb2 import (
    Area as staff_manage_sdk___model___topology___area_pb2___Area,
)

from staff_manage_sdk.model.topology.link_pb2 import (
    Link as staff_manage_sdk___model___topology___link_pb2___Link,
)

from staff_manage_sdk.model.topology.node_pb2 import (
    Node as staff_manage_sdk___model___topology___node_pb2___Node,
)

from staff_manage_sdk.model.topology.note_pb2 import (
    Note as staff_manage_sdk___model___topology___note_pb2___Note,
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


class View(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Diff(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def addNodes(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[staff_manage_sdk___model___topology___node_pb2___Node]: ...

        @property
        def removeNodes(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[staff_manage_sdk___model___topology___node_pb2___Node]: ...

        @property
        def addLinks(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[staff_manage_sdk___model___topology___link_pb2___Link]: ...

        @property
        def removeLinks(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[staff_manage_sdk___model___topology___link_pb2___Link]: ...

        def __init__(self,
            *,
            addNodes : typing___Optional[typing___Iterable[staff_manage_sdk___model___topology___node_pb2___Node]] = None,
            removeNodes : typing___Optional[typing___Iterable[staff_manage_sdk___model___topology___node_pb2___Node]] = None,
            addLinks : typing___Optional[typing___Iterable[staff_manage_sdk___model___topology___link_pb2___Link]] = None,
            removeLinks : typing___Optional[typing___Iterable[staff_manage_sdk___model___topology___link_pb2___Link]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> View.Diff: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> View.Diff: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"addLinks",b"addLinks",u"addNodes",b"addNodes",u"removeLinks",b"removeLinks",u"removeNodes",b"removeNodes"]) -> None: ...

    id = ... # type: typing___Text
    name = ... # type: typing___Text
    creator = ... # type: typing___Text
    modifier = ... # type: typing___Text
    readAuthorizers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    writeAuthorizers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    version = ... # type: typing___Text
    ctime = ... # type: builtin___int
    mtime = ... # type: builtin___int

    @property
    def rootNode(self) -> staff_manage_sdk___model___topology___node_pb2___Node: ...

    @property
    def nodes(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[staff_manage_sdk___model___topology___node_pb2___Node]: ...

    @property
    def links(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[staff_manage_sdk___model___topology___link_pb2___Link]: ...

    @property
    def areas(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[staff_manage_sdk___model___topology___area_pb2___Area]: ...

    @property
    def notes(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[staff_manage_sdk___model___topology___note_pb2___Note]: ...

    @property
    def diff(self) -> View.Diff: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        modifier : typing___Optional[typing___Text] = None,
        readAuthorizers : typing___Optional[typing___Iterable[typing___Text]] = None,
        writeAuthorizers : typing___Optional[typing___Iterable[typing___Text]] = None,
        version : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[builtin___int] = None,
        mtime : typing___Optional[builtin___int] = None,
        rootNode : typing___Optional[staff_manage_sdk___model___topology___node_pb2___Node] = None,
        nodes : typing___Optional[typing___Iterable[staff_manage_sdk___model___topology___node_pb2___Node]] = None,
        links : typing___Optional[typing___Iterable[staff_manage_sdk___model___topology___link_pb2___Link]] = None,
        areas : typing___Optional[typing___Iterable[staff_manage_sdk___model___topology___area_pb2___Area]] = None,
        notes : typing___Optional[typing___Iterable[staff_manage_sdk___model___topology___note_pb2___Note]] = None,
        diff : typing___Optional[View.Diff] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> View: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> View: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"diff",b"diff",u"rootNode",b"rootNode"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"areas",b"areas",u"creator",b"creator",u"ctime",b"ctime",u"diff",b"diff",u"id",b"id",u"links",b"links",u"modifier",b"modifier",u"mtime",b"mtime",u"name",b"name",u"nodes",b"nodes",u"notes",b"notes",u"readAuthorizers",b"readAuthorizers",u"rootNode",b"rootNode",u"version",b"version",u"writeAuthorizers",b"writeAuthorizers"]) -> None: ...
