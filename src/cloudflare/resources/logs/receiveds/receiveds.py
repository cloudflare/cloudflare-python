# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .fields import Fields, AsyncFields

from ...._compat import cached_property

from ....types.logs import ReceivedReceivedGetLogsReceivedResponse

from typing import Union

from typing_extensions import Literal

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
from ....types.logs import received_received_get_logs_received_params
from .fields import (
    Fields,
    AsyncFields,
    FieldsWithRawResponse,
    AsyncFieldsWithRawResponse,
    FieldsWithStreamingResponse,
    AsyncFieldsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Receiveds", "AsyncReceiveds"]


class Receiveds(SyncAPIResource):
    @cached_property
    def fields(self) -> Fields:
        return Fields(self._client)

    @cached_property
    def with_raw_response(self) -> ReceivedsWithRawResponse:
        return ReceivedsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReceivedsWithStreamingResponse:
        return ReceivedsWithStreamingResponse(self)

    def received_get_logs_received(
        self,
        zone_identifier: str,
        *,
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
    ) -> ReceivedReceivedGetLogsReceivedResponse:
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
          zone_identifier: Identifier

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
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return cast(
            ReceivedReceivedGetLogsReceivedResponse,
            self._get(
                f"/zones/{zone_identifier}/logs/received",
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
                        received_received_get_logs_received_params.ReceivedReceivedGetLogsReceivedParams,
                    ),
                ),
                cast_to=cast(
                    Any, ReceivedReceivedGetLogsReceivedResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncReceiveds(AsyncAPIResource):
    @cached_property
    def fields(self) -> AsyncFields:
        return AsyncFields(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReceivedsWithRawResponse:
        return AsyncReceivedsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReceivedsWithStreamingResponse:
        return AsyncReceivedsWithStreamingResponse(self)

    async def received_get_logs_received(
        self,
        zone_identifier: str,
        *,
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
    ) -> ReceivedReceivedGetLogsReceivedResponse:
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
          zone_identifier: Identifier

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
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return cast(
            ReceivedReceivedGetLogsReceivedResponse,
            await self._get(
                f"/zones/{zone_identifier}/logs/received",
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
                        received_received_get_logs_received_params.ReceivedReceivedGetLogsReceivedParams,
                    ),
                ),
                cast_to=cast(
                    Any, ReceivedReceivedGetLogsReceivedResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ReceivedsWithRawResponse:
    def __init__(self, receiveds: Receiveds) -> None:
        self._receiveds = receiveds

        self.received_get_logs_received = to_raw_response_wrapper(
            receiveds.received_get_logs_received,
        )

    @cached_property
    def fields(self) -> FieldsWithRawResponse:
        return FieldsWithRawResponse(self._receiveds.fields)


class AsyncReceivedsWithRawResponse:
    def __init__(self, receiveds: AsyncReceiveds) -> None:
        self._receiveds = receiveds

        self.received_get_logs_received = async_to_raw_response_wrapper(
            receiveds.received_get_logs_received,
        )

    @cached_property
    def fields(self) -> AsyncFieldsWithRawResponse:
        return AsyncFieldsWithRawResponse(self._receiveds.fields)


class ReceivedsWithStreamingResponse:
    def __init__(self, receiveds: Receiveds) -> None:
        self._receiveds = receiveds

        self.received_get_logs_received = to_streamed_response_wrapper(
            receiveds.received_get_logs_received,
        )

    @cached_property
    def fields(self) -> FieldsWithStreamingResponse:
        return FieldsWithStreamingResponse(self._receiveds.fields)


class AsyncReceivedsWithStreamingResponse:
    def __init__(self, receiveds: AsyncReceiveds) -> None:
        self._receiveds = receiveds

        self.received_get_logs_received = async_to_streamed_response_wrapper(
            receiveds.received_get_logs_received,
        )

    @cached_property
    def fields(self) -> AsyncFieldsWithStreamingResponse:
        return AsyncFieldsWithStreamingResponse(self._receiveds.fields)
