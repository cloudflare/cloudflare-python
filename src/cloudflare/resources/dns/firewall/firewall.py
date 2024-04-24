# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .analytics import (
    AnalyticsResource,
    AsyncAnalyticsResource,
    AnalyticsResourceWithRawResponse,
    AsyncAnalyticsResourceWithRawResponse,
    AnalyticsResourceWithStreamingResponse,
    AsyncAnalyticsResourceWithStreamingResponse,
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
from ....types.dns import firewall_edit_params, firewall_list_params, firewall_create_params
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from .analytics.analytics import AnalyticsResource, AsyncAnalyticsResource
from ....types.dns.firewall.firewall import Firewall
from ....types.dns.firewall_ips_param import FirewallIPsParam
from ....types.dns.upstream_ips_param import UpstreamIPsParam
from ....types.dns.attack_mitigation_param import AttackMitigationParam
from ....types.dns.firewall_delete_response import FirewallDeleteResponse

__all__ = ["FirewallResource", "AsyncFirewallResource"]


class FirewallResource(SyncAPIResource):
    @cached_property
    def analytics(self) -> AnalyticsResource:
        return AnalyticsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FirewallResourceWithRawResponse:
        return FirewallResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FirewallResourceWithStreamingResponse:
        return FirewallResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        upstream_ips: List[UpstreamIPsParam],
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
    ) -> Firewall:
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
                post_parser=ResultWrapper[Firewall]._unwrapper,
            ),
            cast_to=cast(Type[Firewall], ResultWrapper[Firewall]),
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
    ) -> SyncV4PagePaginationArray[Firewall]:
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
            page=SyncV4PagePaginationArray[Firewall],
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
            model=Firewall,
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
                post_parser=ResultWrapper[FirewallDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[FirewallDeleteResponse], ResultWrapper[FirewallDeleteResponse]),
        )

    def edit(
        self,
        dns_firewall_id: str,
        *,
        account_id: str,
        deprecate_any_requests: bool,
        dns_firewall_ips: List[FirewallIPsParam],
        ecs_fallback: bool,
        maximum_cache_ttl: float,
        minimum_cache_ttl: float,
        name: str,
        upstream_ips: List[UpstreamIPsParam],
        attack_mitigation: Optional[AttackMitigationParam] | NotGiven = NOT_GIVEN,
        negative_cache_ttl: Optional[float] | NotGiven = NOT_GIVEN,
        ratelimit: Optional[float] | NotGiven = NOT_GIVEN,
        retries: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Firewall:
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
                post_parser=ResultWrapper[Firewall]._unwrapper,
            ),
            cast_to=cast(Type[Firewall], ResultWrapper[Firewall]),
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
    ) -> Firewall:
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
                post_parser=ResultWrapper[Firewall]._unwrapper,
            ),
            cast_to=cast(Type[Firewall], ResultWrapper[Firewall]),
        )


class AsyncFirewallResource(AsyncAPIResource):
    @cached_property
    def analytics(self) -> AsyncAnalyticsResource:
        return AsyncAnalyticsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFirewallResourceWithRawResponse:
        return AsyncFirewallResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFirewallResourceWithStreamingResponse:
        return AsyncFirewallResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        upstream_ips: List[UpstreamIPsParam],
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
    ) -> Firewall:
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
                post_parser=ResultWrapper[Firewall]._unwrapper,
            ),
            cast_to=cast(Type[Firewall], ResultWrapper[Firewall]),
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
    ) -> AsyncPaginator[Firewall, AsyncV4PagePaginationArray[Firewall]]:
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
            page=AsyncV4PagePaginationArray[Firewall],
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
            model=Firewall,
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
                post_parser=ResultWrapper[FirewallDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[FirewallDeleteResponse], ResultWrapper[FirewallDeleteResponse]),
        )

    async def edit(
        self,
        dns_firewall_id: str,
        *,
        account_id: str,
        deprecate_any_requests: bool,
        dns_firewall_ips: List[FirewallIPsParam],
        ecs_fallback: bool,
        maximum_cache_ttl: float,
        minimum_cache_ttl: float,
        name: str,
        upstream_ips: List[UpstreamIPsParam],
        attack_mitigation: Optional[AttackMitigationParam] | NotGiven = NOT_GIVEN,
        negative_cache_ttl: Optional[float] | NotGiven = NOT_GIVEN,
        ratelimit: Optional[float] | NotGiven = NOT_GIVEN,
        retries: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Firewall:
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
                post_parser=ResultWrapper[Firewall]._unwrapper,
            ),
            cast_to=cast(Type[Firewall], ResultWrapper[Firewall]),
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
    ) -> Firewall:
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
                post_parser=ResultWrapper[Firewall]._unwrapper,
            ),
            cast_to=cast(Type[Firewall], ResultWrapper[Firewall]),
        )


class FirewallResourceWithRawResponse:
    def __init__(self, firewall: FirewallResource) -> None:
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
    def analytics(self) -> AnalyticsResourceWithRawResponse:
        return AnalyticsResourceWithRawResponse(self._firewall.analytics)


class AsyncFirewallResourceWithRawResponse:
    def __init__(self, firewall: AsyncFirewallResource) -> None:
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
    def analytics(self) -> AsyncAnalyticsResourceWithRawResponse:
        return AsyncAnalyticsResourceWithRawResponse(self._firewall.analytics)


class FirewallResourceWithStreamingResponse:
    def __init__(self, firewall: FirewallResource) -> None:
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
    def analytics(self) -> AnalyticsResourceWithStreamingResponse:
        return AnalyticsResourceWithStreamingResponse(self._firewall.analytics)


class AsyncFirewallResourceWithStreamingResponse:
    def __init__(self, firewall: AsyncFirewallResource) -> None:
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
    def analytics(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        return AsyncAnalyticsResourceWithStreamingResponse(self._firewall.analytics)
