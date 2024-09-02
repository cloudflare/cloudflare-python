# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.ssl.certificate_packs.quota_get_response import QuotaGetResponse

from ...._wrappers import ResultWrapper

from typing import Optional, Type

from ...._base_client import make_request_options

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
from ....types import shared_params
from typing import cast
from typing import cast

__all__ = ["QuotaResource", "AsyncQuotaResource"]


class QuotaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QuotaResourceWithRawResponse:
        return QuotaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QuotaResourceWithStreamingResponse:
        return QuotaResourceWithStreamingResponse(self)

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
    ) -> Optional[QuotaGetResponse]:
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
                post_parser=ResultWrapper[Optional[QuotaGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[QuotaGetResponse]], ResultWrapper[QuotaGetResponse]),
        )


class AsyncQuotaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQuotaResourceWithRawResponse:
        return AsyncQuotaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQuotaResourceWithStreamingResponse:
        return AsyncQuotaResourceWithStreamingResponse(self)

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
    ) -> Optional[QuotaGetResponse]:
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
                post_parser=ResultWrapper[Optional[QuotaGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[QuotaGetResponse]], ResultWrapper[QuotaGetResponse]),
        )


class QuotaResourceWithRawResponse:
    def __init__(self, quota: QuotaResource) -> None:
        self._quota = quota

        self.get = to_raw_response_wrapper(
            quota.get,
        )


class AsyncQuotaResourceWithRawResponse:
    def __init__(self, quota: AsyncQuotaResource) -> None:
        self._quota = quota

        self.get = async_to_raw_response_wrapper(
            quota.get,
        )


class QuotaResourceWithStreamingResponse:
    def __init__(self, quota: QuotaResource) -> None:
        self._quota = quota

        self.get = to_streamed_response_wrapper(
            quota.get,
        )


class AsyncQuotaResourceWithStreamingResponse:
    def __init__(self, quota: AsyncQuotaResource) -> None:
        self._quota = quota

        self.get = async_to_streamed_response_wrapper(
            quota.get,
        )
