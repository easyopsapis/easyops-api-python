# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from easy_command_sdk.model.console.cmdb_query_strategy_pb2 import (
    CmdbQueryStrategy as easy_command_sdk___model___console___cmdb_query_strategy_pb2___CmdbQueryStrategy,
)

from easy_command_sdk.model.resource_manage.filter_condition_group_pb2 import (
    FilterConditionGroup as easy_command_sdk___model___resource_manage___filter_condition_group_pb2___FilterConditionGroup,
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


class FilterStrategy(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    instanceId = ... # type: typing___Text
    strategyName = ... # type: typing___Text
    strategyObjectId = ... # type: typing___Text
    crontab = ... # type: typing___Text
    ctime = ... # type: typing___Text
    mtime = ... # type: typing___Text
    creator = ... # type: typing___Text
    modifier = ... # type: typing___Text
    nextExecTime = ... # type: typing___Text
    enable = ... # type: builtin___bool
    updateAuthorizers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    readAuthorizers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    deleteAuthorizers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    notifyUsers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    notifyMethods = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    org = ... # type: builtin___int

    @property
    def query(self) -> easy_command_sdk___model___console___cmdb_query_strategy_pb2___CmdbQueryStrategy: ...

    @property
    def filter(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[easy_command_sdk___model___resource_manage___filter_condition_group_pb2___FilterConditionGroup]: ...

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        strategyName : typing___Optional[typing___Text] = None,
        strategyObjectId : typing___Optional[typing___Text] = None,
        query : typing___Optional[easy_command_sdk___model___console___cmdb_query_strategy_pb2___CmdbQueryStrategy] = None,
        filter : typing___Optional[typing___Iterable[easy_command_sdk___model___resource_manage___filter_condition_group_pb2___FilterConditionGroup]] = None,
        crontab : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[typing___Text] = None,
        mtime : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        modifier : typing___Optional[typing___Text] = None,
        nextExecTime : typing___Optional[typing___Text] = None,
        enable : typing___Optional[builtin___bool] = None,
        updateAuthorizers : typing___Optional[typing___Iterable[typing___Text]] = None,
        readAuthorizers : typing___Optional[typing___Iterable[typing___Text]] = None,
        deleteAuthorizers : typing___Optional[typing___Iterable[typing___Text]] = None,
        notifyUsers : typing___Optional[typing___Iterable[typing___Text]] = None,
        notifyMethods : typing___Optional[typing___Iterable[typing___Text]] = None,
        org : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FilterStrategy: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FilterStrategy: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"query",b"query"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"creator",b"creator",u"crontab",b"crontab",u"ctime",b"ctime",u"deleteAuthorizers",b"deleteAuthorizers",u"enable",b"enable",u"filter",b"filter",u"instanceId",b"instanceId",u"modifier",b"modifier",u"mtime",b"mtime",u"nextExecTime",b"nextExecTime",u"notifyMethods",b"notifyMethods",u"notifyUsers",b"notifyUsers",u"org",b"org",u"query",b"query",u"readAuthorizers",b"readAuthorizers",u"strategyName",b"strategyName",u"strategyObjectId",b"strategyObjectId",u"updateAuthorizers",b"updateAuthorizers"]) -> None: ...
