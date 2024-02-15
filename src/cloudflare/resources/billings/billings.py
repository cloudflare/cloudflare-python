# File generated from our OpenAPI spec by Stainless.

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

__all__ = ["Billings", "AsyncBillings"]


class Billings(SyncAPIResource):
    @cached_property
    def profiles(self) -> Profiles:
        return Profiles(self._client)

    @cached_property
    def with_raw_response(self) -> BillingsWithRawResponse:
        return BillingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingsWithStreamingResponse:
        return BillingsWithStreamingResponse(self)


class AsyncBillings(AsyncAPIResource):
    @cached_property
    def profiles(self) -> AsyncProfiles:
        return AsyncProfiles(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBillingsWithRawResponse:
        return AsyncBillingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingsWithStreamingResponse:
        return AsyncBillingsWithStreamingResponse(self)


class BillingsWithRawResponse:
    def __init__(self, billings: Billings) -> None:
        self._billings = billings

    @cached_property
    def profiles(self) -> ProfilesWithRawResponse:
        return ProfilesWithRawResponse(self._billings.profiles)


class AsyncBillingsWithRawResponse:
    def __init__(self, billings: AsyncBillings) -> None:
        self._billings = billings

    @cached_property
    def profiles(self) -> AsyncProfilesWithRawResponse:
        return AsyncProfilesWithRawResponse(self._billings.profiles)


class BillingsWithStreamingResponse:
    def __init__(self, billings: Billings) -> None:
        self._billings = billings

    @cached_property
    def profiles(self) -> ProfilesWithStreamingResponse:
        return ProfilesWithStreamingResponse(self._billings.profiles)


class AsyncBillingsWithStreamingResponse:
    def __init__(self, billings: AsyncBillings) -> None:
        self._billings = billings

    @cached_property
    def profiles(self) -> AsyncProfilesWithStreamingResponse:
        return AsyncProfilesWithStreamingResponse(self._billings.profiles)
