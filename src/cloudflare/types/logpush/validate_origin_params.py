# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ValidateOriginParams"]


class ValidateOriginParams(TypedDict, total=False):
    account_id: Required[str]
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: Required[str]
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    logpull_options: Required[Optional[str]]
    """This field is deprecated.

    Use `output_options` instead. Configuration string. It specifies things like
    requested fields and timestamp formats. If migrating from the logpull api, copy
    the url (full url or just the query string) of your call here, and logpush will
    keep on making this call for you, setting start and end times appropriately.
    """
