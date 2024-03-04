# File generated from our OpenAPI spec by Stainless.

from typing import List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "PostureListResponse",
    "PostureListResponseItem",
    "PostureListResponseItemInput",
    "PostureListResponseItemInputTeamsDevicesFileInputRequest",
    "PostureListResponseItemInputTeamsDevicesUniqueClientIDInputRequest",
    "PostureListResponseItemInputTeamsDevicesDomainJoinedInputRequest",
    "PostureListResponseItemInputTeamsDevicesOSVersionInputRequest",
    "PostureListResponseItemInputTeamsDevicesFirewallInputRequest",
    "PostureListResponseItemInputTeamsDevicesSentineloneInputRequest",
    "PostureListResponseItemInputTeamsDevicesCarbonblackInputRequest",
    "PostureListResponseItemInputTeamsDevicesDiskEncryptionInputRequest",
    "PostureListResponseItemInputTeamsDevicesApplicationInputRequest",
    "PostureListResponseItemInputTeamsDevicesClientCertificateInputRequest",
    "PostureListResponseItemInputTeamsDevicesWorkspaceOneInputRequest",
    "PostureListResponseItemInputTeamsDevicesCrowdstrikeInputRequest",
    "PostureListResponseItemInputTeamsDevicesIntuneInputRequest",
    "PostureListResponseItemInputTeamsDevicesKolideInputRequest",
    "PostureListResponseItemInputTeamsDevicesTaniumInputRequest",
    "PostureListResponseItemInputTeamsDevicesSentineloneS2sInputRequest",
    "PostureListResponseItemMatch",
]


class PostureListResponseItemInputTeamsDevicesFileInputRequest(BaseModel):
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


class PostureListResponseItemInputTeamsDevicesUniqueClientIDInputRequest(BaseModel):
    id: str
    """List ID."""

    operating_system: Literal["android", "ios", "chromeos"]
    """Operating System"""


class PostureListResponseItemInputTeamsDevicesDomainJoinedInputRequest(BaseModel):
    operating_system: Literal["windows"]
    """Operating System"""

    domain: Optional[str] = None
    """Domain"""


class PostureListResponseItemInputTeamsDevicesOSVersionInputRequest(BaseModel):
    operating_system: Literal["windows"]
    """Operating System"""

    operator: Literal["<", "<=", ">", ">=", "=="]
    """Operator"""

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


class PostureListResponseItemInputTeamsDevicesFirewallInputRequest(BaseModel):
    enabled: bool
    """Enabled"""

    operating_system: Literal["windows", "mac"]
    """Operating System"""


class PostureListResponseItemInputTeamsDevicesSentineloneInputRequest(BaseModel):
    operating_system: Literal["windows", "linux", "mac"]
    """Operating system"""

    path: str
    """File path."""

    sha256: Optional[str] = None
    """SHA-256."""

    thumbprint: Optional[str] = None
    """Signing certificate thumbprint."""


class PostureListResponseItemInputTeamsDevicesCarbonblackInputRequest(BaseModel):
    operating_system: Literal["windows", "linux", "mac"]
    """Operating system"""

    path: str
    """File path."""

    sha256: Optional[str] = None
    """SHA-256."""

    thumbprint: Optional[str] = None
    """Signing certificate thumbprint."""


class PostureListResponseItemInputTeamsDevicesDiskEncryptionInputRequest(BaseModel):
    check_disks: Optional[List[str]] = FieldInfo(alias="checkDisks", default=None)
    """List of volume names to be checked for encryption."""

    require_all: Optional[bool] = FieldInfo(alias="requireAll", default=None)
    """Whether to check all disks for encryption."""


class PostureListResponseItemInputTeamsDevicesApplicationInputRequest(BaseModel):
    operating_system: Literal["windows", "linux", "mac"]
    """Operating system"""

    path: str
    """Path for the application."""

    sha256: Optional[str] = None
    """SHA-256."""

    thumbprint: Optional[str] = None
    """Signing certificate thumbprint."""


class PostureListResponseItemInputTeamsDevicesClientCertificateInputRequest(BaseModel):
    certificate_id: str
    """UUID of Cloudflare managed certificate."""

    cn: str
    """Common Name that is protected by the certificate"""


class PostureListResponseItemInputTeamsDevicesWorkspaceOneInputRequest(BaseModel):
    compliance_status: Literal["compliant", "noncompliant", "unknown"]
    """Compliance Status"""

    connection_id: str
    """Posture Integration ID."""


class PostureListResponseItemInputTeamsDevicesCrowdstrikeInputRequest(BaseModel):
    connection_id: str
    """Posture Integration ID."""

    last_seen: Optional[str] = None
    """For more details on last seen, please refer to the Crowdstrike documentation."""

    operator: Optional[Literal["<", "<=", ">", ">=", "=="]] = None
    """Operator"""

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


class PostureListResponseItemInputTeamsDevicesIntuneInputRequest(BaseModel):
    compliance_status: Literal["compliant", "noncompliant", "unknown", "notapplicable", "ingraceperiod", "error"]
    """Compliance Status"""

    connection_id: str
    """Posture Integration ID."""


class PostureListResponseItemInputTeamsDevicesKolideInputRequest(BaseModel):
    connection_id: str
    """Posture Integration ID."""

    count_operator: Literal["<", "<=", ">", ">=", "=="] = FieldInfo(alias="countOperator")
    """Count Operator"""

    issue_count: str
    """The Number of Issues."""


class PostureListResponseItemInputTeamsDevicesTaniumInputRequest(BaseModel):
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


class PostureListResponseItemInputTeamsDevicesSentineloneS2sInputRequest(BaseModel):
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


PostureListResponseItemInput = Union[
    PostureListResponseItemInputTeamsDevicesFileInputRequest,
    PostureListResponseItemInputTeamsDevicesUniqueClientIDInputRequest,
    PostureListResponseItemInputTeamsDevicesDomainJoinedInputRequest,
    PostureListResponseItemInputTeamsDevicesOSVersionInputRequest,
    PostureListResponseItemInputTeamsDevicesFirewallInputRequest,
    PostureListResponseItemInputTeamsDevicesSentineloneInputRequest,
    PostureListResponseItemInputTeamsDevicesCarbonblackInputRequest,
    PostureListResponseItemInputTeamsDevicesDiskEncryptionInputRequest,
    PostureListResponseItemInputTeamsDevicesApplicationInputRequest,
    PostureListResponseItemInputTeamsDevicesClientCertificateInputRequest,
    PostureListResponseItemInputTeamsDevicesWorkspaceOneInputRequest,
    PostureListResponseItemInputTeamsDevicesCrowdstrikeInputRequest,
    PostureListResponseItemInputTeamsDevicesIntuneInputRequest,
    PostureListResponseItemInputTeamsDevicesKolideInputRequest,
    PostureListResponseItemInputTeamsDevicesTaniumInputRequest,
    PostureListResponseItemInputTeamsDevicesSentineloneS2sInputRequest,
]


class PostureListResponseItemMatch(BaseModel):
    platform: Optional[Literal["windows", "mac", "linux", "android", "ios"]] = None


class PostureListResponseItem(BaseModel):
    id: Optional[str] = None
    """API UUID."""

    description: Optional[str] = None
    """The description of the device posture rule."""

    expiration: Optional[str] = None
    """Sets the expiration time for a posture check result.

    If empty, the result remains valid until it is overwritten by new data from the
    WARP client.
    """

    input: Optional[PostureListResponseItemInput] = None
    """The value to be checked against."""

    match: Optional[List[PostureListResponseItemMatch]] = None
    """The conditions that the client must match to run the rule."""

    name: Optional[str] = None
    """The name of the device posture rule."""

    schedule: Optional[str] = None
    """Polling frequency for the WARP client posture check.

    Default: `5m` (poll every five minutes). Minimum: `1m`.
    """

    type: Optional[
        Literal[
            "file",
            "application",
            "tanium",
            "gateway",
            "warp",
            "disk_encryption",
            "sentinelone",
            "carbonblack",
            "firewall",
            "os_version",
            "domain_joined",
            "client_certificate",
            "unique_client_id",
            "kolide",
            "tanium_s2s",
            "crowdstrike_s2s",
            "intune",
            "workspace_one",
            "sentinelone_s2s",
        ]
    ] = None
    """The type of device posture rule."""


PostureListResponse = List[PostureListResponseItem]
