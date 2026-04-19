# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.brand_protection.v2 import logo_get_params, logo_create_params
from ....types.brand_protection.v2.logo_get_response import LogoGetResponse
from ....types.brand_protection.v2.logo_create_response import LogoCreateResponse
from ....types.brand_protection.v2.logo_delete_response import LogoDeleteResponse

__all__ = ["LogosResource", "AsyncLogosResource"]


class LogosResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LogosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return LogosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return LogosResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str | None = None,
        image_data: str,
        similarity_threshold: float,
        tag: str,
        search_lookback: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogoCreateResponse:
        """
        Create a new saved brand protection logo query for visual similarity matching

        Args:
          image_data: Base64 encoded image data. Can include data URI prefix (e.g.,
              'data:image/png;base64,...') or just the base64 string.

          similarity_threshold: Minimum similarity score (0-1) required for visual matches

          tag: Unique identifier for the logo query

          search_lookback: If true, search historic scanned images for matches above the similarity
              threshold

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/queries", account_id=account_id
            ),
            body=maybe_transform(
                {
                    "image_data": image_data,
                    "similarity_threshold": similarity_threshold,
                    "tag": tag,
                    "search_lookback": search_lookback,
                },
                logo_create_params.LogoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogoCreateResponse,
        )

    def delete(
        self,
        query_id: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogoDeleteResponse:
        """Delete a saved brand protection logo query.

        Returns 404 if the query ID doesn't
        exist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not query_id:
            raise ValueError(f"Expected a non-empty value for `query_id` but received {query_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/queries/{query_id}",
                account_id=account_id,
                query_id=query_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogoDeleteResponse,
        )

    def get(
        self,
        *,
        account_id: str | None = None,
        id: str | Omit = omit,
        download: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogoGetResponse:
        """Get all saved brand protection logo queries for an account.

        Optionally specify
        id to get a single query. Set download=true to include base64-encoded image
        data.

        Args:
          id: Optional query ID to retrieve a specific logo query

          download: If true, include base64-encoded image data in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/queries", account_id=account_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "download": download,
                    },
                    logo_get_params.LogoGetParams,
                ),
            ),
            cast_to=LogoGetResponse,
        )


class AsyncLogosResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLogosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLogosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLogosResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str | None = None,
        image_data: str,
        similarity_threshold: float,
        tag: str,
        search_lookback: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogoCreateResponse:
        """
        Create a new saved brand protection logo query for visual similarity matching

        Args:
          image_data: Base64 encoded image data. Can include data URI prefix (e.g.,
              'data:image/png;base64,...') or just the base64 string.

          similarity_threshold: Minimum similarity score (0-1) required for visual matches

          tag: Unique identifier for the logo query

          search_lookback: If true, search historic scanned images for matches above the similarity
              threshold

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/queries", account_id=account_id
            ),
            body=await async_maybe_transform(
                {
                    "image_data": image_data,
                    "similarity_threshold": similarity_threshold,
                    "tag": tag,
                    "search_lookback": search_lookback,
                },
                logo_create_params.LogoCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogoCreateResponse,
        )

    async def delete(
        self,
        query_id: str,
        *,
        account_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogoDeleteResponse:
        """Delete a saved brand protection logo query.

        Returns 404 if the query ID doesn't
        exist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not query_id:
            raise ValueError(f"Expected a non-empty value for `query_id` but received {query_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/queries/{query_id}",
                account_id=account_id,
                query_id=query_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogoDeleteResponse,
        )

    async def get(
        self,
        *,
        account_id: str | None = None,
        id: str | Omit = omit,
        download: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogoGetResponse:
        """Get all saved brand protection logo queries for an account.

        Optionally specify
        id to get a single query. Set download=true to include base64-encoded image
        data.

        Args:
          id: Optional query ID to retrieve a specific logo query

          download: If true, include base64-encoded image data in the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/v2/brand-protection/logo/queries", account_id=account_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "download": download,
                    },
                    logo_get_params.LogoGetParams,
                ),
            ),
            cast_to=LogoGetResponse,
        )


class LogosResourceWithRawResponse:
    def __init__(self, logos: LogosResource) -> None:
        self._logos = logos

        self.create = to_raw_response_wrapper(
            logos.create,
        )
        self.delete = to_raw_response_wrapper(
            logos.delete,
        )
        self.get = to_raw_response_wrapper(
            logos.get,
        )


class AsyncLogosResourceWithRawResponse:
    def __init__(self, logos: AsyncLogosResource) -> None:
        self._logos = logos

        self.create = async_to_raw_response_wrapper(
            logos.create,
        )
        self.delete = async_to_raw_response_wrapper(
            logos.delete,
        )
        self.get = async_to_raw_response_wrapper(
            logos.get,
        )


class LogosResourceWithStreamingResponse:
    def __init__(self, logos: LogosResource) -> None:
        self._logos = logos

        self.create = to_streamed_response_wrapper(
            logos.create,
        )
        self.delete = to_streamed_response_wrapper(
            logos.delete,
        )
        self.get = to_streamed_response_wrapper(
            logos.get,
        )


class AsyncLogosResourceWithStreamingResponse:
    def __init__(self, logos: AsyncLogosResource) -> None:
        self._logos = logos

        self.create = async_to_streamed_response_wrapper(
            logos.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            logos.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            logos.get,
        )
