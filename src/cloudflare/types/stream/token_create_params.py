# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TokenCreateParams", "AccessRule"]


class TokenCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    id: str
    """The optional ID of a Stream signing key.

    If present, the `pem` field is also required.
    """

    access_rules: Annotated[Iterable[AccessRule], PropertyInfo(alias="accessRules")]
    """The optional list of access rule constraints on the token.

    Access can be blocked or allowed based on an IP, IP range, or by country. Access
    rules are evaluated from first to last. If a rule matches, the associated action
    is applied and no further rules are evaluated.
    """

    downloadable: bool
    """
    The optional boolean value that enables using signed tokens to access MP4
    download links for a video.
    """

    exp: int
    """
    The optional unix epoch timestamp that specficies the time after a token is not
    accepted. The maximum time specification is 24 hours from issuing time. If this
    field is not set, the default is one hour after issuing.
    """

    nbf: int
    """
    The optional unix epoch timestamp that specifies the time before a the token is
    not accepted. If this field is not set, the default is one hour before issuing.
    """

    pem: str
    """
    The optional base64 encoded private key in PEM format associated with a Stream
    signing key. If present, the `id` field is also required.
    """


class AccessRule(TypedDict, total=False):
    action: Literal["allow", "block"]
    """The action to take when a request matches a rule.

    If the action is `block`, the signed token blocks views for viewers matching the
    rule.
    """

    country: List[str]
    """
    An array of 2-letter country codes in ISO 3166-1 Alpha-2 format used to match
    requests.
    """

    ip: List[str]
    """An array of IPv4 or IPV6 addresses or CIDRs used to match requests."""

    type: Literal["any", "ip.src", "ip.geoip.country"]
    """Lists available rule types to match for requests.

    An `any` type matches all requests and can be used as a wildcard to apply
    default actions after other rules.
    """
