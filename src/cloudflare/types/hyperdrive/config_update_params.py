# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .configuration_param import ConfigurationParam

__all__ = ["ConfigUpdateParams", "Caching"]


class ConfigUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    name: Required[str]

    origin: Required[ConfigurationParam]

    caching: Caching


class Caching(TypedDict, total=False):
    disabled: bool
    """When set to true, disables the caching of SQL responses. (Default: false)"""

    max_age: int
    """When present, specifies max duration for which items should persist in the
    cache.

    (Default: 60)
    """

    stale_while_revalidate: int
    """
    When present, indicates the number of seconds cache may serve the response after
    it becomes stale. (Default: 15)
    """
