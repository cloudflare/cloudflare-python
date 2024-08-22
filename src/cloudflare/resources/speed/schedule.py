# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.speed.schedule_create_response import ScheduleCreateResponse

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ..._base_client import make_request_options

from typing_extensions import Literal

from ...types.speed.schedule_delete_response import ScheduleDeleteResponse

from ...types.speed.schedule import Schedule

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.speed import schedule_create_params
from ...types.speed import schedule_delete_params
from ...types.speed import schedule_get_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["ScheduleResource", "AsyncScheduleResource"]

class ScheduleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScheduleResourceWithRawResponse:
        return ScheduleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScheduleResourceWithStreamingResponse:
        return ScheduleResourceWithStreamingResponse(self)

    def create(self,
    url: str,
    *,
    zone_id: str,
    region: Literal["asia-east1", "asia-northeast1", "asia-northeast2", "asia-south1", "asia-southeast1", "australia-southeast1", "europe-north1", "europe-southwest1", "europe-west1", "europe-west2", "europe-west3", "europe-west4", "europe-west8", "europe-west9", "me-west1", "southamerica-east1", "us-central1", "us-east1", "us-east4", "us-south1", "us-west1"] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[ScheduleCreateResponse]:
        """
        Creates a scheduled test for a page.

        Args:
          zone_id: Identifier

          url: A URL.

          region: A test region.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not url:
          raise ValueError(
            f'Expected a non-empty value for `url` but received {url!r}'
          )
        return self._post(
            f"/zones/{zone_id}/speed_api/schedule/{url}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "region": region
            }, schedule_create_params.ScheduleCreateParams), post_parser=ResultWrapper[Optional[ScheduleCreateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[ScheduleCreateResponse]], ResultWrapper[ScheduleCreateResponse]),
        )

    def delete(self,
    url: str,
    *,
    zone_id: str,
    region: Literal["asia-east1", "asia-northeast1", "asia-northeast2", "asia-south1", "asia-southeast1", "australia-southeast1", "europe-north1", "europe-southwest1", "europe-west1", "europe-west2", "europe-west3", "europe-west4", "europe-west8", "europe-west9", "me-west1", "southamerica-east1", "us-central1", "us-east1", "us-east4", "us-south1", "us-west1"] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[ScheduleDeleteResponse]:
        """
        Deletes a scheduled test for a page.

        Args:
          zone_id: Identifier

          url: A URL.

          region: A test region.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not url:
          raise ValueError(
            f'Expected a non-empty value for `url` but received {url!r}'
          )
        return self._delete(
            f"/zones/{zone_id}/speed_api/schedule/{url}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "region": region
            }, schedule_delete_params.ScheduleDeleteParams), post_parser=ResultWrapper[Optional[ScheduleDeleteResponse]]._unwrapper),
            cast_to=cast(Type[Optional[ScheduleDeleteResponse]], ResultWrapper[ScheduleDeleteResponse]),
        )

    def get(self,
    url: str,
    *,
    zone_id: str,
    region: Literal["asia-east1", "asia-northeast1", "asia-northeast2", "asia-south1", "asia-southeast1", "australia-southeast1", "europe-north1", "europe-southwest1", "europe-west1", "europe-west2", "europe-west3", "europe-west4", "europe-west8", "europe-west9", "me-west1", "southamerica-east1", "us-central1", "us-east1", "us-east4", "us-south1", "us-west1"] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Schedule]:
        """
        Retrieves the test schedule for a page in a specific region.

        Args:
          zone_id: Identifier

          url: A URL.

          region: A test region.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not url:
          raise ValueError(
            f'Expected a non-empty value for `url` but received {url!r}'
          )
        return self._get(
            f"/zones/{zone_id}/speed_api/schedule/{url}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "region": region
            }, schedule_get_params.ScheduleGetParams), post_parser=ResultWrapper[Optional[Schedule]]._unwrapper),
            cast_to=cast(Type[Optional[Schedule]], ResultWrapper[Schedule]),
        )

class AsyncScheduleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScheduleResourceWithRawResponse:
        return AsyncScheduleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScheduleResourceWithStreamingResponse:
        return AsyncScheduleResourceWithStreamingResponse(self)

    async def create(self,
    url: str,
    *,
    zone_id: str,
    region: Literal["asia-east1", "asia-northeast1", "asia-northeast2", "asia-south1", "asia-southeast1", "australia-southeast1", "europe-north1", "europe-southwest1", "europe-west1", "europe-west2", "europe-west3", "europe-west4", "europe-west8", "europe-west9", "me-west1", "southamerica-east1", "us-central1", "us-east1", "us-east4", "us-south1", "us-west1"] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[ScheduleCreateResponse]:
        """
        Creates a scheduled test for a page.

        Args:
          zone_id: Identifier

          url: A URL.

          region: A test region.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not url:
          raise ValueError(
            f'Expected a non-empty value for `url` but received {url!r}'
          )
        return await self._post(
            f"/zones/{zone_id}/speed_api/schedule/{url}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "region": region
            }, schedule_create_params.ScheduleCreateParams), post_parser=ResultWrapper[Optional[ScheduleCreateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[ScheduleCreateResponse]], ResultWrapper[ScheduleCreateResponse]),
        )

    async def delete(self,
    url: str,
    *,
    zone_id: str,
    region: Literal["asia-east1", "asia-northeast1", "asia-northeast2", "asia-south1", "asia-southeast1", "australia-southeast1", "europe-north1", "europe-southwest1", "europe-west1", "europe-west2", "europe-west3", "europe-west4", "europe-west8", "europe-west9", "me-west1", "southamerica-east1", "us-central1", "us-east1", "us-east4", "us-south1", "us-west1"] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[ScheduleDeleteResponse]:
        """
        Deletes a scheduled test for a page.

        Args:
          zone_id: Identifier

          url: A URL.

          region: A test region.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not url:
          raise ValueError(
            f'Expected a non-empty value for `url` but received {url!r}'
          )
        return await self._delete(
            f"/zones/{zone_id}/speed_api/schedule/{url}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "region": region
            }, schedule_delete_params.ScheduleDeleteParams), post_parser=ResultWrapper[Optional[ScheduleDeleteResponse]]._unwrapper),
            cast_to=cast(Type[Optional[ScheduleDeleteResponse]], ResultWrapper[ScheduleDeleteResponse]),
        )

    async def get(self,
    url: str,
    *,
    zone_id: str,
    region: Literal["asia-east1", "asia-northeast1", "asia-northeast2", "asia-south1", "asia-southeast1", "australia-southeast1", "europe-north1", "europe-southwest1", "europe-west1", "europe-west2", "europe-west3", "europe-west4", "europe-west8", "europe-west9", "me-west1", "southamerica-east1", "us-central1", "us-east1", "us-east4", "us-south1", "us-west1"] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Schedule]:
        """
        Retrieves the test schedule for a page in a specific region.

        Args:
          zone_id: Identifier

          url: A URL.

          region: A test region.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not url:
          raise ValueError(
            f'Expected a non-empty value for `url` but received {url!r}'
          )
        return await self._get(
            f"/zones/{zone_id}/speed_api/schedule/{url}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "region": region
            }, schedule_get_params.ScheduleGetParams), post_parser=ResultWrapper[Optional[Schedule]]._unwrapper),
            cast_to=cast(Type[Optional[Schedule]], ResultWrapper[Schedule]),
        )

class ScheduleResourceWithRawResponse:
    def __init__(self, schedule: ScheduleResource) -> None:
        self._schedule = schedule

        self.create = to_raw_response_wrapper(
            schedule.create,
        )
        self.delete = to_raw_response_wrapper(
            schedule.delete,
        )
        self.get = to_raw_response_wrapper(
            schedule.get,
        )

class AsyncScheduleResourceWithRawResponse:
    def __init__(self, schedule: AsyncScheduleResource) -> None:
        self._schedule = schedule

        self.create = async_to_raw_response_wrapper(
            schedule.create,
        )
        self.delete = async_to_raw_response_wrapper(
            schedule.delete,
        )
        self.get = async_to_raw_response_wrapper(
            schedule.get,
        )

class ScheduleResourceWithStreamingResponse:
    def __init__(self, schedule: ScheduleResource) -> None:
        self._schedule = schedule

        self.create = to_streamed_response_wrapper(
            schedule.create,
        )
        self.delete = to_streamed_response_wrapper(
            schedule.delete,
        )
        self.get = to_streamed_response_wrapper(
            schedule.get,
        )

class AsyncScheduleResourceWithStreamingResponse:
    def __init__(self, schedule: AsyncScheduleResource) -> None:
        self._schedule = schedule

        self.create = async_to_streamed_response_wrapper(
            schedule.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            schedule.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            schedule.get,
        )