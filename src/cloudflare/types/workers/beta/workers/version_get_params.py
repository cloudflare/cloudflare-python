# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VersionGetParams"]


class VersionGetParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    worker_id: Required[str]
    """Identifier for the Worker, which can be ID or name."""

    include: Literal["modules"]
    """
    Whether to include the `modules` property of the version in the response, which
    contains code and sourcemap content and may add several megabytes to the
    response size.
    """
