# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.logs.rayid_get_response import RayIDGetResponse

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options

from typing_extensions import Literal

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.logs import rayid_get_params
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["RayIDResource", "AsyncRayIDResource"]

class RayIDResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RayIDResourceWithRawResponse:
        return RayIDResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RayIDResourceWithStreamingResponse:
        return RayIDResourceWithStreamingResponse(self)

    def get(self,
    rayid: str,
    *,
    zone_id: str,
    fields: str | NotGiven = NOT_GIVEN,
    timestamps: Literal["unix", "unixnano", "rfc3339"] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RayIDGetResponse:
        """The `/rayids` api route allows lookups by specific rayid.

        The rayids route will
        return zero, one, or more records (ray ids are not unique).

        Args:
          zone_id: Identifier

          rayid: Ray identifier.

          fields: The `/received` route by default returns a limited set of fields, and allows
              customers to override the default field set by specifying individual fields. The
              reasons for this are: 1. Most customers require only a small subset of fields,
              but that subset varies from customer to customer; 2. Flat schema is much easier
              to work with downstream (importing into BigTable etc); 3. Performance (time to
              process, file size). If `?fields=` is not specified, default field set is
              returned. This default field set may change at any time. When `?fields=` is
              provided, each record is returned with the specified fields. `fields` must be
              specified as a comma separated list without any whitespaces, and all fields must
              exist. The order in which fields are specified does not matter, and the order of
              fields in the response is not specified.

          timestamps: By default, timestamps in responses are returned as Unix nanosecond integers.
              The `?timestamps=` argument can be set to change the format in which response
              timestamps are returned. Possible values are: `unix`, `unixnano`, `rfc3339`.
              Note that `unix` and `unixnano` return timestamps as integers; `rfc3339` returns
              timestamps as strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not rayid:
          raise ValueError(
            f'Expected a non-empty value for `rayid` but received {rayid!r}'
          )
        return cast(RayIDGetResponse, self._get(
            f"/zones/{zone_id}/logs/rayids/{rayid}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "fields": fields,
                "timestamps": timestamps,
            }, rayid_get_params.RayIDGetParams)),
            cast_to=cast(Any, RayIDGetResponse),  # Union types cannot be passed in as arguments in the type system
        ))

class AsyncRayIDResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRayIDResourceWithRawResponse:
        return AsyncRayIDResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRayIDResourceWithStreamingResponse:
        return AsyncRayIDResourceWithStreamingResponse(self)

    async def get(self,
    rayid: str,
    *,
    zone_id: str,
    fields: str | NotGiven = NOT_GIVEN,
    timestamps: Literal["unix", "unixnano", "rfc3339"] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RayIDGetResponse:
        """The `/rayids` api route allows lookups by specific rayid.

        The rayids route will
        return zero, one, or more records (ray ids are not unique).

        Args:
          zone_id: Identifier

          rayid: Ray identifier.

          fields: The `/received` route by default returns a limited set of fields, and allows
              customers to override the default field set by specifying individual fields. The
              reasons for this are: 1. Most customers require only a small subset of fields,
              but that subset varies from customer to customer; 2. Flat schema is much easier
              to work with downstream (importing into BigTable etc); 3. Performance (time to
              process, file size). If `?fields=` is not specified, default field set is
              returned. This default field set may change at any time. When `?fields=` is
              provided, each record is returned with the specified fields. `fields` must be
              specified as a comma separated list without any whitespaces, and all fields must
              exist. The order in which fields are specified does not matter, and the order of
              fields in the response is not specified.

          timestamps: By default, timestamps in responses are returned as Unix nanosecond integers.
              The `?timestamps=` argument can be set to change the format in which response
              timestamps are returned. Possible values are: `unix`, `unixnano`, `rfc3339`.
              Note that `unix` and `unixnano` return timestamps as integers; `rfc3339` returns
              timestamps as strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not rayid:
          raise ValueError(
            f'Expected a non-empty value for `rayid` but received {rayid!r}'
          )
        return cast(RayIDGetResponse, await self._get(
            f"/zones/{zone_id}/logs/rayids/{rayid}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "fields": fields,
                "timestamps": timestamps,
            }, rayid_get_params.RayIDGetParams)),
            cast_to=cast(Any, RayIDGetResponse),  # Union types cannot be passed in as arguments in the type system
        ))

class RayIDResourceWithRawResponse:
    def __init__(self, rayid: RayIDResource) -> None:
        self._rayid = rayid

        self.get = to_raw_response_wrapper(
            rayid.get,
        )

class AsyncRayIDResourceWithRawResponse:
    def __init__(self, rayid: AsyncRayIDResource) -> None:
        self._rayid = rayid

        self.get = async_to_raw_response_wrapper(
            rayid.get,
        )

class RayIDResourceWithStreamingResponse:
    def __init__(self, rayid: RayIDResource) -> None:
        self._rayid = rayid

        self.get = to_streamed_response_wrapper(
            rayid.get,
        )

class AsyncRayIDResourceWithStreamingResponse:
    def __init__(self, rayid: AsyncRayIDResource) -> None:
        self._rayid = rayid

        self.get = async_to_streamed_response_wrapper(
            rayid.get,
        )