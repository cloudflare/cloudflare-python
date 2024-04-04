# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .unnamed_schema_ref_055aaf3918bf29f81c09d394a864182e_param import (
    UnnamedSchemaRef055aaf3918bf29f81c09d394a864182eParam,
)

__all__ = ["ConfigurationEditParams"]


class ConfigurationEditParams(TypedDict, total=False):
    account_id: Required[str]

    settings: UnnamedSchemaRef055aaf3918bf29f81c09d394a864182eParam
    """account settings."""
