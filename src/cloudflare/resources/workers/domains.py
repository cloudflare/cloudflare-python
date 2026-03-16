# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.workers import domain_list_params, domain_update_params
from ...types.workers.domain_get_response import DomainGetResponse
from ...types.workers.domain_list_response import DomainListResponse
from ...types.workers.domain_delete_response import DomainDeleteResponse
from ...types.workers.domain_update_response import DomainUpdateResponse

__all__ = ["DomainsResource", "AsyncDomainsResource"]


class DomainsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DomainsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        account_id: str,
        hostname: str,
        service: str,
        environment: str | Omit = omit,
        zone_id: str | Omit = omit,
        zone_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainUpdateResponse:
        """
        Attaches a domain that routes traffic to a Worker.

        Args:
          account_id: Identifier.

          hostname: Hostname of the domain. Can be either the zone apex or a subdomain of the zone.
              Requests to this hostname will be routed to the configured Worker.

          service: Name of the Worker associated with the domain. Requests to the configured
              hostname will be routed to this Worker.

          environment: Worker environment associated with the domain.

          zone_id: ID of the zone containing the domain hostname.

          zone_name: Name of the zone containing the domain hostname.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/workers/domains",
            body=maybe_transform(
                {
                    "hostname": hostname,
                    "service": service,
                    "environment": environment,
                    "zone_id": zone_id,
                    "zone_name": zone_name,
                },
                domain_update_params.DomainUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DomainUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[DomainUpdateResponse], ResultWrapper[DomainUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        environment: str | Omit = omit,
        hostname: str | Omit = omit,
        service: str | Omit = omit,
        zone_id: str | Omit = omit,
        zone_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[DomainListResponse]:
        """
        Lists all domains for an account.

        Args:
          account_id: Identifier.

          environment: Worker environment associated with the domain.

          hostname: Hostname of the domain.

          service: Name of the Worker associated with the domain.

          zone_id: ID of the zone containing the domain hostname.

          zone_name: Name of the zone containing the domain hostname.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/workers/domains",
            page=SyncSinglePage[DomainListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "hostname": hostname,
                        "service": service,
                        "zone_id": zone_id,
                        "zone_name": zone_name,
                    },
                    domain_list_params.DomainListParams,
                ),
            ),
            model=DomainListResponse,
        )

    def delete(
        self,
        domain_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainDeleteResponse:
        """Detaches a domain from a Worker.

        Both the Worker and all of its previews are no
        longer routable using this domain.

        Args:
          account_id: Identifier.

          domain_id: ID of the domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return self._delete(
            f"/accounts/{account_id}/workers/domains/{domain_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainDeleteResponse,
        )

    def get(
        self,
        domain_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainGetResponse:
        """
        Gets information about a domain.

        Args:
          account_id: Identifier.

          domain_id: ID of the domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return self._get(
            f"/accounts/{account_id}/workers/domains/{domain_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DomainGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[DomainGetResponse], ResultWrapper[DomainGetResponse]),
        )


class AsyncDomainsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDomainsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        account_id: str,
        hostname: str,
        service: str,
        environment: str | Omit = omit,
        zone_id: str | Omit = omit,
        zone_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainUpdateResponse:
        """
        Attaches a domain that routes traffic to a Worker.

        Args:
          account_id: Identifier.

          hostname: Hostname of the domain. Can be either the zone apex or a subdomain of the zone.
              Requests to this hostname will be routed to the configured Worker.

          service: Name of the Worker associated with the domain. Requests to the configured
              hostname will be routed to this Worker.

          environment: Worker environment associated with the domain.

          zone_id: ID of the zone containing the domain hostname.

          zone_name: Name of the zone containing the domain hostname.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/workers/domains",
            body=await async_maybe_transform(
                {
                    "hostname": hostname,
                    "service": service,
                    "environment": environment,
                    "zone_id": zone_id,
                    "zone_name": zone_name,
                },
                domain_update_params.DomainUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DomainUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[DomainUpdateResponse], ResultWrapper[DomainUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        environment: str | Omit = omit,
        hostname: str | Omit = omit,
        service: str | Omit = omit,
        zone_id: str | Omit = omit,
        zone_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DomainListResponse, AsyncSinglePage[DomainListResponse]]:
        """
        Lists all domains for an account.

        Args:
          account_id: Identifier.

          environment: Worker environment associated with the domain.

          hostname: Hostname of the domain.

          service: Name of the Worker associated with the domain.

          zone_id: ID of the zone containing the domain hostname.

          zone_name: Name of the zone containing the domain hostname.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/workers/domains",
            page=AsyncSinglePage[DomainListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "environment": environment,
                        "hostname": hostname,
                        "service": service,
                        "zone_id": zone_id,
                        "zone_name": zone_name,
                    },
                    domain_list_params.DomainListParams,
                ),
            ),
            model=DomainListResponse,
        )

    async def delete(
        self,
        domain_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainDeleteResponse:
        """Detaches a domain from a Worker.

        Both the Worker and all of its previews are no
        longer routable using this domain.

        Args:
          account_id: Identifier.

          domain_id: ID of the domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/workers/domains/{domain_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainDeleteResponse,
        )

    async def get(
        self,
        domain_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainGetResponse:
        """
        Gets information about a domain.

        Args:
          account_id: Identifier.

          domain_id: ID of the domain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not domain_id:
            raise ValueError(f"Expected a non-empty value for `domain_id` but received {domain_id!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/domains/{domain_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[DomainGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[DomainGetResponse], ResultWrapper[DomainGetResponse]),
        )


class DomainsResourceWithRawResponse:
    def __init__(self, domains: DomainsResource) -> None:
        self._domains = domains

        self.update = to_raw_response_wrapper(
            domains.update,
        )
        self.list = to_raw_response_wrapper(
            domains.list,
        )
        self.delete = to_raw_response_wrapper(
            domains.delete,
        )
        self.get = to_raw_response_wrapper(
            domains.get,
        )


class AsyncDomainsResourceWithRawResponse:
    def __init__(self, domains: AsyncDomainsResource) -> None:
        self._domains = domains

        self.update = async_to_raw_response_wrapper(
            domains.update,
        )
        self.list = async_to_raw_response_wrapper(
            domains.list,
        )
        self.delete = async_to_raw_response_wrapper(
            domains.delete,
        )
        self.get = async_to_raw_response_wrapper(
            domains.get,
        )


class DomainsResourceWithStreamingResponse:
    def __init__(self, domains: DomainsResource) -> None:
        self._domains = domains

        self.update = to_streamed_response_wrapper(
            domains.update,
        )
        self.list = to_streamed_response_wrapper(
            domains.list,
        )
        self.delete = to_streamed_response_wrapper(
            domains.delete,
        )
        self.get = to_streamed_response_wrapper(
            domains.get,
        )


class AsyncDomainsResourceWithStreamingResponse:
    def __init__(self, domains: AsyncDomainsResource) -> None:
        self._domains = domains

        self.update = async_to_streamed_response_wrapper(
            domains.update,
        )
        self.list = async_to_streamed_response_wrapper(
            domains.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            domains.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            domains.get,
        )
