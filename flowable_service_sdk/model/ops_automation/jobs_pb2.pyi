# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from flowable_service_sdk.model.ops_automation.bind_resource_pb2 import (
    BindResource as flowable_service_sdk___model___ops_automation___bind_resource_pb2___BindResource,
)

from flowable_service_sdk.model.ops_automation.mail_info_pb2 import (
    MailInfo as flowable_service_sdk___model___ops_automation___mail_info_pb2___MailInfo,
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


class Jobs(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text
    category = ... # type: typing___Text
    menuId = ... # type: typing___Text
    desc = ... # type: typing___Text
    allowModify = ... # type: builtin___bool
    id = ... # type: typing___Text

    @property
    def bindResource(self) -> flowable_service_sdk___model___ops_automation___bind_resource_pb2___BindResource: ...

    @property
    def mail(self) -> flowable_service_sdk___model___ops_automation___mail_info_pb2___MailInfo: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        category : typing___Optional[typing___Text] = None,
        menuId : typing___Optional[typing___Text] = None,
        bindResource : typing___Optional[flowable_service_sdk___model___ops_automation___bind_resource_pb2___BindResource] = None,
        desc : typing___Optional[typing___Text] = None,
        allowModify : typing___Optional[builtin___bool] = None,
        mail : typing___Optional[flowable_service_sdk___model___ops_automation___mail_info_pb2___MailInfo] = None,
        id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Jobs: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Jobs: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"bindResource",b"bindResource",u"mail",b"mail"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"allowModify",b"allowModify",u"bindResource",b"bindResource",u"category",b"category",u"desc",b"desc",u"id",b"id",u"mail",b"mail",u"menuId",b"menuId",u"name",b"name"]) -> None: ...
