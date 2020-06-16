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

from resource_package_tools_sdk.model.container.container_pb2 import (
    ContainerConfig as resource_package_tools_sdk___model___container___container_pb2___ContainerConfig,
)

from resource_package_tools_sdk.model.container.deployment_status_pb2 import (
    DeploymentStatus as resource_package_tools_sdk___model___container___deployment_status_pb2___DeploymentStatus,
)

from resource_package_tools_sdk.model.container.deployment_strategy_pb2 import (
    DeploymentStrategy as resource_package_tools_sdk___model___container___deployment_strategy_pb2___DeploymentStrategy,
)

from resource_package_tools_sdk.model.container.local_object_reference_pb2 import (
    LocalObjectReference as resource_package_tools_sdk___model___container___local_object_reference_pb2___LocalObjectReference,
)

from resource_package_tools_sdk.model.container.volume_pb2 import (
    Volume as resource_package_tools_sdk___model___container___volume_pb2___Volume,
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


class Workload(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    instanceId = ... # type: typing___Text
    kind = ... # type: typing___Text
    name = ... # type: typing___Text
    namespace = ... # type: typing___Text
    resourceName = ... # type: typing___Text
    replicas = ... # type: builtin___int
    dnsPolicy = ... # type: typing___Text
    restartPolicy = ... # type: typing___Text
    resourceSpec = ... # type: typing___Text
    creator = ... # type: typing___Text
    creationTimestamp = ... # type: typing___Text
    state = ... # type: typing___Text
    transitionMessage = ... # type: typing___Text

    @property
    def containers(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[resource_package_tools_sdk___model___container___container_pb2___ContainerConfig]: ...

    @property
    def volumes(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[resource_package_tools_sdk___model___container___volume_pb2___Volume]: ...

    @property
    def annotations(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def labels(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def deploymentStrategy(self) -> resource_package_tools_sdk___model___container___deployment_strategy_pb2___DeploymentStrategy: ...

    @property
    def imagePullSecrets(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[resource_package_tools_sdk___model___container___local_object_reference_pb2___LocalObjectReference]: ...

    @property
    def deploymentStatus(self) -> resource_package_tools_sdk___model___container___deployment_status_pb2___DeploymentStatus: ...

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        kind : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        namespace : typing___Optional[typing___Text] = None,
        resourceName : typing___Optional[typing___Text] = None,
        containers : typing___Optional[typing___Iterable[resource_package_tools_sdk___model___container___container_pb2___ContainerConfig]] = None,
        replicas : typing___Optional[builtin___int] = None,
        volumes : typing___Optional[typing___Iterable[resource_package_tools_sdk___model___container___volume_pb2___Volume]] = None,
        annotations : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        labels : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        dnsPolicy : typing___Optional[typing___Text] = None,
        restartPolicy : typing___Optional[typing___Text] = None,
        deploymentStrategy : typing___Optional[resource_package_tools_sdk___model___container___deployment_strategy_pb2___DeploymentStrategy] = None,
        imagePullSecrets : typing___Optional[typing___Iterable[resource_package_tools_sdk___model___container___local_object_reference_pb2___LocalObjectReference]] = None,
        deploymentStatus : typing___Optional[resource_package_tools_sdk___model___container___deployment_status_pb2___DeploymentStatus] = None,
        resourceSpec : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        creationTimestamp : typing___Optional[typing___Text] = None,
        state : typing___Optional[typing___Text] = None,
        transitionMessage : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Workload: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Workload: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"annotations",b"annotations",u"deploymentStatus",b"deploymentStatus",u"deploymentStrategy",b"deploymentStrategy",u"labels",b"labels"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"annotations",b"annotations",u"containers",b"containers",u"creationTimestamp",b"creationTimestamp",u"creator",b"creator",u"deploymentStatus",b"deploymentStatus",u"deploymentStrategy",b"deploymentStrategy",u"dnsPolicy",b"dnsPolicy",u"imagePullSecrets",b"imagePullSecrets",u"instanceId",b"instanceId",u"kind",b"kind",u"labels",b"labels",u"name",b"name",u"namespace",b"namespace",u"replicas",b"replicas",u"resourceName",b"resourceName",u"resourceSpec",b"resourceSpec",u"restartPolicy",b"restartPolicy",u"state",b"state",u"transitionMessage",b"transitionMessage",u"volumes",b"volumes"]) -> None: ...
