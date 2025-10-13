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
    "AbuseReportsCsamReport",
    "AbuseReportsThreatReport",
    "AbuseReportsRegistrarWhoisReport",
    "AbuseReportsNcseiReport",
]


class AbuseReportsDmcaReport(TypedDict, total=False):
    account_id: Required[str]

    act: Required[Literal["abuse_dmca"]]
    """The abuse report type."""

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

    agree: Required[Literal[1]]
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

    email: Required[str]
    """A valid email of the abuse reporter.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    email2: Required[str]
    """Should match the value provided in `email`"""

    host_notification: Required[Literal["send"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    name: Required[str]
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    original_work: Required[str]
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    owner_notification: Required[Literal["send"]]
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

    urls: Required[str]
    """A list of valid URLs separated by ‘\n’ (new line character).

    The list of the URLs should not exceed 250 URLs. All URLs should have the same
    hostname. Each URL should be unique. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
    """

    comments: str
    """Any additional comments about the infringement not exceeding 2000 characters"""

    company: str
    """Text not exceeding 100 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    reported_country: str
    """Text containing 2 characters"""

    reported_user_agent: str
    """Text not exceeding 255 characters"""

    tele: str
    """Text not exceeding 20 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    title: str
    """Text not exceeding 255 characters"""


class AbuseReportsTrademarkReport(TypedDict, total=False):
    account_id: Required[str]

    act: Required[Literal["abuse_trademark"]]
    """The abuse report type."""

    email: Required[str]
    """A valid email of the abuse reporter.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    email2: Required[str]
    """Should match the value provided in `email`"""

    host_notification: Required[Literal["send"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    justification: Required[str]
    """
    A detailed description of the infringement, including any necessary access
    details and the exact steps needed to view the content, not exceeding 5000
    characters.
    """

    name: Required[str]
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    owner_notification: Required[Literal["send"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    trademark_number: Required[str]
    """Text not exceeding 1000 characters"""

    trademark_office: Required[str]
    """Text not exceeding 1000 characters"""

    trademark_symbol: Required[str]
    """Text not exceeding 1000 characters"""

    urls: Required[str]
    """A list of valid URLs separated by ‘\n’ (new line character).

    The list of the URLs should not exceed 250 URLs. All URLs should have the same
    hostname. Each URL should be unique. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
    """

    comments: str
    """Any additional comments about the infringement not exceeding 2000 characters"""

    company: str
    """Text not exceeding 100 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    reported_country: str
    """Text containing 2 characters"""

    reported_user_agent: str
    """Text not exceeding 255 characters"""

    tele: str
    """Text not exceeding 20 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    title: str
    """Text not exceeding 255 characters"""


class AbuseReportsGeneralReport(TypedDict, total=False):
    account_id: Required[str]

    act: Required[Literal["abuse_general"]]
    """The abuse report type."""

    email: Required[str]
    """A valid email of the abuse reporter.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    email2: Required[str]
    """Should match the value provided in `email`"""

    host_notification: Required[Literal["send", "send-anon"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    justification: Required[str]
    """
    A detailed description of the infringement, including any necessary access
    details and the exact steps needed to view the content, not exceeding 5000
    characters.
    """

    name: Required[str]
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    owner_notification: Required[Literal["send", "send-anon", "none"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    urls: Required[str]
    """A list of valid URLs separated by ‘\n’ (new line character).

    The list of the URLs should not exceed 250 URLs. All URLs should have the same
    hostname. Each URL should be unique. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
    """

    comments: str
    """Any additional comments about the infringement not exceeding 2000 characters"""

    company: str
    """Text not exceeding 100 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    destination_ips: str
    """A list of IP addresses separated by ‘\n’ (new line character).

    The list of destination IPs should not exceed 30 IP addresses. Each one of the
    IP addresses ought to be unique.
    """

    ports_protocols: str
    """A comma separated list of ports and protocols e.g.

    80/TCP, 22/UDP. The total size of the field should not exceed 2000 characters.
    Each individual port/protocol should not exceed 100 characters. The list should
    not have more than 30 unique ports and protocols.
    """

    reported_country: str
    """Text containing 2 characters"""

    reported_user_agent: str
    """Text not exceeding 255 characters"""

    source_ips: str
    """A list of IP addresses separated by ‘\n’ (new line character).

    The list of source IPs should not exceed 30 IP addresses. Each one of the IP
    addresses ought to be unique.
    """

    tele: str
    """Text not exceeding 20 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    title: str
    """Text not exceeding 255 characters"""


class AbuseReportsPhishingReport(TypedDict, total=False):
    account_id: Required[str]

    act: Required[Literal["abuse_phishing"]]
    """The abuse report type."""

    email: Required[str]
    """A valid email of the abuse reporter.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    email2: Required[str]
    """Should match the value provided in `email`"""

    host_notification: Required[Literal["send", "send-anon"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    justification: Required[str]
    """
    A detailed description of the infringement, including any necessary access
    details and the exact steps needed to view the content, not exceeding 5000
    characters.
    """

    name: Required[str]
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    owner_notification: Required[Literal["send", "send-anon"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    urls: Required[str]
    """A list of valid URLs separated by ‘\n’ (new line character).

    The list of the URLs should not exceed 250 URLs. All URLs should have the same
    hostname. Each URL should be unique. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
    """

    comments: str
    """Any additional comments about the infringement not exceeding 2000 characters"""

    company: str
    """Text not exceeding 100 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    original_work: str
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    reported_country: str
    """Text containing 2 characters"""

    reported_user_agent: str
    """Text not exceeding 255 characters"""

    tele: str
    """Text not exceeding 20 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    title: str
    """Text not exceeding 255 characters"""


class AbuseReportsCsamReport(TypedDict, total=False):
    account_id: Required[str]

    act: Required[Literal["abuse_children"]]
    """The abuse report type."""

    email: Required[str]
    """A valid email of the abuse reporter.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    email2: Required[str]
    """Should match the value provided in `email`"""

    host_notification: Required[Literal["send", "send-anon"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    justification: Required[str]
    """
    A detailed description of the infringement, including any necessary access
    details and the exact steps needed to view the content, not exceeding 5000
    characters.
    """

    name: Required[str]
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    ncmec_notification: Required[Literal["send", "send-anon"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    owner_notification: Required[Literal["send", "send-anon", "none"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    urls: Required[str]
    """A list of valid URLs separated by ‘\n’ (new line character).

    The list of the URLs should not exceed 250 URLs. All URLs should have the same
    hostname. Each URL should be unique. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
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

    reported_country: str
    """Text containing 2 characters"""

    reported_user_agent: str
    """Text not exceeding 255 characters"""

    tele: str
    """Text not exceeding 20 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    title: str
    """Text not exceeding 255 characters"""


class AbuseReportsThreatReport(TypedDict, total=False):
    account_id: Required[str]

    act: Required[Literal["abuse_threat"]]
    """The abuse report type."""

    email: Required[str]
    """A valid email of the abuse reporter.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    email2: Required[str]
    """Should match the value provided in `email`"""

    host_notification: Required[Literal["send", "send-anon"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    justification: Required[str]
    """
    A detailed description of the infringement, including any necessary access
    details and the exact steps needed to view the content, not exceeding 5000
    characters.
    """

    name: Required[str]
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    owner_notification: Required[Literal["send", "send-anon"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    urls: Required[str]
    """A list of valid URLs separated by ‘\n’ (new line character).

    The list of the URLs should not exceed 250 URLs. All URLs should have the same
    hostname. Each URL should be unique. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
    """

    comments: str
    """Any additional comments about the infringement not exceeding 2000 characters"""

    company: str
    """Text not exceeding 100 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    reported_country: str
    """Text containing 2 characters"""

    reported_user_agent: str
    """Text not exceeding 255 characters"""

    tele: str
    """Text not exceeding 20 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    title: str
    """Text not exceeding 255 characters"""


class AbuseReportsRegistrarWhoisReport(TypedDict, total=False):
    account_id: Required[str]

    act: Required[Literal["abuse_registrar_whois"]]
    """The abuse report type."""

    email: Required[str]
    """A valid email of the abuse reporter.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    email2: Required[str]
    """Should match the value provided in `email`"""

    name: Required[str]
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    owner_notification: Required[Literal["send", "send-anon", "none"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    urls: Required[str]
    """A list of valid URLs separated by ‘\n’ (new line character).

    The list of the URLs should not exceed 250 URLs. All URLs should have the same
    hostname. Each URL should be unique. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
    """

    comments: str
    """Any additional comments about the infringement not exceeding 2000 characters"""

    company: str
    """Text not exceeding 100 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    reported_country: str
    """Text containing 2 characters"""

    reported_user_agent: str
    """Text not exceeding 255 characters"""

    tele: str
    """Text not exceeding 20 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    title: str
    """Text not exceeding 255 characters"""


class AbuseReportsNcseiReport(TypedDict, total=False):
    account_id: Required[str]

    act: Required[Literal["abuse_ncsei"]]
    """The abuse report type."""

    email: Required[str]
    """A valid email of the abuse reporter.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    email2: Required[str]
    """Should match the value provided in `email`"""

    host_notification: Required[Literal["send", "send-anon"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    name: Required[str]
    """Text not exceeding 255 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    ncsei_subject_representation: Required[bool]
    """If the submitter is the target of NCSEI in the URLs of the abuse report."""

    owner_notification: Required[Literal["send", "send-anon", "none"]]
    """Notification type based on the abuse type.

    NOTE: Copyright (DMCA) and Trademark reports cannot be anonymous.
    """

    urls: Required[str]
    """A list of valid URLs separated by ‘\n’ (new line character).

    The list of the URLs should not exceed 250 URLs. All URLs should have the same
    hostname. Each URL should be unique. This field may be released by Cloudflare to
    third parties such as the Lumen Database (https://lumendatabase.org/).
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

    reported_country: str
    """Text containing 2 characters"""

    reported_user_agent: str
    """Text not exceeding 255 characters"""

    tele: str
    """Text not exceeding 20 characters.

    This field may be released by Cloudflare to third parties such as the Lumen
    Database (https://lumendatabase.org/).
    """

    title: str
    """Text not exceeding 255 characters"""


AbuseReportCreateParams: TypeAlias = Union[
    AbuseReportsDmcaReport,
    AbuseReportsTrademarkReport,
    AbuseReportsGeneralReport,
    AbuseReportsPhishingReport,
    AbuseReportsCsamReport,
    AbuseReportsThreatReport,
    AbuseReportsRegistrarWhoisReport,
    AbuseReportsNcseiReport,
]
