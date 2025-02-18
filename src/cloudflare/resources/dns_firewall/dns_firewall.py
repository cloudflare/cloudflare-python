# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from .reverse_dns import (
    ReverseDNSResource,
    AsyncReverseDNSResource,
    ReverseDNSResourceWithRawResponse,
    AsyncReverseDNSResourceWithRawResponse,
    ReverseDNSResourceWithStreamingResponse,
    AsyncReverseDNSResourceWithStreamingResponse,
)
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from .analytics.analytics import (
    AnalyticsResource,
    AsyncAnalyticsResource,
    AnalyticsResourceWithRawResponse,
    AsyncAnalyticsResourceWithRawResponse,
    AnalyticsResourceWithStreamingResponse,
    AsyncAnalyticsResourceWithStreamingResponse,
)
from ...types.dns_firewall import (
    dns_firewall_edit_params,
    dns_firewall_list_params,
    dns_firewall_create_params,
)
from ...types.dns_firewall.upstream_ips import UpstreamIPs
from ...types.dns_firewall.attack_mitigation_param import AttackMitigationParam
from ...types.dns_firewall.dns_firewall_get_response import DNSFirewallGetResponse
from ...types.dns_firewall.dns_firewall_edit_response import DNSFirewallEditResponse
from ...types.dns_firewall.dns_firewall_list_response import DNSFirewallListResponse
from ...types.dns_firewall.dns_firewall_create_response import DNSFirewallCreateResponse
from ...types.dns_firewall.dns_firewall_delete_response import DNSFirewallDeleteResponse

__all__ = ["DNSFirewallResource", "AsyncDNSFirewallResource"]


class DNSFirewallResource(SyncAPIResource):
    @cached_property
    def analytics(self) -> AnalyticsResource:
        return AnalyticsResource(self._client)

    @cached_property
    def reverse_dns(self) -> ReverseDNSResource:
        return ReverseDNSResource(self._client)

    @cached_property
    def with_raw_response(self) -> DNSFirewallResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DNSFirewallResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DNSFirewallResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DNSFirewallResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        upstream_ips: List[UpstreamIPs],
        attack_mitigation: Optional[AttackMitigationParam] | NotGiven = NOT_GIVEN,
        deprecate_any_requests: bool | NotGiven = NOT_GIVEN,
        ecs_fallback: bool | NotGiven = NOT_GIVEN,
        maximum_cache_ttl: float | NotGiven = NOT_GIVEN,
        minimum_cache_ttl: float | NotGiven = NOT_GIVEN,
        negative_cache_ttl: Optional[float] | NotGiven = NOT_GIVEN,
        ratelimit: Optional[float] | NotGiven = NOT_GIVEN,
        retries: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DNSFirewallCreateResponse]:
        """
        Create a DNS Firewall cluster

        Args:
          account_id: Identifier

          name: DNS Firewall cluster name

          attack_mitigation: Attack mitigation settings

          deprecate_any_requests: Whether to refuse to answer queries for the ANY type

          ecs_fallback: Whether to forward client IP (resolver) subnet if no EDNS Client Subnet is sent

          maximum_cache_ttl: Maximum DNS cache TTL This setting sets an upper bound on DNS TTLs for purposes
              of caching between DNS Firewall and the upstream servers. Higher TTLs will be
              decreased to the maximum defined here for caching purposes.

          minimum_cache_ttl: Minimum DNS cache TTL This setting sets a lower bound on DNS TTLs for purposes
              of caching between DNS Firewall and the upstream servers. Lower TTLs will be
              increased to the minimum defined here for caching purposes.

          negative_cache_ttl: Negative DNS cache TTL This setting controls how long DNS Firewall should cache
              negative responses (e.g., NXDOMAIN) from the upstream servers.

          ratelimit: Ratelimit in queries per second per datacenter (applies to DNS queries sent to
              the upstream nameservers configured on the cluster)

          retries: Number of retries for fetching DNS responses from upstream nameservers (not
              counting the initial attempt)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/dns_firewall",
            body=maybe_transform(
                {
                    "name": name,
                    "upstream_ips": upstream_ips,
                    "attack_mitigation": attack_mitigation,
                    "deprecate_any_requests": deprecate_any_requests,
                    "ecs_fallback": ecs_fallback,
                    "maximum_cache_ttl": maximum_cache_ttl,
                    "minimum_cache_ttl": minimum_cache_ttl,
                    "negative_cache_ttl": negative_cache_ttl,
                    "ratelimit": ratelimit,
                    "retries": retries,
                },
                dns_firewall_create_params.DNSFirewallCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DNSFirewallCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DNSFirewallCreateResponse]], ResultWrapper[DNSFirewallCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[DNSFirewallListResponse]:
        """
        List DNS Firewall clusters for an account

        Args:
          account_id: Identifier

          page: Page number of paginated results

          per_page: Number of clusters per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/dns_firewall",
            page=SyncV4PagePaginationArray[DNSFirewallListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    dns_firewall_list_params.DNSFirewallListParams,
                ),
            ),
            model=DNSFirewallListResponse,
        )

    def delete(
        self,
        dns_firewall_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DNSFirewallDeleteResponse]:
        """
        Delete a DNS Firewall cluster

        Args:
          account_id: Identifier

          dns_firewall_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dns_firewall_id:
            raise ValueError(f"Expected a non-empty value for `dns_firewall_id` but received {dns_firewall_id!r}")
        return self._delete(
            f"/accounts/{account_id}/dns_firewall/{dns_firewall_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DNSFirewallDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DNSFirewallDeleteResponse]], ResultWrapper[DNSFirewallDeleteResponse]),
        )

    def edit(
        self,
        dns_firewall_id: str,
        *,
        account_id: str,
        attack_mitigation: Optional[AttackMitigationParam] | NotGiven = NOT_GIVEN,
        deprecate_any_requests: bool | NotGiven = NOT_GIVEN,
        ecs_fallback: bool | NotGiven = NOT_GIVEN,
        maximum_cache_ttl: float | NotGiven = NOT_GIVEN,
        minimum_cache_ttl: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        negative_cache_ttl: Optional[float] | NotGiven = NOT_GIVEN,
        ratelimit: Optional[float] | NotGiven = NOT_GIVEN,
        retries: float | NotGiven = NOT_GIVEN,
        upstream_ips: List[UpstreamIPs] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DNSFirewallEditResponse]:
        """
        Modify the configuration of a DNS Firewall cluster

        Args:
          account_id: Identifier

          dns_firewall_id: Identifier

          attack_mitigation: Attack mitigation settings

          deprecate_any_requests: Whether to refuse to answer queries for the ANY type

          ecs_fallback: Whether to forward client IP (resolver) subnet if no EDNS Client Subnet is sent

          maximum_cache_ttl: Maximum DNS cache TTL This setting sets an upper bound on DNS TTLs for purposes
              of caching between DNS Firewall and the upstream servers. Higher TTLs will be
              decreased to the maximum defined here for caching purposes.

          minimum_cache_ttl: Minimum DNS cache TTL This setting sets a lower bound on DNS TTLs for purposes
              of caching between DNS Firewall and the upstream servers. Lower TTLs will be
              increased to the minimum defined here for caching purposes.

          name: DNS Firewall cluster name

          negative_cache_ttl: Negative DNS cache TTL This setting controls how long DNS Firewall should cache
              negative responses (e.g., NXDOMAIN) from the upstream servers.

          ratelimit: Ratelimit in queries per second per datacenter (applies to DNS queries sent to
              the upstream nameservers configured on the cluster)

          retries: Number of retries for fetching DNS responses from upstream nameservers (not
              counting the initial attempt)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dns_firewall_id:
            raise ValueError(f"Expected a non-empty value for `dns_firewall_id` but received {dns_firewall_id!r}")
        return self._patch(
            f"/accounts/{account_id}/dns_firewall/{dns_firewall_id}",
            body=maybe_transform(
                {
                    "attack_mitigation": attack_mitigation,
                    "deprecate_any_requests": deprecate_any_requests,
                    "ecs_fallback": ecs_fallback,
                    "maximum_cache_ttl": maximum_cache_ttl,
                    "minimum_cache_ttl": minimum_cache_ttl,
                    "name": name,
                    "negative_cache_ttl": negative_cache_ttl,
                    "ratelimit": ratelimit,
                    "retries": retries,
                    "upstream_ips": upstream_ips,
                },
                dns_firewall_edit_params.DNSFirewallEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DNSFirewallEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DNSFirewallEditResponse]], ResultWrapper[DNSFirewallEditResponse]),
        )

    def get(
        self,
        dns_firewall_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DNSFirewallGetResponse]:
        """
        Show a single DNS Firewall cluster for an account

        Args:
          account_id: Identifier

          dns_firewall_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dns_firewall_id:
            raise ValueError(f"Expected a non-empty value for `dns_firewall_id` but received {dns_firewall_id!r}")
        return self._get(
            f"/accounts/{account_id}/dns_firewall/{dns_firewall_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DNSFirewallGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DNSFirewallGetResponse]], ResultWrapper[DNSFirewallGetResponse]),
        )


class AsyncDNSFirewallResource(AsyncAPIResource):
    @cached_property
    def analytics(self) -> AsyncAnalyticsResource:
        return AsyncAnalyticsResource(self._client)

    @cached_property
    def reverse_dns(self) -> AsyncReverseDNSResource:
        return AsyncReverseDNSResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDNSFirewallResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDNSFirewallResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDNSFirewallResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDNSFirewallResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        upstream_ips: List[UpstreamIPs],
        attack_mitigation: Optional[AttackMitigationParam] | NotGiven = NOT_GIVEN,
        deprecate_any_requests: bool | NotGiven = NOT_GIVEN,
        ecs_fallback: bool | NotGiven = NOT_GIVEN,
        maximum_cache_ttl: float | NotGiven = NOT_GIVEN,
        minimum_cache_ttl: float | NotGiven = NOT_GIVEN,
        negative_cache_ttl: Optional[float] | NotGiven = NOT_GIVEN,
        ratelimit: Optional[float] | NotGiven = NOT_GIVEN,
        retries: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DNSFirewallCreateResponse]:
        """
        Create a DNS Firewall cluster

        Args:
          account_id: Identifier

          name: DNS Firewall cluster name

          attack_mitigation: Attack mitigation settings

          deprecate_any_requests: Whether to refuse to answer queries for the ANY type

          ecs_fallback: Whether to forward client IP (resolver) subnet if no EDNS Client Subnet is sent

          maximum_cache_ttl: Maximum DNS cache TTL This setting sets an upper bound on DNS TTLs for purposes
              of caching between DNS Firewall and the upstream servers. Higher TTLs will be
              decreased to the maximum defined here for caching purposes.

          minimum_cache_ttl: Minimum DNS cache TTL This setting sets a lower bound on DNS TTLs for purposes
              of caching between DNS Firewall and the upstream servers. Lower TTLs will be
              increased to the minimum defined here for caching purposes.

          negative_cache_ttl: Negative DNS cache TTL This setting controls how long DNS Firewall should cache
              negative responses (e.g., NXDOMAIN) from the upstream servers.

          ratelimit: Ratelimit in queries per second per datacenter (applies to DNS queries sent to
              the upstream nameservers configured on the cluster)

          retries: Number of retries for fetching DNS responses from upstream nameservers (not
              counting the initial attempt)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/dns_firewall",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "upstream_ips": upstream_ips,
                    "attack_mitigation": attack_mitigation,
                    "deprecate_any_requests": deprecate_any_requests,
                    "ecs_fallback": ecs_fallback,
                    "maximum_cache_ttl": maximum_cache_ttl,
                    "minimum_cache_ttl": minimum_cache_ttl,
                    "negative_cache_ttl": negative_cache_ttl,
                    "ratelimit": ratelimit,
                    "retries": retries,
                },
                dns_firewall_create_params.DNSFirewallCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DNSFirewallCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DNSFirewallCreateResponse]], ResultWrapper[DNSFirewallCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DNSFirewallListResponse, AsyncV4PagePaginationArray[DNSFirewallListResponse]]:
        """
        List DNS Firewall clusters for an account

        Args:
          account_id: Identifier

          page: Page number of paginated results

          per_page: Number of clusters per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/dns_firewall",
            page=AsyncV4PagePaginationArray[DNSFirewallListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    dns_firewall_list_params.DNSFirewallListParams,
                ),
            ),
            model=DNSFirewallListResponse,
        )

    async def delete(
        self,
        dns_firewall_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DNSFirewallDeleteResponse]:
        """
        Delete a DNS Firewall cluster

        Args:
          account_id: Identifier

          dns_firewall_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dns_firewall_id:
            raise ValueError(f"Expected a non-empty value for `dns_firewall_id` but received {dns_firewall_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/dns_firewall/{dns_firewall_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DNSFirewallDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DNSFirewallDeleteResponse]], ResultWrapper[DNSFirewallDeleteResponse]),
        )

    async def edit(
        self,
        dns_firewall_id: str,
        *,
        account_id: str,
        attack_mitigation: Optional[AttackMitigationParam] | NotGiven = NOT_GIVEN,
        deprecate_any_requests: bool | NotGiven = NOT_GIVEN,
        ecs_fallback: bool | NotGiven = NOT_GIVEN,
        maximum_cache_ttl: float | NotGiven = NOT_GIVEN,
        minimum_cache_ttl: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        negative_cache_ttl: Optional[float] | NotGiven = NOT_GIVEN,
        ratelimit: Optional[float] | NotGiven = NOT_GIVEN,
        retries: float | NotGiven = NOT_GIVEN,
        upstream_ips: List[UpstreamIPs] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DNSFirewallEditResponse]:
        """
        Modify the configuration of a DNS Firewall cluster

        Args:
          account_id: Identifier

          dns_firewall_id: Identifier

          attack_mitigation: Attack mitigation settings

          deprecate_any_requests: Whether to refuse to answer queries for the ANY type

          ecs_fallback: Whether to forward client IP (resolver) subnet if no EDNS Client Subnet is sent

          maximum_cache_ttl: Maximum DNS cache TTL This setting sets an upper bound on DNS TTLs for purposes
              of caching between DNS Firewall and the upstream servers. Higher TTLs will be
              decreased to the maximum defined here for caching purposes.

          minimum_cache_ttl: Minimum DNS cache TTL This setting sets a lower bound on DNS TTLs for purposes
              of caching between DNS Firewall and the upstream servers. Lower TTLs will be
              increased to the minimum defined here for caching purposes.

          name: DNS Firewall cluster name

          negative_cache_ttl: Negative DNS cache TTL This setting controls how long DNS Firewall should cache
              negative responses (e.g., NXDOMAIN) from the upstream servers.

          ratelimit: Ratelimit in queries per second per datacenter (applies to DNS queries sent to
              the upstream nameservers configured on the cluster)

          retries: Number of retries for fetching DNS responses from upstream nameservers (not
              counting the initial attempt)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dns_firewall_id:
            raise ValueError(f"Expected a non-empty value for `dns_firewall_id` but received {dns_firewall_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/dns_firewall/{dns_firewall_id}",
            body=await async_maybe_transform(
                {
                    "attack_mitigation": attack_mitigation,
                    "deprecate_any_requests": deprecate_any_requests,
                    "ecs_fallback": ecs_fallback,
                    "maximum_cache_ttl": maximum_cache_ttl,
                    "minimum_cache_ttl": minimum_cache_ttl,
                    "name": name,
                    "negative_cache_ttl": negative_cache_ttl,
                    "ratelimit": ratelimit,
                    "retries": retries,
                    "upstream_ips": upstream_ips,
                },
                dns_firewall_edit_params.DNSFirewallEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DNSFirewallEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DNSFirewallEditResponse]], ResultWrapper[DNSFirewallEditResponse]),
        )

    async def get(
        self,
        dns_firewall_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DNSFirewallGetResponse]:
        """
        Show a single DNS Firewall cluster for an account

        Args:
          account_id: Identifier

          dns_firewall_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not dns_firewall_id:
            raise ValueError(f"Expected a non-empty value for `dns_firewall_id` but received {dns_firewall_id!r}")
        return await self._get(
            f"/accounts/{account_id}/dns_firewall/{dns_firewall_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DNSFirewallGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DNSFirewallGetResponse]], ResultWrapper[DNSFirewallGetResponse]),
        )


class DNSFirewallResourceWithRawResponse:
    def __init__(self, dns_firewall: DNSFirewallResource) -> None:
        self._dns_firewall = dns_firewall

        self.create = to_raw_response_wrapper(
            dns_firewall.create,
        )
        self.list = to_raw_response_wrapper(
            dns_firewall.list,
        )
        self.delete = to_raw_response_wrapper(
            dns_firewall.delete,
        )
        self.edit = to_raw_response_wrapper(
            dns_firewall.edit,
        )
        self.get = to_raw_response_wrapper(
            dns_firewall.get,
        )

    @cached_property
    def analytics(self) -> AnalyticsResourceWithRawResponse:
        return AnalyticsResourceWithRawResponse(self._dns_firewall.analytics)

    @cached_property
    def reverse_dns(self) -> ReverseDNSResourceWithRawResponse:
        return ReverseDNSResourceWithRawResponse(self._dns_firewall.reverse_dns)


class AsyncDNSFirewallResourceWithRawResponse:
    def __init__(self, dns_firewall: AsyncDNSFirewallResource) -> None:
        self._dns_firewall = dns_firewall

        self.create = async_to_raw_response_wrapper(
            dns_firewall.create,
        )
        self.list = async_to_raw_response_wrapper(
            dns_firewall.list,
        )
        self.delete = async_to_raw_response_wrapper(
            dns_firewall.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            dns_firewall.edit,
        )
        self.get = async_to_raw_response_wrapper(
            dns_firewall.get,
        )

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithRawResponse:
        return AsyncAnalyticsResourceWithRawResponse(self._dns_firewall.analytics)

    @cached_property
    def reverse_dns(self) -> AsyncReverseDNSResourceWithRawResponse:
        return AsyncReverseDNSResourceWithRawResponse(self._dns_firewall.reverse_dns)


class DNSFirewallResourceWithStreamingResponse:
    def __init__(self, dns_firewall: DNSFirewallResource) -> None:
        self._dns_firewall = dns_firewall

        self.create = to_streamed_response_wrapper(
            dns_firewall.create,
        )
        self.list = to_streamed_response_wrapper(
            dns_firewall.list,
        )
        self.delete = to_streamed_response_wrapper(
            dns_firewall.delete,
        )
        self.edit = to_streamed_response_wrapper(
            dns_firewall.edit,
        )
        self.get = to_streamed_response_wrapper(
            dns_firewall.get,
        )

    @cached_property
    def analytics(self) -> AnalyticsResourceWithStreamingResponse:
        return AnalyticsResourceWithStreamingResponse(self._dns_firewall.analytics)

    @cached_property
    def reverse_dns(self) -> ReverseDNSResourceWithStreamingResponse:
        return ReverseDNSResourceWithStreamingResponse(self._dns_firewall.reverse_dns)


class AsyncDNSFirewallResourceWithStreamingResponse:
    def __init__(self, dns_firewall: AsyncDNSFirewallResource) -> None:
        self._dns_firewall = dns_firewall

        self.create = async_to_streamed_response_wrapper(
            dns_firewall.create,
        )
        self.list = async_to_streamed_response_wrapper(
            dns_firewall.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            dns_firewall.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            dns_firewall.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            dns_firewall.get,
        )

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        return AsyncAnalyticsResourceWithStreamingResponse(self._dns_firewall.analytics)

    @cached_property
    def reverse_dns(self) -> AsyncReverseDNSResourceWithStreamingResponse:
        return AsyncReverseDNSResourceWithStreamingResponse(self._dns_firewall.reverse_dns)
