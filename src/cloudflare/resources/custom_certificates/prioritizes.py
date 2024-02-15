# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.custom_certificates import (
    PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponse,
    prioritize_custom_ssl_for_a_zone_re_prioritize_ssl_certificates_params,
)

__all__ = ["Prioritizes", "AsyncPrioritizes"]


class Prioritizes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrioritizesWithRawResponse:
        return PrioritizesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrioritizesWithStreamingResponse:
        return PrioritizesWithStreamingResponse(self)

    def custom_ssl_for_a_zone_re_prioritize_ssl_certificates(
        self,
        zone_id: str,
        *,
        certificates: Iterable[prioritize_custom_ssl_for_a_zone_re_prioritize_ssl_certificates_params.Certificate],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponse]:
        """
        If a zone has multiple SSL certificates, you can set the order in which they
        should be used during a request. The higher priority will break ties across
        overlapping 'legacy_custom' certificates.

        Args:
          zone_id: Identifier

          certificates: Array of ordered certificates.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/custom_certificates/prioritize",
            body=maybe_transform(
                {"certificates": certificates},
                prioritize_custom_ssl_for_a_zone_re_prioritize_ssl_certificates_params.PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponse]],
                ResultWrapper[PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponse],
            ),
        )


class AsyncPrioritizes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrioritizesWithRawResponse:
        return AsyncPrioritizesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrioritizesWithStreamingResponse:
        return AsyncPrioritizesWithStreamingResponse(self)

    async def custom_ssl_for_a_zone_re_prioritize_ssl_certificates(
        self,
        zone_id: str,
        *,
        certificates: Iterable[prioritize_custom_ssl_for_a_zone_re_prioritize_ssl_certificates_params.Certificate],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponse]:
        """
        If a zone has multiple SSL certificates, you can set the order in which they
        should be used during a request. The higher priority will break ties across
        overlapping 'legacy_custom' certificates.

        Args:
          zone_id: Identifier

          certificates: Array of ordered certificates.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/custom_certificates/prioritize",
            body=maybe_transform(
                {"certificates": certificates},
                prioritize_custom_ssl_for_a_zone_re_prioritize_ssl_certificates_params.PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponse]],
                ResultWrapper[PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponse],
            ),
        )


class PrioritizesWithRawResponse:
    def __init__(self, prioritizes: Prioritizes) -> None:
        self._prioritizes = prioritizes

        self.custom_ssl_for_a_zone_re_prioritize_ssl_certificates = to_raw_response_wrapper(
            prioritizes.custom_ssl_for_a_zone_re_prioritize_ssl_certificates,
        )


class AsyncPrioritizesWithRawResponse:
    def __init__(self, prioritizes: AsyncPrioritizes) -> None:
        self._prioritizes = prioritizes

        self.custom_ssl_for_a_zone_re_prioritize_ssl_certificates = async_to_raw_response_wrapper(
            prioritizes.custom_ssl_for_a_zone_re_prioritize_ssl_certificates,
        )


class PrioritizesWithStreamingResponse:
    def __init__(self, prioritizes: Prioritizes) -> None:
        self._prioritizes = prioritizes

        self.custom_ssl_for_a_zone_re_prioritize_ssl_certificates = to_streamed_response_wrapper(
            prioritizes.custom_ssl_for_a_zone_re_prioritize_ssl_certificates,
        )


class AsyncPrioritizesWithStreamingResponse:
    def __init__(self, prioritizes: AsyncPrioritizes) -> None:
        self._prioritizes = prioritizes

        self.custom_ssl_for_a_zone_re_prioritize_ssl_certificates = async_to_streamed_response_wrapper(
            prioritizes.custom_ssl_for_a_zone_re_prioritize_ssl_certificates,
        )
