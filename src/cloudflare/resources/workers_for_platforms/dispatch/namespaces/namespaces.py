# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from .scripts import (
    Scripts,
    AsyncScripts,
    ScriptsWithRawResponse,
    AsyncScriptsWithRawResponse,
    ScriptsWithStreamingResponse,
    AsyncScriptsWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .scripts.scripts import Scripts, AsyncScripts
from ....._base_client import (
    make_request_options,
)
from .....types.workers_for_platforms.dispatch import (
    NamespaceGetResponse,
    NamespaceListResponse,
    NamespaceCreateResponse,
    namespace_create_params,
)

__all__ = ["Namespaces", "AsyncNamespaces"]


class Namespaces(SyncAPIResource):
    @cached_property
    def scripts(self) -> Scripts:
        return Scripts(self._client)

    @cached_property
    def with_raw_response(self) -> NamespacesWithRawResponse:
        return NamespacesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NamespacesWithStreamingResponse:
        return NamespacesWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NamespaceCreateResponse:
        """
        Create a new Workers for Platforms namespace.

        Args:
          account_id: Identifier

          name: The name of the dispatch namespace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/workers/dispatch/namespaces",
            body=maybe_transform({"name": name}, namespace_create_params.NamespaceCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[NamespaceCreateResponse], ResultWrapper[NamespaceCreateResponse]),
        )

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
    ) -> NamespaceListResponse:
        """
        Fetch a list of Workers for Platforms namespaces.

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
            f"/accounts/{account_id}/workers/dispatch/namespaces",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[NamespaceListResponse], ResultWrapper[NamespaceListResponse]),
        )

    def delete(
        self,
        dispatch_namespace: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete a Workers for Platforms namespace.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dispatch_namespace:
            raise ValueError(f"Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}")
        return self._delete(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def get(
        self,
        dispatch_namespace: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NamespaceGetResponse:
        """
        Fetch a Workers for Platforms namespace.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dispatch_namespace:
            raise ValueError(f"Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}")
        return self._get(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[NamespaceGetResponse], ResultWrapper[NamespaceGetResponse]),
        )


class AsyncNamespaces(AsyncAPIResource):
    @cached_property
    def scripts(self) -> AsyncScripts:
        return AsyncScripts(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNamespacesWithRawResponse:
        return AsyncNamespacesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNamespacesWithStreamingResponse:
        return AsyncNamespacesWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NamespaceCreateResponse:
        """
        Create a new Workers for Platforms namespace.

        Args:
          account_id: Identifier

          name: The name of the dispatch namespace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/workers/dispatch/namespaces",
            body=await async_maybe_transform({"name": name}, namespace_create_params.NamespaceCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[NamespaceCreateResponse], ResultWrapper[NamespaceCreateResponse]),
        )

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
    ) -> NamespaceListResponse:
        """
        Fetch a list of Workers for Platforms namespaces.

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
            f"/accounts/{account_id}/workers/dispatch/namespaces",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[NamespaceListResponse], ResultWrapper[NamespaceListResponse]),
        )

    async def delete(
        self,
        dispatch_namespace: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Delete a Workers for Platforms namespace.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dispatch_namespace:
            raise ValueError(f"Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}")
        return await self._delete(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def get(
        self,
        dispatch_namespace: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NamespaceGetResponse:
        """
        Fetch a Workers for Platforms namespace.

        Args:
          account_id: Identifier

          dispatch_namespace: Name of the Workers for Platforms dispatch namespace.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dispatch_namespace:
            raise ValueError(f"Expected a non-empty value for `dispatch_namespace` but received {dispatch_namespace!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[NamespaceGetResponse], ResultWrapper[NamespaceGetResponse]),
        )


class NamespacesWithRawResponse:
    def __init__(self, namespaces: Namespaces) -> None:
        self._namespaces = namespaces

        self.create = to_raw_response_wrapper(
            namespaces.create,
        )
        self.list = to_raw_response_wrapper(
            namespaces.list,
        )
        self.delete = to_raw_response_wrapper(
            namespaces.delete,
        )
        self.get = to_raw_response_wrapper(
            namespaces.get,
        )

    @cached_property
    def scripts(self) -> ScriptsWithRawResponse:
        return ScriptsWithRawResponse(self._namespaces.scripts)


class AsyncNamespacesWithRawResponse:
    def __init__(self, namespaces: AsyncNamespaces) -> None:
        self._namespaces = namespaces

        self.create = async_to_raw_response_wrapper(
            namespaces.create,
        )
        self.list = async_to_raw_response_wrapper(
            namespaces.list,
        )
        self.delete = async_to_raw_response_wrapper(
            namespaces.delete,
        )
        self.get = async_to_raw_response_wrapper(
            namespaces.get,
        )

    @cached_property
    def scripts(self) -> AsyncScriptsWithRawResponse:
        return AsyncScriptsWithRawResponse(self._namespaces.scripts)


class NamespacesWithStreamingResponse:
    def __init__(self, namespaces: Namespaces) -> None:
        self._namespaces = namespaces

        self.create = to_streamed_response_wrapper(
            namespaces.create,
        )
        self.list = to_streamed_response_wrapper(
            namespaces.list,
        )
        self.delete = to_streamed_response_wrapper(
            namespaces.delete,
        )
        self.get = to_streamed_response_wrapper(
            namespaces.get,
        )

    @cached_property
    def scripts(self) -> ScriptsWithStreamingResponse:
        return ScriptsWithStreamingResponse(self._namespaces.scripts)


class AsyncNamespacesWithStreamingResponse:
    def __init__(self, namespaces: AsyncNamespaces) -> None:
        self._namespaces = namespaces

        self.create = async_to_streamed_response_wrapper(
            namespaces.create,
        )
        self.list = async_to_streamed_response_wrapper(
            namespaces.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            namespaces.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            namespaces.get,
        )

    @cached_property
    def scripts(self) -> AsyncScriptsWithStreamingResponse:
        return AsyncScriptsWithStreamingResponse(self._namespaces.scripts)
