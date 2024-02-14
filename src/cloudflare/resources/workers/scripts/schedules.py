# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.workers.scripts import (
    ScheduleWorkerCronTriggerGetCronTriggersResponse,
    ScheduleWorkerCronTriggerUpdateCronTriggersResponse,
    schedule_worker_cron_trigger_update_cron_triggers_params,
)

__all__ = ["Schedules", "AsyncSchedules"]


class Schedules(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SchedulesWithRawResponse:
        return SchedulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchedulesWithStreamingResponse:
        return SchedulesWithStreamingResponse(self)

    def worker_cron_trigger_get_cron_triggers(
        self,
        script_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleWorkerCronTriggerGetCronTriggersResponse:
        """
        Fetches Cron Triggers for a Worker.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}/schedules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ScheduleWorkerCronTriggerGetCronTriggersResponse],
                ResultWrapper[ScheduleWorkerCronTriggerGetCronTriggersResponse],
            ),
        )

    def worker_cron_trigger_update_cron_triggers(
        self,
        script_name: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleWorkerCronTriggerUpdateCronTriggersResponse:
        """
        Updates Cron Triggers for a Worker.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return self._put(
            f"/accounts/{account_id}/workers/scripts/{script_name}/schedules",
            body=maybe_transform(
                body,
                schedule_worker_cron_trigger_update_cron_triggers_params.ScheduleWorkerCronTriggerUpdateCronTriggersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ScheduleWorkerCronTriggerUpdateCronTriggersResponse],
                ResultWrapper[ScheduleWorkerCronTriggerUpdateCronTriggersResponse],
            ),
        )


class AsyncSchedules(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSchedulesWithRawResponse:
        return AsyncSchedulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchedulesWithStreamingResponse:
        return AsyncSchedulesWithStreamingResponse(self)

    async def worker_cron_trigger_get_cron_triggers(
        self,
        script_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleWorkerCronTriggerGetCronTriggersResponse:
        """
        Fetches Cron Triggers for a Worker.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}/schedules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ScheduleWorkerCronTriggerGetCronTriggersResponse],
                ResultWrapper[ScheduleWorkerCronTriggerGetCronTriggersResponse],
            ),
        )

    async def worker_cron_trigger_update_cron_triggers(
        self,
        script_name: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleWorkerCronTriggerUpdateCronTriggersResponse:
        """
        Updates Cron Triggers for a Worker.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return await self._put(
            f"/accounts/{account_id}/workers/scripts/{script_name}/schedules",
            body=maybe_transform(
                body,
                schedule_worker_cron_trigger_update_cron_triggers_params.ScheduleWorkerCronTriggerUpdateCronTriggersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ScheduleWorkerCronTriggerUpdateCronTriggersResponse],
                ResultWrapper[ScheduleWorkerCronTriggerUpdateCronTriggersResponse],
            ),
        )


class SchedulesWithRawResponse:
    def __init__(self, schedules: Schedules) -> None:
        self._schedules = schedules

        self.worker_cron_trigger_get_cron_triggers = to_raw_response_wrapper(
            schedules.worker_cron_trigger_get_cron_triggers,
        )
        self.worker_cron_trigger_update_cron_triggers = to_raw_response_wrapper(
            schedules.worker_cron_trigger_update_cron_triggers,
        )


class AsyncSchedulesWithRawResponse:
    def __init__(self, schedules: AsyncSchedules) -> None:
        self._schedules = schedules

        self.worker_cron_trigger_get_cron_triggers = async_to_raw_response_wrapper(
            schedules.worker_cron_trigger_get_cron_triggers,
        )
        self.worker_cron_trigger_update_cron_triggers = async_to_raw_response_wrapper(
            schedules.worker_cron_trigger_update_cron_triggers,
        )


class SchedulesWithStreamingResponse:
    def __init__(self, schedules: Schedules) -> None:
        self._schedules = schedules

        self.worker_cron_trigger_get_cron_triggers = to_streamed_response_wrapper(
            schedules.worker_cron_trigger_get_cron_triggers,
        )
        self.worker_cron_trigger_update_cron_triggers = to_streamed_response_wrapper(
            schedules.worker_cron_trigger_update_cron_triggers,
        )


class AsyncSchedulesWithStreamingResponse:
    def __init__(self, schedules: AsyncSchedules) -> None:
        self._schedules = schedules

        self.worker_cron_trigger_get_cron_triggers = async_to_streamed_response_wrapper(
            schedules.worker_cron_trigger_get_cron_triggers,
        )
        self.worker_cron_trigger_update_cron_triggers = async_to_streamed_response_wrapper(
            schedules.worker_cron_trigger_update_cron_triggers,
        )
