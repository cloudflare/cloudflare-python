# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ...types.acm import CertificateAuthority, total_tls_create_params
from ..._base_client import (
    make_request_options,
)
from ...types.acm.certificate_authority import CertificateAuthority
from ...types.acm.total_tls_get_response import TotalTLSGetResponse
from ...types.acm.total_tls_create_response import TotalTLSCreateResponse

__all__ = ["TotalTLSResource", "AsyncTotalTLSResource"]


class TotalTLSResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TotalTLSResourceWithRawResponse:
        return TotalTLSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TotalTLSResourceWithStreamingResponse:
        return TotalTLSResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        enabled: bool,
        certificate_authority: CertificateAuthority | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TotalTLSCreateResponse]:
        """
        Set Total TLS Settings or disable the feature for a Zone.

        Args:
          zone_id: Identifier

          enabled: If enabled, Total TLS will order a hostname specific TLS certificate for any
              proxied A, AAAA, or CNAME record in your zone.

          certificate_authority: The Certificate Authority that Total TLS certificates will be issued through.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/acm/total_tls",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "certificate_authority": certificate_authority,
                },
                total_tls_create_params.TotalTLSCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TotalTLSCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TotalTLSCreateResponse]], ResultWrapper[TotalTLSCreateResponse]),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TotalTLSGetResponse]:
        """
        Get Total TLS Settings for a Zone.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/acm/total_tls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TotalTLSGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TotalTLSGetResponse]], ResultWrapper[TotalTLSGetResponse]),
        )


class AsyncTotalTLSResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTotalTLSResourceWithRawResponse:
        return AsyncTotalTLSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTotalTLSResourceWithStreamingResponse:
        return AsyncTotalTLSResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        enabled: bool,
        certificate_authority: CertificateAuthority | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TotalTLSCreateResponse]:
        """
        Set Total TLS Settings or disable the feature for a Zone.

        Args:
          zone_id: Identifier

          enabled: If enabled, Total TLS will order a hostname specific TLS certificate for any
              proxied A, AAAA, or CNAME record in your zone.

          certificate_authority: The Certificate Authority that Total TLS certificates will be issued through.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/acm/total_tls",
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "certificate_authority": certificate_authority,
                },
                total_tls_create_params.TotalTLSCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TotalTLSCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TotalTLSCreateResponse]], ResultWrapper[TotalTLSCreateResponse]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TotalTLSGetResponse]:
        """
        Get Total TLS Settings for a Zone.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/acm/total_tls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[TotalTLSGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[TotalTLSGetResponse]], ResultWrapper[TotalTLSGetResponse]),
        )


class TotalTLSResourceWithRawResponse:
    def __init__(self, total_tls: TotalTLSResource) -> None:
        self._total_tls = total_tls

        self.create = to_raw_response_wrapper(
            total_tls.create,
        )
        self.get = to_raw_response_wrapper(
            total_tls.get,
        )


class AsyncTotalTLSResourceWithRawResponse:
    def __init__(self, total_tls: AsyncTotalTLSResource) -> None:
        self._total_tls = total_tls

        self.create = async_to_raw_response_wrapper(
            total_tls.create,
        )
        self.get = async_to_raw_response_wrapper(
            total_tls.get,
        )


class TotalTLSResourceWithStreamingResponse:
    def __init__(self, total_tls: TotalTLSResource) -> None:
        self._total_tls = total_tls

        self.create = to_streamed_response_wrapper(
            total_tls.create,
        )
        self.get = to_streamed_response_wrapper(
            total_tls.get,
        )


class AsyncTotalTLSResourceWithStreamingResponse:
    def __init__(self, total_tls: AsyncTotalTLSResource) -> None:
        self._total_tls = total_tls

        self.create = async_to_streamed_response_wrapper(
            total_tls.create,
        )
        self.get = async_to_streamed_response_wrapper(
            total_tls.get,
        )
