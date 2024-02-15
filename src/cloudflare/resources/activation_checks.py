# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types import ActivationCheckPutZonesZoneIDActivationCheckResponse

from typing import Type

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ..types import shared_params
from .._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["ActivationChecks", "AsyncActivationChecks"]


class ActivationChecks(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActivationChecksWithRawResponse:
        return ActivationChecksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActivationChecksWithStreamingResponse:
        return ActivationChecksWithStreamingResponse(self)

    def put_zones_zone_id_activation_check(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActivationCheckPutZonesZoneIDActivationCheckResponse:
        """Triggeres a new activation check for a PENDING Zone.

        This can be triggered every
        5 min for paygo/ent customers, every hour for FREE Zones.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/activation_check",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ActivationCheckPutZonesZoneIDActivationCheckResponse],
                ResultWrapper[ActivationCheckPutZonesZoneIDActivationCheckResponse],
            ),
        )


class AsyncActivationChecks(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActivationChecksWithRawResponse:
        return AsyncActivationChecksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActivationChecksWithStreamingResponse:
        return AsyncActivationChecksWithStreamingResponse(self)

    async def put_zones_zone_id_activation_check(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActivationCheckPutZonesZoneIDActivationCheckResponse:
        """Triggeres a new activation check for a PENDING Zone.

        This can be triggered every
        5 min for paygo/ent customers, every hour for FREE Zones.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/activation_check",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ActivationCheckPutZonesZoneIDActivationCheckResponse],
                ResultWrapper[ActivationCheckPutZonesZoneIDActivationCheckResponse],
            ),
        )


class ActivationChecksWithRawResponse:
    def __init__(self, activation_checks: ActivationChecks) -> None:
        self._activation_checks = activation_checks

        self.put_zones_zone_id_activation_check = to_raw_response_wrapper(
            activation_checks.put_zones_zone_id_activation_check,
        )


class AsyncActivationChecksWithRawResponse:
    def __init__(self, activation_checks: AsyncActivationChecks) -> None:
        self._activation_checks = activation_checks

        self.put_zones_zone_id_activation_check = async_to_raw_response_wrapper(
            activation_checks.put_zones_zone_id_activation_check,
        )


class ActivationChecksWithStreamingResponse:
    def __init__(self, activation_checks: ActivationChecks) -> None:
        self._activation_checks = activation_checks

        self.put_zones_zone_id_activation_check = to_streamed_response_wrapper(
            activation_checks.put_zones_zone_id_activation_check,
        )


class AsyncActivationChecksWithStreamingResponse:
    def __init__(self, activation_checks: AsyncActivationChecks) -> None:
        self._activation_checks = activation_checks

        self.put_zones_zone_id_activation_check = async_to_streamed_response_wrapper(
            activation_checks.put_zones_zone_id_activation_check,
        )
