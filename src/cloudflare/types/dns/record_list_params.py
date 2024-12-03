# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..shared.sort_direction import SortDirection

__all__ = ["RecordListParams", "Comment", "Content", "Name", "Tag"]


class RecordListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    comment: Comment

    content: Content

    direction: SortDirection
    """Direction to order DNS records in."""

    match: Literal["any", "all"]
    """Whether to match all search requirements or at least one (any).

    If set to `all`, acts like a logical AND between filters. If set to `any`, acts
    like a logical OR instead. Note that the interaction between tag filters is
    controlled by the `tag-match` parameter instead.
    """

    name: Name

    order: Literal["type", "name", "content", "ttl", "proxied"]
    """Field to order DNS records by."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of DNS records per page."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    search: str
    """Allows searching in multiple properties of a DNS record simultaneously.

    This parameter is intended for human users, not automation. Its exact behavior
    is intentionally left unspecified and is subject to change in the future. This
    parameter works independently of the `match` setting. For automated searches,
    please use the other available parameters.
    """

    tag: Tag

    tag_match: Literal["any", "all"]
    """Whether to match all tag search requirements or at least one (any).

    If set to `all`, acts like a logical AND between tag filters. If set to `any`,
    acts like a logical OR instead. Note that the regular `match` parameter is still
    used to combine the resulting condition with other filters that aren't related
    to tags.
    """

    type: Literal[
        "A",
        "AAAA",
        "CAA",
        "CERT",
        "CNAME",
        "DNSKEY",
        "DS",
        "HTTPS",
        "LOC",
        "MX",
        "NAPTR",
        "NS",
        "OPENPGPKEY",
        "PTR",
        "SMIMEA",
        "SRV",
        "SSHFP",
        "SVCB",
        "TLSA",
        "TXT",
        "URI",
    ]
    """Record type."""


class Comment(TypedDict, total=False):
    absent: str
    """If this parameter is present, only records _without_ a comment are returned."""

    contains: str
    """Substring of the DNS record comment. Comment filters are case-insensitive."""

    endswith: str
    """Suffix of the DNS record comment. Comment filters are case-insensitive."""

    exact: str
    """Exact value of the DNS record comment. Comment filters are case-insensitive."""

    present: str
    """If this parameter is present, only records _with_ a comment are returned."""

    startswith: str
    """Prefix of the DNS record comment. Comment filters are case-insensitive."""


class Content(TypedDict, total=False):
    contains: str
    """Substring of the DNS record content. Content filters are case-insensitive."""

    endswith: str
    """Suffix of the DNS record content. Content filters are case-insensitive."""

    exact: str
    """Exact value of the DNS record content. Content filters are case-insensitive."""

    startswith: str
    """Prefix of the DNS record content. Content filters are case-insensitive."""


class Name(TypedDict, total=False):
    contains: str
    """Substring of the DNS record name. Name filters are case-insensitive."""

    endswith: str
    """Suffix of the DNS record name. Name filters are case-insensitive."""

    exact: str
    """Exact value of the DNS record name. Name filters are case-insensitive."""

    startswith: str
    """Prefix of the DNS record name. Name filters are case-insensitive."""


class Tag(TypedDict, total=False):
    absent: str
    """Name of a tag which must _not_ be present on the DNS record.

    Tag filters are case-insensitive.
    """

    contains: str
    """A tag and value, of the form `<tag-name>:<tag-value>`.

    The API will only return DNS records that have a tag named `<tag-name>` whose
    value contains `<tag-value>`. Tag filters are case-insensitive.
    """

    endswith: str
    """A tag and value, of the form `<tag-name>:<tag-value>`.

    The API will only return DNS records that have a tag named `<tag-name>` whose
    value ends with `<tag-value>`. Tag filters are case-insensitive.
    """

    exact: str
    """A tag and value, of the form `<tag-name>:<tag-value>`.

    The API will only return DNS records that have a tag named `<tag-name>` whose
    value is `<tag-value>`. Tag filters are case-insensitive.
    """

    present: str
    """Name of a tag which must be present on the DNS record.

    Tag filters are case-insensitive.
    """

    startswith: str
    """A tag and value, of the form `<tag-name>:<tag-value>`.

    The API will only return DNS records that have a tag named `<tag-name>` whose
    value starts with `<tag-value>`. Tag filters are case-insensitive.
    """
