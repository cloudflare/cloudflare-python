# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.ssls.certificate_packs import OrderCertificatePacksOrderAdvancedCertificateManagerCertificatePackResponse

from typing import Type, List

from typing_extensions import Literal

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.ssls.certificate_packs import (
    order_certificate_packs_order_advanced_certificate_manager_certificate_pack_params,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Orders", "AsyncOrders"]


class Orders(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrdersWithRawResponse:
        return OrdersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrdersWithStreamingResponse:
        return OrdersWithStreamingResponse(self)

    def certificate_packs_order_advanced_certificate_manager_certificate_pack(
        self,
        zone_id: str,
        *,
        certificate_authority: Literal["google", "lets_encrypt"],
        hosts: List[str],
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
    ) -> OrderCertificatePacksOrderAdvancedCertificateManagerCertificatePackResponse:
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
                order_certificate_packs_order_advanced_certificate_manager_certificate_pack_params.OrderCertificatePacksOrderAdvancedCertificateManagerCertificatePackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[OrderCertificatePacksOrderAdvancedCertificateManagerCertificatePackResponse],
                ResultWrapper[OrderCertificatePacksOrderAdvancedCertificateManagerCertificatePackResponse],
            ),
        )


class AsyncOrders(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrdersWithRawResponse:
        return AsyncOrdersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrdersWithStreamingResponse:
        return AsyncOrdersWithStreamingResponse(self)

    async def certificate_packs_order_advanced_certificate_manager_certificate_pack(
        self,
        zone_id: str,
        *,
        certificate_authority: Literal["google", "lets_encrypt"],
        hosts: List[str],
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
    ) -> OrderCertificatePacksOrderAdvancedCertificateManagerCertificatePackResponse:
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
            body=maybe_transform(
                {
                    "certificate_authority": certificate_authority,
                    "hosts": hosts,
                    "type": type,
                    "validation_method": validation_method,
                    "validity_days": validity_days,
                    "cloudflare_branding": cloudflare_branding,
                },
                order_certificate_packs_order_advanced_certificate_manager_certificate_pack_params.OrderCertificatePacksOrderAdvancedCertificateManagerCertificatePackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[OrderCertificatePacksOrderAdvancedCertificateManagerCertificatePackResponse],
                ResultWrapper[OrderCertificatePacksOrderAdvancedCertificateManagerCertificatePackResponse],
            ),
        )


class OrdersWithRawResponse:
    def __init__(self, orders: Orders) -> None:
        self._orders = orders

        self.certificate_packs_order_advanced_certificate_manager_certificate_pack = to_raw_response_wrapper(
            orders.certificate_packs_order_advanced_certificate_manager_certificate_pack,
        )


class AsyncOrdersWithRawResponse:
    def __init__(self, orders: AsyncOrders) -> None:
        self._orders = orders

        self.certificate_packs_order_advanced_certificate_manager_certificate_pack = async_to_raw_response_wrapper(
            orders.certificate_packs_order_advanced_certificate_manager_certificate_pack,
        )


class OrdersWithStreamingResponse:
    def __init__(self, orders: Orders) -> None:
        self._orders = orders

        self.certificate_packs_order_advanced_certificate_manager_certificate_pack = to_streamed_response_wrapper(
            orders.certificate_packs_order_advanced_certificate_manager_certificate_pack,
        )


class AsyncOrdersWithStreamingResponse:
    def __init__(self, orders: AsyncOrders) -> None:
        self._orders = orders

        self.certificate_packs_order_advanced_certificate_manager_certificate_pack = async_to_streamed_response_wrapper(
            orders.certificate_packs_order_advanced_certificate_manager_certificate_pack,
        )
