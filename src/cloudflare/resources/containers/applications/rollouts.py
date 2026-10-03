# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.containers.applications import rollout_create_params
from ....types.containers.applications.rollout_create_response import RolloutCreateResponse

__all__ = ["RolloutsResource", "AsyncRolloutsResource"]


class RolloutsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RolloutsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RolloutsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RolloutsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RolloutsResourceWithStreamingResponse(self)

    def create(
        self,
        application_id: str,
        *,
        account_id: str,
        description: str,
        strategy: Literal["rolling", "new_instances"],
        target_configuration: rollout_create_params.TargetConfiguration,
        kind: Literal["full_auto", "full_manual"] | Omit = omit,
        percentage: int | Omit = omit,
        step_percentage: Literal[5, 10, 20, 25, 50, 100] | Omit = omit,
        steps: Iterable[rollout_create_params.Step] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RolloutCreateResponse:
        """
        Creates a rollout to update the application's configuration across instances
        with minimal downtime. Rollouts apply only to scheduler-backed applications with
        `scheduling_policy: "default"`. Versions and rollouts do not apply to
        applications with `scheduling_policy: "durable_object"`.

        Args:
          application_id: An Application ID represents an identifier of an application.

          description: Description of the rollout process.

          strategy: Strategy used for the rollout.

              - "rolling": Step-based rollout with health gates. Actively replaces instances
                to reach each step's target percentage.
              - "new_instances": Percentage control over version distribution. Version sync
                actively replaces instances to match the configured percentage. The
                "full_auto" kind advances through fixed percentage targets after
                target-version health is observed.

          target_configuration: User-specified container configuration changes.

          kind: Kind of the rollout process. Defaults to "full_auto".

              - "full_auto": For rolling rollouts, starts progressing steps upon rollout
                creation. For new_instances rollouts, advances percentage targets
                automatically after target-version health is observed.
              - "full_manual": Requires manually progressing each step in the rollout using
                the UpdateRollout's action parameter.

          percentage: Initial target version percentage (0-100). Version sync actively replaces
              instances to match. Required when strategy is "new_instances" and kind is
              "full_manual". When strategy is "new_instances" and kind is "full_auto", omitted
              percentage starts at 10% or the smallest percentage that targets at least one
              instance. Unused for "rolling".

          step_percentage: Percentage of rollout to increase in each step when "steps" is absent.
              Applicable values: 5, 10, 20, 25, 50, 100. These create rollouts with 20, 10, 5,
              4, 2, 1 steps respectively. Only valid for "rolling" strategy.

          steps: Steps defining the rollout process, used when "step_percentage" is absent.
              Specify only one of "step_percentage" or "steps" when creating a rollout.
              "steps" allow granular control over each step. Only valid for "rolling"
              strategy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/containers/applications/{application_id}/rollouts",
                account_id=account_id,
                application_id=application_id,
            ),
            body=maybe_transform(
                {
                    "description": description,
                    "strategy": strategy,
                    "target_configuration": target_configuration,
                    "kind": kind,
                    "percentage": percentage,
                    "step_percentage": step_percentage,
                    "steps": steps,
                },
                rollout_create_params.RolloutCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RolloutCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[RolloutCreateResponse], ResultWrapper[RolloutCreateResponse]),
        )


class AsyncRolloutsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRolloutsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRolloutsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRolloutsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRolloutsResourceWithStreamingResponse(self)

    async def create(
        self,
        application_id: str,
        *,
        account_id: str,
        description: str,
        strategy: Literal["rolling", "new_instances"],
        target_configuration: rollout_create_params.TargetConfiguration,
        kind: Literal["full_auto", "full_manual"] | Omit = omit,
        percentage: int | Omit = omit,
        step_percentage: Literal[5, 10, 20, 25, 50, 100] | Omit = omit,
        steps: Iterable[rollout_create_params.Step] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RolloutCreateResponse:
        """
        Creates a rollout to update the application's configuration across instances
        with minimal downtime. Rollouts apply only to scheduler-backed applications with
        `scheduling_policy: "default"`. Versions and rollouts do not apply to
        applications with `scheduling_policy: "durable_object"`.

        Args:
          application_id: An Application ID represents an identifier of an application.

          description: Description of the rollout process.

          strategy: Strategy used for the rollout.

              - "rolling": Step-based rollout with health gates. Actively replaces instances
                to reach each step's target percentage.
              - "new_instances": Percentage control over version distribution. Version sync
                actively replaces instances to match the configured percentage. The
                "full_auto" kind advances through fixed percentage targets after
                target-version health is observed.

          target_configuration: User-specified container configuration changes.

          kind: Kind of the rollout process. Defaults to "full_auto".

              - "full_auto": For rolling rollouts, starts progressing steps upon rollout
                creation. For new_instances rollouts, advances percentage targets
                automatically after target-version health is observed.
              - "full_manual": Requires manually progressing each step in the rollout using
                the UpdateRollout's action parameter.

          percentage: Initial target version percentage (0-100). Version sync actively replaces
              instances to match. Required when strategy is "new_instances" and kind is
              "full_manual". When strategy is "new_instances" and kind is "full_auto", omitted
              percentage starts at 10% or the smallest percentage that targets at least one
              instance. Unused for "rolling".

          step_percentage: Percentage of rollout to increase in each step when "steps" is absent.
              Applicable values: 5, 10, 20, 25, 50, 100. These create rollouts with 20, 10, 5,
              4, 2, 1 steps respectively. Only valid for "rolling" strategy.

          steps: Steps defining the rollout process, used when "step_percentage" is absent.
              Specify only one of "step_percentage" or "steps" when creating a rollout.
              "steps" allow granular control over each step. Only valid for "rolling"
              strategy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/containers/applications/{application_id}/rollouts",
                account_id=account_id,
                application_id=application_id,
            ),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "strategy": strategy,
                    "target_configuration": target_configuration,
                    "kind": kind,
                    "percentage": percentage,
                    "step_percentage": step_percentage,
                    "steps": steps,
                },
                rollout_create_params.RolloutCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RolloutCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[RolloutCreateResponse], ResultWrapper[RolloutCreateResponse]),
        )


class RolloutsResourceWithRawResponse:
    def __init__(self, rollouts: RolloutsResource) -> None:
        self._rollouts = rollouts

        self.create = to_raw_response_wrapper(
            rollouts.create,
        )


class AsyncRolloutsResourceWithRawResponse:
    def __init__(self, rollouts: AsyncRolloutsResource) -> None:
        self._rollouts = rollouts

        self.create = async_to_raw_response_wrapper(
            rollouts.create,
        )


class RolloutsResourceWithStreamingResponse:
    def __init__(self, rollouts: RolloutsResource) -> None:
        self._rollouts = rollouts

        self.create = to_streamed_response_wrapper(
            rollouts.create,
        )


class AsyncRolloutsResourceWithStreamingResponse:
    def __init__(self, rollouts: AsyncRolloutsResource) -> None:
        self._rollouts = rollouts

        self.create = async_to_streamed_response_wrapper(
            rollouts.create,
        )
