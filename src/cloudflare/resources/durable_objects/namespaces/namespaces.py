# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .objects import (
    Objects,
    AsyncObjects,
    ObjectsWithRawResponse,
    AsyncObjectsWithRawResponse,
    ObjectsWithStreamingResponse,
    AsyncObjectsWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.durable_objects import NamespaceListResponse

__all__ = ["Namespaces", "AsyncNamespaces"]


class Namespaces(SyncAPIResource):
    @cached_property
    def objects(self) -> Objects:
        return Objects(self._client)

    @cached_property
    def with_raw_response(self) -> NamespacesWithRawResponse:
        return NamespacesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NamespacesWithStreamingResponse:
        return NamespacesWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[NamespaceListResponse]:
        """
        Returns the Durable Object namespaces owned by an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/workers/durable_objects/namespaces",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[NamespaceListResponse]], ResultWrapper[NamespaceListResponse]),
        )


class AsyncNamespaces(AsyncAPIResource):
    @cached_property
    def objects(self) -> AsyncObjects:
        return AsyncObjects(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNamespacesWithRawResponse:
        return AsyncNamespacesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNamespacesWithStreamingResponse:
        return AsyncNamespacesWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[NamespaceListResponse]:
        """
        Returns the Durable Object namespaces owned by an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/durable_objects/namespaces",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[NamespaceListResponse]], ResultWrapper[NamespaceListResponse]),
        )


class NamespacesWithRawResponse:
    def __init__(self, namespaces: Namespaces) -> None:
        self._namespaces = namespaces

        self.list = to_raw_response_wrapper(
            namespaces.list,
        )

    @cached_property
    def objects(self) -> ObjectsWithRawResponse:
        return ObjectsWithRawResponse(self._namespaces.objects)


class AsyncNamespacesWithRawResponse:
    def __init__(self, namespaces: AsyncNamespaces) -> None:
        self._namespaces = namespaces

        self.list = async_to_raw_response_wrapper(
            namespaces.list,
        )

    @cached_property
    def objects(self) -> AsyncObjectsWithRawResponse:
        return AsyncObjectsWithRawResponse(self._namespaces.objects)


class NamespacesWithStreamingResponse:
    def __init__(self, namespaces: Namespaces) -> None:
        self._namespaces = namespaces

        self.list = to_streamed_response_wrapper(
            namespaces.list,
        )

    @cached_property
    def objects(self) -> ObjectsWithStreamingResponse:
        return ObjectsWithStreamingResponse(self._namespaces.objects)


class AsyncNamespacesWithStreamingResponse:
    def __init__(self, namespaces: AsyncNamespaces) -> None:
        self._namespaces = namespaces

        self.list = async_to_streamed_response_wrapper(
            namespaces.list,
        )

    @cached_property
    def objects(self) -> AsyncObjectsWithStreamingResponse:
        return AsyncObjectsWithStreamingResponse(self._namespaces.objects)
