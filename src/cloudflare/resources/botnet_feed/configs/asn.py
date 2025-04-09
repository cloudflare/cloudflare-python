# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

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
from ...._base_client import make_request_options
from ....types.botnet_feed.configs.asn_get_response import ASNGetResponse
from ....types.botnet_feed.configs.asn_delete_response import ASNDeleteResponse

__all__ = ["ASNResource", "AsyncASNResource"]


class ASNResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ASNResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ASNResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ASNResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ASNResourceWithStreamingResponse(self)

    def delete(
        self,
        asn_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ASNDeleteResponse]:
        """
        Delete an ASN from botnet threat feed for a given user.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._delete(
            f"/accounts/{account_id}/botnet_feed/configs/asn/{asn_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ASNDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ASNDeleteResponse]], ResultWrapper[ASNDeleteResponse]),
        )

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ASNGetResponse]:
        """
        Gets a list of all ASNs registered for a user for the DDoS Botnet Feed API.

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
            f"/accounts/{account_id}/botnet_feed/configs/asn",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ASNGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ASNGetResponse]], ResultWrapper[ASNGetResponse]),
        )


class AsyncASNResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncASNResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncASNResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncASNResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncASNResourceWithStreamingResponse(self)

    async def delete(
        self,
        asn_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ASNDeleteResponse]:
        """
        Delete an ASN from botnet threat feed for a given user.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/botnet_feed/configs/asn/{asn_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ASNDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ASNDeleteResponse]], ResultWrapper[ASNDeleteResponse]),
        )

    async def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ASNGetResponse]:
        """
        Gets a list of all ASNs registered for a user for the DDoS Botnet Feed API.

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
            f"/accounts/{account_id}/botnet_feed/configs/asn",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ASNGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ASNGetResponse]], ResultWrapper[ASNGetResponse]),
        )


class ASNResourceWithRawResponse:
    def __init__(self, asn: ASNResource) -> None:
        self._asn = asn

        self.delete = to_raw_response_wrapper(
            asn.delete,
        )
        self.get = to_raw_response_wrapper(
            asn.get,
        )


class AsyncASNResourceWithRawResponse:
    def __init__(self, asn: AsyncASNResource) -> None:
        self._asn = asn

        self.delete = async_to_raw_response_wrapper(
            asn.delete,
        )
        self.get = async_to_raw_response_wrapper(
            asn.get,
        )


class ASNResourceWithStreamingResponse:
    def __init__(self, asn: ASNResource) -> None:
        self._asn = asn

        self.delete = to_streamed_response_wrapper(
            asn.delete,
        )
        self.get = to_streamed_response_wrapper(
            asn.get,
        )


class AsyncASNResourceWithStreamingResponse:
    def __init__(self, asn: AsyncASNResource) -> None:
        self._asn = asn

        self.delete = async_to_streamed_response_wrapper(
            asn.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            asn.get,
        )
