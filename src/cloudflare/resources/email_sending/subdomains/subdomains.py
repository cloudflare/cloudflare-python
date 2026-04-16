# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .dns import (
    DNSResource,
    AsyncDNSResource,
    DNSResourceWithRawResponse,
    AsyncDNSResourceWithRawResponse,
    DNSResourceWithStreamingResponse,
    AsyncDNSResourceWithStreamingResponse,
)
from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.email_sending import subdomain_create_params
from ....types.email_sending.subdomain_get_response import SubdomainGetResponse
from ....types.email_sending.subdomain_list_response import SubdomainListResponse
from ....types.email_sending.subdomain_create_response import SubdomainCreateResponse
from ....types.email_sending.subdomain_delete_response import SubdomainDeleteResponse

__all__ = ["SubdomainsResource", "AsyncSubdomainsResource"]


class SubdomainsResource(SyncAPIResource):
    @cached_property
    def dns(self) -> DNSResource:
        return DNSResource(self._client)

    @cached_property
    def with_raw_response(self) -> SubdomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SubdomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubdomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SubdomainsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str | None = None,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SubdomainCreateResponse]:
        """
        Creates a new sending subdomain or re-enables sending on an existing subdomain
        that had it disabled. If zone-level Email Sending has not been enabled yet, the
        zone flag is automatically set when the entitlement is present.

        Args:
          zone_id: Identifier.

          name: The subdomain name. Must be within the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            path_template("/zones/{zone_id}/email/sending/subdomains", zone_id=zone_id),
            body=maybe_transform({"name": name}, subdomain_create_params.SubdomainCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SubdomainCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SubdomainCreateResponse]], ResultWrapper[SubdomainCreateResponse]),
        )

    def list(
        self,
        *,
        zone_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[SubdomainListResponse]:
        """
        Lists all sending-enabled subdomains for the zone.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            path_template("/zones/{zone_id}/email/sending/subdomains", zone_id=zone_id),
            page=SyncSinglePage[SubdomainListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SubdomainListResponse,
        )

    def delete(
        self,
        subdomain_id: str,
        *,
        zone_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubdomainDeleteResponse:
        """Disables sending on a subdomain and removes its DNS records.

        If routing is still
        active on the subdomain, only sending is disabled.

        Args:
          zone_id: Identifier.

          subdomain_id: Sending subdomain identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not subdomain_id:
            raise ValueError(f"Expected a non-empty value for `subdomain_id` but received {subdomain_id!r}")
        return self._delete(
            path_template(
                "/zones/{zone_id}/email/sending/subdomains/{subdomain_id}", zone_id=zone_id, subdomain_id=subdomain_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubdomainDeleteResponse,
        )

    def get(
        self,
        subdomain_id: str,
        *,
        zone_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SubdomainGetResponse]:
        """
        Gets information for a specific sending subdomain.

        Args:
          zone_id: Identifier.

          subdomain_id: Sending subdomain identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not subdomain_id:
            raise ValueError(f"Expected a non-empty value for `subdomain_id` but received {subdomain_id!r}")
        return self._get(
            path_template(
                "/zones/{zone_id}/email/sending/subdomains/{subdomain_id}", zone_id=zone_id, subdomain_id=subdomain_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SubdomainGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SubdomainGetResponse]], ResultWrapper[SubdomainGetResponse]),
        )


class AsyncSubdomainsResource(AsyncAPIResource):
    @cached_property
    def dns(self) -> AsyncDNSResource:
        return AsyncDNSResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSubdomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubdomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubdomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSubdomainsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str | None = None,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SubdomainCreateResponse]:
        """
        Creates a new sending subdomain or re-enables sending on an existing subdomain
        that had it disabled. If zone-level Email Sending has not been enabled yet, the
        zone flag is automatically set when the entitlement is present.

        Args:
          zone_id: Identifier.

          name: The subdomain name. Must be within the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            path_template("/zones/{zone_id}/email/sending/subdomains", zone_id=zone_id),
            body=await async_maybe_transform({"name": name}, subdomain_create_params.SubdomainCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SubdomainCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SubdomainCreateResponse]], ResultWrapper[SubdomainCreateResponse]),
        )

    def list(
        self,
        *,
        zone_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SubdomainListResponse, AsyncSinglePage[SubdomainListResponse]]:
        """
        Lists all sending-enabled subdomains for the zone.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            path_template("/zones/{zone_id}/email/sending/subdomains", zone_id=zone_id),
            page=AsyncSinglePage[SubdomainListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=SubdomainListResponse,
        )

    async def delete(
        self,
        subdomain_id: str,
        *,
        zone_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubdomainDeleteResponse:
        """Disables sending on a subdomain and removes its DNS records.

        If routing is still
        active on the subdomain, only sending is disabled.

        Args:
          zone_id: Identifier.

          subdomain_id: Sending subdomain identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not subdomain_id:
            raise ValueError(f"Expected a non-empty value for `subdomain_id` but received {subdomain_id!r}")
        return await self._delete(
            path_template(
                "/zones/{zone_id}/email/sending/subdomains/{subdomain_id}", zone_id=zone_id, subdomain_id=subdomain_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubdomainDeleteResponse,
        )

    async def get(
        self,
        subdomain_id: str,
        *,
        zone_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SubdomainGetResponse]:
        """
        Gets information for a specific sending subdomain.

        Args:
          zone_id: Identifier.

          subdomain_id: Sending subdomain identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if zone_id is None:
            zone_id = self._client._get_zone_id_path_param()
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not subdomain_id:
            raise ValueError(f"Expected a non-empty value for `subdomain_id` but received {subdomain_id!r}")
        return await self._get(
            path_template(
                "/zones/{zone_id}/email/sending/subdomains/{subdomain_id}", zone_id=zone_id, subdomain_id=subdomain_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[SubdomainGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[SubdomainGetResponse]], ResultWrapper[SubdomainGetResponse]),
        )


class SubdomainsResourceWithRawResponse:
    def __init__(self, subdomains: SubdomainsResource) -> None:
        self._subdomains = subdomains

        self.create = to_raw_response_wrapper(
            subdomains.create,
        )
        self.list = to_raw_response_wrapper(
            subdomains.list,
        )
        self.delete = to_raw_response_wrapper(
            subdomains.delete,
        )
        self.get = to_raw_response_wrapper(
            subdomains.get,
        )

    @cached_property
    def dns(self) -> DNSResourceWithRawResponse:
        return DNSResourceWithRawResponse(self._subdomains.dns)


class AsyncSubdomainsResourceWithRawResponse:
    def __init__(self, subdomains: AsyncSubdomainsResource) -> None:
        self._subdomains = subdomains

        self.create = async_to_raw_response_wrapper(
            subdomains.create,
        )
        self.list = async_to_raw_response_wrapper(
            subdomains.list,
        )
        self.delete = async_to_raw_response_wrapper(
            subdomains.delete,
        )
        self.get = async_to_raw_response_wrapper(
            subdomains.get,
        )

    @cached_property
    def dns(self) -> AsyncDNSResourceWithRawResponse:
        return AsyncDNSResourceWithRawResponse(self._subdomains.dns)


class SubdomainsResourceWithStreamingResponse:
    def __init__(self, subdomains: SubdomainsResource) -> None:
        self._subdomains = subdomains

        self.create = to_streamed_response_wrapper(
            subdomains.create,
        )
        self.list = to_streamed_response_wrapper(
            subdomains.list,
        )
        self.delete = to_streamed_response_wrapper(
            subdomains.delete,
        )
        self.get = to_streamed_response_wrapper(
            subdomains.get,
        )

    @cached_property
    def dns(self) -> DNSResourceWithStreamingResponse:
        return DNSResourceWithStreamingResponse(self._subdomains.dns)


class AsyncSubdomainsResourceWithStreamingResponse:
    def __init__(self, subdomains: AsyncSubdomainsResource) -> None:
        self._subdomains = subdomains

        self.create = async_to_streamed_response_wrapper(
            subdomains.create,
        )
        self.list = async_to_streamed_response_wrapper(
            subdomains.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            subdomains.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            subdomains.get,
        )

    @cached_property
    def dns(self) -> AsyncDNSResourceWithStreamingResponse:
        return AsyncDNSResourceWithStreamingResponse(self._subdomains.dns)
