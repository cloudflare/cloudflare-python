# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Union, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .analytics import (
    Analytics,
    AsyncAnalytics,
    AnalyticsWithRawResponse,
    AsyncAnalyticsWithRawResponse,
    AnalyticsWithStreamingResponse,
    AsyncAnalyticsWithStreamingResponse,
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
from ....types.dns import (
    DNSFirewallDNSFirewall,
    FirewallDeleteResponse,
    firewall_edit_params,
    firewall_list_params,
    firewall_create_params,
)
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from .analytics.analytics import Analytics, AsyncAnalytics

__all__ = ["Firewall", "AsyncFirewall"]


class Firewall(SyncAPIResource):
    @cached_property
    def analytics(self) -> Analytics:
        return Analytics(self._client)

    @cached_property
    def with_raw_response(self) -> FirewallWithRawResponse:
        return FirewallWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FirewallWithStreamingResponse:
        return FirewallWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        upstream_ips: List[Union[str, str]],
        attack_mitigation: Optional[firewall_create_params.AttackMitigation] | NotGiven = NOT_GIVEN,
        deprecate_any_requests: bool | NotGiven = NOT_GIVEN,
        ecs_fallback: bool | NotGiven = NOT_GIVEN,
        maximum_cache_ttl: float | NotGiven = NOT_GIVEN,
        minimum_cache_ttl: float | NotGiven = NOT_GIVEN,
        negative_cache_ttl: Optional[float] | NotGiven = NOT_GIVEN,
        origin_ips: object | NotGiven = NOT_GIVEN,
        ratelimit: Optional[float] | NotGiven = NOT_GIVEN,
        retries: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSFirewallDNSFirewall:
        """
        Create a configured DNS Firewall Cluster.

        Args:
          account_id: Identifier

          name: DNS Firewall Cluster Name.

          attack_mitigation: Attack mitigation settings.

          deprecate_any_requests: Deprecate the response to ANY requests.

          ecs_fallback: Forward client IP (resolver) subnet if no EDNS Client Subnet is sent.

          maximum_cache_ttl: Maximum DNS Cache TTL.

          minimum_cache_ttl: Minimum DNS Cache TTL.

          negative_cache_ttl: Negative DNS Cache TTL.

          origin_ips: Deprecated alias for "upstream_ips".

          ratelimit: Ratelimit in queries per second per datacenter (applies to DNS queries sent to
              the upstream nameservers configured on the cluster).

          retries: Number of retries for fetching DNS responses from upstream nameservers (not
              counting the initial attempt).

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
                    "origin_ips": origin_ips,
                    "ratelimit": ratelimit,
                    "retries": retries,
                },
                firewall_create_params.FirewallCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DNSFirewallDNSFirewall], ResultWrapper[DNSFirewallDNSFirewall]),
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
    ) -> SyncV4PagePaginationArray[DNSFirewallDNSFirewall]:
        """
        List configured DNS Firewall clusters for an account.

        Args:
          account_id: Identifier

          page: Page number of paginated results.

          per_page: Number of clusters per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/dns_firewall",
            page=SyncV4PagePaginationArray[DNSFirewallDNSFirewall],
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
                    firewall_list_params.FirewallListParams,
                ),
            ),
            model=DNSFirewallDNSFirewall,
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
    ) -> FirewallDeleteResponse:
        """
        Delete a configured DNS Firewall Cluster.

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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[FirewallDeleteResponse], ResultWrapper[FirewallDeleteResponse]),
        )

    def edit(
        self,
        dns_firewall_id: str,
        *,
        account_id: str,
        deprecate_any_requests: bool,
        dns_firewall_ips: List[Union[str, str]],
        ecs_fallback: bool,
        maximum_cache_ttl: float,
        minimum_cache_ttl: float,
        name: str,
        upstream_ips: List[Union[str, str]],
        attack_mitigation: Optional[firewall_edit_params.AttackMitigation] | NotGiven = NOT_GIVEN,
        negative_cache_ttl: Optional[float] | NotGiven = NOT_GIVEN,
        origin_ips: object | NotGiven = NOT_GIVEN,
        ratelimit: Optional[float] | NotGiven = NOT_GIVEN,
        retries: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSFirewallDNSFirewall:
        """
        Modify a DNS Firewall Cluster configuration.

        Args:
          account_id: Identifier

          dns_firewall_id: Identifier

          deprecate_any_requests: Deprecate the response to ANY requests.

          ecs_fallback: Forward client IP (resolver) subnet if no EDNS Client Subnet is sent.

          maximum_cache_ttl: Maximum DNS Cache TTL.

          minimum_cache_ttl: Minimum DNS Cache TTL.

          name: DNS Firewall Cluster Name.

          attack_mitigation: Attack mitigation settings.

          negative_cache_ttl: Negative DNS Cache TTL.

          origin_ips: Deprecated alias for "upstream_ips".

          ratelimit: Ratelimit in queries per second per datacenter (applies to DNS queries sent to
              the upstream nameservers configured on the cluster).

          retries: Number of retries for fetching DNS responses from upstream nameservers (not
              counting the initial attempt).

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
                    "deprecate_any_requests": deprecate_any_requests,
                    "dns_firewall_ips": dns_firewall_ips,
                    "ecs_fallback": ecs_fallback,
                    "maximum_cache_ttl": maximum_cache_ttl,
                    "minimum_cache_ttl": minimum_cache_ttl,
                    "name": name,
                    "upstream_ips": upstream_ips,
                    "attack_mitigation": attack_mitigation,
                    "negative_cache_ttl": negative_cache_ttl,
                    "origin_ips": origin_ips,
                    "ratelimit": ratelimit,
                    "retries": retries,
                },
                firewall_edit_params.FirewallEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DNSFirewallDNSFirewall], ResultWrapper[DNSFirewallDNSFirewall]),
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
    ) -> DNSFirewallDNSFirewall:
        """
        Show a single configured DNS Firewall cluster for an account.

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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DNSFirewallDNSFirewall], ResultWrapper[DNSFirewallDNSFirewall]),
        )


class AsyncFirewall(AsyncAPIResource):
    @cached_property
    def analytics(self) -> AsyncAnalytics:
        return AsyncAnalytics(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFirewallWithRawResponse:
        return AsyncFirewallWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFirewallWithStreamingResponse:
        return AsyncFirewallWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        upstream_ips: List[Union[str, str]],
        attack_mitigation: Optional[firewall_create_params.AttackMitigation] | NotGiven = NOT_GIVEN,
        deprecate_any_requests: bool | NotGiven = NOT_GIVEN,
        ecs_fallback: bool | NotGiven = NOT_GIVEN,
        maximum_cache_ttl: float | NotGiven = NOT_GIVEN,
        minimum_cache_ttl: float | NotGiven = NOT_GIVEN,
        negative_cache_ttl: Optional[float] | NotGiven = NOT_GIVEN,
        origin_ips: object | NotGiven = NOT_GIVEN,
        ratelimit: Optional[float] | NotGiven = NOT_GIVEN,
        retries: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSFirewallDNSFirewall:
        """
        Create a configured DNS Firewall Cluster.

        Args:
          account_id: Identifier

          name: DNS Firewall Cluster Name.

          attack_mitigation: Attack mitigation settings.

          deprecate_any_requests: Deprecate the response to ANY requests.

          ecs_fallback: Forward client IP (resolver) subnet if no EDNS Client Subnet is sent.

          maximum_cache_ttl: Maximum DNS Cache TTL.

          minimum_cache_ttl: Minimum DNS Cache TTL.

          negative_cache_ttl: Negative DNS Cache TTL.

          origin_ips: Deprecated alias for "upstream_ips".

          ratelimit: Ratelimit in queries per second per datacenter (applies to DNS queries sent to
              the upstream nameservers configured on the cluster).

          retries: Number of retries for fetching DNS responses from upstream nameservers (not
              counting the initial attempt).

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
                    "origin_ips": origin_ips,
                    "ratelimit": ratelimit,
                    "retries": retries,
                },
                firewall_create_params.FirewallCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DNSFirewallDNSFirewall], ResultWrapper[DNSFirewallDNSFirewall]),
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
    ) -> AsyncPaginator[DNSFirewallDNSFirewall, AsyncV4PagePaginationArray[DNSFirewallDNSFirewall]]:
        """
        List configured DNS Firewall clusters for an account.

        Args:
          account_id: Identifier

          page: Page number of paginated results.

          per_page: Number of clusters per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/dns_firewall",
            page=AsyncV4PagePaginationArray[DNSFirewallDNSFirewall],
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
                    firewall_list_params.FirewallListParams,
                ),
            ),
            model=DNSFirewallDNSFirewall,
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
    ) -> FirewallDeleteResponse:
        """
        Delete a configured DNS Firewall Cluster.

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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[FirewallDeleteResponse], ResultWrapper[FirewallDeleteResponse]),
        )

    async def edit(
        self,
        dns_firewall_id: str,
        *,
        account_id: str,
        deprecate_any_requests: bool,
        dns_firewall_ips: List[Union[str, str]],
        ecs_fallback: bool,
        maximum_cache_ttl: float,
        minimum_cache_ttl: float,
        name: str,
        upstream_ips: List[Union[str, str]],
        attack_mitigation: Optional[firewall_edit_params.AttackMitigation] | NotGiven = NOT_GIVEN,
        negative_cache_ttl: Optional[float] | NotGiven = NOT_GIVEN,
        origin_ips: object | NotGiven = NOT_GIVEN,
        ratelimit: Optional[float] | NotGiven = NOT_GIVEN,
        retries: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DNSFirewallDNSFirewall:
        """
        Modify a DNS Firewall Cluster configuration.

        Args:
          account_id: Identifier

          dns_firewall_id: Identifier

          deprecate_any_requests: Deprecate the response to ANY requests.

          ecs_fallback: Forward client IP (resolver) subnet if no EDNS Client Subnet is sent.

          maximum_cache_ttl: Maximum DNS Cache TTL.

          minimum_cache_ttl: Minimum DNS Cache TTL.

          name: DNS Firewall Cluster Name.

          attack_mitigation: Attack mitigation settings.

          negative_cache_ttl: Negative DNS Cache TTL.

          origin_ips: Deprecated alias for "upstream_ips".

          ratelimit: Ratelimit in queries per second per datacenter (applies to DNS queries sent to
              the upstream nameservers configured on the cluster).

          retries: Number of retries for fetching DNS responses from upstream nameservers (not
              counting the initial attempt).

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
                    "deprecate_any_requests": deprecate_any_requests,
                    "dns_firewall_ips": dns_firewall_ips,
                    "ecs_fallback": ecs_fallback,
                    "maximum_cache_ttl": maximum_cache_ttl,
                    "minimum_cache_ttl": minimum_cache_ttl,
                    "name": name,
                    "upstream_ips": upstream_ips,
                    "attack_mitigation": attack_mitigation,
                    "negative_cache_ttl": negative_cache_ttl,
                    "origin_ips": origin_ips,
                    "ratelimit": ratelimit,
                    "retries": retries,
                },
                firewall_edit_params.FirewallEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DNSFirewallDNSFirewall], ResultWrapper[DNSFirewallDNSFirewall]),
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
    ) -> DNSFirewallDNSFirewall:
        """
        Show a single configured DNS Firewall cluster for an account.

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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DNSFirewallDNSFirewall], ResultWrapper[DNSFirewallDNSFirewall]),
        )


class FirewallWithRawResponse:
    def __init__(self, firewall: Firewall) -> None:
        self._firewall = firewall

        self.create = to_raw_response_wrapper(
            firewall.create,
        )
        self.list = to_raw_response_wrapper(
            firewall.list,
        )
        self.delete = to_raw_response_wrapper(
            firewall.delete,
        )
        self.edit = to_raw_response_wrapper(
            firewall.edit,
        )
        self.get = to_raw_response_wrapper(
            firewall.get,
        )

    @cached_property
    def analytics(self) -> AnalyticsWithRawResponse:
        return AnalyticsWithRawResponse(self._firewall.analytics)


class AsyncFirewallWithRawResponse:
    def __init__(self, firewall: AsyncFirewall) -> None:
        self._firewall = firewall

        self.create = async_to_raw_response_wrapper(
            firewall.create,
        )
        self.list = async_to_raw_response_wrapper(
            firewall.list,
        )
        self.delete = async_to_raw_response_wrapper(
            firewall.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            firewall.edit,
        )
        self.get = async_to_raw_response_wrapper(
            firewall.get,
        )

    @cached_property
    def analytics(self) -> AsyncAnalyticsWithRawResponse:
        return AsyncAnalyticsWithRawResponse(self._firewall.analytics)


class FirewallWithStreamingResponse:
    def __init__(self, firewall: Firewall) -> None:
        self._firewall = firewall

        self.create = to_streamed_response_wrapper(
            firewall.create,
        )
        self.list = to_streamed_response_wrapper(
            firewall.list,
        )
        self.delete = to_streamed_response_wrapper(
            firewall.delete,
        )
        self.edit = to_streamed_response_wrapper(
            firewall.edit,
        )
        self.get = to_streamed_response_wrapper(
            firewall.get,
        )

    @cached_property
    def analytics(self) -> AnalyticsWithStreamingResponse:
        return AnalyticsWithStreamingResponse(self._firewall.analytics)


class AsyncFirewallWithStreamingResponse:
    def __init__(self, firewall: AsyncFirewall) -> None:
        self._firewall = firewall

        self.create = async_to_streamed_response_wrapper(
            firewall.create,
        )
        self.list = async_to_streamed_response_wrapper(
            firewall.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            firewall.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            firewall.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            firewall.get,
        )

    @cached_property
    def analytics(self) -> AsyncAnalyticsWithStreamingResponse:
        return AsyncAnalyticsWithStreamingResponse(self._firewall.analytics)
