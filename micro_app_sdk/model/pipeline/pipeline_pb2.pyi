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


class Pipeline(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Variables(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        name = ... # type: typing___Text
        value = ... # type: typing___Text

        def __init__(self,
            *,
            name : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Pipeline.Variables: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Pipeline.Variables: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name",u"value",b"value"]) -> None: ...

    class Notify(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        mode = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
        methods = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
        users = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
        user_groups = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

        def __init__(self,
            *,
            mode : typing___Optional[typing___Iterable[typing___Text]] = None,
            methods : typing___Optional[typing___Iterable[typing___Text]] = None,
            users : typing___Optional[typing___Iterable[typing___Text]] = None,
            user_groups : typing___Optional[typing___Iterable[typing___Text]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Pipeline.Notify: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Pipeline.Notify: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"methods",b"methods",u"mode",b"mode",u"user_groups",b"user_groups",u"users",b"users"]) -> None: ...

    id = ... # type: typing___Text
    alias_name = ... # type: typing___Text
    workflow_type = ... # type: typing___Text
    yaml_path = ... # type: typing___Text
    yaml_string = ... # type: typing___Text
    yaml_url = ... # type: typing___Text
    step_timeout = ... # type: builtin___int
    creator = ... # type: typing___Text
    ctime = ... # type: typing___Text
    mtime = ... # type: typing___Text

    @property
    def variables(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Pipeline.Variables]: ...

    @property
    def notify(self) -> Pipeline.Notify: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        alias_name : typing___Optional[typing___Text] = None,
        workflow_type : typing___Optional[typing___Text] = None,
        yaml_path : typing___Optional[typing___Text] = None,
        yaml_string : typing___Optional[typing___Text] = None,
        yaml_url : typing___Optional[typing___Text] = None,
        step_timeout : typing___Optional[builtin___int] = None,
        variables : typing___Optional[typing___Iterable[Pipeline.Variables]] = None,
        notify : typing___Optional[Pipeline.Notify] = None,
        creator : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[typing___Text] = None,
        mtime : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Pipeline: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Pipeline: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"notify",b"notify"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"alias_name",b"alias_name",u"creator",b"creator",u"ctime",b"ctime",u"id",b"id",u"mtime",b"mtime",u"notify",b"notify",u"step_timeout",b"step_timeout",u"variables",b"variables",u"workflow_type",b"workflow_type",u"yaml_path",b"yaml_path",u"yaml_string",b"yaml_string",u"yaml_url",b"yaml_url"]) -> None: ...
