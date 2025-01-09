# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AbuseReportCreateParams"]


class AbuseReportCreateParams(TypedDict, total=False):
    account_id: Required[str]

    act: Required[
        Literal[
            "abuse_dmca",
            "abuse_trademark",
            "abuse_general",
            "abuse_phishing",
            "abuse_children",
            "abuse_threat",
            "abuse_registrar_whois",
            "abuse_ncsei",
        ]
    ]
    """The abuse report type"""

    email: Required[str]
    """A valid email of the abuse reporter"""

    email2: Required[str]
    """Should match the value provided in `email`"""

    host_notification: Required[Literal["send", "send-anon", "none"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    ncmec_notification: Required[Literal["send", "send-anon", "none"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    owner_notification: Required[Literal["send", "send-anon", "none"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    urls: Required[str]
    """A list of valid URLs separated by ‘ ’ (new line character).

    The list of the URLs should not exceed 250 URLs. All URLs should have the same
    hostname. Each URL should be unique
    """

    address1: str
    """Text not exceeding 100 characters"""

    agent_name: str
    """The name of the copyright holder. Text not exceeding 60 characters."""

    agree: Literal[0, 1]
    """Can be 0 or 1"""

    city: str
    """Text not exceeding 255 characters"""

    comments: str
    """Any additional comments about the infringement not exceeding 2000 characters"""

    company: str
    """Text not exceeding 100 characters"""

    country: str
    """Text not exceeding 255 characters"""

    destination_ips: str
    """A list of IP addresses separated by ‘ ’ (new line character).

    The list of destination IPs should not exceed 30 IP addresses. Each one of the
    IP addresses ought to be unique
    """

    justification: str
    """
    A detailed description of the infringement, including any necessary access
    details and the exact steps needed to view the content, not exceeding 5000
    characters
    """

    name: str
    """Text not exceeding 255 characters"""

    ncsei_subject_representation: bool
    """If the submitter is the target of NCSEI in the URLs of the abuse report"""

    original_work: str
    """Text not exceeding 255 characters"""

    ports_protocols: str
    """A comma separated list of ports and protocols e.g.

    80/TCP, 22/UDP. The total size of the field should not exceed 2000 characters.
    Each individual port/protocol should not exceed 100 characters. The list should
    not have more than 30 unique ports and protocols.
    """

    signature: str
    """Required for DMCA reports, should be same as Name.

    An affirmation that all information in the report is true and accurate while
    agreeing to the policies of Cloudflare's abuse reports
    """

    source_ips: str
    """A list of IP addresses separated by ‘ ’ (new line character).

    The list of source IPs should not exceed 30 IP addresses. Each one of the IP
    addresses ought to be unique
    """

    state: str
    """Text not exceeding 255 characters"""

    tele: str
    """Text not exceeding 20 characters"""

    title: str
    """Text not exceeding 255 characters"""

    trademark_number: str
    """Text not exceeding 1000 characters"""

    trademark_office: str
    """Text not exceeding 1000 characters"""

    trademark_symbol: str
    """Text not exceeding 1000 characters"""
