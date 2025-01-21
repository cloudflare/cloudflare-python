# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ....types.zero_trust.organizations import doh_update_params
from ....types.zero_trust.organizations.doh_get_response import DOHGetResponse
from ....types.zero_trust.organizations.doh_update_response import DOHUpdateResponse

__all__ = ["DOHResource", "AsyncDOHResource"]


class DOHResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DOHResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DOHResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DOHResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DOHResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        account_id: str,
        doh_jwt_duration: str | NotGiven = NOT_GIVEN,
        service_token_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DOHUpdateResponse]:
        """
        Updates the DoH settings for your Zero Trust organization.

        Args:
          account_id: Identifier

          doh_jwt_duration: The duration the DoH JWT is valid for. Must be in the format `300ms` or `2h45m`.
              Valid time units are: ns, us (or µs), ms, s, m, h. Note that the maximum
              duration for this setting is the same as the key rotation period on the account.
              Default expiration is 24h

          service_token_id: The uuid of the service token you want to use for DoH authentication

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/access/organizations/doh",
            body=maybe_transform(
                {
                    "doh_jwt_duration": doh_jwt_duration,
                    "service_token_id": service_token_id,
                },
                doh_update_params.DOHUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DOHUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DOHUpdateResponse]], ResultWrapper[DOHUpdateResponse]),
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
    ) -> Optional[DOHGetResponse]:
        """
        Returns the DoH settings for your Zero Trust organization.

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
            f"/accounts/{account_id}/access/organizations/doh",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DOHGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DOHGetResponse]], ResultWrapper[DOHGetResponse]),
        )


class AsyncDOHResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDOHResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDOHResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDOHResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDOHResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        account_id: str,
        doh_jwt_duration: str | NotGiven = NOT_GIVEN,
        service_token_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DOHUpdateResponse]:
        """
        Updates the DoH settings for your Zero Trust organization.

        Args:
          account_id: Identifier

          doh_jwt_duration: The duration the DoH JWT is valid for. Must be in the format `300ms` or `2h45m`.
              Valid time units are: ns, us (or µs), ms, s, m, h. Note that the maximum
              duration for this setting is the same as the key rotation period on the account.
              Default expiration is 24h

          service_token_id: The uuid of the service token you want to use for DoH authentication

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/access/organizations/doh",
            body=await async_maybe_transform(
                {
                    "doh_jwt_duration": doh_jwt_duration,
                    "service_token_id": service_token_id,
                },
                doh_update_params.DOHUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DOHUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DOHUpdateResponse]], ResultWrapper[DOHUpdateResponse]),
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
    ) -> Optional[DOHGetResponse]:
        """
        Returns the DoH settings for your Zero Trust organization.

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
            f"/accounts/{account_id}/access/organizations/doh",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DOHGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DOHGetResponse]], ResultWrapper[DOHGetResponse]),
        )


class DOHResourceWithRawResponse:
    def __init__(self, doh: DOHResource) -> None:
        self._doh = doh

        self.update = to_raw_response_wrapper(
            doh.update,
        )
        self.get = to_raw_response_wrapper(
            doh.get,
        )


class AsyncDOHResourceWithRawResponse:
    def __init__(self, doh: AsyncDOHResource) -> None:
        self._doh = doh

        self.update = async_to_raw_response_wrapper(
            doh.update,
        )
        self.get = async_to_raw_response_wrapper(
            doh.get,
        )


class DOHResourceWithStreamingResponse:
    def __init__(self, doh: DOHResource) -> None:
        self._doh = doh

        self.update = to_streamed_response_wrapper(
            doh.update,
        )
        self.get = to_streamed_response_wrapper(
            doh.get,
        )


class AsyncDOHResourceWithStreamingResponse:
    def __init__(self, doh: AsyncDOHResource) -> None:
        self._doh = doh

        self.update = async_to_streamed_response_wrapper(
            doh.update,
        )
        self.get = async_to_streamed_response_wrapper(
            doh.get,
        )
