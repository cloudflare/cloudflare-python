# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, Type, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.logpush import (
    JobGetResponse,
    JobListResponse,
    JobCreateResponse,
    JobDeleteResponse,
    JobUpdateResponse,
    job_create_params,
    job_update_params,
)

__all__ = ["Jobs", "AsyncJobs"]


class Jobs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobsWithRawResponse:
        return JobsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobsWithStreamingResponse:
        return JobsWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        zone_id: str,
        destination_conf: str,
        dataset: Optional[str] | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        frequency: Optional[Literal["high", "low"]] | NotGiven = NOT_GIVEN,
        logpull_options: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        output_options: Optional[job_create_params.OutputOptions] | NotGiven = NOT_GIVEN,
        ownership_challenge: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[JobCreateResponse]:
        """
        Creates a new Logpush job for an account or zone.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          destination_conf: Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.
              Additional configuration parameters supported by the destination may be
              included.

          dataset: Name of the dataset.

          enabled: Flag that indicates if the job is enabled.

          frequency: The frequency at which Cloudflare sends batches of logs to your destination.
              Setting frequency to high sends your logs in larger quantities of smaller files.
              Setting frequency to low sends logs in smaller quantities of larger files.

          logpull_options: This field is deprecated. Use `output_options` instead. Configuration string. It
              specifies things like requested fields and timestamp formats. If migrating from
              the logpull api, copy the url (full url or just the query string) of your call
              here, and logpush will keep on making this call for you, setting start and end
              times appropriately.

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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/{account_id}/{zone_id}/logpush/jobs",
            body=maybe_transform(
                {
                    "destination_conf": destination_conf,
                    "dataset": dataset,
                    "enabled": enabled,
                    "frequency": frequency,
                    "logpull_options": logpull_options,
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[JobCreateResponse]], ResultWrapper[JobCreateResponse]),
        )

    def update(
        self,
        job_id: int,
        *,
        account_id: str,
        zone_id: str,
        destination_conf: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        frequency: Optional[Literal["high", "low"]] | NotGiven = NOT_GIVEN,
        logpull_options: Optional[str] | NotGiven = NOT_GIVEN,
        output_options: Optional[job_update_params.OutputOptions] | NotGiven = NOT_GIVEN,
        ownership_challenge: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[JobUpdateResponse]:
        """
        Updates a Logpush job.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          job_id: Unique id of the job.

          destination_conf: Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.
              Additional configuration parameters supported by the destination may be
              included.

          enabled: Flag that indicates if the job is enabled.

          frequency: The frequency at which Cloudflare sends batches of logs to your destination.
              Setting frequency to high sends your logs in larger quantities of smaller files.
              Setting frequency to low sends logs in smaller quantities of larger files.

          logpull_options: This field is deprecated. Use `output_options` instead. Configuration string. It
              specifies things like requested fields and timestamp formats. If migrating from
              the logpull api, copy the url (full url or just the query string) of your call
              here, and logpush will keep on making this call for you, setting start and end
              times appropriately.

          output_options: The structured replacement for `logpull_options`. When including this field, the
              `logpull_option` field will be ignored.

          ownership_challenge: Ownership challenge token to prove destination ownership.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/{account_id}/{zone_id}/logpush/jobs/{job_id}",
            body=maybe_transform(
                {
                    "destination_conf": destination_conf,
                    "enabled": enabled,
                    "frequency": frequency,
                    "logpull_options": logpull_options,
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[JobUpdateResponse]], ResultWrapper[JobUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobListResponse:
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/{account_id}/{zone_id}/logpush/jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[JobListResponse], ResultWrapper[JobListResponse]),
        )

    def delete(
        self,
        job_id: int,
        *,
        account_id: str,
        zone_id: str,
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
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          job_id: Unique id of the job.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            Optional[JobDeleteResponse],
            self._delete(
                f"/{account_id}/{zone_id}/logpush/jobs/{job_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[JobDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        job_id: int,
        *,
        account_id: str,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[JobGetResponse]:
        """
        Gets the details of a Logpush job.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          job_id: Unique id of the job.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/{account_id}/{zone_id}/logpush/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[JobGetResponse]], ResultWrapper[JobGetResponse]),
        )


class AsyncJobs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobsWithRawResponse:
        return AsyncJobsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobsWithStreamingResponse:
        return AsyncJobsWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        zone_id: str,
        destination_conf: str,
        dataset: Optional[str] | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        frequency: Optional[Literal["high", "low"]] | NotGiven = NOT_GIVEN,
        logpull_options: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        output_options: Optional[job_create_params.OutputOptions] | NotGiven = NOT_GIVEN,
        ownership_challenge: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[JobCreateResponse]:
        """
        Creates a new Logpush job for an account or zone.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          destination_conf: Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.
              Additional configuration parameters supported by the destination may be
              included.

          dataset: Name of the dataset.

          enabled: Flag that indicates if the job is enabled.

          frequency: The frequency at which Cloudflare sends batches of logs to your destination.
              Setting frequency to high sends your logs in larger quantities of smaller files.
              Setting frequency to low sends logs in smaller quantities of larger files.

          logpull_options: This field is deprecated. Use `output_options` instead. Configuration string. It
              specifies things like requested fields and timestamp formats. If migrating from
              the logpull api, copy the url (full url or just the query string) of your call
              here, and logpush will keep on making this call for you, setting start and end
              times appropriately.

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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/{account_id}/{zone_id}/logpush/jobs",
            body=maybe_transform(
                {
                    "destination_conf": destination_conf,
                    "dataset": dataset,
                    "enabled": enabled,
                    "frequency": frequency,
                    "logpull_options": logpull_options,
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[JobCreateResponse]], ResultWrapper[JobCreateResponse]),
        )

    async def update(
        self,
        job_id: int,
        *,
        account_id: str,
        zone_id: str,
        destination_conf: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        frequency: Optional[Literal["high", "low"]] | NotGiven = NOT_GIVEN,
        logpull_options: Optional[str] | NotGiven = NOT_GIVEN,
        output_options: Optional[job_update_params.OutputOptions] | NotGiven = NOT_GIVEN,
        ownership_challenge: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[JobUpdateResponse]:
        """
        Updates a Logpush job.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          job_id: Unique id of the job.

          destination_conf: Uniquely identifies a resource (such as an s3 bucket) where data will be pushed.
              Additional configuration parameters supported by the destination may be
              included.

          enabled: Flag that indicates if the job is enabled.

          frequency: The frequency at which Cloudflare sends batches of logs to your destination.
              Setting frequency to high sends your logs in larger quantities of smaller files.
              Setting frequency to low sends logs in smaller quantities of larger files.

          logpull_options: This field is deprecated. Use `output_options` instead. Configuration string. It
              specifies things like requested fields and timestamp formats. If migrating from
              the logpull api, copy the url (full url or just the query string) of your call
              here, and logpush will keep on making this call for you, setting start and end
              times appropriately.

          output_options: The structured replacement for `logpull_options`. When including this field, the
              `logpull_option` field will be ignored.

          ownership_challenge: Ownership challenge token to prove destination ownership.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/{account_id}/{zone_id}/logpush/jobs/{job_id}",
            body=maybe_transform(
                {
                    "destination_conf": destination_conf,
                    "enabled": enabled,
                    "frequency": frequency,
                    "logpull_options": logpull_options,
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[JobUpdateResponse]], ResultWrapper[JobUpdateResponse]),
        )

    async def list(
        self,
        *,
        account_id: str,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> JobListResponse:
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/{account_id}/{zone_id}/logpush/jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[JobListResponse], ResultWrapper[JobListResponse]),
        )

    async def delete(
        self,
        job_id: int,
        *,
        account_id: str,
        zone_id: str,
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
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          job_id: Unique id of the job.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            Optional[JobDeleteResponse],
            await self._delete(
                f"/{account_id}/{zone_id}/logpush/jobs/{job_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[JobDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        job_id: int,
        *,
        account_id: str,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[JobGetResponse]:
        """
        Gets the details of a Logpush job.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          job_id: Unique id of the job.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/{account_id}/{zone_id}/logpush/jobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[JobGetResponse]], ResultWrapper[JobGetResponse]),
        )


class JobsWithRawResponse:
    def __init__(self, jobs: Jobs) -> None:
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


class AsyncJobsWithRawResponse:
    def __init__(self, jobs: AsyncJobs) -> None:
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


class JobsWithStreamingResponse:
    def __init__(self, jobs: Jobs) -> None:
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


class AsyncJobsWithStreamingResponse:
    def __init__(self, jobs: AsyncJobs) -> None:
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
