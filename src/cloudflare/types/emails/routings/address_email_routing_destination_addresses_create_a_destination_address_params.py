# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AddressEmailRoutingDestinationAddressesCreateADestinationAddressParams"]


class AddressEmailRoutingDestinationAddressesCreateADestinationAddressParams(TypedDict, total=False):
    email: Required[str]
    """The contact email address of the user."""
