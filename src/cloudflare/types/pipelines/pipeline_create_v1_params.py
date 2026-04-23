# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PipelineCreateV1Params"]


class PipelineCreateV1Params(TypedDict, total=False):
    account_id: Required[str]
    """Specifies the public ID of the account."""

    name: Required[str]
    """Specifies the name of the Pipeline."""

    sql: Required[str]
    """Specifies SQL for the Pipeline processing flow."""
