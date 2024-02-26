# File generated from our OpenAPI spec by Stainless.

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

__all__ = ["DcvDelegation", "AsyncDcvDelegation"]


class DcvDelegation(SyncAPIResource):
    @cached_property
    def uuid(self) -> UUID:
        return UUID(self._client)

    @cached_property
    def with_raw_response(self) -> DcvDelegationWithRawResponse:
        return DcvDelegationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DcvDelegationWithStreamingResponse:
        return DcvDelegationWithStreamingResponse(self)


class AsyncDcvDelegation(AsyncAPIResource):
    @cached_property
    def uuid(self) -> AsyncUUID:
        return AsyncUUID(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDcvDelegationWithRawResponse:
        return AsyncDcvDelegationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDcvDelegationWithStreamingResponse:
        return AsyncDcvDelegationWithStreamingResponse(self)


class DcvDelegationWithRawResponse:
    def __init__(self, dcv_delegation: DcvDelegation) -> None:
        self._dcv_delegation = dcv_delegation

    @cached_property
    def uuid(self) -> UUIDWithRawResponse:
        return UUIDWithRawResponse(self._dcv_delegation.uuid)


class AsyncDcvDelegationWithRawResponse:
    def __init__(self, dcv_delegation: AsyncDcvDelegation) -> None:
        self._dcv_delegation = dcv_delegation

    @cached_property
    def uuid(self) -> AsyncUUIDWithRawResponse:
        return AsyncUUIDWithRawResponse(self._dcv_delegation.uuid)


class DcvDelegationWithStreamingResponse:
    def __init__(self, dcv_delegation: DcvDelegation) -> None:
        self._dcv_delegation = dcv_delegation

    @cached_property
    def uuid(self) -> UUIDWithStreamingResponse:
        return UUIDWithStreamingResponse(self._dcv_delegation.uuid)


class AsyncDcvDelegationWithStreamingResponse:
    def __init__(self, dcv_delegation: AsyncDcvDelegation) -> None:
        self._dcv_delegation = dcv_delegation

    @cached_property
    def uuid(self) -> AsyncUUIDWithStreamingResponse:
        return AsyncUUIDWithStreamingResponse(self._dcv_delegation.uuid)
