# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.acms import TotalTLSUpdateResponse, TotalTLSGetResponse

from typing import Type

from typing_extensions import Literal

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
from ...types.acms import total_tls_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["TotalTLS", "AsyncTotalTLS"]


class TotalTLS(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TotalTLSWithRawResponse:
        return TotalTLSWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TotalTLSWithStreamingResponse:
        return TotalTLSWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        enabled: bool,
        certificate_authority: Literal["google", "lets_encrypt"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TotalTLSUpdateResponse:
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
                total_tls_update_params.TotalTLSUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TotalTLSUpdateResponse], ResultWrapper[TotalTLSUpdateResponse]),
        )

    def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TotalTLSGetResponse:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TotalTLSGetResponse], ResultWrapper[TotalTLSGetResponse]),
        )


class AsyncTotalTLS(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTotalTLSWithRawResponse:
        return AsyncTotalTLSWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTotalTLSWithStreamingResponse:
        return AsyncTotalTLSWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        enabled: bool,
        certificate_authority: Literal["google", "lets_encrypt"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TotalTLSUpdateResponse:
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
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "certificate_authority": certificate_authority,
                },
                total_tls_update_params.TotalTLSUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TotalTLSUpdateResponse], ResultWrapper[TotalTLSUpdateResponse]),
        )

    async def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TotalTLSGetResponse:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TotalTLSGetResponse], ResultWrapper[TotalTLSGetResponse]),
        )


class TotalTLSWithRawResponse:
    def __init__(self, total_tls: TotalTLS) -> None:
        self._total_tls = total_tls

        self.update = to_raw_response_wrapper(
            total_tls.update,
        )
        self.get = to_raw_response_wrapper(
            total_tls.get,
        )


class AsyncTotalTLSWithRawResponse:
    def __init__(self, total_tls: AsyncTotalTLS) -> None:
        self._total_tls = total_tls

        self.update = async_to_raw_response_wrapper(
            total_tls.update,
        )
        self.get = async_to_raw_response_wrapper(
            total_tls.get,
        )


class TotalTLSWithStreamingResponse:
    def __init__(self, total_tls: TotalTLS) -> None:
        self._total_tls = total_tls

        self.update = to_streamed_response_wrapper(
            total_tls.update,
        )
        self.get = to_streamed_response_wrapper(
            total_tls.get,
        )


class AsyncTotalTLSWithStreamingResponse:
    def __init__(self, total_tls: AsyncTotalTLS) -> None:
        self._total_tls = total_tls

        self.update = async_to_streamed_response_wrapper(
            total_tls.update,
        )
        self.get = async_to_streamed_response_wrapper(
            total_tls.get,
        )
