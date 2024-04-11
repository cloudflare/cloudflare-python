# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal

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

__all__ = ["DeviceInput", "TeamsDevicesCarbonblackInputRequest", "TeamsDevicesApplicationInputRequest"]


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


DeviceInput = Union[
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
    WorkspaceOneInput,
    CrowdstrikeInput,
    IntuneInput,
    KolideInput,
    TaniumInput,
    SentineloneS2sInput,
]
