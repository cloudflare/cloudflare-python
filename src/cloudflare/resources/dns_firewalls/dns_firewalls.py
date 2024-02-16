# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .dns_analytics.dns_analytics import DNSAnalytics, AsyncDNSAnalytics

from ..._compat import cached_property

from ...types import (
    DNSFirewallCreateResponse,
    DNSFirewallUpdateResponse,
    DNSFirewallListResponse,
    DNSFirewallDeleteResponse,
    DNSFirewallGetResponse,
    dns_firewall_create_params,
    dns_firewall_update_params,
)

from typing import Type, List, Union, Optional

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types import dns_firewall_create_params
from ...types import dns_firewall_update_params
from ...types import dns_firewall_list_params
from .dns_analytics import (
    DNSAnalytics,
    AsyncDNSAnalytics,
    DNSAnalyticsWithRawResponse,
    AsyncDNSAnalyticsWithRawResponse,
    DNSAnalyticsWithStreamingResponse,
    AsyncDNSAnalyticsWithStreamingResponse,
)
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["DNSFirewalls", "AsyncDNSFirewalls"]


class DNSFirewalls(SyncAPIResource):
    @cached_property
    def dns_analytics(self) -> DNSAnalytics:
        return DNSAnalytics(self._client)

    @cached_property
    def with_raw_response(self) -> DNSFirewallsWithRawResponse:
        return DNSFirewallsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DNSFirewallsWithStreamingResponse:
        return DNSFirewallsWithStreamingResponse(self)

    def create(
        self,
        account_id: str,
        *,
        name: str,
        upstream_ips: List[Union[str, str]],
        attack_mitigation: Optional[dns_firewall_create_params.AttackMitigation] | NotGiven = NOT_GIVEN,
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
    ) -> DNSFirewallCreateResponse:
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
                dns_firewall_create_params.DNSFirewallCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DNSFirewallCreateResponse], ResultWrapper[DNSFirewallCreateResponse]),
        )

    def update(
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
        attack_mitigation: Optional[dns_firewall_update_params.AttackMitigation] | NotGiven = NOT_GIVEN,
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
    ) -> DNSFirewallUpdateResponse:
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
                dns_firewall_update_params.DNSFirewallUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DNSFirewallUpdateResponse], ResultWrapper[DNSFirewallUpdateResponse]),
        )

    def list(
        self,
        account_id: str,
        *,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DNSFirewallListResponse]:
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
        return self._get(
            f"/accounts/{account_id}/dns_firewall",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DNSFirewallListResponse]], ResultWrapper[DNSFirewallListResponse]),
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
    ) -> DNSFirewallDeleteResponse:
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
            cast_to=cast(Type[DNSFirewallDeleteResponse], ResultWrapper[DNSFirewallDeleteResponse]),
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
    ) -> DNSFirewallGetResponse:
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
            cast_to=cast(Type[DNSFirewallGetResponse], ResultWrapper[DNSFirewallGetResponse]),
        )


class AsyncDNSFirewalls(AsyncAPIResource):
    @cached_property
    def dns_analytics(self) -> AsyncDNSAnalytics:
        return AsyncDNSAnalytics(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDNSFirewallsWithRawResponse:
        return AsyncDNSFirewallsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDNSFirewallsWithStreamingResponse:
        return AsyncDNSFirewallsWithStreamingResponse(self)

    async def create(
        self,
        account_id: str,
        *,
        name: str,
        upstream_ips: List[Union[str, str]],
        attack_mitigation: Optional[dns_firewall_create_params.AttackMitigation] | NotGiven = NOT_GIVEN,
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
    ) -> DNSFirewallCreateResponse:
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
                dns_firewall_create_params.DNSFirewallCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DNSFirewallCreateResponse], ResultWrapper[DNSFirewallCreateResponse]),
        )

    async def update(
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
        attack_mitigation: Optional[dns_firewall_update_params.AttackMitigation] | NotGiven = NOT_GIVEN,
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
    ) -> DNSFirewallUpdateResponse:
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
                dns_firewall_update_params.DNSFirewallUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[DNSFirewallUpdateResponse], ResultWrapper[DNSFirewallUpdateResponse]),
        )

    async def list(
        self,
        account_id: str,
        *,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DNSFirewallListResponse]:
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
        return await self._get(
            f"/accounts/{account_id}/dns_firewall",
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[DNSFirewallListResponse]], ResultWrapper[DNSFirewallListResponse]),
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
    ) -> DNSFirewallDeleteResponse:
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
            cast_to=cast(Type[DNSFirewallDeleteResponse], ResultWrapper[DNSFirewallDeleteResponse]),
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
    ) -> DNSFirewallGetResponse:
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
            cast_to=cast(Type[DNSFirewallGetResponse], ResultWrapper[DNSFirewallGetResponse]),
        )


class DNSFirewallsWithRawResponse:
    def __init__(self, dns_firewalls: DNSFirewalls) -> None:
        self._dns_firewalls = dns_firewalls

        self.create = to_raw_response_wrapper(
            dns_firewalls.create,
        )
        self.update = to_raw_response_wrapper(
            dns_firewalls.update,
        )
        self.list = to_raw_response_wrapper(
            dns_firewalls.list,
        )
        self.delete = to_raw_response_wrapper(
            dns_firewalls.delete,
        )
        self.get = to_raw_response_wrapper(
            dns_firewalls.get,
        )

    @cached_property
    def dns_analytics(self) -> DNSAnalyticsWithRawResponse:
        return DNSAnalyticsWithRawResponse(self._dns_firewalls.dns_analytics)


class AsyncDNSFirewallsWithRawResponse:
    def __init__(self, dns_firewalls: AsyncDNSFirewalls) -> None:
        self._dns_firewalls = dns_firewalls

        self.create = async_to_raw_response_wrapper(
            dns_firewalls.create,
        )
        self.update = async_to_raw_response_wrapper(
            dns_firewalls.update,
        )
        self.list = async_to_raw_response_wrapper(
            dns_firewalls.list,
        )
        self.delete = async_to_raw_response_wrapper(
            dns_firewalls.delete,
        )
        self.get = async_to_raw_response_wrapper(
            dns_firewalls.get,
        )

    @cached_property
    def dns_analytics(self) -> AsyncDNSAnalyticsWithRawResponse:
        return AsyncDNSAnalyticsWithRawResponse(self._dns_firewalls.dns_analytics)


class DNSFirewallsWithStreamingResponse:
    def __init__(self, dns_firewalls: DNSFirewalls) -> None:
        self._dns_firewalls = dns_firewalls

        self.create = to_streamed_response_wrapper(
            dns_firewalls.create,
        )
        self.update = to_streamed_response_wrapper(
            dns_firewalls.update,
        )
        self.list = to_streamed_response_wrapper(
            dns_firewalls.list,
        )
        self.delete = to_streamed_response_wrapper(
            dns_firewalls.delete,
        )
        self.get = to_streamed_response_wrapper(
            dns_firewalls.get,
        )

    @cached_property
    def dns_analytics(self) -> DNSAnalyticsWithStreamingResponse:
        return DNSAnalyticsWithStreamingResponse(self._dns_firewalls.dns_analytics)


class AsyncDNSFirewallsWithStreamingResponse:
    def __init__(self, dns_firewalls: AsyncDNSFirewalls) -> None:
        self._dns_firewalls = dns_firewalls

        self.create = async_to_streamed_response_wrapper(
            dns_firewalls.create,
        )
        self.update = async_to_streamed_response_wrapper(
            dns_firewalls.update,
        )
        self.list = async_to_streamed_response_wrapper(
            dns_firewalls.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            dns_firewalls.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            dns_firewalls.get,
        )

    @cached_property
    def dns_analytics(self) -> AsyncDNSAnalyticsWithStreamingResponse:
        return AsyncDNSAnalyticsWithStreamingResponse(self._dns_firewalls.dns_analytics)
