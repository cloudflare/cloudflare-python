# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.custom_certificates.prioritize_update_response import PrioritizeUpdateResponse

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type, Iterable

from ..._base_client import make_request_options

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from ...types.custom_certificates import prioritize_update_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.custom_certificates import prioritize_update_params
from typing import cast
from typing import cast

__all__ = ["PrioritizeResource", "AsyncPrioritizeResource"]

class PrioritizeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrioritizeResourceWithRawResponse:
        return PrioritizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrioritizeResourceWithStreamingResponse:
        return PrioritizeResourceWithStreamingResponse(self)

    def update(self,
    *,
    zone_id: str,
    certificates: Iterable[prioritize_update_params.Certificate],
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[PrioritizeUpdateResponse]:
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
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        return self._put(
            f"/zones/{zone_id}/custom_certificates/prioritize",
            body=maybe_transform({
                "certificates": certificates
            }, prioritize_update_params.PrioritizeUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[PrioritizeUpdateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[PrioritizeUpdateResponse]], ResultWrapper[PrioritizeUpdateResponse]),
        )

class AsyncPrioritizeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrioritizeResourceWithRawResponse:
        return AsyncPrioritizeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrioritizeResourceWithStreamingResponse:
        return AsyncPrioritizeResourceWithStreamingResponse(self)

    async def update(self,
    *,
    zone_id: str,
    certificates: Iterable[prioritize_update_params.Certificate],
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[PrioritizeUpdateResponse]:
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
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        return await self._put(
            f"/zones/{zone_id}/custom_certificates/prioritize",
            body=await async_maybe_transform({
                "certificates": certificates
            }, prioritize_update_params.PrioritizeUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[PrioritizeUpdateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[PrioritizeUpdateResponse]], ResultWrapper[PrioritizeUpdateResponse]),
        )

class PrioritizeResourceWithRawResponse:
    def __init__(self, prioritize: PrioritizeResource) -> None:
        self._prioritize = prioritize

        self.update = to_raw_response_wrapper(
            prioritize.update,
        )

class AsyncPrioritizeResourceWithRawResponse:
    def __init__(self, prioritize: AsyncPrioritizeResource) -> None:
        self._prioritize = prioritize

        self.update = async_to_raw_response_wrapper(
            prioritize.update,
        )

class PrioritizeResourceWithStreamingResponse:
    def __init__(self, prioritize: PrioritizeResource) -> None:
        self._prioritize = prioritize

        self.update = to_streamed_response_wrapper(
            prioritize.update,
        )

class AsyncPrioritizeResourceWithStreamingResponse:
    def __init__(self, prioritize: AsyncPrioritizeResource) -> None:
        self._prioritize = prioritize

        self.update = async_to_streamed_response_wrapper(
            prioritize.update,
        )