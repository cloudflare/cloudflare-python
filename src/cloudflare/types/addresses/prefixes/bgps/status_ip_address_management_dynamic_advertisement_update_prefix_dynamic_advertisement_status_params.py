# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["StatusIPAddressManagementDynamicAdvertisementUpdatePrefixDynamicAdvertisementStatusParams"]


class StatusIPAddressManagementDynamicAdvertisementUpdatePrefixDynamicAdvertisementStatusParams(TypedDict, total=False):
    account_identifier: Required[str]
    """Identifier"""

    advertised: Required[bool]
    """Enablement of prefix advertisement to the Internet."""
