# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, cast
from typing_extensions import Literal

import httpx

from .fields import (
    FieldsResource,
    AsyncFieldsResource,
    FieldsResourceWithRawResponse,
    AsyncFieldsResourceWithRawResponse,
    FieldsResourceWithStreamingResponse,
    AsyncFieldsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.logs import received_get_params
from ...._base_client import make_request_options
from ....types.logs.received_get_response import ReceivedGetResponse

__all__ = ["ReceivedResource", "AsyncReceivedResource"]


class ReceivedResource(SyncAPIResource):
    @cached_property
    def fields(self) -> FieldsResource:
        return FieldsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReceivedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ReceivedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReceivedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ReceivedResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        zone_id: str,
        end: Union[str, int],
        count: int | NotGiven = NOT_GIVEN,
        fields: str | NotGiven = NOT_GIVEN,
        sample: float | NotGiven = NOT_GIVEN,
        start: Union[str, int] | NotGiven = NOT_GIVEN,
        timestamps: Literal["unix", "unixnano", "rfc3339"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReceivedGetResponse:
        """The `/received` api route allows customers to retrieve their edge HTTP logs.

        The
        basic access pattern is "give me all the logs for zone Z for minute M", where
        the minute M refers to the time records were received at Cloudflare's central
        data center. `start` is inclusive, and `end` is exclusive. Because of that, to
        get all data, at minutely cadence, starting at 10AM, the proper values are:
        `start=2018-05-20T10:00:00Z&end=2018-05-20T10:01:00Z`, then
        `start=2018-05-20T10:01:00Z&end=2018-05-20T10:02:00Z` and so on; the overlap
        will be handled properly.

        Args:
          zone_id: Identifier

          end: Sets the (exclusive) end of the requested time frame. This can be a unix
              timestamp (in seconds or nanoseconds), or an absolute timestamp that conforms to
              RFC 3339. `end` must be at least five minutes earlier than now and must be later
              than `start`. Difference between `start` and `end` must be not greater than one
              hour.

          count: When `?count=` is provided, the response will contain up to `count` results.
              Since results are not sorted, you are likely to get different data for repeated
              requests. `count` must be an integer > 0.

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

          sample: When `?sample=` is provided, a sample of matching records is returned. If
              `sample=0.1` then 10% of records will be returned. Sampling is random: repeated
              calls will not only return different records, but likely will also vary slightly
              in number of returned records. When `?count=` is also specified, `count` is
              applied to the number of returned records, not the sampled records. So, with
              `sample=0.05` and `count=7`, when there is a total of 100 records available,
              approximately five will be returned. When there are 1000 records, seven will be
              returned. When there are 10,000 records, seven will be returned.

          start: Sets the (inclusive) beginning of the requested time frame. This can be a unix
              timestamp (in seconds or nanoseconds), or an absolute timestamp that conforms to
              RFC 3339. At this point in time, it cannot exceed a time in the past greater
              than seven days.

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
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            ReceivedGetResponse,
            self._get(
                f"/zones/{zone_id}/logs/received",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "end": end,
                            "count": count,
                            "fields": fields,
                            "sample": sample,
                            "start": start,
                            "timestamps": timestamps,
                        },
                        received_get_params.ReceivedGetParams,
                    ),
                ),
                cast_to=cast(
                    Any, ReceivedGetResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncReceivedResource(AsyncAPIResource):
    @cached_property
    def fields(self) -> AsyncFieldsResource:
        return AsyncFieldsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReceivedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReceivedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReceivedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncReceivedResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        zone_id: str,
        end: Union[str, int],
        count: int | NotGiven = NOT_GIVEN,
        fields: str | NotGiven = NOT_GIVEN,
        sample: float | NotGiven = NOT_GIVEN,
        start: Union[str, int] | NotGiven = NOT_GIVEN,
        timestamps: Literal["unix", "unixnano", "rfc3339"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReceivedGetResponse:
        """The `/received` api route allows customers to retrieve their edge HTTP logs.

        The
        basic access pattern is "give me all the logs for zone Z for minute M", where
        the minute M refers to the time records were received at Cloudflare's central
        data center. `start` is inclusive, and `end` is exclusive. Because of that, to
        get all data, at minutely cadence, starting at 10AM, the proper values are:
        `start=2018-05-20T10:00:00Z&end=2018-05-20T10:01:00Z`, then
        `start=2018-05-20T10:01:00Z&end=2018-05-20T10:02:00Z` and so on; the overlap
        will be handled properly.

        Args:
          zone_id: Identifier

          end: Sets the (exclusive) end of the requested time frame. This can be a unix
              timestamp (in seconds or nanoseconds), or an absolute timestamp that conforms to
              RFC 3339. `end` must be at least five minutes earlier than now and must be later
              than `start`. Difference between `start` and `end` must be not greater than one
              hour.

          count: When `?count=` is provided, the response will contain up to `count` results.
              Since results are not sorted, you are likely to get different data for repeated
              requests. `count` must be an integer > 0.

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

          sample: When `?sample=` is provided, a sample of matching records is returned. If
              `sample=0.1` then 10% of records will be returned. Sampling is random: repeated
              calls will not only return different records, but likely will also vary slightly
              in number of returned records. When `?count=` is also specified, `count` is
              applied to the number of returned records, not the sampled records. So, with
              `sample=0.05` and `count=7`, when there is a total of 100 records available,
              approximately five will be returned. When there are 1000 records, seven will be
              returned. When there are 10,000 records, seven will be returned.

          start: Sets the (inclusive) beginning of the requested time frame. This can be a unix
              timestamp (in seconds or nanoseconds), or an absolute timestamp that conforms to
              RFC 3339. At this point in time, it cannot exceed a time in the past greater
              than seven days.

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
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            ReceivedGetResponse,
            await self._get(
                f"/zones/{zone_id}/logs/received",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "end": end,
                            "count": count,
                            "fields": fields,
                            "sample": sample,
                            "start": start,
                            "timestamps": timestamps,
                        },
                        received_get_params.ReceivedGetParams,
                    ),
                ),
                cast_to=cast(
                    Any, ReceivedGetResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ReceivedResourceWithRawResponse:
    def __init__(self, received: ReceivedResource) -> None:
        self._received = received

        self.get = to_raw_response_wrapper(
            received.get,
        )

    @cached_property
    def fields(self) -> FieldsResourceWithRawResponse:
        return FieldsResourceWithRawResponse(self._received.fields)


class AsyncReceivedResourceWithRawResponse:
    def __init__(self, received: AsyncReceivedResource) -> None:
        self._received = received

        self.get = async_to_raw_response_wrapper(
            received.get,
        )

    @cached_property
    def fields(self) -> AsyncFieldsResourceWithRawResponse:
        return AsyncFieldsResourceWithRawResponse(self._received.fields)


class ReceivedResourceWithStreamingResponse:
    def __init__(self, received: ReceivedResource) -> None:
        self._received = received

        self.get = to_streamed_response_wrapper(
            received.get,
        )

    @cached_property
    def fields(self) -> FieldsResourceWithStreamingResponse:
        return FieldsResourceWithStreamingResponse(self._received.fields)


class AsyncReceivedResourceWithStreamingResponse:
    def __init__(self, received: AsyncReceivedResource) -> None:
        self._received = received

        self.get = async_to_streamed_response_wrapper(
            received.get,
        )

    @cached_property
    def fields(self) -> AsyncFieldsResourceWithStreamingResponse:
        return AsyncFieldsResourceWithStreamingResponse(self._received.fields)
