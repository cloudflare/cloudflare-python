# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast
from typing_extensions import Literal

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
from ....types.ssl.host import Host
from ....types.ssl.certificate_packs import order_create_params
from ....types.ssl.certificate_packs.order_create_response import OrderCreateResponse

__all__ = ["OrderResource", "AsyncOrderResource"]


class OrderResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrderResourceWithRawResponse:
        return OrderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrderResourceWithStreamingResponse:
        return OrderResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        certificate_authority: Literal["google", "lets_encrypt", "ssl_com"],
        hosts: List[Host],
        type: Literal["advanced"],
        validation_method: Literal["txt", "http", "email"],
        validity_days: Literal[14, 30, 90, 365],
        cloudflare_branding: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OrderCreateResponse]:
        """
        For a given zone, order an advanced certificate pack.

        Args:
          zone_id: Identifier

          certificate_authority: Certificate Authority selected for the order. For information on any certificate
              authority specific details or restrictions
              [see this page for more details.](https://developers.cloudflare.com/ssl/reference/certificate-authorities)

          hosts: Comma separated list of valid host names for the certificate packs. Must contain
              the zone apex, may not contain more than 50 hosts, and may not be empty.

          type: Type of certificate pack.

          validation_method: Validation Method selected for the order.

          validity_days: Validity Days selected for the order.

          cloudflare_branding: Whether or not to add Cloudflare Branding for the order. This will add
              sni.cloudflaressl.com as the Common Name if set true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/ssl/certificate_packs/order",
            body=maybe_transform(
                {
                    "certificate_authority": certificate_authority,
                    "hosts": hosts,
                    "type": type,
                    "validation_method": validation_method,
                    "validity_days": validity_days,
                    "cloudflare_branding": cloudflare_branding,
                },
                order_create_params.OrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OrderCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OrderCreateResponse]], ResultWrapper[OrderCreateResponse]),
        )


class AsyncOrderResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrderResourceWithRawResponse:
        return AsyncOrderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrderResourceWithStreamingResponse:
        return AsyncOrderResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        certificate_authority: Literal["google", "lets_encrypt", "ssl_com"],
        hosts: List[Host],
        type: Literal["advanced"],
        validation_method: Literal["txt", "http", "email"],
        validity_days: Literal[14, 30, 90, 365],
        cloudflare_branding: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OrderCreateResponse]:
        """
        For a given zone, order an advanced certificate pack.

        Args:
          zone_id: Identifier

          certificate_authority: Certificate Authority selected for the order. For information on any certificate
              authority specific details or restrictions
              [see this page for more details.](https://developers.cloudflare.com/ssl/reference/certificate-authorities)

          hosts: Comma separated list of valid host names for the certificate packs. Must contain
              the zone apex, may not contain more than 50 hosts, and may not be empty.

          type: Type of certificate pack.

          validation_method: Validation Method selected for the order.

          validity_days: Validity Days selected for the order.

          cloudflare_branding: Whether or not to add Cloudflare Branding for the order. This will add
              sni.cloudflaressl.com as the Common Name if set true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/ssl/certificate_packs/order",
            body=await async_maybe_transform(
                {
                    "certificate_authority": certificate_authority,
                    "hosts": hosts,
                    "type": type,
                    "validation_method": validation_method,
                    "validity_days": validity_days,
                    "cloudflare_branding": cloudflare_branding,
                },
                order_create_params.OrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OrderCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OrderCreateResponse]], ResultWrapper[OrderCreateResponse]),
        )


class OrderResourceWithRawResponse:
    def __init__(self, order: OrderResource) -> None:
        self._order = order

        self.create = to_raw_response_wrapper(
            order.create,
        )


class AsyncOrderResourceWithRawResponse:
    def __init__(self, order: AsyncOrderResource) -> None:
        self._order = order

        self.create = async_to_raw_response_wrapper(
            order.create,
        )


class OrderResourceWithStreamingResponse:
    def __init__(self, order: OrderResource) -> None:
        self._order = order

        self.create = to_streamed_response_wrapper(
            order.create,
        )


class AsyncOrderResourceWithStreamingResponse:
    def __init__(self, order: AsyncOrderResource) -> None:
        self._order = order

        self.create = async_to_streamed_response_wrapper(
            order.create,
        )
