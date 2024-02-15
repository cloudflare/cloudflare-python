# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "PcapMagicPcapCollectionCreatePcapRequestParams",
    "O1v8KFfTPcapsRequestSimple",
    "O1v8KFfTPcapsRequestSimpleFilterV1",
    "O1v8KFfTPcapsRequestFull",
    "O1v8KFfTPcapsRequestFullFilterV1",
]


class O1v8KFfTPcapsRequestSimple(TypedDict, total=False):
    packet_limit: Required[float]
    """The limit of packets contained in a packet capture."""

    system: Required[Literal["magic-transit"]]
    """The system used to collect packet captures."""

    time_limit: Required[float]
    """The packet capture duration in seconds."""

    type: Required[Literal["simple", "full"]]
    """The type of packet capture.

    `Simple` captures sampled packets, and `full` captures entire payloads and
    non-sampled packets.
    """

    filter_v1: O1v8KFfTPcapsRequestSimpleFilterV1
    """The packet capture filter. When this field is empty, all packets are captured."""


class O1v8KFfTPcapsRequestSimpleFilterV1(TypedDict, total=False):
    destination_address: str
    """The destination IP address of the packet."""

    destination_port: float
    """The destination port of the packet."""

    protocol: float
    """The protocol number of the packet."""

    source_address: str
    """The source IP address of the packet."""

    source_port: float
    """The source port of the packet."""


class O1v8KFfTPcapsRequestFull(TypedDict, total=False):
    colo_name: Required[str]
    """The name of the data center used for the packet capture.

    This can be a specific colo (ord02) or a multi-colo name (ORD). This field only
    applies to `full` packet captures.
    """

    destination_conf: Required[str]
    """The full URI for the bucket. This field only applies to `full` packet captures."""

    system: Required[Literal["magic-transit"]]
    """The system used to collect packet captures."""

    time_limit: Required[float]
    """The packet capture duration in seconds."""

    type: Required[Literal["simple", "full"]]
    """The type of packet capture.

    `Simple` captures sampled packets, and `full` captures entire payloads and
    non-sampled packets.
    """

    byte_limit: float
    """The maximum number of bytes to capture.

    This field only applies to `full` packet captures.
    """

    filter_v1: O1v8KFfTPcapsRequestFullFilterV1
    """The packet capture filter. When this field is empty, all packets are captured."""

    packet_limit: float
    """The limit of packets contained in a packet capture."""


class O1v8KFfTPcapsRequestFullFilterV1(TypedDict, total=False):
    destination_address: str
    """The destination IP address of the packet."""

    destination_port: float
    """The destination port of the packet."""

    protocol: float
    """The protocol number of the packet."""

    source_address: str
    """The source IP address of the packet."""

    source_port: float
    """The source port of the packet."""


PcapMagicPcapCollectionCreatePcapRequestParams = Union[O1v8KFfTPcapsRequestSimple, O1v8KFfTPcapsRequestFull]
