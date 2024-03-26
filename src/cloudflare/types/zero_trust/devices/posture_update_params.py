# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "PostureUpdateParams",
    "Input",
    "InputTeamsDevicesFileInputRequest",
    "InputTeamsDevicesUniqueClientIDInputRequest",
    "InputTeamsDevicesDomainJoinedInputRequest",
    "InputTeamsDevicesOSVersionInputRequest",
    "InputTeamsDevicesFirewallInputRequest",
    "InputTeamsDevicesSentineloneInputRequest",
    "InputTeamsDevicesCarbonblackInputRequest",
    "InputTeamsDevicesDiskEncryptionInputRequest",
    "InputTeamsDevicesApplicationInputRequest",
    "InputTeamsDevicesClientCertificateInputRequest",
    "InputTeamsDevicesWorkspaceOneInputRequest",
    "InputTeamsDevicesCrowdstrikeInputRequest",
    "InputTeamsDevicesIntuneInputRequest",
    "InputTeamsDevicesKolideInputRequest",
    "InputTeamsDevicesTaniumInputRequest",
    "InputTeamsDevicesSentineloneS2sInputRequest",
    "Match",
]


class PostureUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]
    """The name of the device posture rule."""

    type: Required[
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
    ]
    """The type of device posture rule."""

    description: str
    """The description of the device posture rule."""

    expiration: str
    """Sets the expiration time for a posture check result.

    If empty, the result remains valid until it is overwritten by new data from the
    WARP client.
    """

    input: Input
    """The value to be checked against."""

    match: Iterable[Match]
    """The conditions that the client must match to run the rule."""

    schedule: str
    """Polling frequency for the WARP client posture check.

    Default: `5m` (poll every five minutes). Minimum: `1m`.
    """


class InputTeamsDevicesFileInputRequest(TypedDict, total=False):
    operating_system: Required[Literal["windows", "linux", "mac"]]
    """Operating system"""

    path: Required[str]
    """File path."""

    exists: bool
    """Whether or not file exists"""

    sha256: str
    """SHA-256."""

    thumbprint: str
    """Signing certificate thumbprint."""


class InputTeamsDevicesUniqueClientIDInputRequest(TypedDict, total=False):
    id: Required[str]
    """List ID."""

    operating_system: Required[Literal["android", "ios", "chromeos"]]
    """Operating System"""


class InputTeamsDevicesDomainJoinedInputRequest(TypedDict, total=False):
    operating_system: Required[Literal["windows"]]
    """Operating System"""

    domain: str
    """Domain"""


class InputTeamsDevicesOSVersionInputRequest(TypedDict, total=False):
    operating_system: Required[Literal["windows"]]
    """Operating System"""

    operator: Required[Literal["<", "<=", ">", ">=", "=="]]
    """Operator"""

    version: Required[str]
    """Version of OS"""

    os_distro_name: str
    """Operating System Distribution Name (linux only)"""

    os_distro_revision: str
    """Version of OS Distribution (linux only)"""

    os_version_extra: str
    """Additional version data.

    For Mac or iOS, the Product Verison Extra. For Linux, the kernel release
    version. (Mac, iOS, and Linux only)
    """


class InputTeamsDevicesFirewallInputRequest(TypedDict, total=False):
    enabled: Required[bool]
    """Enabled"""

    operating_system: Required[Literal["windows", "mac"]]
    """Operating System"""


class InputTeamsDevicesSentineloneInputRequest(TypedDict, total=False):
    operating_system: Required[Literal["windows", "linux", "mac"]]
    """Operating system"""

    path: Required[str]
    """File path."""

    sha256: str
    """SHA-256."""

    thumbprint: str
    """Signing certificate thumbprint."""


class InputTeamsDevicesCarbonblackInputRequest(TypedDict, total=False):
    operating_system: Required[Literal["windows", "linux", "mac"]]
    """Operating system"""

    path: Required[str]
    """File path."""

    sha256: str
    """SHA-256."""

    thumbprint: str
    """Signing certificate thumbprint."""


class InputTeamsDevicesDiskEncryptionInputRequest(TypedDict, total=False):
    check_disks: Annotated[List[str], PropertyInfo(alias="checkDisks")]
    """List of volume names to be checked for encryption."""

    require_all: Annotated[bool, PropertyInfo(alias="requireAll")]
    """Whether to check all disks for encryption."""


class InputTeamsDevicesApplicationInputRequest(TypedDict, total=False):
    operating_system: Required[Literal["windows", "linux", "mac"]]
    """Operating system"""

    path: Required[str]
    """Path for the application."""

    sha256: str
    """SHA-256."""

    thumbprint: str
    """Signing certificate thumbprint."""


class InputTeamsDevicesClientCertificateInputRequest(TypedDict, total=False):
    certificate_id: Required[str]
    """UUID of Cloudflare managed certificate."""

    cn: Required[str]
    """Common Name that is protected by the certificate"""


class InputTeamsDevicesWorkspaceOneInputRequest(TypedDict, total=False):
    compliance_status: Required[Literal["compliant", "noncompliant", "unknown"]]
    """Compliance Status"""

    connection_id: Required[str]
    """Posture Integration ID."""


class InputTeamsDevicesCrowdstrikeInputRequest(TypedDict, total=False):
    connection_id: Required[str]
    """Posture Integration ID."""

    last_seen: str
    """For more details on last seen, please refer to the Crowdstrike documentation."""

    operator: Literal["<", "<=", ">", ">=", "=="]
    """Operator"""

    os: str
    """Os Version"""

    overall: str
    """overall"""

    sensor_config: str
    """SensorConfig"""

    state: Literal["online", "offline", "unknown"]
    """For more details on state, please refer to the Crowdstrike documentation."""

    version: str
    """Version"""

    version_operator: Annotated[Literal["<", "<=", ">", ">=", "=="], PropertyInfo(alias="versionOperator")]
    """Version Operator"""


class InputTeamsDevicesIntuneInputRequest(TypedDict, total=False):
    compliance_status: Required[
        Literal["compliant", "noncompliant", "unknown", "notapplicable", "ingraceperiod", "error"]
    ]
    """Compliance Status"""

    connection_id: Required[str]
    """Posture Integration ID."""


class InputTeamsDevicesKolideInputRequest(TypedDict, total=False):
    connection_id: Required[str]
    """Posture Integration ID."""

    count_operator: Required[Annotated[Literal["<", "<=", ">", ">=", "=="], PropertyInfo(alias="countOperator")]]
    """Count Operator"""

    issue_count: Required[str]
    """The Number of Issues."""


class InputTeamsDevicesTaniumInputRequest(TypedDict, total=False):
    connection_id: Required[str]
    """Posture Integration ID."""

    eid_last_seen: str
    """For more details on eid last seen, refer to the Tanium documentation."""

    operator: Literal["<", "<=", ">", ">=", "=="]
    """Operator to evaluate risk_level or eid_last_seen."""

    risk_level: Literal["low", "medium", "high", "critical"]
    """For more details on risk level, refer to the Tanium documentation."""

    score_operator: Annotated[Literal["<", "<=", ">", ">=", "=="], PropertyInfo(alias="scoreOperator")]
    """Score Operator"""

    total_score: float
    """For more details on total score, refer to the Tanium documentation."""


class InputTeamsDevicesSentineloneS2sInputRequest(TypedDict, total=False):
    connection_id: Required[str]
    """Posture Integration ID."""

    active_threats: float
    """The Number of active threats."""

    infected: bool
    """Whether device is infected."""

    is_active: bool
    """Whether device is active."""

    network_status: Literal["connected", "disconnected", "disconnecting", "connecting"]
    """Network status of device."""

    operator: Literal["<", "<=", ">", ">=", "=="]
    """operator"""


Input = Union[
    InputTeamsDevicesFileInputRequest,
    InputTeamsDevicesUniqueClientIDInputRequest,
    InputTeamsDevicesDomainJoinedInputRequest,
    InputTeamsDevicesOSVersionInputRequest,
    InputTeamsDevicesFirewallInputRequest,
    InputTeamsDevicesSentineloneInputRequest,
    InputTeamsDevicesCarbonblackInputRequest,
    InputTeamsDevicesDiskEncryptionInputRequest,
    InputTeamsDevicesApplicationInputRequest,
    InputTeamsDevicesClientCertificateInputRequest,
    InputTeamsDevicesWorkspaceOneInputRequest,
    InputTeamsDevicesCrowdstrikeInputRequest,
    InputTeamsDevicesIntuneInputRequest,
    InputTeamsDevicesKolideInputRequest,
    InputTeamsDevicesTaniumInputRequest,
    InputTeamsDevicesSentineloneS2sInputRequest,
]


class Match(TypedDict, total=False):
    platform: Literal["windows", "mac", "linux", "android", "ios"]
