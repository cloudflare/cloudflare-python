# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .uuid import (
    UUIDResource,
    AsyncUUIDResource,
    UUIDResourceWithRawResponse,
    AsyncUUIDResourceWithRawResponse,
    UUIDResourceWithStreamingResponse,
    AsyncUUIDResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DCVDelegationResource", "AsyncDCVDelegationResource"]


class DCVDelegationResource(SyncAPIResource):
    @cached_property
    def uuid(self) -> UUIDResource:
        return UUIDResource(self._client)

    @cached_property
    def with_raw_response(self) -> DCVDelegationResourceWithRawResponse:
        return DCVDelegationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DCVDelegationResourceWithStreamingResponse:
        return DCVDelegationResourceWithStreamingResponse(self)


class AsyncDCVDelegationResource(AsyncAPIResource):
    @cached_property
    def uuid(self) -> AsyncUUIDResource:
        return AsyncUUIDResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDCVDelegationResourceWithRawResponse:
        return AsyncDCVDelegationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDCVDelegationResourceWithStreamingResponse:
        return AsyncDCVDelegationResourceWithStreamingResponse(self)


class DCVDelegationResourceWithRawResponse:
    def __init__(self, dcv_delegation: DCVDelegationResource) -> None:
        self._dcv_delegation = dcv_delegation

    @cached_property
    def uuid(self) -> UUIDResourceWithRawResponse:
        return UUIDResourceWithRawResponse(self._dcv_delegation.uuid)


class AsyncDCVDelegationResourceWithRawResponse:
    def __init__(self, dcv_delegation: AsyncDCVDelegationResource) -> None:
        self._dcv_delegation = dcv_delegation

    @cached_property
    def uuid(self) -> AsyncUUIDResourceWithRawResponse:
        return AsyncUUIDResourceWithRawResponse(self._dcv_delegation.uuid)


class DCVDelegationResourceWithStreamingResponse:
    def __init__(self, dcv_delegation: DCVDelegationResource) -> None:
        self._dcv_delegation = dcv_delegation

    @cached_property
    def uuid(self) -> UUIDResourceWithStreamingResponse:
        return UUIDResourceWithStreamingResponse(self._dcv_delegation.uuid)


class AsyncDCVDelegationResourceWithStreamingResponse:
    def __init__(self, dcv_delegation: AsyncDCVDelegationResource) -> None:
        self._dcv_delegation = dcv_delegation

    @cached_property
    def uuid(self) -> AsyncUUIDResourceWithStreamingResponse:
        return AsyncUUIDResourceWithStreamingResponse(self._dcv_delegation.uuid)
