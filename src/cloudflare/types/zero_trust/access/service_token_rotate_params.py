# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ServiceTokenRotateParams"]


class ServiceTokenRotateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    previous_client_secret_expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The expiration of the previous `client_secret`.

    If not provided, it defaults to the current timestamp in order to immediately
    expire the previous secret.
    """
