# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel
from .file_input import FileInput
from .intune_input import IntuneInput
from .kolide_input import KolideInput
from .tanium_input import TaniumInput
from .firewall_input import FirewallInput
from .os_version_input import OSVersionInput
from .crowdstrike_input import CrowdstrikeInput
from .sentinelone_input import SentineloneInput
from .domain_joined_input import DomainJoinedInput
from .workspace_one_input import WorkspaceOneInput
from .disk_encryption_input import DiskEncryptionInput
from .sentinelone_s2s_input import SentineloneS2sInput
from .unique_client_id_input import UniqueClientIDInput
from .client_certificate_input import ClientCertificateInput

__all__ = [
    "DeviceInput",
    "TeamsDevicesCarbonblackInputRequest",
    "TeamsDevicesApplicationInputRequest",
    "TeamsDevicesClientCertificateV2InputRequest",
    "TeamsDevicesClientCertificateV2InputRequestLocations",
    "TeamsDevicesCustomS2sInputRequest",
]


class TeamsDevicesCarbonblackInputRequest(BaseModel):
    operating_system: Literal["windows", "linux", "mac"]
    """Operating system"""

    path: str
    """File path."""

    sha256: Optional[str] = None
    """SHA-256."""

    thumbprint: Optional[str] = None
    """Signing certificate thumbprint."""


class TeamsDevicesApplicationInputRequest(BaseModel):
    operating_system: Literal["windows", "linux", "mac"]
    """Operating system"""

    path: str
    """Path for the application."""

    sha256: Optional[str] = None
    """SHA-256."""

    thumbprint: Optional[str] = None
    """Signing certificate thumbprint."""


class TeamsDevicesClientCertificateV2InputRequestLocations(BaseModel):
    paths: Optional[List[str]] = None
    """List of paths to check for client certificate on linux."""

    trust_stores: Optional[List[Literal["system", "user"]]] = None
    """List of trust stores to check for client certificate."""


class TeamsDevicesClientCertificateV2InputRequest(BaseModel):
    certificate_id: str
    """UUID of Cloudflare managed certificate."""

    check_private_key: bool
    """Confirm the certificate was not imported from another device.

    We recommend keeping this enabled unless the certificate was deployed without a
    private key.
    """

    operating_system: Literal["windows", "linux", "mac"]
    """Operating system"""

    cn: Optional[str] = None
    """Common Name that is protected by the client certificate.

    This may include one or more variables in the ${ } notation. Only
    ${serial_number} and ${hostname} are valid variables.
    """

    extended_key_usage: Optional[List[Literal["clientAuth", "emailProtection"]]] = None
    """
    List of values indicating purposes for which the certificate public key can be
    used
    """

    locations: Optional[TeamsDevicesClientCertificateV2InputRequestLocations] = None


class TeamsDevicesCustomS2sInputRequest(BaseModel):
    connection_id: str
    """Posture Integration ID."""

    operator: Literal["<", "<=", ">", ">=", "=="]
    """operator"""

    score: float
    """
    A value between 0-100 assigned to devices set by the 3rd party posture provider.
    """


DeviceInput: TypeAlias = Union[
    FileInput,
    UniqueClientIDInput,
    DomainJoinedInput,
    OSVersionInput,
    FirewallInput,
    SentineloneInput,
    TeamsDevicesCarbonblackInputRequest,
    DiskEncryptionInput,
    TeamsDevicesApplicationInputRequest,
    ClientCertificateInput,
    TeamsDevicesClientCertificateV2InputRequest,
    WorkspaceOneInput,
    CrowdstrikeInput,
    IntuneInput,
    KolideInput,
    TaniumInput,
    SentineloneS2sInput,
    TeamsDevicesCustomS2sInputRequest,
]
