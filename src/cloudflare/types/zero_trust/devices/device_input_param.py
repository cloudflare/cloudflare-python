# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .file_input_param import FileInputParam
from .intune_input_param import IntuneInputParam
from .kolide_input_param import KolideInputParam
from .tanium_input_param import TaniumInputParam
from .firewall_input_param import FirewallInputParam
from .os_version_input_param import OSVersionInputParam
from .crowdstrike_input_param import CrowdstrikeInputParam
from .sentinelone_input_param import SentineloneInputParam
from .domain_joined_input_param import DomainJoinedInputParam
from .workspace_one_input_param import WorkspaceOneInputParam
from .disk_encryption_input_param import DiskEncryptionInputParam
from .sentinelone_s2s_input_param import SentineloneS2sInputParam
from .unique_client_id_input_param import UniqueClientIDInputParam
from .client_certificate_input_param import ClientCertificateInputParam

__all__ = [
    "DeviceInputParam",
    "TeamsDevicesCarbonblackInputRequest",
    "TeamsDevicesApplicationInputRequest",
    "TeamsDevicesClientCertificateV2InputRequest",
    "TeamsDevicesClientCertificateV2InputRequestLocations",
    "TeamsDevicesCustomS2sInputRequest",
]


class TeamsDevicesCarbonblackInputRequest(TypedDict, total=False):
    operating_system: Required[Literal["windows", "linux", "mac"]]
    """Operating system"""

    path: Required[str]
    """File path."""

    sha256: str
    """SHA-256."""

    thumbprint: str
    """Signing certificate thumbprint."""


class TeamsDevicesApplicationInputRequest(TypedDict, total=False):
    operating_system: Required[Literal["windows", "linux", "mac"]]
    """Operating system"""

    path: Required[str]
    """Path for the application."""

    sha256: str
    """SHA-256."""

    thumbprint: str
    """Signing certificate thumbprint."""


class TeamsDevicesClientCertificateV2InputRequestLocations(TypedDict, total=False):
    paths: List[str]
    """List of paths to check for client certificate on linux."""

    trust_stores: List[Literal["system", "user"]]
    """List of trust stores to check for client certificate."""


class TeamsDevicesClientCertificateV2InputRequest(TypedDict, total=False):
    certificate_id: Required[str]
    """UUID of Cloudflare managed certificate."""

    check_private_key: Required[bool]
    """Confirm the certificate was not imported from another device.

    We recommend keeping this enabled unless the certificate was deployed without a
    private key.
    """

    operating_system: Required[Literal["windows", "linux", "mac"]]
    """Operating system"""

    cn: str
    """Common Name that is protected by the client certificate.

    This may include one or more variables in the ${ } notation. Only
    ${serial_number} and ${hostname} are valid variables.
    """

    extended_key_usage: List[Literal["clientAuth", "emailProtection"]]
    """
    List of values indicating purposes for which the certificate public key can be
    used
    """

    locations: TeamsDevicesClientCertificateV2InputRequestLocations


class TeamsDevicesCustomS2sInputRequest(TypedDict, total=False):
    connection_id: Required[str]
    """Posture Integration ID."""

    operator: Required[Literal["<", "<=", ">", ">=", "=="]]
    """operator"""

    score: Required[float]
    """
    A value between 0-100 assigned to devices set by the 3rd party posture provider.
    """


DeviceInputParam: TypeAlias = Union[
    FileInputParam,
    UniqueClientIDInputParam,
    DomainJoinedInputParam,
    OSVersionInputParam,
    FirewallInputParam,
    SentineloneInputParam,
    TeamsDevicesCarbonblackInputRequest,
    DiskEncryptionInputParam,
    TeamsDevicesApplicationInputRequest,
    ClientCertificateInputParam,
    TeamsDevicesClientCertificateV2InputRequest,
    WorkspaceOneInputParam,
    CrowdstrikeInputParam,
    IntuneInputParam,
    KolideInputParam,
    TaniumInputParam,
    SentineloneS2sInputParam,
    TeamsDevicesCustomS2sInputRequest,
]
