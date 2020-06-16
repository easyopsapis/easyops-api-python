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

from patch_manager_sdk.model.cmdb.object_attr_value_pb2 import (
    ObjectAttrValue as patch_manager_sdk___model___cmdb___object_attr_value_pb2___ObjectAttrValue,
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


class ObjectImport(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class AttrList(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        id = ... # type: typing___Text
        name = ... # type: typing___Text
        unique = ... # type: typing___Text
        readonly = ... # type: typing___Text
        required = ... # type: typing___Text
        tag = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
        description = ... # type: typing___Text
        tips = ... # type: typing___Text

        @property
        def value(self) -> patch_manager_sdk___model___cmdb___object_attr_value_pb2___ObjectAttrValue: ...

        def __init__(self,
            *,
            id : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            unique : typing___Optional[typing___Text] = None,
            readonly : typing___Optional[typing___Text] = None,
            required : typing___Optional[typing___Text] = None,
            tag : typing___Optional[typing___Iterable[typing___Text]] = None,
            description : typing___Optional[typing___Text] = None,
            tips : typing___Optional[typing___Text] = None,
            value : typing___Optional[patch_manager_sdk___model___cmdb___object_attr_value_pb2___ObjectAttrValue] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ObjectImport.AttrList: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ObjectImport.AttrList: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"description",b"description",u"id",b"id",u"name",b"name",u"readonly",b"readonly",u"required",b"required",u"tag",b"tag",u"tips",b"tips",u"unique",b"unique",u"value",b"value"]) -> None: ...

    class RelationGroups(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        id = ... # type: typing___Text
        name = ... # type: typing___Text

        def __init__(self,
            *,
            id : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ObjectImport.RelationGroups: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ObjectImport.RelationGroups: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"name",b"name"]) -> None: ...

    class RelationList(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        name = ... # type: typing___Text
        left_object_id = ... # type: typing___Text
        left_id = ... # type: typing___Text
        left_description = ... # type: typing___Text
        left_min = ... # type: builtin___int
        left_max = ... # type: builtin___int
        left_groups = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
        left_tags = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
        right_object_id = ... # type: typing___Text
        right_id = ... # type: typing___Text
        right_description = ... # type: typing___Text
        right_min = ... # type: builtin___int
        right_max = ... # type: builtin___int
        right_groups = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
        right_tags = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

        def __init__(self,
            *,
            name : typing___Optional[typing___Text] = None,
            left_object_id : typing___Optional[typing___Text] = None,
            left_id : typing___Optional[typing___Text] = None,
            left_description : typing___Optional[typing___Text] = None,
            left_min : typing___Optional[builtin___int] = None,
            left_max : typing___Optional[builtin___int] = None,
            left_groups : typing___Optional[typing___Iterable[typing___Text]] = None,
            left_tags : typing___Optional[typing___Iterable[typing___Text]] = None,
            right_object_id : typing___Optional[typing___Text] = None,
            right_id : typing___Optional[typing___Text] = None,
            right_description : typing___Optional[typing___Text] = None,
            right_min : typing___Optional[builtin___int] = None,
            right_max : typing___Optional[builtin___int] = None,
            right_groups : typing___Optional[typing___Iterable[typing___Text]] = None,
            right_tags : typing___Optional[typing___Iterable[typing___Text]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ObjectImport.RelationList: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ObjectImport.RelationList: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"left_description",b"left_description",u"left_groups",b"left_groups",u"left_id",b"left_id",u"left_max",b"left_max",u"left_min",b"left_min",u"left_object_id",b"left_object_id",u"left_tags",b"left_tags",u"name",b"name",u"right_description",b"right_description",u"right_groups",b"right_groups",u"right_id",b"right_id",u"right_max",b"right_max",u"right_min",b"right_min",u"right_object_id",b"right_object_id",u"right_tags",b"right_tags"]) -> None: ...

    objectId = ... # type: typing___Text
    name = ... # type: typing___Text
    icon = ... # type: typing___Text
    category = ... # type: typing___Text
    memo = ... # type: typing___Text

    @property
    def attrList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ObjectImport.AttrList]: ...

    @property
    def relation_groups(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ObjectImport.RelationGroups]: ...

    @property
    def relation_list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ObjectImport.RelationList]: ...

    def __init__(self,
        *,
        objectId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        icon : typing___Optional[typing___Text] = None,
        category : typing___Optional[typing___Text] = None,
        memo : typing___Optional[typing___Text] = None,
        attrList : typing___Optional[typing___Iterable[ObjectImport.AttrList]] = None,
        relation_groups : typing___Optional[typing___Iterable[ObjectImport.RelationGroups]] = None,
        relation_list : typing___Optional[typing___Iterable[ObjectImport.RelationList]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ObjectImport: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ObjectImport: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"attrList",b"attrList",u"category",b"category",u"icon",b"icon",u"memo",b"memo",u"name",b"name",u"objectId",b"objectId",u"relation_groups",b"relation_groups",u"relation_list",b"relation_list"]) -> None: ...
