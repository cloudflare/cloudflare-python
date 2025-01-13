# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from .pcap import PCAP
from ..._models import BaseModel
from .pcap_filter import PCAPFilter

__all__ = ["PCAPCreateResponse", "MagicVisibilityPCAPsPCAPsResponseFull"]


class MagicVisibilityPCAPsPCAPsResponseFull(BaseModel):
    id: Optional[str] = None
    """The ID for the packet capture."""

    byte_limit: Optional[float] = None
    """The maximum number of bytes to capture.

    This field only applies to `full` packet captures.
    """

    colo_name: Optional[str] = None
    """The name of the data center used for the packet capture.

    This can be a specific colo (ord02) or a multi-colo name (ORD). This field only
    applies to `full` packet captures.
    """

    destination_conf: Optional[str] = None
    """The full URI for the bucket. This field only applies to `full` packet captures."""

    error_message: Optional[str] = None
    """An error message that describes why the packet capture failed.

    This field only applies to `full` packet captures.
    """

    filter_v1: Optional[PCAPFilter] = None
    """The packet capture filter. When this field is empty, all packets are captured."""

    status: Optional[
        Literal[
            "unknown", "success", "pending", "running", "conversion_pending", "conversion_running", "complete", "failed"
        ]
    ] = None
    """The status of the packet capture request."""

    submitted: Optional[str] = None
    """The RFC 3339 timestamp when the packet capture was created."""

    system: Optional[Literal["magic-transit"]] = None
    """The system used to collect packet captures."""

    time_limit: Optional[float] = None
    """The packet capture duration in seconds."""

    type: Optional[Literal["simple", "full"]] = None
    """The type of packet capture.

    `Simple` captures sampled packets, and `full` captures entire payloads and
    non-sampled packets.
    """


PCAPCreateResponse: TypeAlias = Union[PCAP, MagicVisibilityPCAPsPCAPsResponseFull]
