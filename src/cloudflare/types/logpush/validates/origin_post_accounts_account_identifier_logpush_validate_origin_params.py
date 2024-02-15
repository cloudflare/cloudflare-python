# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["OriginPostAccountsAccountIdentifierLogpushValidateOriginParams"]


class OriginPostAccountsAccountIdentifierLogpushValidateOriginParams(TypedDict, total=False):
    account_or_zone: Required[str]

    logpull_options: Required[Optional[str]]
    """This field is deprecated.

    Use `output_options` instead. Configuration string. It specifies things like
    requested fields and timestamp formats. If migrating from the logpull api, copy
    the url (full url or just the query string) of your call here, and logpush will
    keep on making this call for you, setting start and end times appropriately.
    """
