# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .asn_configuration import ASNConfiguration
from .ipv6_configuration import IPV6Configuration
from .country_configuration import CountryConfiguration
from .access_rule_ip_configuration import AccessRuleIPConfiguration
from .access_rule_cidr_configuration import AccessRuleCIDRConfiguration

__all__ = ["AccessRuleCreateResponse", "Configuration", "Scope"]

Configuration: TypeAlias = Union[
    AccessRuleIPConfiguration, IPV6Configuration, AccessRuleCIDRConfiguration, ASNConfiguration, CountryConfiguration
]


class Scope(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    email: Optional[str] = None
    """The contact email address of the user."""

    type: Optional[Literal["user", "organization"]] = None
    """The scope of the rule."""


class AccessRuleCreateResponse(BaseModel):
    id: str
    """The unique identifier of the IP Access rule."""

    allowed_modes: List[Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"]]
    """The available actions that a rule can apply to a matched request."""

    configuration: Configuration
    """The rule configuration."""

    mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"]
    """The action to apply to a matched request."""

    created_on: Optional[datetime] = None
    """The timestamp of when the rule was created."""

    modified_on: Optional[datetime] = None
    """The timestamp of when the rule was last modified."""

    notes: Optional[str] = None
    """
    An informative summary of the rule, typically used as a reminder or explanation.
    """

    scope: Optional[Scope] = None
    """All zones owned by the user will have the rule applied."""
