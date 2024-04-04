# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ....types import shared_params

__all__ = ["ConfigurationEditParams"]


class ConfigurationEditParams(TypedDict, total=False):
    account_id: Required[str]

    settings: shared_params.UnnamedSchemaRef125
    """account settings."""
