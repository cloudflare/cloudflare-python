# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.ssls.certificate_packs import QuotaCertificatePacksGetCertificatePackQuotasResponse

from typing import Type

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
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Quotas", "AsyncQuotas"]


class Quotas(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QuotasWithRawResponse:
        return QuotasWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QuotasWithStreamingResponse:
        return QuotasWithStreamingResponse(self)

    def certificate_packs_get_certificate_pack_quotas(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QuotaCertificatePacksGetCertificatePackQuotasResponse:
        """
        For a given zone, list certificate pack quotas.

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
            f"/zones/{zone_id}/ssl/certificate_packs/quota",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[QuotaCertificatePacksGetCertificatePackQuotasResponse],
                ResultWrapper[QuotaCertificatePacksGetCertificatePackQuotasResponse],
            ),
        )


class AsyncQuotas(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQuotasWithRawResponse:
        return AsyncQuotasWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQuotasWithStreamingResponse:
        return AsyncQuotasWithStreamingResponse(self)

    async def certificate_packs_get_certificate_pack_quotas(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QuotaCertificatePacksGetCertificatePackQuotasResponse:
        """
        For a given zone, list certificate pack quotas.

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
            f"/zones/{zone_id}/ssl/certificate_packs/quota",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[QuotaCertificatePacksGetCertificatePackQuotasResponse],
                ResultWrapper[QuotaCertificatePacksGetCertificatePackQuotasResponse],
            ),
        )


class QuotasWithRawResponse:
    def __init__(self, quotas: Quotas) -> None:
        self._quotas = quotas

        self.certificate_packs_get_certificate_pack_quotas = to_raw_response_wrapper(
            quotas.certificate_packs_get_certificate_pack_quotas,
        )


class AsyncQuotasWithRawResponse:
    def __init__(self, quotas: AsyncQuotas) -> None:
        self._quotas = quotas

        self.certificate_packs_get_certificate_pack_quotas = async_to_raw_response_wrapper(
            quotas.certificate_packs_get_certificate_pack_quotas,
        )


class QuotasWithStreamingResponse:
    def __init__(self, quotas: Quotas) -> None:
        self._quotas = quotas

        self.certificate_packs_get_certificate_pack_quotas = to_streamed_response_wrapper(
            quotas.certificate_packs_get_certificate_pack_quotas,
        )


class AsyncQuotasWithStreamingResponse:
    def __init__(self, quotas: AsyncQuotas) -> None:
        self._quotas = quotas

        self.certificate_packs_get_certificate_pack_quotas = async_to_streamed_response_wrapper(
            quotas.certificate_packs_get_certificate_pack_quotas,
        )
