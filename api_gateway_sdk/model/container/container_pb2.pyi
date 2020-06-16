# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from api_gateway_sdk.model.container.container_port_pb2 import (
    ContainerPort as api_gateway_sdk___model___container___container_port_pb2___ContainerPort,
)

from api_gateway_sdk.model.container.env_var_pb2 import (
    EnvVar as api_gateway_sdk___model___container___env_var_pb2___EnvVar,
)

from api_gateway_sdk.model.container.probe_pb2 import (
    Probe as api_gateway_sdk___model___container___probe_pb2___Probe,
)

from api_gateway_sdk.model.container.resource_requirements_pb2 import (
    ResourceRequirements as api_gateway_sdk___model___container___resource_requirements_pb2___ResourceRequirements,
)

from api_gateway_sdk.model.container.volume_mount_pb2 import (
    VolumeMount as api_gateway_sdk___model___container___volume_mount_pb2___VolumeMount,
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


class ContainerConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text
    image = ... # type: typing___Text
    workingDir = ... # type: typing___Text
    imagePullPolicy = ... # type: typing___Text
    command = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    args = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    artifactVersion = ... # type: typing___Text

    @property
    def ports(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[api_gateway_sdk___model___container___container_port_pb2___ContainerPort]: ...

    @property
    def volumeMounts(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[api_gateway_sdk___model___container___volume_mount_pb2___VolumeMount]: ...

    @property
    def env(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[api_gateway_sdk___model___container___env_var_pb2___EnvVar]: ...

    @property
    def resources(self) -> api_gateway_sdk___model___container___resource_requirements_pb2___ResourceRequirements: ...

    @property
    def readinessProbe(self) -> api_gateway_sdk___model___container___probe_pb2___Probe: ...

    @property
    def livenessProbe(self) -> api_gateway_sdk___model___container___probe_pb2___Probe: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        image : typing___Optional[typing___Text] = None,
        workingDir : typing___Optional[typing___Text] = None,
        imagePullPolicy : typing___Optional[typing___Text] = None,
        command : typing___Optional[typing___Iterable[typing___Text]] = None,
        args : typing___Optional[typing___Iterable[typing___Text]] = None,
        ports : typing___Optional[typing___Iterable[api_gateway_sdk___model___container___container_port_pb2___ContainerPort]] = None,
        volumeMounts : typing___Optional[typing___Iterable[api_gateway_sdk___model___container___volume_mount_pb2___VolumeMount]] = None,
        env : typing___Optional[typing___Iterable[api_gateway_sdk___model___container___env_var_pb2___EnvVar]] = None,
        resources : typing___Optional[api_gateway_sdk___model___container___resource_requirements_pb2___ResourceRequirements] = None,
        readinessProbe : typing___Optional[api_gateway_sdk___model___container___probe_pb2___Probe] = None,
        livenessProbe : typing___Optional[api_gateway_sdk___model___container___probe_pb2___Probe] = None,
        artifactVersion : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ContainerConfig: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ContainerConfig: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"livenessProbe",b"livenessProbe",u"readinessProbe",b"readinessProbe",u"resources",b"resources"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"args",b"args",u"artifactVersion",b"artifactVersion",u"command",b"command",u"env",b"env",u"image",b"image",u"imagePullPolicy",b"imagePullPolicy",u"livenessProbe",b"livenessProbe",u"name",b"name",u"ports",b"ports",u"readinessProbe",b"readinessProbe",u"resources",b"resources",u"volumeMounts",b"volumeMounts",u"workingDir",b"workingDir"]) -> None: ...
