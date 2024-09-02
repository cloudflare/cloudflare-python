# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .file_input import FileInput

from .unique_client_id_input import UniqueClientIDInput

from .domain_joined_input import DomainJoinedInput

from .os_version_input import OSVersionInput

from .firewall_input import FirewallInput

from .sentinelone_input import SentineloneInput

from .disk_encryption_input import DiskEncryptionInput

from .client_certificate_input import ClientCertificateInput

from .workspace_one_input import WorkspaceOneInput

from .crowdstrike_input import CrowdstrikeInput

from .intune_input import IntuneInput

from .kolide_input import KolideInput

from .tanium_input import TaniumInput

from .sentinelone_s2s_input import SentineloneS2sInput

from ...._models import BaseModel

from typing_extensions import Literal, TypeAlias

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = [
    "DeviceInput",
    "TeamsDevicesCarbonblackInputRequest",
    "TeamsDevicesApplicationInputRequest",
    "TeamsDevicesClientCertificateV2InputRequest",
    "TeamsDevicesClientCertificateV2InputRequestLocations",
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
]
