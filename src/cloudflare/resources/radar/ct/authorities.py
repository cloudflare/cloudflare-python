# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.radar.ct import authority_get_params, authority_list_params
from ....types.radar.ct.authority_get_response import AuthorityGetResponse
from ....types.radar.ct.authority_list_response import AuthorityListResponse

__all__ = ["AuthoritiesResource", "AsyncAuthoritiesResource"]


class AuthoritiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthoritiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AuthoritiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthoritiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AuthoritiesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorityListResponse:
        """
        Retrieves a list of certificate authorities.

        Args:
          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          offset: Skips the specified number of objects before fetching the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/ct/authorities",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "format": format,
                        "limit": limit,
                        "offset": offset,
                    },
                    authority_list_params.AuthorityListParams,
                ),
                post_parser=ResultWrapper[AuthorityListResponse]._unwrapper,
            ),
            cast_to=cast(Type[AuthorityListResponse], ResultWrapper[AuthorityListResponse]),
        )

    def get(
        self,
        ca_slug: str,
        *,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorityGetResponse:
        """
        Retrieves the requested CA information.

        Args:
          ca_slug: Certificate authority SHA256 fingerprint.

          format: Format in which results will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ca_slug:
            raise ValueError(f"Expected a non-empty value for `ca_slug` but received {ca_slug!r}")
        return self._get(
            f"/radar/ct/authorities/{ca_slug}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, authority_get_params.AuthorityGetParams),
                post_parser=ResultWrapper[AuthorityGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[AuthorityGetResponse], ResultWrapper[AuthorityGetResponse]),
        )


class AsyncAuthoritiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthoritiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthoritiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthoritiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAuthoritiesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorityListResponse:
        """
        Retrieves a list of certificate authorities.

        Args:
          format: Format in which results will be returned.

          limit: Limits the number of objects returned in the response.

          offset: Skips the specified number of objects before fetching the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/ct/authorities",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "format": format,
                        "limit": limit,
                        "offset": offset,
                    },
                    authority_list_params.AuthorityListParams,
                ),
                post_parser=ResultWrapper[AuthorityListResponse]._unwrapper,
            ),
            cast_to=cast(Type[AuthorityListResponse], ResultWrapper[AuthorityListResponse]),
        )

    async def get(
        self,
        ca_slug: str,
        *,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorityGetResponse:
        """
        Retrieves the requested CA information.

        Args:
          ca_slug: Certificate authority SHA256 fingerprint.

          format: Format in which results will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ca_slug:
            raise ValueError(f"Expected a non-empty value for `ca_slug` but received {ca_slug!r}")
        return await self._get(
            f"/radar/ct/authorities/{ca_slug}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"format": format}, authority_get_params.AuthorityGetParams),
                post_parser=ResultWrapper[AuthorityGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[AuthorityGetResponse], ResultWrapper[AuthorityGetResponse]),
        )


class AuthoritiesResourceWithRawResponse:
    def __init__(self, authorities: AuthoritiesResource) -> None:
        self._authorities = authorities

        self.list = to_raw_response_wrapper(
            authorities.list,
        )
        self.get = to_raw_response_wrapper(
            authorities.get,
        )


class AsyncAuthoritiesResourceWithRawResponse:
    def __init__(self, authorities: AsyncAuthoritiesResource) -> None:
        self._authorities = authorities

        self.list = async_to_raw_response_wrapper(
            authorities.list,
        )
        self.get = async_to_raw_response_wrapper(
            authorities.get,
        )


class AuthoritiesResourceWithStreamingResponse:
    def __init__(self, authorities: AuthoritiesResource) -> None:
        self._authorities = authorities

        self.list = to_streamed_response_wrapper(
            authorities.list,
        )
        self.get = to_streamed_response_wrapper(
            authorities.get,
        )


class AsyncAuthoritiesResourceWithStreamingResponse:
    def __init__(self, authorities: AsyncAuthoritiesResource) -> None:
        self._authorities = authorities

        self.list = async_to_streamed_response_wrapper(
            authorities.list,
        )
        self.get = async_to_streamed_response_wrapper(
            authorities.get,
        )
