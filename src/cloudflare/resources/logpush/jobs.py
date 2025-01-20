# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.logpush import job_create_params, job_update_params
from ...types.logpush.logpush_job import LogpushJob
from ...types.logpush.job_delete_response import JobDeleteResponse
from ...types.logpush.output_options_param import OutputOptionsParam

__all__ = ["JobsResource", "AsyncJobsResource"]


class JobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return JobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return JobsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        destination_conf: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        dataset: Optional[str] | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        frequency: Optional[Literal["high", "low"]] | NotGiven = NOT_GIVEN,
        kind: Optional[Literal["edge"]] | NotGiven = NOT_GIVEN,
        logpull_options: Optional[str] | NotGiven = NOT_GIVEN,
        max_upload_bytes: Optional[int] | NotGiven = NOT_GIVEN,
        max_upload_interval_seconds: Optional[int] | NotGiven = NOT_GIVEN,
        max_upload_records: Optional[int] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        output_options: Optional[OutputOptionsParam] | NotGiven = NOT_GIVEN,
        ownership_challenge: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LogpushJob]:
        """
        Creates a new Logpush job for an account or zone.

        Args:
          destination_conf: Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.
              Additional configuration parameters supported by the destination may be
              included.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          dataset: Name of the dataset. A list of supported datasets can be found on the
              [Developer Docs](https://developers.cloudflare.com/logs/reference/log-fields/).

          enabled: Flag that indicates if the job is enabled.

          frequency: This field is deprecated. Please use `max_upload_*` parameters instead. The
              frequency at which Cloudflare sends batches of logs to your destination. Setting
              frequency to high sends your logs in larger quantities of smaller files. Setting
              frequency to low sends logs in smaller quantities of larger files.

          kind: The kind parameter (optional) is used to differentiate between Logpush and Edge
              Log Delivery jobs. Currently, Edge Log Delivery is only supported for the
              `http_requests` dataset.

          logpull_options: This field is deprecated. Use `output_options` instead. Configuration string. It
              specifies things like requested fields and timestamp formats. If migrating from
              the logpull api, copy the url (full url or just the query string) of your call
              here, and logpush will keep on making this call for you, setting start and end
              times appropriately.

          max_upload_bytes: The maximum uncompressed file size of a batch of logs. This setting value must
              be between `5 MB` and `1 GB`, or `0` to disable it. Note that you cannot set a
              minimum file size; this means that log files may be much smaller than this batch
              size. This parameter is not available for jobs with `edge` as its kind.

          max_upload_interval_seconds: The maximum interval in seconds for log batches. This setting must be between 30
              and 300 seconds (5 minutes), or `0` to disable it. Note that you cannot specify
              a minimum interval for log batches; this means that log files may be sent in
              shorter intervals than this. This parameter is only used for jobs with `edge` as
              its kind.

          max_upload_records: The maximum number of log lines per batch. This setting must be between 1000 and
              1,000,000 lines, or `0` to disable it. Note that you cannot specify a minimum
              number of log lines per batch; this means that log files may contain many fewer
              lines than this. This parameter is not available for jobs with `edge` as its
              kind.

          name: Optional human readable job name. Not unique. Cloudflare suggests that you set
              this to a meaningful string, like the domain name, to make it easier to identify
              your job.

          output_options: The structured replacement for `logpull_options`. When including this field, the
              `logpull_option` field will be ignored.

          ownership_challenge: Ownership challenge token to prove destination ownership.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._post(
            f"/{account_or_zone}/{account_or_zone_id}/logpush/jobs",
            body=maybe_transform(
                {
                    "destination_conf": destination_conf,
                    "dataset": dataset,
                    "enabled": enabled,
                    "frequency": frequency,
                    "kind": kind,
                    "logpull_options": logpull_options,
                    "max_upload_bytes": max_upload_bytes,
                    "max_upload_interval_seconds": max_upload_interval_seconds,
                    "max_upload_records": max_upload_records,
                    "name": name,
                    "output_options": output_options,
                    "ownership_challenge": ownership_challenge,
                },
                job_create_params.JobCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[LogpushJob]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LogpushJob]], ResultWrapper[LogpushJob]),
        )

    def update(
        self,
        job_id: int,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        destination_conf: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        frequency: Optional[Literal["high", "low"]] | NotGiven = NOT_GIVEN,
        kind: Optional[Literal["edge"]] | NotGiven = NOT_GIVEN,
        logpull_options: Optional[str] | NotGiven = NOT_GIVEN,
        max_upload_bytes: Optional[int] | NotGiven = NOT_GIVEN,
        max_upload_interval_seconds: Optional[int] | NotGiven = NOT_GIVEN,
        max_upload_records: Optional[int] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        output_options: Optional[OutputOptionsParam] | NotGiven = NOT_GIVEN,
        ownership_challenge: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LogpushJob]:
        """
        Updates a Logpush job.

        Args:
          job_id: Unique id of the job.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          destination_conf: Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.
              Additional configuration parameters supported by the destination may be
              included.

          enabled: Flag that indicates if the job is enabled.

          frequency: This field is deprecated. Please use `max_upload_*` parameters instead. The
              frequency at which Cloudflare sends batches of logs to your destination. Setting
              frequency to high sends your logs in larger quantities of smaller files. Setting
              frequency to low sends logs in smaller quantities of larger files.

          kind: The kind parameter (optional) is used to differentiate between Logpush and Edge
              Log Delivery jobs. Currently, Edge Log Delivery is only supported for the
              `http_requests` dataset.

          logpull_options: This field is deprecated. Use `output_options` instead. Configuration string. It
              specifies things like requested fields and timestamp formats. If migrating from
              the logpull api, copy the url (full url or just the query string) of your call
              here, and logpush will keep on making this call for you, setting start and end
              times appropriately.

          max_upload_bytes: The maximum uncompressed file size of a batch of logs. This setting value must
              be between `5 MB` and `1 GB`, or `0` to disable it. Note that you cannot set a
              minimum file size; this means that log files may be much smaller than this batch
              size. This parameter is not available for jobs with `edge` as its kind.

          max_upload_interval_seconds: The maximum interval in seconds for log batches. This setting must be between 30
              and 300 seconds (5 minutes), or `0` to disable it. Note that you cannot specify
              a minimum interval for log batches; this means that log files may be sent in
              shorter intervals than this. This parameter is only used for jobs with `edge` as
              its kind.

          max_upload_records: The maximum number of log lines per batch. This setting must be between 1000 and
              1,000,000 lines, or `0` to disable it. Note that you cannot specify a minimum
              number of log lines per batch; this means that log files may contain many fewer
              lines than this. This parameter is not available for jobs with `edge` as its
              kind.

          name: Optional human readable job name. Not unique. Cloudflare suggests that you set
              this to a meaningful string, like the domain name, to make it easier to identify
              your job.

          output_options: The structured replacement for `logpull_options`. When including this field, the
              `logpull_option` field will be ignored.

          ownership_challenge: Ownership challenge token to prove destination ownership.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._put(
            f"/{account_or_zone}/{account_or_zone_id}/logpush/jobs/{job_id}",
            body=maybe_transform(
                {
                    "destination_conf": destination_conf,
                    "enabled": enabled,
                    "frequency": frequency,
                    "kind": kind,
                    "logpull_options": logpull_options,
                    "max_upload_bytes": max_upload_bytes,
                    "max_upload_interval_seconds": max_upload_interval_seconds,
                    "max_upload_records": max_upload_records,
                    "name": name,
                    "output_options": output_options,
                    "ownership_challenge": ownership_challenge,
                },
                job_update_params.JobUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[LogpushJob]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LogpushJob]], ResultWrapper[LogpushJob]),
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[Optional[LogpushJob]]:
        """
        Lists Logpush jobs for an account or zone.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get_api_list(
            f"/{account_or_zone}/{account_or_zone_id}/logpush/jobs",
            page=SyncSinglePage[Optional[LogpushJob]],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=LogpushJob,
        )

    def delete(
        self,
        job_id: int,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[JobDeleteResponse]:
        """
        Deletes a Logpush job.

        Args:
          job_id: Unique id of the job.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/logpush/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[JobDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[JobDeleteResponse]], ResultWrapper[JobDeleteResponse]),
        )

    def get(
        self,
        job_id: int,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LogpushJob]:
        """
        Gets the details of a Logpush job.

        Args:
          job_id: Unique id of the job.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get(
            f"/{account_or_zone}/{account_or_zone_id}/logpush/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[LogpushJob]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LogpushJob]], ResultWrapper[LogpushJob]),
        )


class AsyncJobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncJobsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        destination_conf: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        dataset: Optional[str] | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        frequency: Optional[Literal["high", "low"]] | NotGiven = NOT_GIVEN,
        kind: Optional[Literal["edge"]] | NotGiven = NOT_GIVEN,
        logpull_options: Optional[str] | NotGiven = NOT_GIVEN,
        max_upload_bytes: Optional[int] | NotGiven = NOT_GIVEN,
        max_upload_interval_seconds: Optional[int] | NotGiven = NOT_GIVEN,
        max_upload_records: Optional[int] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        output_options: Optional[OutputOptionsParam] | NotGiven = NOT_GIVEN,
        ownership_challenge: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LogpushJob]:
        """
        Creates a new Logpush job for an account or zone.

        Args:
          destination_conf: Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.
              Additional configuration parameters supported by the destination may be
              included.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          dataset: Name of the dataset. A list of supported datasets can be found on the
              [Developer Docs](https://developers.cloudflare.com/logs/reference/log-fields/).

          enabled: Flag that indicates if the job is enabled.

          frequency: This field is deprecated. Please use `max_upload_*` parameters instead. The
              frequency at which Cloudflare sends batches of logs to your destination. Setting
              frequency to high sends your logs in larger quantities of smaller files. Setting
              frequency to low sends logs in smaller quantities of larger files.

          kind: The kind parameter (optional) is used to differentiate between Logpush and Edge
              Log Delivery jobs. Currently, Edge Log Delivery is only supported for the
              `http_requests` dataset.

          logpull_options: This field is deprecated. Use `output_options` instead. Configuration string. It
              specifies things like requested fields and timestamp formats. If migrating from
              the logpull api, copy the url (full url or just the query string) of your call
              here, and logpush will keep on making this call for you, setting start and end
              times appropriately.

          max_upload_bytes: The maximum uncompressed file size of a batch of logs. This setting value must
              be between `5 MB` and `1 GB`, or `0` to disable it. Note that you cannot set a
              minimum file size; this means that log files may be much smaller than this batch
              size. This parameter is not available for jobs with `edge` as its kind.

          max_upload_interval_seconds: The maximum interval in seconds for log batches. This setting must be between 30
              and 300 seconds (5 minutes), or `0` to disable it. Note that you cannot specify
              a minimum interval for log batches; this means that log files may be sent in
              shorter intervals than this. This parameter is only used for jobs with `edge` as
              its kind.

          max_upload_records: The maximum number of log lines per batch. This setting must be between 1000 and
              1,000,000 lines, or `0` to disable it. Note that you cannot specify a minimum
              number of log lines per batch; this means that log files may contain many fewer
              lines than this. This parameter is not available for jobs with `edge` as its
              kind.

          name: Optional human readable job name. Not unique. Cloudflare suggests that you set
              this to a meaningful string, like the domain name, to make it easier to identify
              your job.

          output_options: The structured replacement for `logpull_options`. When including this field, the
              `logpull_option` field will be ignored.

          ownership_challenge: Ownership challenge token to prove destination ownership.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._post(
            f"/{account_or_zone}/{account_or_zone_id}/logpush/jobs",
            body=await async_maybe_transform(
                {
                    "destination_conf": destination_conf,
                    "dataset": dataset,
                    "enabled": enabled,
                    "frequency": frequency,
                    "kind": kind,
                    "logpull_options": logpull_options,
                    "max_upload_bytes": max_upload_bytes,
                    "max_upload_interval_seconds": max_upload_interval_seconds,
                    "max_upload_records": max_upload_records,
                    "name": name,
                    "output_options": output_options,
                    "ownership_challenge": ownership_challenge,
                },
                job_create_params.JobCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[LogpushJob]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LogpushJob]], ResultWrapper[LogpushJob]),
        )

    async def update(
        self,
        job_id: int,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        destination_conf: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        frequency: Optional[Literal["high", "low"]] | NotGiven = NOT_GIVEN,
        kind: Optional[Literal["edge"]] | NotGiven = NOT_GIVEN,
        logpull_options: Optional[str] | NotGiven = NOT_GIVEN,
        max_upload_bytes: Optional[int] | NotGiven = NOT_GIVEN,
        max_upload_interval_seconds: Optional[int] | NotGiven = NOT_GIVEN,
        max_upload_records: Optional[int] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        output_options: Optional[OutputOptionsParam] | NotGiven = NOT_GIVEN,
        ownership_challenge: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LogpushJob]:
        """
        Updates a Logpush job.

        Args:
          job_id: Unique id of the job.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          destination_conf: Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.
              Additional configuration parameters supported by the destination may be
              included.

          enabled: Flag that indicates if the job is enabled.

          frequency: This field is deprecated. Please use `max_upload_*` parameters instead. The
              frequency at which Cloudflare sends batches of logs to your destination. Setting
              frequency to high sends your logs in larger quantities of smaller files. Setting
              frequency to low sends logs in smaller quantities of larger files.

          kind: The kind parameter (optional) is used to differentiate between Logpush and Edge
              Log Delivery jobs. Currently, Edge Log Delivery is only supported for the
              `http_requests` dataset.

          logpull_options: This field is deprecated. Use `output_options` instead. Configuration string. It
              specifies things like requested fields and timestamp formats. If migrating from
              the logpull api, copy the url (full url or just the query string) of your call
              here, and logpush will keep on making this call for you, setting start and end
              times appropriately.

          max_upload_bytes: The maximum uncompressed file size of a batch of logs. This setting value must
              be between `5 MB` and `1 GB`, or `0` to disable it. Note that you cannot set a
              minimum file size; this means that log files may be much smaller than this batch
              size. This parameter is not available for jobs with `edge` as its kind.

          max_upload_interval_seconds: The maximum interval in seconds for log batches. This setting must be between 30
              and 300 seconds (5 minutes), or `0` to disable it. Note that you cannot specify
              a minimum interval for log batches; this means that log files may be sent in
              shorter intervals than this. This parameter is only used for jobs with `edge` as
              its kind.

          max_upload_records: The maximum number of log lines per batch. This setting must be between 1000 and
              1,000,000 lines, or `0` to disable it. Note that you cannot specify a minimum
              number of log lines per batch; this means that log files may contain many fewer
              lines than this. This parameter is not available for jobs with `edge` as its
              kind.

          name: Optional human readable job name. Not unique. Cloudflare suggests that you set
              this to a meaningful string, like the domain name, to make it easier to identify
              your job.

          output_options: The structured replacement for `logpull_options`. When including this field, the
              `logpull_option` field will be ignored.

          ownership_challenge: Ownership challenge token to prove destination ownership.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._put(
            f"/{account_or_zone}/{account_or_zone_id}/logpush/jobs/{job_id}",
            body=await async_maybe_transform(
                {
                    "destination_conf": destination_conf,
                    "enabled": enabled,
                    "frequency": frequency,
                    "kind": kind,
                    "logpull_options": logpull_options,
                    "max_upload_bytes": max_upload_bytes,
                    "max_upload_interval_seconds": max_upload_interval_seconds,
                    "max_upload_records": max_upload_records,
                    "name": name,
                    "output_options": output_options,
                    "ownership_challenge": ownership_challenge,
                },
                job_update_params.JobUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[LogpushJob]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LogpushJob]], ResultWrapper[LogpushJob]),
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Optional[LogpushJob], AsyncSinglePage[Optional[LogpushJob]]]:
        """
        Lists Logpush jobs for an account or zone.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get_api_list(
            f"/{account_or_zone}/{account_or_zone_id}/logpush/jobs",
            page=AsyncSinglePage[Optional[LogpushJob]],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=LogpushJob,
        )

    async def delete(
        self,
        job_id: int,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[JobDeleteResponse]:
        """
        Deletes a Logpush job.

        Args:
          job_id: Unique id of the job.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/logpush/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[JobDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[JobDeleteResponse]], ResultWrapper[JobDeleteResponse]),
        )

    async def get(
        self,
        job_id: int,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LogpushJob]:
        """
        Gets the details of a Logpush job.

        Args:
          job_id: Unique id of the job.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/logpush/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[LogpushJob]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[LogpushJob]], ResultWrapper[LogpushJob]),
        )


class JobsResourceWithRawResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.create = to_raw_response_wrapper(
            jobs.create,
        )
        self.update = to_raw_response_wrapper(
            jobs.update,
        )
        self.list = to_raw_response_wrapper(
            jobs.list,
        )
        self.delete = to_raw_response_wrapper(
            jobs.delete,
        )
        self.get = to_raw_response_wrapper(
            jobs.get,
        )


class AsyncJobsResourceWithRawResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.create = async_to_raw_response_wrapper(
            jobs.create,
        )
        self.update = async_to_raw_response_wrapper(
            jobs.update,
        )
        self.list = async_to_raw_response_wrapper(
            jobs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            jobs.delete,
        )
        self.get = async_to_raw_response_wrapper(
            jobs.get,
        )


class JobsResourceWithStreamingResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.create = to_streamed_response_wrapper(
            jobs.create,
        )
        self.update = to_streamed_response_wrapper(
            jobs.update,
        )
        self.list = to_streamed_response_wrapper(
            jobs.list,
        )
        self.delete = to_streamed_response_wrapper(
            jobs.delete,
        )
        self.get = to_streamed_response_wrapper(
            jobs.get,
        )


class AsyncJobsResourceWithStreamingResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.create = async_to_streamed_response_wrapper(
            jobs.create,
        )
        self.update = async_to_streamed_response_wrapper(
            jobs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            jobs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            jobs.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            jobs.get,
        )
