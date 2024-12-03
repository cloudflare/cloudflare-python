# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

import httpx

from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import (
    maybe_transform,
    async_maybe_transform,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_wrappers import ResultWrapper
from ......_base_client import make_request_options
from ......types.zero_trust.devices.fallback_domain_param import FallbackDomainParam
from ......types.zero_trust.devices.policies.default.fallback_domain_get_response import FallbackDomainGetResponse
from ......types.zero_trust.devices.policies.default.fallback_domain_update_response import FallbackDomainUpdateResponse

__all__ = ["FallbackDomainsResource", "AsyncFallbackDomainsResource"]


class FallbackDomainsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FallbackDomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return FallbackDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FallbackDomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return FallbackDomainsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        account_id: str,
        domains: Iterable[FallbackDomainParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FallbackDomainUpdateResponse]:
        """Sets the list of domains to bypass Gateway DNS resolution.

        These domains will
        use the specified local DNS resolver instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/devices/policy/fallback_domains",
            body=maybe_transform(domains, Iterable[FallbackDomainParam]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FallbackDomainUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FallbackDomainUpdateResponse]], ResultWrapper[FallbackDomainUpdateResponse]),
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
    ) -> Optional[FallbackDomainGetResponse]:
        """Fetches a list of domains to bypass Gateway DNS resolution.

        These domains will
        use the specified local DNS resolver instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/devices/policy/fallback_domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FallbackDomainGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FallbackDomainGetResponse]], ResultWrapper[FallbackDomainGetResponse]),
        )


class AsyncFallbackDomainsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFallbackDomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFallbackDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFallbackDomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncFallbackDomainsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        account_id: str,
        domains: Iterable[FallbackDomainParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FallbackDomainUpdateResponse]:
        """Sets the list of domains to bypass Gateway DNS resolution.

        These domains will
        use the specified local DNS resolver instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/devices/policy/fallback_domains",
            body=await async_maybe_transform(domains, Iterable[FallbackDomainParam]),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FallbackDomainUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FallbackDomainUpdateResponse]], ResultWrapper[FallbackDomainUpdateResponse]),
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
    ) -> Optional[FallbackDomainGetResponse]:
        """Fetches a list of domains to bypass Gateway DNS resolution.

        These domains will
        use the specified local DNS resolver instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/devices/policy/fallback_domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FallbackDomainGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FallbackDomainGetResponse]], ResultWrapper[FallbackDomainGetResponse]),
        )


class FallbackDomainsResourceWithRawResponse:
    def __init__(self, fallback_domains: FallbackDomainsResource) -> None:
        self._fallback_domains = fallback_domains

        self.update = to_raw_response_wrapper(
            fallback_domains.update,
        )
        self.get = to_raw_response_wrapper(
            fallback_domains.get,
        )


class AsyncFallbackDomainsResourceWithRawResponse:
    def __init__(self, fallback_domains: AsyncFallbackDomainsResource) -> None:
        self._fallback_domains = fallback_domains

        self.update = async_to_raw_response_wrapper(
            fallback_domains.update,
        )
        self.get = async_to_raw_response_wrapper(
            fallback_domains.get,
        )


class FallbackDomainsResourceWithStreamingResponse:
    def __init__(self, fallback_domains: FallbackDomainsResource) -> None:
        self._fallback_domains = fallback_domains

        self.update = to_streamed_response_wrapper(
            fallback_domains.update,
        )
        self.get = to_streamed_response_wrapper(
            fallback_domains.get,
        )


class AsyncFallbackDomainsResourceWithStreamingResponse:
    def __init__(self, fallback_domains: AsyncFallbackDomainsResource) -> None:
        self._fallback_domains = fallback_domains

        self.update = async_to_streamed_response_wrapper(
            fallback_domains.update,
        )
        self.get = async_to_streamed_response_wrapper(
            fallback_domains.get,
        )
