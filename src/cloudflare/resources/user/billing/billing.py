# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .history import (
    History,
    AsyncHistory,
    HistoryWithRawResponse,
    AsyncHistoryWithRawResponse,
    HistoryWithStreamingResponse,
    AsyncHistoryWithStreamingResponse,
)
from .profile import (
    Profile,
    AsyncProfile,
    ProfileWithRawResponse,
    AsyncProfileWithRawResponse,
    ProfileWithStreamingResponse,
    AsyncProfileWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Billing", "AsyncBilling"]


class Billing(SyncAPIResource):
    @cached_property
    def history(self) -> History:
        return History(self._client)

    @cached_property
    def profile(self) -> Profile:
        return Profile(self._client)

    @cached_property
    def with_raw_response(self) -> BillingWithRawResponse:
        return BillingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingWithStreamingResponse:
        return BillingWithStreamingResponse(self)


class AsyncBilling(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistory:
        return AsyncHistory(self._client)

    @cached_property
    def profile(self) -> AsyncProfile:
        return AsyncProfile(self._client)

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
    def history(self) -> HistoryWithRawResponse:
        return HistoryWithRawResponse(self._billing.history)

    @cached_property
    def profile(self) -> ProfileWithRawResponse:
        return ProfileWithRawResponse(self._billing.profile)


class AsyncBillingWithRawResponse:
    def __init__(self, billing: AsyncBilling) -> None:
        self._billing = billing

    @cached_property
    def history(self) -> AsyncHistoryWithRawResponse:
        return AsyncHistoryWithRawResponse(self._billing.history)

    @cached_property
    def profile(self) -> AsyncProfileWithRawResponse:
        return AsyncProfileWithRawResponse(self._billing.profile)


class BillingWithStreamingResponse:
    def __init__(self, billing: Billing) -> None:
        self._billing = billing

    @cached_property
    def history(self) -> HistoryWithStreamingResponse:
        return HistoryWithStreamingResponse(self._billing.history)

    @cached_property
    def profile(self) -> ProfileWithStreamingResponse:
        return ProfileWithStreamingResponse(self._billing.profile)


class AsyncBillingWithStreamingResponse:
    def __init__(self, billing: AsyncBilling) -> None:
        self._billing = billing

    @cached_property
    def history(self) -> AsyncHistoryWithStreamingResponse:
        return AsyncHistoryWithStreamingResponse(self._billing.history)

    @cached_property
    def profile(self) -> AsyncProfileWithStreamingResponse:
        return AsyncProfileWithStreamingResponse(self._billing.profile)
