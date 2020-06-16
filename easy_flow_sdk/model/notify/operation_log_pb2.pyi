# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from easy_flow_sdk.model.notify.app_pb2 import (
    App as easy_flow_sdk___model___notify___app_pb2___App,
)

from easy_flow_sdk.model.notify.deploy_info_pb2 import (
    DeployInfo as easy_flow_sdk___model___notify___deploy_info_pb2___DeployInfo,
)

from easy_flow_sdk.model.notify.device_pb2 import (
    Device as easy_flow_sdk___model___notify___device_pb2___Device,
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

from google.protobuf.struct_pb2 import (
    Struct as google___protobuf___struct_pb2___Struct,
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


class OperationLog(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    system = ... # type: typing___Text
    topic = ... # type: typing___Text
    event_id = ... # type: typing___Text
    parent_event_id = ... # type: typing___Text
    event = ... # type: typing___Text
    status = ... # type: typing___Text
    operator = ... # type: typing___Text
    target_name = ... # type: typing___Text
    target_id = ... # type: typing___Text
    target_category = ... # type: typing___Text
    notifiers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    trigger = ... # type: typing___Text
    memo = ... # type: typing___Text
    app_id = ... # type: typing___Text
    cluster_id = ... # type: typing___Text
    package_id = ... # type: typing___Text
    package_name = ... # type: typing___Text
    version_id = ... # type: typing___Text
    version_name = ... # type: typing___Text
    content = ... # type: typing___Text
    data_name = ... # type: typing___Text
    ip = ... # type: typing___Text
    ip_list = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    subject = ... # type: typing___Text
    mtime = ... # type: builtin___int
    ctime = ... # type: builtin___int

    @property
    def parent_event(self) -> OperationLog: ...

    @property
    def device_list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[easy_flow_sdk___model___notify___device_pb2___Device]: ...

    @property
    def app_list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[easy_flow_sdk___model___notify___app_pb2___App]: ...

    @property
    def ext_info(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def deploy_info(self) -> easy_flow_sdk___model___notify___deploy_info_pb2___DeployInfo: ...

    def __init__(self,
        *,
        system : typing___Optional[typing___Text] = None,
        topic : typing___Optional[typing___Text] = None,
        event_id : typing___Optional[typing___Text] = None,
        parent_event_id : typing___Optional[typing___Text] = None,
        parent_event : typing___Optional[OperationLog] = None,
        event : typing___Optional[typing___Text] = None,
        status : typing___Optional[typing___Text] = None,
        device_list : typing___Optional[typing___Iterable[easy_flow_sdk___model___notify___device_pb2___Device]] = None,
        operator : typing___Optional[typing___Text] = None,
        target_name : typing___Optional[typing___Text] = None,
        target_id : typing___Optional[typing___Text] = None,
        target_category : typing___Optional[typing___Text] = None,
        app_list : typing___Optional[typing___Iterable[easy_flow_sdk___model___notify___app_pb2___App]] = None,
        ext_info : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        notifiers : typing___Optional[typing___Iterable[typing___Text]] = None,
        trigger : typing___Optional[typing___Text] = None,
        memo : typing___Optional[typing___Text] = None,
        app_id : typing___Optional[typing___Text] = None,
        cluster_id : typing___Optional[typing___Text] = None,
        package_id : typing___Optional[typing___Text] = None,
        package_name : typing___Optional[typing___Text] = None,
        version_id : typing___Optional[typing___Text] = None,
        version_name : typing___Optional[typing___Text] = None,
        deploy_info : typing___Optional[easy_flow_sdk___model___notify___deploy_info_pb2___DeployInfo] = None,
        content : typing___Optional[typing___Text] = None,
        data_name : typing___Optional[typing___Text] = None,
        ip : typing___Optional[typing___Text] = None,
        ip_list : typing___Optional[typing___Iterable[typing___Text]] = None,
        subject : typing___Optional[typing___Text] = None,
        mtime : typing___Optional[builtin___int] = None,
        ctime : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> OperationLog: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> OperationLog: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"deploy_info",b"deploy_info",u"ext_info",b"ext_info",u"parent_event",b"parent_event"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"app_id",b"app_id",u"app_list",b"app_list",u"cluster_id",b"cluster_id",u"content",b"content",u"ctime",b"ctime",u"data_name",b"data_name",u"deploy_info",b"deploy_info",u"device_list",b"device_list",u"event",b"event",u"event_id",b"event_id",u"ext_info",b"ext_info",u"ip",b"ip",u"ip_list",b"ip_list",u"memo",b"memo",u"mtime",b"mtime",u"notifiers",b"notifiers",u"operator",b"operator",u"package_id",b"package_id",u"package_name",b"package_name",u"parent_event",b"parent_event",u"parent_event_id",b"parent_event_id",u"status",b"status",u"subject",b"subject",u"system",b"system",u"target_category",b"target_category",u"target_id",b"target_id",u"target_name",b"target_name",u"topic",b"topic",u"trigger",b"trigger",u"version_id",b"version_id",u"version_name",b"version_name"]) -> None: ...
