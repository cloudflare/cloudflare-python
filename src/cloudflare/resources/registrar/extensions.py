# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncCursorPagination, AsyncCursorPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.registrar import extension_list_params
from ...types.registrar.extension_get_response import ExtensionGetResponse
from ...types.registrar.extension_list_response import ExtensionListResponse

__all__ = ["ExtensionsResource", "AsyncExtensionsResource"]


class ExtensionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExtensionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ExtensionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtensionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ExtensionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        name: str | Omit = omit,
        per_page: int | Omit = omit,
        sort_by: Literal["name", "created_at", "updated_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[ExtensionListResponse]:
        """
        Returns metadata and JSON Schema documents describing the expected input
        structure for registration operations on each supported extension (TLD).

        This endpoint uses cursor-based pagination. Results are ordered by extension
        name by default. To fetch the next page, pass the `cursor` value from the
        `result_info` object in the response as the `cursor` query parameter in your
        next request. An empty `cursor` string indicates there are no more pages.

        Supports HTTP conditional GET via `ETag`. Include the `ETag` value from a
        previous response in an `If-None-Match` header to receive a `304 Not Modified`
        when the data has not changed.

        Args:
          account_id: Identifier

          cursor: Opaque token from a previous response's `result_info.cursor`. Pass this value to
              fetch the next page of results. Omit (or pass an empty string) for the first
              page.

          direction: Sort direction for results. Defaults to ascending order.

          name: Filter extensions by exact name match. For example, `name=com` returns only the
              `com` extension.

          per_page: Number of items to return per page.

          sort_by: Column to sort results by. Defaults to `name` when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/registrar/extensions", account_id=account_id),
            page=SyncCursorPagination[ExtensionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "name": name,
                        "per_page": per_page,
                        "sort_by": sort_by,
                    },
                    extension_list_params.ExtensionListParams,
                ),
            ),
            model=ExtensionListResponse,
        )

    def get(
        self,
        extension: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtensionGetResponse:
        """
        Returns metadata and JSON Schema documents describing the expected input
        structure for registration operations on a specific extension (TLD).

        Supports HTTP conditional GET via `ETag`. Include the `ETag` value from a
        previous response in an `If-None-Match` header to receive a `304 Not Modified`
        when the data has not changed.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not extension:
            raise ValueError(f"Expected a non-empty value for `extension` but received {extension!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/registrar/extensions/{extension}", account_id=account_id, extension=extension
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ExtensionGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ExtensionGetResponse], ResultWrapper[ExtensionGetResponse]),
        )


class AsyncExtensionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExtensionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExtensionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtensionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncExtensionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        direction: Literal["asc", "desc"] | Omit = omit,
        name: str | Omit = omit,
        per_page: int | Omit = omit,
        sort_by: Literal["name", "created_at", "updated_at"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ExtensionListResponse, AsyncCursorPagination[ExtensionListResponse]]:
        """
        Returns metadata and JSON Schema documents describing the expected input
        structure for registration operations on each supported extension (TLD).

        This endpoint uses cursor-based pagination. Results are ordered by extension
        name by default. To fetch the next page, pass the `cursor` value from the
        `result_info` object in the response as the `cursor` query parameter in your
        next request. An empty `cursor` string indicates there are no more pages.

        Supports HTTP conditional GET via `ETag`. Include the `ETag` value from a
        previous response in an `If-None-Match` header to receive a `304 Not Modified`
        when the data has not changed.

        Args:
          account_id: Identifier

          cursor: Opaque token from a previous response's `result_info.cursor`. Pass this value to
              fetch the next page of results. Omit (or pass an empty string) for the first
              page.

          direction: Sort direction for results. Defaults to ascending order.

          name: Filter extensions by exact name match. For example, `name=com` returns only the
              `com` extension.

          per_page: Number of items to return per page.

          sort_by: Column to sort results by. Defaults to `name` when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/registrar/extensions", account_id=account_id),
            page=AsyncCursorPagination[ExtensionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "direction": direction,
                        "name": name,
                        "per_page": per_page,
                        "sort_by": sort_by,
                    },
                    extension_list_params.ExtensionListParams,
                ),
            ),
            model=ExtensionListResponse,
        )

    async def get(
        self,
        extension: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtensionGetResponse:
        """
        Returns metadata and JSON Schema documents describing the expected input
        structure for registration operations on a specific extension (TLD).

        Supports HTTP conditional GET via `ETag`. Include the `ETag` value from a
        previous response in an `If-None-Match` header to receive a `304 Not Modified`
        when the data has not changed.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not extension:
            raise ValueError(f"Expected a non-empty value for `extension` but received {extension!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/registrar/extensions/{extension}", account_id=account_id, extension=extension
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ExtensionGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ExtensionGetResponse], ResultWrapper[ExtensionGetResponse]),
        )


class ExtensionsResourceWithRawResponse:
    def __init__(self, extensions: ExtensionsResource) -> None:
        self._extensions = extensions

        self.list = to_raw_response_wrapper(
            extensions.list,
        )
        self.get = to_raw_response_wrapper(
            extensions.get,
        )


class AsyncExtensionsResourceWithRawResponse:
    def __init__(self, extensions: AsyncExtensionsResource) -> None:
        self._extensions = extensions

        self.list = async_to_raw_response_wrapper(
            extensions.list,
        )
        self.get = async_to_raw_response_wrapper(
            extensions.get,
        )


class ExtensionsResourceWithStreamingResponse:
    def __init__(self, extensions: ExtensionsResource) -> None:
        self._extensions = extensions

        self.list = to_streamed_response_wrapper(
            extensions.list,
        )
        self.get = to_streamed_response_wrapper(
            extensions.get,
        )


class AsyncExtensionsResourceWithStreamingResponse:
    def __init__(self, extensions: AsyncExtensionsResource) -> None:
        self._extensions = extensions

        self.list = async_to_streamed_response_wrapper(
            extensions.list,
        )
        self.get = async_to_streamed_response_wrapper(
            extensions.get,
        )
