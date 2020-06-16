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

from webshell_sdk.model.topboard.issue_pb2 import (
    Issue as webshell_sdk___model___topboard___issue_pb2___Issue,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class RequirementInstance(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    instanceId = ... # type: typing___Text
    name = ... # type: typing___Text
    sequence = ... # type: typing___Text
    given = ... # type: typing___Text
    when = ... # type: typing___Text
    then = ... # type: typing___Text
    type = ... # type: typing___Text
    dataDescription = ... # type: typing___Text
    data = ... # type: typing___Text
    tag = ... # type: typing___Text
    interfaceName = ... # type: typing___Text

    @property
    def contracts(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___struct_pb2___Struct]: ...

    @property
    def ISSUE(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[webshell_sdk___model___topboard___issue_pb2___Issue]: ...

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        sequence : typing___Optional[typing___Text] = None,
        given : typing___Optional[typing___Text] = None,
        when : typing___Optional[typing___Text] = None,
        then : typing___Optional[typing___Text] = None,
        type : typing___Optional[typing___Text] = None,
        dataDescription : typing___Optional[typing___Text] = None,
        data : typing___Optional[typing___Text] = None,
        tag : typing___Optional[typing___Text] = None,
        interfaceName : typing___Optional[typing___Text] = None,
        contracts : typing___Optional[typing___Iterable[google___protobuf___struct_pb2___Struct]] = None,
        ISSUE : typing___Optional[typing___Iterable[webshell_sdk___model___topboard___issue_pb2___Issue]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> RequirementInstance: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> RequirementInstance: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"ISSUE",b"ISSUE",u"contracts",b"contracts",u"data",b"data",u"dataDescription",b"dataDescription",u"given",b"given",u"instanceId",b"instanceId",u"interfaceName",b"interfaceName",u"name",b"name",u"sequence",b"sequence",u"tag",b"tag",u"then",b"then",u"type",b"type",u"when",b"when"]) -> None: ...
