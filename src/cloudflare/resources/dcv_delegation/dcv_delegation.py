# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .uuid import (
    UUID,
    AsyncUUID,
    UUIDWithRawResponse,
    AsyncUUIDWithRawResponse,
    UUIDWithStreamingResponse,
    AsyncUUIDWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DCVDelegation", "AsyncDCVDelegation"]


class DCVDelegation(SyncAPIResource):
    @cached_property
    def uuid(self) -> UUID:
        return UUID(self._client)

    @cached_property
    def with_raw_response(self) -> DCVDelegationWithRawResponse:
        return DCVDelegationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DCVDelegationWithStreamingResponse:
        return DCVDelegationWithStreamingResponse(self)


class AsyncDCVDelegation(AsyncAPIResource):
    @cached_property
    def uuid(self) -> AsyncUUID:
        return AsyncUUID(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDCVDelegationWithRawResponse:
        return AsyncDCVDelegationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDCVDelegationWithStreamingResponse:
        return AsyncDCVDelegationWithStreamingResponse(self)


class DCVDelegationWithRawResponse:
    def __init__(self, dcv_delegation: DCVDelegation) -> None:
        self._dcv_delegation = dcv_delegation

    @cached_property
    def uuid(self) -> UUIDWithRawResponse:
        return UUIDWithRawResponse(self._dcv_delegation.uuid)


class AsyncDCVDelegationWithRawResponse:
    def __init__(self, dcv_delegation: AsyncDCVDelegation) -> None:
        self._dcv_delegation = dcv_delegation

    @cached_property
    def uuid(self) -> AsyncUUIDWithRawResponse:
        return AsyncUUIDWithRawResponse(self._dcv_delegation.uuid)


class DCVDelegationWithStreamingResponse:
    def __init__(self, dcv_delegation: DCVDelegation) -> None:
        self._dcv_delegation = dcv_delegation

    @cached_property
    def uuid(self) -> UUIDWithStreamingResponse:
        return UUIDWithStreamingResponse(self._dcv_delegation.uuid)


class AsyncDCVDelegationWithStreamingResponse:
    def __init__(self, dcv_delegation: AsyncDCVDelegation) -> None:
        self._dcv_delegation = dcv_delegation

    @cached_property
    def uuid(self) -> AsyncUUIDWithStreamingResponse:
        return AsyncUUIDWithStreamingResponse(self._dcv_delegation.uuid)
