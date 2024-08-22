# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict, Required, TypeAlias

from typing import List, Union

from .file_input_param import FileInputParam

from .unique_client_id_input_param import UniqueClientIDInputParam

from .domain_joined_input_param import DomainJoinedInputParam

from .os_version_input_param import OSVersionInputParam

from .firewall_input_param import FirewallInputParam

from .sentinelone_input_param import SentineloneInputParam

from .disk_encryption_input_param import DiskEncryptionInputParam

from .client_certificate_input_param import ClientCertificateInputParam

from .workspace_one_input_param import WorkspaceOneInputParam

from .crowdstrike_input_param import CrowdstrikeInputParam

from .intune_input_param import IntuneInputParam

from .kolide_input_param import KolideInputParam

from .tanium_input_param import TaniumInputParam

from .sentinelone_s2s_input_param import SentineloneS2sInputParam

__all__ = ["DeviceInputParam", "TeamsDevicesCarbonblackInputRequest", "TeamsDevicesApplicationInputRequest", "TeamsDevicesClientCertificateV2InputRequest", "TeamsDevicesClientCertificateV2InputRequestLocations"]

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

DeviceInputParam: TypeAlias = Union[FileInputParam, UniqueClientIDInputParam, DomainJoinedInputParam, OSVersionInputParam, FirewallInputParam, SentineloneInputParam, TeamsDevicesCarbonblackInputRequest, DiskEncryptionInputParam, TeamsDevicesApplicationInputRequest, ClientCertificateInputParam, TeamsDevicesClientCertificateV2InputRequest, WorkspaceOneInputParam, CrowdstrikeInputParam, IntuneInputParam, KolideInputParam, TaniumInputParam, SentineloneS2sInputParam]