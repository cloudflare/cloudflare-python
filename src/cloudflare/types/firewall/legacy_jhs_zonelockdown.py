# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "LegacyJhsZonelockdown",
    "Configurations",
    "ConfigurationsLegacyJhsSchemasIPConfiguration",
    "ConfigurationsLegacyJhsSchemasCIDRConfiguration",
]


class ConfigurationsLegacyJhsSchemasIPConfiguration(BaseModel):
    target: Optional[Literal["ip"]] = None
    """The configuration target.

    You must set the target to `ip` when specifying an IP address in the Zone
    Lockdown rule.
    """

    value: Optional[str] = None
    """The IP address to match.

    This address will be compared to the IP address of incoming requests.
    """


class ConfigurationsLegacyJhsSchemasCIDRConfiguration(BaseModel):
    target: Optional[Literal["ip_range"]] = None
    """The configuration target.

    You must set the target to `ip_range` when specifying an IP address range in the
    Zone Lockdown rule.
    """

    value: Optional[str] = None
    """The IP address range to match. You can only use prefix lengths `/16` and `/24`."""


Configurations = Union[ConfigurationsLegacyJhsSchemasIPConfiguration, ConfigurationsLegacyJhsSchemasCIDRConfiguration]


class LegacyJhsZonelockdown(BaseModel):
    id: str
    """The unique identifier of the Zone Lockdown rule."""

    configurations: Configurations
    """
    A list of IP addresses or CIDR ranges that will be allowed to access the URLs
    specified in the Zone Lockdown rule. You can include any number of `ip` or
    `ip_range` configurations.
    """

    created_on: datetime
    """The timestamp of when the rule was created."""

    description: str
    """An informative summary of the rule."""

    modified_on: datetime
    """The timestamp of when the rule was last modified."""

    paused: bool
    """When true, indicates that the rule is currently paused."""

    urls: List[str]
    """The URLs to include in the rule definition.

    You can use wildcards. Each entered URL will be escaped before use, which means
    you can only use simple wildcard patterns.
    """
