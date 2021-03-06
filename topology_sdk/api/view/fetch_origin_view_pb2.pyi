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

from topology_sdk.model.topology.hideLink_pb2 import (
    HideLink as topology_sdk___model___topology___hideLink_pb2___HideLink,
)

from topology_sdk.model.topology.relation_pb2 import (
    Relation as topology_sdk___model___topology___relation_pb2___Relation,
)

from topology_sdk.model.topology.view_pb2 import (
    View as topology_sdk___model___topology___view_pb2___View,
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


class FetchOriginViewRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    objectId = ... # type: typing___Text
    instanceId = ... # type: typing___Text
    dataSource = ... # type: typing___Text

    @property
    def relations(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[topology_sdk___model___topology___relation_pb2___Relation]: ...

    @property
    def hideLinks(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[topology_sdk___model___topology___hideLink_pb2___HideLink]: ...

    def __init__(self,
        *,
        objectId : typing___Optional[typing___Text] = None,
        instanceId : typing___Optional[typing___Text] = None,
        relations : typing___Optional[typing___Iterable[topology_sdk___model___topology___relation_pb2___Relation]] = None,
        dataSource : typing___Optional[typing___Text] = None,
        hideLinks : typing___Optional[typing___Iterable[topology_sdk___model___topology___hideLink_pb2___HideLink]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FetchOriginViewRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FetchOriginViewRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"dataSource",b"dataSource",u"hideLinks",b"hideLinks",u"instanceId",b"instanceId",u"objectId",b"objectId",u"relations",b"relations"]) -> None: ...

class FetchOriginViewResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> topology_sdk___model___topology___view_pb2___View: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[topology_sdk___model___topology___view_pb2___View] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FetchOriginViewResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FetchOriginViewResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
