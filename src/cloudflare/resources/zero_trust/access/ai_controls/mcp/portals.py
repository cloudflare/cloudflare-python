# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast

import httpx

from ......_types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ......_utils import maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_wrappers import ResultWrapper
from ......pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ......_base_client import AsyncPaginator, make_request_options
from ......types.zero_trust.access.ai_controls.mcp import portal_list_params, portal_create_params, portal_update_params
from ......types.zero_trust.access.ai_controls.mcp.portal_list_response import PortalListResponse
from ......types.zero_trust.access.ai_controls.mcp.portal_read_response import PortalReadResponse
from ......types.zero_trust.access.ai_controls.mcp.portal_create_response import PortalCreateResponse
from ......types.zero_trust.access.ai_controls.mcp.portal_delete_response import PortalDeleteResponse
from ......types.zero_trust.access.ai_controls.mcp.portal_update_response import PortalUpdateResponse

__all__ = ["PortalsResource", "AsyncPortalsResource"]


class PortalsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PortalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PortalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PortalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PortalsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        id: str,
        hostname: str,
        name: str,
        description: str | Omit = omit,
        servers: Iterable[portal_create_params.Server] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalCreateResponse:
        """
        Create a new MCP Portal

        Args:
          id: portal id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/access/ai-controls/mcp/portals",
            body=maybe_transform(
                {
                    "id": id,
                    "hostname": hostname,
                    "name": name,
                    "description": description,
                    "servers": servers,
                },
                portal_create_params.PortalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PortalCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[PortalCreateResponse], ResultWrapper[PortalCreateResponse]),
        )

    def update(
        self,
        id: str,
        *,
        account_id: str,
        description: str | Omit = omit,
        hostname: str | Omit = omit,
        name: str | Omit = omit,
        servers: Iterable[portal_update_params.Server] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalUpdateResponse:
        """
        Update a MCP Portal

        Args:
          id: portal id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/accounts/{account_id}/access/ai-controls/mcp/portals/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "hostname": hostname,
                    "name": name,
                    "servers": servers,
                },
                portal_update_params.PortalUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PortalUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[PortalUpdateResponse], ResultWrapper[PortalUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[PortalListResponse]:
        """
        List MCP Portals

        Args:
          search: Search by id, name, hostname

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/access/ai-controls/mcp/portals",
            page=SyncV4PagePaginationArray[PortalListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                    },
                    portal_list_params.PortalListParams,
                ),
            ),
            model=PortalListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalDeleteResponse:
        """
        Delete a MCP Portal

        Args:
          id: portal id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/accounts/{account_id}/access/ai-controls/mcp/portals/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PortalDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[PortalDeleteResponse], ResultWrapper[PortalDeleteResponse]),
        )

    def read(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalReadResponse:
        """
        Read details of an MCP Portal

        Args:
          id: portal id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/accounts/{account_id}/access/ai-controls/mcp/portals/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PortalReadResponse]._unwrapper,
            ),
            cast_to=cast(Type[PortalReadResponse], ResultWrapper[PortalReadResponse]),
        )


class AsyncPortalsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPortalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPortalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPortalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPortalsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        id: str,
        hostname: str,
        name: str,
        description: str | Omit = omit,
        servers: Iterable[portal_create_params.Server] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalCreateResponse:
        """
        Create a new MCP Portal

        Args:
          id: portal id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/access/ai-controls/mcp/portals",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "hostname": hostname,
                    "name": name,
                    "description": description,
                    "servers": servers,
                },
                portal_create_params.PortalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PortalCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[PortalCreateResponse], ResultWrapper[PortalCreateResponse]),
        )

    async def update(
        self,
        id: str,
        *,
        account_id: str,
        description: str | Omit = omit,
        hostname: str | Omit = omit,
        name: str | Omit = omit,
        servers: Iterable[portal_update_params.Server] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalUpdateResponse:
        """
        Update a MCP Portal

        Args:
          id: portal id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/accounts/{account_id}/access/ai-controls/mcp/portals/{id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "hostname": hostname,
                    "name": name,
                    "servers": servers,
                },
                portal_update_params.PortalUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PortalUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[PortalUpdateResponse], ResultWrapper[PortalUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        search: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PortalListResponse, AsyncV4PagePaginationArray[PortalListResponse]]:
        """
        List MCP Portals

        Args:
          search: Search by id, name, hostname

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/access/ai-controls/mcp/portals",
            page=AsyncV4PagePaginationArray[PortalListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "search": search,
                    },
                    portal_list_params.PortalListParams,
                ),
            ),
            model=PortalListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalDeleteResponse:
        """
        Delete a MCP Portal

        Args:
          id: portal id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/accounts/{account_id}/access/ai-controls/mcp/portals/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PortalDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[PortalDeleteResponse], ResultWrapper[PortalDeleteResponse]),
        )

    async def read(
        self,
        id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortalReadResponse:
        """
        Read details of an MCP Portal

        Args:
          id: portal id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/accounts/{account_id}/access/ai-controls/mcp/portals/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PortalReadResponse]._unwrapper,
            ),
            cast_to=cast(Type[PortalReadResponse], ResultWrapper[PortalReadResponse]),
        )


class PortalsResourceWithRawResponse:
    def __init__(self, portals: PortalsResource) -> None:
        self._portals = portals

        self.create = to_raw_response_wrapper(
            portals.create,
        )
        self.update = to_raw_response_wrapper(
            portals.update,
        )
        self.list = to_raw_response_wrapper(
            portals.list,
        )
        self.delete = to_raw_response_wrapper(
            portals.delete,
        )
        self.read = to_raw_response_wrapper(
            portals.read,
        )


class AsyncPortalsResourceWithRawResponse:
    def __init__(self, portals: AsyncPortalsResource) -> None:
        self._portals = portals

        self.create = async_to_raw_response_wrapper(
            portals.create,
        )
        self.update = async_to_raw_response_wrapper(
            portals.update,
        )
        self.list = async_to_raw_response_wrapper(
            portals.list,
        )
        self.delete = async_to_raw_response_wrapper(
            portals.delete,
        )
        self.read = async_to_raw_response_wrapper(
            portals.read,
        )


class PortalsResourceWithStreamingResponse:
    def __init__(self, portals: PortalsResource) -> None:
        self._portals = portals

        self.create = to_streamed_response_wrapper(
            portals.create,
        )
        self.update = to_streamed_response_wrapper(
            portals.update,
        )
        self.list = to_streamed_response_wrapper(
            portals.list,
        )
        self.delete = to_streamed_response_wrapper(
            portals.delete,
        )
        self.read = to_streamed_response_wrapper(
            portals.read,
        )


class AsyncPortalsResourceWithStreamingResponse:
    def __init__(self, portals: AsyncPortalsResource) -> None:
        self._portals = portals

        self.create = async_to_streamed_response_wrapper(
            portals.create,
        )
        self.update = async_to_streamed_response_wrapper(
            portals.update,
        )
        self.list = async_to_streamed_response_wrapper(
            portals.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            portals.delete,
        )
        self.read = async_to_streamed_response_wrapper(
            portals.read,
        )
