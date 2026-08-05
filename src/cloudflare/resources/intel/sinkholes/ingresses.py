# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

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
from ...._base_client import make_request_options
from ....types.intel.sinkholes import ingress_create_params, ingress_update_params
from ....types.intel.sinkholes.ingress_get_response import IngressGetResponse
from ....types.intel.sinkholes.ingress_create_response import IngressCreateResponse

__all__ = ["IngressesResource", "AsyncIngressesResource"]


class IngressesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IngressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return IngressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IngressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return IngressesResourceWithStreamingResponse(self)

    def create(
        self,
        sinkhole_id: str,
        *,
        zone_id: str,
        cidr: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[IngressCreateResponse]:
        """Create a new ingress rule for the specified sinkhole.

        The CIDR block must be a
        Cloudflare BYOIP associated with your account. The zone_id must be a zone with
        the ability to create Spectrum Apps. The sinkhole must belong to the same
        account as the zone.

        Args:
          zone_id: Identifier.

          cidr: The CIDR block for the ingress rule in IPv4 or IPv6 notation (e.g.,
              192.0.2.0/24). Must be a Cloudflare BYOIP associated with your account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not sinkhole_id:
            raise ValueError(f"Expected a non-empty value for `sinkhole_id` but received {sinkhole_id!r}")
        return self._post(
            path_template(
                "/zones/{zone_id}/intel/sinkholes/{sinkhole_id}/ingresses", zone_id=zone_id, sinkhole_id=sinkhole_id
            ),
            body=maybe_transform({"cidr": cidr}, ingress_create_params.IngressCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IngressCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IngressCreateResponse]], ResultWrapper[IngressCreateResponse]),
        )

    def update(
        self,
        ingress_id: str,
        *,
        zone_id: str,
        sinkhole_id: str,
        cidr: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Update the specified ingress rule.

        The sinkhole must belong to the same account
        as the zone.

        Args:
          zone_id: Identifier.

          cidr: The CIDR block for the ingress rule in IPv4 or IPv6 notation (e.g.,
              192.0.2.0/24). Must be a Cloudflare BYOIP associated with your account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not sinkhole_id:
            raise ValueError(f"Expected a non-empty value for `sinkhole_id` but received {sinkhole_id!r}")
        if not ingress_id:
            raise ValueError(f"Expected a non-empty value for `ingress_id` but received {ingress_id!r}")
        return self._put(
            path_template(
                "/zones/{zone_id}/intel/sinkholes/{sinkhole_id}/ingresses/{ingress_id}",
                zone_id=zone_id,
                sinkhole_id=sinkhole_id,
                ingress_id=ingress_id,
            ),
            body=maybe_transform({"cidr": cidr}, ingress_update_params.IngressUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def delete(
        self,
        ingress_id: str,
        *,
        zone_id: str,
        sinkhole_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Delete the specified ingress rule.

        The sinkhole must belong to the same account
        as the zone.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not sinkhole_id:
            raise ValueError(f"Expected a non-empty value for `sinkhole_id` but received {sinkhole_id!r}")
        if not ingress_id:
            raise ValueError(f"Expected a non-empty value for `ingress_id` but received {ingress_id!r}")
        return self._delete(
            path_template(
                "/zones/{zone_id}/intel/sinkholes/{sinkhole_id}/ingresses/{ingress_id}",
                zone_id=zone_id,
                sinkhole_id=sinkhole_id,
                ingress_id=ingress_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def get(
        self,
        ingress_id: str,
        *,
        zone_id: str,
        sinkhole_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[IngressGetResponse]:
        """Get the specified ingress rule associated with a sinkhole.

        The sinkhole must
        belong to the same account as the zone.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not sinkhole_id:
            raise ValueError(f"Expected a non-empty value for `sinkhole_id` but received {sinkhole_id!r}")
        if not ingress_id:
            raise ValueError(f"Expected a non-empty value for `ingress_id` but received {ingress_id!r}")
        return self._get(
            path_template(
                "/zones/{zone_id}/intel/sinkholes/{sinkhole_id}/ingresses/{ingress_id}",
                zone_id=zone_id,
                sinkhole_id=sinkhole_id,
                ingress_id=ingress_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IngressGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IngressGetResponse]], ResultWrapper[IngressGetResponse]),
        )


class AsyncIngressesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIngressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIngressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIngressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncIngressesResourceWithStreamingResponse(self)

    async def create(
        self,
        sinkhole_id: str,
        *,
        zone_id: str,
        cidr: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[IngressCreateResponse]:
        """Create a new ingress rule for the specified sinkhole.

        The CIDR block must be a
        Cloudflare BYOIP associated with your account. The zone_id must be a zone with
        the ability to create Spectrum Apps. The sinkhole must belong to the same
        account as the zone.

        Args:
          zone_id: Identifier.

          cidr: The CIDR block for the ingress rule in IPv4 or IPv6 notation (e.g.,
              192.0.2.0/24). Must be a Cloudflare BYOIP associated with your account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not sinkhole_id:
            raise ValueError(f"Expected a non-empty value for `sinkhole_id` but received {sinkhole_id!r}")
        return await self._post(
            path_template(
                "/zones/{zone_id}/intel/sinkholes/{sinkhole_id}/ingresses", zone_id=zone_id, sinkhole_id=sinkhole_id
            ),
            body=await async_maybe_transform({"cidr": cidr}, ingress_create_params.IngressCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IngressCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IngressCreateResponse]], ResultWrapper[IngressCreateResponse]),
        )

    async def update(
        self,
        ingress_id: str,
        *,
        zone_id: str,
        sinkhole_id: str,
        cidr: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Update the specified ingress rule.

        The sinkhole must belong to the same account
        as the zone.

        Args:
          zone_id: Identifier.

          cidr: The CIDR block for the ingress rule in IPv4 or IPv6 notation (e.g.,
              192.0.2.0/24). Must be a Cloudflare BYOIP associated with your account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not sinkhole_id:
            raise ValueError(f"Expected a non-empty value for `sinkhole_id` but received {sinkhole_id!r}")
        if not ingress_id:
            raise ValueError(f"Expected a non-empty value for `ingress_id` but received {ingress_id!r}")
        return await self._put(
            path_template(
                "/zones/{zone_id}/intel/sinkholes/{sinkhole_id}/ingresses/{ingress_id}",
                zone_id=zone_id,
                sinkhole_id=sinkhole_id,
                ingress_id=ingress_id,
            ),
            body=await async_maybe_transform({"cidr": cidr}, ingress_update_params.IngressUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def delete(
        self,
        ingress_id: str,
        *,
        zone_id: str,
        sinkhole_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Delete the specified ingress rule.

        The sinkhole must belong to the same account
        as the zone.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not sinkhole_id:
            raise ValueError(f"Expected a non-empty value for `sinkhole_id` but received {sinkhole_id!r}")
        if not ingress_id:
            raise ValueError(f"Expected a non-empty value for `ingress_id` but received {ingress_id!r}")
        return await self._delete(
            path_template(
                "/zones/{zone_id}/intel/sinkholes/{sinkhole_id}/ingresses/{ingress_id}",
                zone_id=zone_id,
                sinkhole_id=sinkhole_id,
                ingress_id=ingress_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def get(
        self,
        ingress_id: str,
        *,
        zone_id: str,
        sinkhole_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[IngressGetResponse]:
        """Get the specified ingress rule associated with a sinkhole.

        The sinkhole must
        belong to the same account as the zone.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not sinkhole_id:
            raise ValueError(f"Expected a non-empty value for `sinkhole_id` but received {sinkhole_id!r}")
        if not ingress_id:
            raise ValueError(f"Expected a non-empty value for `ingress_id` but received {ingress_id!r}")
        return await self._get(
            path_template(
                "/zones/{zone_id}/intel/sinkholes/{sinkhole_id}/ingresses/{ingress_id}",
                zone_id=zone_id,
                sinkhole_id=sinkhole_id,
                ingress_id=ingress_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[IngressGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[IngressGetResponse]], ResultWrapper[IngressGetResponse]),
        )


class IngressesResourceWithRawResponse:
    def __init__(self, ingresses: IngressesResource) -> None:
        self._ingresses = ingresses

        self.create = to_raw_response_wrapper(
            ingresses.create,
        )
        self.update = to_raw_response_wrapper(
            ingresses.update,
        )
        self.delete = to_raw_response_wrapper(
            ingresses.delete,
        )
        self.get = to_raw_response_wrapper(
            ingresses.get,
        )


class AsyncIngressesResourceWithRawResponse:
    def __init__(self, ingresses: AsyncIngressesResource) -> None:
        self._ingresses = ingresses

        self.create = async_to_raw_response_wrapper(
            ingresses.create,
        )
        self.update = async_to_raw_response_wrapper(
            ingresses.update,
        )
        self.delete = async_to_raw_response_wrapper(
            ingresses.delete,
        )
        self.get = async_to_raw_response_wrapper(
            ingresses.get,
        )


class IngressesResourceWithStreamingResponse:
    def __init__(self, ingresses: IngressesResource) -> None:
        self._ingresses = ingresses

        self.create = to_streamed_response_wrapper(
            ingresses.create,
        )
        self.update = to_streamed_response_wrapper(
            ingresses.update,
        )
        self.delete = to_streamed_response_wrapper(
            ingresses.delete,
        )
        self.get = to_streamed_response_wrapper(
            ingresses.get,
        )


class AsyncIngressesResourceWithStreamingResponse:
    def __init__(self, ingresses: AsyncIngressesResource) -> None:
        self._ingresses = ingresses

        self.create = async_to_streamed_response_wrapper(
            ingresses.create,
        )
        self.update = async_to_streamed_response_wrapper(
            ingresses.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            ingresses.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            ingresses.get,
        )
