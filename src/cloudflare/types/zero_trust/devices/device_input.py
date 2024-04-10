# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "DeviceInput",
    "TeamsDevicesFileInputRequest",
    "TeamsDevicesUniqueClientIDInputRequest",
    "TeamsDevicesDomainJoinedInputRequest",
    "TeamsDevicesOSVersionInputRequest",
    "TeamsDevicesFirewallInputRequest",
    "TeamsDevicesSentineloneInputRequest",
    "TeamsDevicesCarbonblackInputRequest",
    "TeamsDevicesDiskEncryptionInputRequest",
    "TeamsDevicesApplicationInputRequest",
    "TeamsDevicesClientCertificateInputRequest",
    "TeamsDevicesWorkspaceOneInputRequest",
    "TeamsDevicesCrowdstrikeInputRequest",
    "TeamsDevicesIntuneInputRequest",
    "TeamsDevicesKolideInputRequest",
    "TeamsDevicesTaniumInputRequest",
    "TeamsDevicesSentineloneS2sInputRequest",
]


class TeamsDevicesFileInputRequest(BaseModel):
    operating_system: Literal["windows", "linux", "mac"]
    """Operating system"""

    path: str
    """File path."""

    exists: Optional[bool] = None
    """Whether or not file exists"""

    sha256: Optional[str] = None
    """SHA-256."""

    thumbprint: Optional[str] = None
    """Signing certificate thumbprint."""


class TeamsDevicesUniqueClientIDInputRequest(BaseModel):
    id: str
    """List ID."""

    operating_system: Literal["android", "ios", "chromeos"]
    """Operating System"""


class TeamsDevicesDomainJoinedInputRequest(BaseModel):
    operating_system: Literal["windows"]
    """Operating System"""

    domain: Optional[str] = None
    """Domain"""


class TeamsDevicesOSVersionInputRequest(BaseModel):
    operating_system: Literal["windows"]
    """Operating System"""

    operator: Literal["<", "<=", ">", ">=", "=="]
    """operator"""

    version: str
    """Version of OS"""

    os_distro_name: Optional[str] = None
    """Operating System Distribution Name (linux only)"""

    os_distro_revision: Optional[str] = None
    """Version of OS Distribution (linux only)"""

    os_version_extra: Optional[str] = None
    """Additional version data.

    For Mac or iOS, the Product Verison Extra. For Linux, the kernel release
    version. (Mac, iOS, and Linux only)
    """


class TeamsDevicesFirewallInputRequest(BaseModel):
    enabled: bool
    """Enabled"""

    operating_system: Literal["windows", "mac"]
    """Operating System"""


class TeamsDevicesSentineloneInputRequest(BaseModel):
    operating_system: Literal["windows", "linux", "mac"]
    """Operating system"""

    path: str
    """File path."""

    sha256: Optional[str] = None
    """SHA-256."""

    thumbprint: Optional[str] = None
    """Signing certificate thumbprint."""


class TeamsDevicesCarbonblackInputRequest(BaseModel):
    operating_system: Literal["windows", "linux", "mac"]
    """Operating system"""

    path: str
    """File path."""

    sha256: Optional[str] = None
    """SHA-256."""

    thumbprint: Optional[str] = None
    """Signing certificate thumbprint."""


class TeamsDevicesDiskEncryptionInputRequest(BaseModel):
    check_disks: Optional[List[str]] = FieldInfo(alias="checkDisks", default=None)
    """List of volume names to be checked for encryption."""

    require_all: Optional[bool] = FieldInfo(alias="requireAll", default=None)
    """Whether to check all disks for encryption."""


class TeamsDevicesApplicationInputRequest(BaseModel):
    operating_system: Literal["windows", "linux", "mac"]
    """Operating system"""

    path: str
    """Path for the application."""

    sha256: Optional[str] = None
    """SHA-256."""

    thumbprint: Optional[str] = None
    """Signing certificate thumbprint."""


class TeamsDevicesClientCertificateInputRequest(BaseModel):
    certificate_id: str
    """UUID of Cloudflare managed certificate."""

    cn: str
    """Common Name that is protected by the certificate"""


class TeamsDevicesWorkspaceOneInputRequest(BaseModel):
    compliance_status: Literal["compliant", "noncompliant", "unknown"]
    """Compliance Status"""

    connection_id: str
    """Posture Integration ID."""


class TeamsDevicesCrowdstrikeInputRequest(BaseModel):
    connection_id: str
    """Posture Integration ID."""

    last_seen: Optional[str] = None
    """For more details on last seen, please refer to the Crowdstrike documentation."""

    operator: Optional[Literal["<", "<=", ">", ">=", "=="]] = None
    """operator"""

    os: Optional[str] = None
    """Os Version"""

    overall: Optional[str] = None
    """overall"""

    sensor_config: Optional[str] = None
    """SensorConfig"""

    state: Optional[Literal["online", "offline", "unknown"]] = None
    """For more details on state, please refer to the Crowdstrike documentation."""

    version: Optional[str] = None
    """Version"""

    version_operator: Optional[Literal["<", "<=", ">", ">=", "=="]] = FieldInfo(alias="versionOperator", default=None)
    """Version Operator"""


class TeamsDevicesIntuneInputRequest(BaseModel):
    compliance_status: Literal["compliant", "noncompliant", "unknown", "notapplicable", "ingraceperiod", "error"]
    """Compliance Status"""

    connection_id: str
    """Posture Integration ID."""


class TeamsDevicesKolideInputRequest(BaseModel):
    connection_id: str
    """Posture Integration ID."""

    count_operator: Literal["<", "<=", ">", ">=", "=="] = FieldInfo(alias="countOperator")
    """Count Operator"""

    issue_count: str
    """The Number of Issues."""


class TeamsDevicesTaniumInputRequest(BaseModel):
    connection_id: str
    """Posture Integration ID."""

    eid_last_seen: Optional[str] = None
    """For more details on eid last seen, refer to the Tanium documentation."""

    operator: Optional[Literal["<", "<=", ">", ">=", "=="]] = None
    """Operator to evaluate risk_level or eid_last_seen."""

    risk_level: Optional[Literal["low", "medium", "high", "critical"]] = None
    """For more details on risk level, refer to the Tanium documentation."""

    score_operator: Optional[Literal["<", "<=", ">", ">=", "=="]] = FieldInfo(alias="scoreOperator", default=None)
    """Score Operator"""

    total_score: Optional[float] = None
    """For more details on total score, refer to the Tanium documentation."""


class TeamsDevicesSentineloneS2sInputRequest(BaseModel):
    connection_id: str
    """Posture Integration ID."""

    active_threats: Optional[float] = None
    """The Number of active threats."""

    infected: Optional[bool] = None
    """Whether device is infected."""

    is_active: Optional[bool] = None
    """Whether device is active."""

    network_status: Optional[Literal["connected", "disconnected", "disconnecting", "connecting"]] = None
    """Network status of device."""

    operator: Optional[Literal["<", "<=", ">", ">=", "=="]] = None
    """operator"""


DeviceInput = Union[
    TeamsDevicesFileInputRequest,
    TeamsDevicesUniqueClientIDInputRequest,
    TeamsDevicesDomainJoinedInputRequest,
    TeamsDevicesOSVersionInputRequest,
    TeamsDevicesFirewallInputRequest,
    TeamsDevicesSentineloneInputRequest,
    TeamsDevicesCarbonblackInputRequest,
    TeamsDevicesDiskEncryptionInputRequest,
    TeamsDevicesApplicationInputRequest,
    TeamsDevicesClientCertificateInputRequest,
    TeamsDevicesWorkspaceOneInputRequest,
    TeamsDevicesCrowdstrikeInputRequest,
    TeamsDevicesIntuneInputRequest,
    TeamsDevicesKolideInputRequest,
    TeamsDevicesTaniumInputRequest,
    TeamsDevicesSentineloneS2sInputRequest,
]
