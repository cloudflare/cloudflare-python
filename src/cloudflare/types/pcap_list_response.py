# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal

from .pcap import PCAP
from .filter import Filter
from .._models import BaseModel

__all__ = ["PCAPListResponse", "MagicVisibilityPCAPsResponseSimple"]


class MagicVisibilityPCAPsResponseSimple(BaseModel):
    id: Optional[str] = None
    """The ID for the packet capture."""

    filter_v1: Optional[Filter] = None
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


PCAPListResponse = Union[MagicVisibilityPCAPsResponseSimple, PCAP]
