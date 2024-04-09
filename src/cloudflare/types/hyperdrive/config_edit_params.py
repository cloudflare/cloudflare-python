# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..configuration_param import ConfigurationParam

__all__ = ["ConfigEditParams"]


class ConfigEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    origin: ConfigurationParam
