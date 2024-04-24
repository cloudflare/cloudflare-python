# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

import httpx

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
from .....pagination import SyncSinglePage, AsyncSinglePage
from ....._base_client import (
    AsyncPaginator,
    make_request_options,
)
from .....types.zero_trust.devices.policies import fallback_domain_update_params
from .....types.zero_trust.devices.policies.fallback_domain import FallbackDomain
from .....types.zero_trust.devices.policies.fallback_domain_param import FallbackDomainParam
from .....types.zero_trust.devices.policies.fallback_domain_get_response import FallbackDomainGetResponse
from .....types.zero_trust.devices.policies.fallback_domain_update_response import FallbackDomainUpdateResponse

__all__ = ["FallbackDomainsResource", "AsyncFallbackDomainsResource"]


class FallbackDomainsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FallbackDomainsResourceWithRawResponse:
        return FallbackDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FallbackDomainsResourceWithStreamingResponse:
        return FallbackDomainsResourceWithStreamingResponse(self)

    def update(
        self,
        policy_id: str,
        *,
        account_id: str,
        body: Iterable[FallbackDomainParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FallbackDomainUpdateResponse]:
        """Sets the list of domains to bypass Gateway DNS resolution.

        These domains will
        use the specified local DNS resolver instead. This will only apply to the
        specified device settings profile.

        Args:
          policy_id: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._put(
            f"/accounts/{account_id}/devices/policy/{policy_id}/fallback_domains",
            body=maybe_transform(body, fallback_domain_update_params.FallbackDomainUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FallbackDomainUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FallbackDomainUpdateResponse]], ResultWrapper[FallbackDomainUpdateResponse]),
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
    ) -> SyncSinglePage[FallbackDomain]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/devices/policy/fallback_domains",
            page=SyncSinglePage[FallbackDomain],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=FallbackDomain,
        )

    def get(
        self,
        policy_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FallbackDomainGetResponse]:
        """
        Fetches the list of domains to bypass Gateway DNS resolution from a specified
        device settings profile. These domains will use the specified local DNS resolver
        instead.

        Args:
          policy_id: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._get(
            f"/accounts/{account_id}/devices/policy/{policy_id}/fallback_domains",
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
        return AsyncFallbackDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFallbackDomainsResourceWithStreamingResponse:
        return AsyncFallbackDomainsResourceWithStreamingResponse(self)

    async def update(
        self,
        policy_id: str,
        *,
        account_id: str,
        body: Iterable[FallbackDomainParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FallbackDomainUpdateResponse]:
        """Sets the list of domains to bypass Gateway DNS resolution.

        These domains will
        use the specified local DNS resolver instead. This will only apply to the
        specified device settings profile.

        Args:
          policy_id: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._put(
            f"/accounts/{account_id}/devices/policy/{policy_id}/fallback_domains",
            body=await async_maybe_transform(body, fallback_domain_update_params.FallbackDomainUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[FallbackDomainUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[FallbackDomainUpdateResponse]], ResultWrapper[FallbackDomainUpdateResponse]),
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
    ) -> AsyncPaginator[FallbackDomain, AsyncSinglePage[FallbackDomain]]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/devices/policy/fallback_domains",
            page=AsyncSinglePage[FallbackDomain],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=FallbackDomain,
        )

    async def get(
        self,
        policy_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FallbackDomainGetResponse]:
        """
        Fetches the list of domains to bypass Gateway DNS resolution from a specified
        device settings profile. These domains will use the specified local DNS resolver
        instead.

        Args:
          policy_id: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return await self._get(
            f"/accounts/{account_id}/devices/policy/{policy_id}/fallback_domains",
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
        self.list = to_raw_response_wrapper(
            fallback_domains.list,
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
        self.list = async_to_raw_response_wrapper(
            fallback_domains.list,
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
        self.list = to_streamed_response_wrapper(
            fallback_domains.list,
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
        self.list = async_to_streamed_response_wrapper(
            fallback_domains.list,
        )
        self.get = async_to_streamed_response_wrapper(
            fallback_domains.get,
        )
