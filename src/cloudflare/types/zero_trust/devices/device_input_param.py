# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

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

__all__ = ["DeviceInputParam", "TeamsDevicesCarbonblackInputRequest", "TeamsDevicesApplicationInputRequest"]


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


DeviceInputParam = Union[
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
    WorkspaceOneInputParam,
    CrowdstrikeInputParam,
    IntuneInputParam,
    KolideInputParam,
    TaniumInputParam,
    SentineloneS2sInputParam,
]
