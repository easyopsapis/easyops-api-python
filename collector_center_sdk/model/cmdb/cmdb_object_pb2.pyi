# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from collector_center_sdk.model.cmdb.object_attr_pb2 import (
    ObjectAttr as collector_center_sdk___model___cmdb___object_attr_pb2___ObjectAttr,
)

from collector_center_sdk.model.cmdb.object_index_pb2 import (
    ObjectIndex as collector_center_sdk___model___cmdb___object_index_pb2___ObjectIndex,
)

from collector_center_sdk.model.cmdb.object_relation_group_pb2 import (
    ObjectRelationGroup as collector_center_sdk___model___cmdb___object_relation_group_pb2___ObjectRelationGroup,
)

from collector_center_sdk.model.cmdb.object_relation_pb2 import (
    ObjectRelation as collector_center_sdk___model___cmdb___object_relation_pb2___ObjectRelation,
)

from collector_center_sdk.model.cmdb.object_view_pb2 import (
    ObjectView as collector_center_sdk___model___cmdb___object_view_pb2___ObjectView,
)

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


class CmdbObject(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text
    objectId = ... # type: typing___Text
    memo = ... # type: typing___Text
    protected = ... # type: builtin___bool
    wordIndexDenied = ... # type: builtin___bool
    category = ... # type: typing___Text
    icon = ... # type: typing___Text
    system = ... # type: typing___Text
    ctime = ... # type: typing___Text
    mtime = ... # type: typing___Text
    creator = ... # type: typing___Text
    modifier = ... # type: typing___Text
    _ts = ... # type: builtin___int
    _version = ... # type: builtin___int
    updateAuthorizers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    deleteAuthorizers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    isAbstract = ... # type: builtin___bool
    parentObjectId = ... # type: typing___Text
    permissionDenied = ... # type: builtin___bool

    @property
    def attrList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[collector_center_sdk___model___cmdb___object_attr_pb2___ObjectAttr]: ...

    @property
    def relation_list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[collector_center_sdk___model___cmdb___object_relation_pb2___ObjectRelation]: ...

    @property
    def relation_groups(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[collector_center_sdk___model___cmdb___object_relation_group_pb2___ObjectRelationGroup]: ...

    @property
    def indexList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[collector_center_sdk___model___cmdb___object_index_pb2___ObjectIndex]: ...

    @property
    def view(self) -> collector_center_sdk___model___cmdb___object_view_pb2___ObjectView: ...

    def __init__(self,
        *,
        attrList : typing___Optional[typing___Iterable[collector_center_sdk___model___cmdb___object_attr_pb2___ObjectAttr]] = None,
        relation_list : typing___Optional[typing___Iterable[collector_center_sdk___model___cmdb___object_relation_pb2___ObjectRelation]] = None,
        relation_groups : typing___Optional[typing___Iterable[collector_center_sdk___model___cmdb___object_relation_group_pb2___ObjectRelationGroup]] = None,
        indexList : typing___Optional[typing___Iterable[collector_center_sdk___model___cmdb___object_index_pb2___ObjectIndex]] = None,
        name : typing___Optional[typing___Text] = None,
        objectId : typing___Optional[typing___Text] = None,
        memo : typing___Optional[typing___Text] = None,
        view : typing___Optional[collector_center_sdk___model___cmdb___object_view_pb2___ObjectView] = None,
        protected : typing___Optional[builtin___bool] = None,
        wordIndexDenied : typing___Optional[builtin___bool] = None,
        category : typing___Optional[typing___Text] = None,
        icon : typing___Optional[typing___Text] = None,
        system : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[typing___Text] = None,
        mtime : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        modifier : typing___Optional[typing___Text] = None,
        _ts : typing___Optional[builtin___int] = None,
        _version : typing___Optional[builtin___int] = None,
        updateAuthorizers : typing___Optional[typing___Iterable[typing___Text]] = None,
        deleteAuthorizers : typing___Optional[typing___Iterable[typing___Text]] = None,
        isAbstract : typing___Optional[builtin___bool] = None,
        parentObjectId : typing___Optional[typing___Text] = None,
        permissionDenied : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CmdbObject: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CmdbObject: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"view",b"view"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"_ts",b"_ts",u"_version",b"_version",u"attrList",b"attrList",u"category",b"category",u"creator",b"creator",u"ctime",b"ctime",u"deleteAuthorizers",b"deleteAuthorizers",u"icon",b"icon",u"indexList",b"indexList",u"isAbstract",b"isAbstract",u"memo",b"memo",u"modifier",b"modifier",u"mtime",b"mtime",u"name",b"name",u"objectId",b"objectId",u"parentObjectId",b"parentObjectId",u"permissionDenied",b"permissionDenied",u"protected",b"protected",u"relation_groups",b"relation_groups",u"relation_list",b"relation_list",u"system",b"system",u"updateAuthorizers",b"updateAuthorizers",u"view",b"view",u"wordIndexDenied",b"wordIndexDenied"]) -> None: ...
