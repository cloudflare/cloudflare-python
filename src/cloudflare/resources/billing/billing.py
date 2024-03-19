# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .profiles import (
    Profiles,
    AsyncProfiles,
    ProfilesWithRawResponse,
    AsyncProfilesWithRawResponse,
    ProfilesWithStreamingResponse,
    AsyncProfilesWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Billing", "AsyncBilling"]


class Billing(SyncAPIResource):
    @cached_property
    def profiles(self) -> Profiles:
        return Profiles(self._client)

    @cached_property
    def with_raw_response(self) -> BillingWithRawResponse:
        return BillingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingWithStreamingResponse:
        return BillingWithStreamingResponse(self)


class AsyncBilling(AsyncAPIResource):
    @cached_property
    def profiles(self) -> AsyncProfiles:
        return AsyncProfiles(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBillingWithRawResponse:
        return AsyncBillingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingWithStreamingResponse:
        return AsyncBillingWithStreamingResponse(self)


class BillingWithRawResponse:
    def __init__(self, billing: Billing) -> None:
        self._billing = billing

    @cached_property
    def profiles(self) -> ProfilesWithRawResponse:
        return ProfilesWithRawResponse(self._billing.profiles)


class AsyncBillingWithRawResponse:
    def __init__(self, billing: AsyncBilling) -> None:
        self._billing = billing

    @cached_property
    def profiles(self) -> AsyncProfilesWithRawResponse:
        return AsyncProfilesWithRawResponse(self._billing.profiles)


class BillingWithStreamingResponse:
    def __init__(self, billing: Billing) -> None:
        self._billing = billing

    @cached_property
    def profiles(self) -> ProfilesWithStreamingResponse:
        return ProfilesWithStreamingResponse(self._billing.profiles)


class AsyncBillingWithStreamingResponse:
    def __init__(self, billing: AsyncBilling) -> None:
        self._billing = billing

    @cached_property
    def profiles(self) -> AsyncProfilesWithStreamingResponse:
        return AsyncProfilesWithStreamingResponse(self._billing.profiles)
