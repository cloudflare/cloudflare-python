# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "AbuseReportCreateParams",
    "AbuseReportsDmcaReport",
    "AbuseReportsTrademarkReport",
    "AbuseReportsGeneralReport",
    "AbuseReportsPhishingReport",
    "AbuseReportsChildrenAbuseReport",
    "AbuseReportsThreatReport",
    "AbuseReportsRegistrarWhoisReport",
    "AbuseReportsNcseiReport",
]


class AbuseReportsDmcaReport(TypedDict, total=False):
    account_id: Required[str]

    address1: Required[str]
    """Text not exceeding 100 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    agent_name: Required[str]
    """The name of the copyright holder.

    Text not exceeding 60 characters. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
    """

    agree: Required[Literal[0, 1]]
    """Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports"""

    city: Required[str]
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    country: Required[str]
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    host_notification: Required[Literal["send", "send-anon", "none"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    original_work: Required[str]
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    owner_notification: Required[Literal["send", "send-anon", "none"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    signature: Required[str]
    """Required for DMCA reports, should be same as Name.

    An affirmation that all information in the report is true and accurate while
    agreeing to the policies of Cloudflare's abuse reports
    """

    state: Required[str]
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    act: Literal[
        "abuse_dmca",
        "abuse_trademark",
        "abuse_general",
        "abuse_phishing",
        "abuse_children",
        "abuse_threat",
        "abuse_registrar_whois",
        "abuse_ncsei",
    ]
    """The abuse report type"""

    comments: str
    """Any additional comments about the infringement not exceeding 2000 characters"""

    company: str
    """Text not exceeding 100 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    destination_ips: str
    """A list of IP addresses separated by ‘ ’ (new line character).

    The list of destination IPs should not exceed 30 IP addresses. Each one of the
    IP addresses ought to be unique
    """

    email: str
    """A valid email of the abuse reporter.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    email2: str
    """Should match the value provided in `email`"""

    justification: str
    """
    A detailed description of the infringement, including any necessary access
    details and the exact steps needed to view the content, not exceeding 5000
    characters
    """

    name: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    ncmec_notification: Literal["send", "send-anon", "none"]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    ncsei_subject_representation: bool
    """If the submitter is the target of NCSEI in the URLs of the abuse report."""

    ports_protocols: str
    """A comma separated list of ports and protocols e.g.

    80/TCP, 22/UDP. The total size of the field should not exceed 2000 characters.
    Each individual port/protocol should not exceed 100 characters. The list should
    not have more than 30 unique ports and protocols.
    """

    source_ips: str
    """A list of IP addresses separated by ‘ ’ (new line character).

    The list of source IPs should not exceed 30 IP addresses. Each one of the IP
    addresses ought to be unique
    """

    tele: str
    """Text not exceeding 20 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    title: str
    """Text not exceeding 255 characters"""

    trademark_number: str
    """Text not exceeding 1000 characters"""

    trademark_office: str
    """Text not exceeding 1000 characters"""

    trademark_symbol: str
    """Text not exceeding 1000 characters"""

    urls: str
    """A list of valid URLs separated by ‘ ’ (new line character).

    The list of the URLs should not exceed 250 URLs. All URLs should have the same
    hostname. Each URL should be unique. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
    """


class AbuseReportsTrademarkReport(TypedDict, total=False):
    account_id: Required[str]

    host_notification: Required[Literal["send", "send-anon", "none"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    justification: Required[str]
    """
    A detailed description of the infringement, including any necessary access
    details and the exact steps needed to view the content, not exceeding 5000
    characters
    """

    owner_notification: Required[Literal["send", "send-anon", "none"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    trademark_number: Required[str]
    """Text not exceeding 1000 characters"""

    trademark_office: Required[str]
    """Text not exceeding 1000 characters"""

    trademark_symbol: Required[str]
    """Text not exceeding 1000 characters"""

    act: Literal[
        "abuse_dmca",
        "abuse_trademark",
        "abuse_general",
        "abuse_phishing",
        "abuse_children",
        "abuse_threat",
        "abuse_registrar_whois",
        "abuse_ncsei",
    ]
    """The abuse report type"""

    address1: str
    """Text not exceeding 100 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    agent_name: str
    """The name of the copyright holder.

    Text not exceeding 60 characters. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
    """

    agree: Literal[0, 1]
    """Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports"""

    city: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    comments: str
    """Any additional comments about the infringement not exceeding 2000 characters"""

    company: str
    """Text not exceeding 100 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    country: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    destination_ips: str
    """A list of IP addresses separated by ‘ ’ (new line character).

    The list of destination IPs should not exceed 30 IP addresses. Each one of the
    IP addresses ought to be unique
    """

    email: str
    """A valid email of the abuse reporter.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    email2: str
    """Should match the value provided in `email`"""

    name: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    ncmec_notification: Literal["send", "send-anon", "none"]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    ncsei_subject_representation: bool
    """If the submitter is the target of NCSEI in the URLs of the abuse report."""

    original_work: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

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
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    tele: str
    """Text not exceeding 20 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    title: str
    """Text not exceeding 255 characters"""

    urls: str
    """A list of valid URLs separated by ‘ ’ (new line character).

    The list of the URLs should not exceed 250 URLs. All URLs should have the same
    hostname. Each URL should be unique. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
    """


class AbuseReportsGeneralReport(TypedDict, total=False):
    account_id: Required[str]

    host_notification: Required[Literal["send", "send-anon", "none"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    justification: Required[str]
    """
    A detailed description of the infringement, including any necessary access
    details and the exact steps needed to view the content, not exceeding 5000
    characters
    """

    owner_notification: Required[Literal["send", "send-anon", "none"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    act: Literal[
        "abuse_dmca",
        "abuse_trademark",
        "abuse_general",
        "abuse_phishing",
        "abuse_children",
        "abuse_threat",
        "abuse_registrar_whois",
        "abuse_ncsei",
    ]
    """The abuse report type"""

    address1: str
    """Text not exceeding 100 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    agent_name: str
    """The name of the copyright holder.

    Text not exceeding 60 characters. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
    """

    agree: Literal[0, 1]
    """Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports"""

    city: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    comments: str
    """Any additional comments about the infringement not exceeding 2000 characters"""

    company: str
    """Text not exceeding 100 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    country: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    destination_ips: str
    """A list of IP addresses separated by ‘ ’ (new line character).

    The list of destination IPs should not exceed 30 IP addresses. Each one of the
    IP addresses ought to be unique
    """

    email: str
    """A valid email of the abuse reporter.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    email2: str
    """Should match the value provided in `email`"""

    name: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    ncmec_notification: Literal["send", "send-anon", "none"]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    ncsei_subject_representation: bool
    """If the submitter is the target of NCSEI in the URLs of the abuse report."""

    original_work: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

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
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    tele: str
    """Text not exceeding 20 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    title: str
    """Text not exceeding 255 characters"""

    trademark_number: str
    """Text not exceeding 1000 characters"""

    trademark_office: str
    """Text not exceeding 1000 characters"""

    trademark_symbol: str
    """Text not exceeding 1000 characters"""

    urls: str
    """A list of valid URLs separated by ‘ ’ (new line character).

    The list of the URLs should not exceed 250 URLs. All URLs should have the same
    hostname. Each URL should be unique. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
    """


class AbuseReportsPhishingReport(TypedDict, total=False):
    account_id: Required[str]

    host_notification: Required[Literal["send", "send-anon", "none"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    justification: Required[str]
    """
    A detailed description of the infringement, including any necessary access
    details and the exact steps needed to view the content, not exceeding 5000
    characters
    """

    owner_notification: Required[Literal["send", "send-anon", "none"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    act: Literal[
        "abuse_dmca",
        "abuse_trademark",
        "abuse_general",
        "abuse_phishing",
        "abuse_children",
        "abuse_threat",
        "abuse_registrar_whois",
        "abuse_ncsei",
    ]
    """The abuse report type"""

    address1: str
    """Text not exceeding 100 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    agent_name: str
    """The name of the copyright holder.

    Text not exceeding 60 characters. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
    """

    agree: Literal[0, 1]
    """Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports"""

    city: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    comments: str
    """Any additional comments about the infringement not exceeding 2000 characters"""

    company: str
    """Text not exceeding 100 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    country: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    destination_ips: str
    """A list of IP addresses separated by ‘ ’ (new line character).

    The list of destination IPs should not exceed 30 IP addresses. Each one of the
    IP addresses ought to be unique
    """

    email: str
    """A valid email of the abuse reporter.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    email2: str
    """Should match the value provided in `email`"""

    name: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    ncmec_notification: Literal["send", "send-anon", "none"]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    ncsei_subject_representation: bool
    """If the submitter is the target of NCSEI in the URLs of the abuse report."""

    original_work: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

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
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    tele: str
    """Text not exceeding 20 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    title: str
    """Text not exceeding 255 characters"""

    trademark_number: str
    """Text not exceeding 1000 characters"""

    trademark_office: str
    """Text not exceeding 1000 characters"""

    trademark_symbol: str
    """Text not exceeding 1000 characters"""

    urls: str
    """A list of valid URLs separated by ‘ ’ (new line character).

    The list of the URLs should not exceed 250 URLs. All URLs should have the same
    hostname. Each URL should be unique. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
    """


class AbuseReportsChildrenAbuseReport(TypedDict, total=False):
    account_id: Required[str]

    host_notification: Required[Literal["send", "send-anon", "none"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    justification: Required[str]
    """
    A detailed description of the infringement, including any necessary access
    details and the exact steps needed to view the content, not exceeding 5000
    characters
    """

    ncmec_notification: Required[Literal["send", "send-anon", "none"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    owner_notification: Required[Literal["send", "send-anon", "none"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    act: Literal[
        "abuse_dmca",
        "abuse_trademark",
        "abuse_general",
        "abuse_phishing",
        "abuse_children",
        "abuse_threat",
        "abuse_registrar_whois",
        "abuse_ncsei",
    ]
    """The abuse report type"""

    address1: str
    """Text not exceeding 100 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    agent_name: str
    """The name of the copyright holder.

    Text not exceeding 60 characters. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
    """

    agree: Literal[0, 1]
    """Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports"""

    city: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    comments: str
    """Any additional comments about the infringement not exceeding 2000 characters"""

    company: str
    """Text not exceeding 100 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    country: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    destination_ips: str
    """A list of IP addresses separated by ‘ ’ (new line character).

    The list of destination IPs should not exceed 30 IP addresses. Each one of the
    IP addresses ought to be unique
    """

    email: str
    """A valid email of the abuse reporter.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    email2: str
    """Should match the value provided in `email`"""

    name: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    ncsei_subject_representation: bool
    """If the submitter is the target of NCSEI in the URLs of the abuse report."""

    original_work: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

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
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    tele: str
    """Text not exceeding 20 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    title: str
    """Text not exceeding 255 characters"""

    trademark_number: str
    """Text not exceeding 1000 characters"""

    trademark_office: str
    """Text not exceeding 1000 characters"""

    trademark_symbol: str
    """Text not exceeding 1000 characters"""

    urls: str
    """A list of valid URLs separated by ‘ ’ (new line character).

    The list of the URLs should not exceed 250 URLs. All URLs should have the same
    hostname. Each URL should be unique. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
    """


class AbuseReportsThreatReport(TypedDict, total=False):
    account_id: Required[str]

    host_notification: Required[Literal["send", "send-anon", "none"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    justification: Required[str]
    """
    A detailed description of the infringement, including any necessary access
    details and the exact steps needed to view the content, not exceeding 5000
    characters
    """

    owner_notification: Required[Literal["send", "send-anon", "none"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    act: Literal[
        "abuse_dmca",
        "abuse_trademark",
        "abuse_general",
        "abuse_phishing",
        "abuse_children",
        "abuse_threat",
        "abuse_registrar_whois",
        "abuse_ncsei",
    ]
    """The abuse report type"""

    address1: str
    """Text not exceeding 100 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    agent_name: str
    """The name of the copyright holder.

    Text not exceeding 60 characters. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
    """

    agree: Literal[0, 1]
    """Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports"""

    city: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    comments: str
    """Any additional comments about the infringement not exceeding 2000 characters"""

    company: str
    """Text not exceeding 100 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    country: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    destination_ips: str
    """A list of IP addresses separated by ‘ ’ (new line character).

    The list of destination IPs should not exceed 30 IP addresses. Each one of the
    IP addresses ought to be unique
    """

    email: str
    """A valid email of the abuse reporter.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    email2: str
    """Should match the value provided in `email`"""

    name: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    ncmec_notification: Literal["send", "send-anon", "none"]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    ncsei_subject_representation: bool
    """If the submitter is the target of NCSEI in the URLs of the abuse report."""

    original_work: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

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
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    tele: str
    """Text not exceeding 20 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    title: str
    """Text not exceeding 255 characters"""

    trademark_number: str
    """Text not exceeding 1000 characters"""

    trademark_office: str
    """Text not exceeding 1000 characters"""

    trademark_symbol: str
    """Text not exceeding 1000 characters"""

    urls: str
    """A list of valid URLs separated by ‘ ’ (new line character).

    The list of the URLs should not exceed 250 URLs. All URLs should have the same
    hostname. Each URL should be unique. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
    """


class AbuseReportsRegistrarWhoisReport(TypedDict, total=False):
    account_id: Required[str]

    owner_notification: Required[Literal["send", "send-anon", "none"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    act: Literal[
        "abuse_dmca",
        "abuse_trademark",
        "abuse_general",
        "abuse_phishing",
        "abuse_children",
        "abuse_threat",
        "abuse_registrar_whois",
        "abuse_ncsei",
    ]
    """The abuse report type"""

    address1: str
    """Text not exceeding 100 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    agent_name: str
    """The name of the copyright holder.

    Text not exceeding 60 characters. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
    """

    agree: Literal[0, 1]
    """Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports"""

    city: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    comments: str
    """Any additional comments about the infringement not exceeding 2000 characters"""

    company: str
    """Text not exceeding 100 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    country: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    destination_ips: str
    """A list of IP addresses separated by ‘ ’ (new line character).

    The list of destination IPs should not exceed 30 IP addresses. Each one of the
    IP addresses ought to be unique
    """

    email: str
    """A valid email of the abuse reporter.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    email2: str
    """Should match the value provided in `email`"""

    host_notification: Literal["send", "send-anon", "none"]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    justification: str
    """
    A detailed description of the infringement, including any necessary access
    details and the exact steps needed to view the content, not exceeding 5000
    characters
    """

    name: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    ncmec_notification: Literal["send", "send-anon", "none"]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    ncsei_subject_representation: bool
    """If the submitter is the target of NCSEI in the URLs of the abuse report."""

    original_work: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

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
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    tele: str
    """Text not exceeding 20 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    title: str
    """Text not exceeding 255 characters"""

    trademark_number: str
    """Text not exceeding 1000 characters"""

    trademark_office: str
    """Text not exceeding 1000 characters"""

    trademark_symbol: str
    """Text not exceeding 1000 characters"""

    urls: str
    """A list of valid URLs separated by ‘ ’ (new line character).

    The list of the URLs should not exceed 250 URLs. All URLs should have the same
    hostname. Each URL should be unique. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
    """


class AbuseReportsNcseiReport(TypedDict, total=False):
    account_id: Required[str]

    host_notification: Required[Literal["send", "send-anon", "none"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    ncsei_subject_representation: Required[bool]
    """If the submitter is the target of NCSEI in the URLs of the abuse report."""

    owner_notification: Required[Literal["send", "send-anon", "none"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    act: Literal[
        "abuse_dmca",
        "abuse_trademark",
        "abuse_general",
        "abuse_phishing",
        "abuse_children",
        "abuse_threat",
        "abuse_registrar_whois",
        "abuse_ncsei",
    ]
    """The abuse report type"""

    address1: str
    """Text not exceeding 100 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    agent_name: str
    """The name of the copyright holder.

    Text not exceeding 60 characters. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
    """

    agree: Literal[0, 1]
    """Can be `0` for false or `1` for true. Must be value: 1 for DMCA reports"""

    city: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    comments: str
    """Any additional comments about the infringement not exceeding 2000 characters"""

    company: str
    """Text not exceeding 100 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    country: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    destination_ips: str
    """A list of IP addresses separated by ‘ ’ (new line character).

    The list of destination IPs should not exceed 30 IP addresses. Each one of the
    IP addresses ought to be unique
    """

    email: str
    """A valid email of the abuse reporter.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    email2: str
    """Should match the value provided in `email`"""

    justification: str
    """
    A detailed description of the infringement, including any necessary access
    details and the exact steps needed to view the content, not exceeding 5000
    characters
    """

    name: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    ncmec_notification: Literal["send", "send-anon", "none"]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    original_work: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

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
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    tele: str
    """Text not exceeding 20 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    title: str
    """Text not exceeding 255 characters"""

    trademark_number: str
    """Text not exceeding 1000 characters"""

    trademark_office: str
    """Text not exceeding 1000 characters"""

    trademark_symbol: str
    """Text not exceeding 1000 characters"""

    urls: str
    """A list of valid URLs separated by ‘ ’ (new line character).

    The list of the URLs should not exceed 250 URLs. All URLs should have the same
    hostname. Each URL should be unique. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
    """


AbuseReportCreateParams: TypeAlias = Union[
    AbuseReportsDmcaReport,
    AbuseReportsTrademarkReport,
    AbuseReportsGeneralReport,
    AbuseReportsPhishingReport,
    AbuseReportsChildrenAbuseReport,
    AbuseReportsThreatReport,
    AbuseReportsRegistrarWhoisReport,
    AbuseReportsNcseiReport,
]
