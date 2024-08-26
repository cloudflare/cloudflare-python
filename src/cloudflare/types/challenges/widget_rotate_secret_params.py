# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WidgetRotateSecretParams"]


class WidgetRotateSecretParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    invalidate_immediately: bool
    """
    If `invalidate_immediately` is set to `false`, the previous secret will remain
    valid for two hours. Otherwise, the secret is immediately invalidated, and
    requests using it will be rejected.
    """
