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

from pipeline_sdk.model.container.key_to_path_pb2 import (
    KeyToPath as pipeline_sdk___model___container___key_to_path_pb2___KeyToPath,
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


class Volume(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class HostPath(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        path = ... # type: typing___Text
        type = ... # type: typing___Text

        def __init__(self,
            *,
            path : typing___Optional[typing___Text] = None,
            type : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Volume.HostPath: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Volume.HostPath: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"path",b"path",u"type",b"type"]) -> None: ...

    class EmptyDir(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        medium = ... # type: typing___Text
        sizeLimit = ... # type: typing___Text

        def __init__(self,
            *,
            medium : typing___Optional[typing___Text] = None,
            sizeLimit : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Volume.EmptyDir: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Volume.EmptyDir: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"medium",b"medium",u"sizeLimit",b"sizeLimit"]) -> None: ...

    class Secret(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        secretName = ... # type: typing___Text
        defaultMode = ... # type: builtin___int
        optional = ... # type: builtin___bool

        @property
        def items(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[pipeline_sdk___model___container___key_to_path_pb2___KeyToPath]: ...

        def __init__(self,
            *,
            secretName : typing___Optional[typing___Text] = None,
            items : typing___Optional[typing___Iterable[pipeline_sdk___model___container___key_to_path_pb2___KeyToPath]] = None,
            defaultMode : typing___Optional[builtin___int] = None,
            optional : typing___Optional[builtin___bool] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Volume.Secret: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Volume.Secret: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"defaultMode",b"defaultMode",u"items",b"items",u"optional",b"optional",u"secretName",b"secretName"]) -> None: ...

    class ConfigMap(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        name = ... # type: typing___Text
        defaultMode = ... # type: builtin___int
        optional = ... # type: builtin___bool

        @property
        def items(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[pipeline_sdk___model___container___key_to_path_pb2___KeyToPath]: ...

        def __init__(self,
            *,
            name : typing___Optional[typing___Text] = None,
            items : typing___Optional[typing___Iterable[pipeline_sdk___model___container___key_to_path_pb2___KeyToPath]] = None,
            defaultMode : typing___Optional[builtin___int] = None,
            optional : typing___Optional[builtin___bool] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Volume.ConfigMap: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Volume.ConfigMap: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"defaultMode",b"defaultMode",u"items",b"items",u"name",b"name",u"optional",b"optional"]) -> None: ...

    class PersistentVolumeClaim(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        claimName = ... # type: typing___Text
        readOnly = ... # type: builtin___bool

        def __init__(self,
            *,
            claimName : typing___Optional[typing___Text] = None,
            readOnly : typing___Optional[builtin___bool] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Volume.PersistentVolumeClaim: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Volume.PersistentVolumeClaim: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"claimName",b"claimName",u"readOnly",b"readOnly"]) -> None: ...

    name = ... # type: typing___Text

    @property
    def hostPath(self) -> Volume.HostPath: ...

    @property
    def emptyDir(self) -> Volume.EmptyDir: ...

    @property
    def secret(self) -> Volume.Secret: ...

    @property
    def configMap(self) -> Volume.ConfigMap: ...

    @property
    def persistentVolumeClaim(self) -> Volume.PersistentVolumeClaim: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        hostPath : typing___Optional[Volume.HostPath] = None,
        emptyDir : typing___Optional[Volume.EmptyDir] = None,
        secret : typing___Optional[Volume.Secret] = None,
        configMap : typing___Optional[Volume.ConfigMap] = None,
        persistentVolumeClaim : typing___Optional[Volume.PersistentVolumeClaim] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Volume: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Volume: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"configMap",b"configMap",u"emptyDir",b"emptyDir",u"hostPath",b"hostPath",u"persistentVolumeClaim",b"persistentVolumeClaim",u"secret",b"secret"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"configMap",b"configMap",u"emptyDir",b"emptyDir",u"hostPath",b"hostPath",u"name",b"name",u"persistentVolumeClaim",b"persistentVolumeClaim",u"secret",b"secret"]) -> None: ...
