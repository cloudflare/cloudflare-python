# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..configuration_param import ConfigurationParam

__all__ = ["ConfigUpdateParams"]


class ConfigUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    name: Required[object]

    origin: Required[ConfigurationParam]
