# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast
from typing_extensions import Literal

import httpx

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
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.zero_trust.gateway import rule_create_params, rule_update_params
from ....types.zero_trust.gateway.gateway_rule import GatewayRule
from ....types.zero_trust.gateway.gateway_filter import GatewayFilter
from ....types.zero_trust.gateway.schedule_param import ScheduleParam
from ....types.zero_trust.gateway.rule_setting_param import RuleSettingParam

__all__ = ["RulesResource", "AsyncRulesResource"]


class RulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RulesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        action: Literal[
            "on",
            "off",
            "allow",
            "block",
            "scan",
            "noscan",
            "safesearch",
            "ytrestricted",
            "isolate",
            "noisolate",
            "override",
            "l4_override",
            "egress",
            "resolve",
            "quarantine",
        ],
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        device_posture: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expiration: rule_create_params.Expiration | NotGiven = NOT_GIVEN,
        filters: List[GatewayFilter] | NotGiven = NOT_GIVEN,
        identity: str | NotGiven = NOT_GIVEN,
        precedence: int | NotGiven = NOT_GIVEN,
        rule_settings: RuleSettingParam | NotGiven = NOT_GIVEN,
        schedule: ScheduleParam | NotGiven = NOT_GIVEN,
        traffic: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GatewayRule]:
        """
        Creates a new Zero Trust Gateway rule.

        Args:
          action: The action to preform when the associated traffic, identity, and device posture
              expressions are either absent or evaluate to `true`.

          name: The name of the rule.

          description: The description of the rule.

          device_posture: The wirefilter expression used for device posture check matching.

          enabled: True if the rule is enabled.

          expiration: The expiration time stamp and default duration of a DNS policy. Takes precedence
              over the policy's `schedule` configuration, if any.

              This does not apply to HTTP or network policies.

          filters: The protocol or layer to evaluate the traffic, identity, and device posture
              expressions.

          identity: The wirefilter expression used for identity matching.

          precedence: Precedence sets the order of your rules. Lower values indicate higher
              precedence. At each processing phase, applicable rules are evaluated in
              ascending order of this value.

          rule_settings: Additional settings that modify the rule's action.

          schedule: The schedule for activating DNS policies. This does not apply to HTTP or network
              policies.

          traffic: The wirefilter expression used for traffic matching.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/gateway/rules",
            body=maybe_transform(
                {
                    "action": action,
                    "name": name,
                    "description": description,
                    "device_posture": device_posture,
                    "enabled": enabled,
                    "expiration": expiration,
                    "filters": filters,
                    "identity": identity,
                    "precedence": precedence,
                    "rule_settings": rule_settings,
                    "schedule": schedule,
                    "traffic": traffic,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[GatewayRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GatewayRule]], ResultWrapper[GatewayRule]),
        )

    def update(
        self,
        rule_id: str,
        *,
        account_id: str,
        action: Literal[
            "on",
            "off",
            "allow",
            "block",
            "scan",
            "noscan",
            "safesearch",
            "ytrestricted",
            "isolate",
            "noisolate",
            "override",
            "l4_override",
            "egress",
            "resolve",
            "quarantine",
        ],
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        device_posture: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expiration: rule_update_params.Expiration | NotGiven = NOT_GIVEN,
        filters: List[GatewayFilter] | NotGiven = NOT_GIVEN,
        identity: str | NotGiven = NOT_GIVEN,
        precedence: int | NotGiven = NOT_GIVEN,
        rule_settings: RuleSettingParam | NotGiven = NOT_GIVEN,
        schedule: ScheduleParam | NotGiven = NOT_GIVEN,
        traffic: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GatewayRule]:
        """
        Updates a configured Zero Trust Gateway rule.

        Args:
          rule_id: The API resource UUID.

          action: The action to preform when the associated traffic, identity, and device posture
              expressions are either absent or evaluate to `true`.

          name: The name of the rule.

          description: The description of the rule.

          device_posture: The wirefilter expression used for device posture check matching.

          enabled: True if the rule is enabled.

          expiration: The expiration time stamp and default duration of a DNS policy. Takes precedence
              over the policy's `schedule` configuration, if any.

              This does not apply to HTTP or network policies.

          filters: The protocol or layer to evaluate the traffic, identity, and device posture
              expressions.

          identity: The wirefilter expression used for identity matching.

          precedence: Precedence sets the order of your rules. Lower values indicate higher
              precedence. At each processing phase, applicable rules are evaluated in
              ascending order of this value.

          rule_settings: Additional settings that modify the rule's action.

          schedule: The schedule for activating DNS policies. This does not apply to HTTP or network
              policies.

          traffic: The wirefilter expression used for traffic matching.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._put(
            f"/accounts/{account_id}/gateway/rules/{rule_id}",
            body=maybe_transform(
                {
                    "action": action,
                    "name": name,
                    "description": description,
                    "device_posture": device_posture,
                    "enabled": enabled,
                    "expiration": expiration,
                    "filters": filters,
                    "identity": identity,
                    "precedence": precedence,
                    "rule_settings": rule_settings,
                    "schedule": schedule,
                    "traffic": traffic,
                },
                rule_update_params.RuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[GatewayRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GatewayRule]], ResultWrapper[GatewayRule]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[GatewayRule]:
        """
        Fetches the Zero Trust Gateway rules for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/gateway/rules",
            page=SyncSinglePage[GatewayRule],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=GatewayRule,
        )

    def delete(
        self,
        rule_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes a Zero Trust Gateway rule.

        Args:
          rule_id: The API resource UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._delete(
            f"/accounts/{account_id}/gateway/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def get(
        self,
        rule_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GatewayRule]:
        """
        Fetches a single Zero Trust Gateway rule.

        Args:
          rule_id: The API resource UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._get(
            f"/accounts/{account_id}/gateway/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[GatewayRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GatewayRule]], ResultWrapper[GatewayRule]),
        )

    def reset_expiration(
        self,
        rule_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GatewayRule]:
        """
        Resets the expiration of a Zero Trust Gateway Rule if its duration has elapsed
        and it has a default duration.

        The Zero Trust Gateway Rule must have values for both `expiration.expires_at`
        and `expiration.duration`.

        Args:
          rule_id: The API resource UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._post(
            f"/accounts/{account_id}/gateway/rules/{rule_id}/reset_expiration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[GatewayRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GatewayRule]], ResultWrapper[GatewayRule]),
        )


class AsyncRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRulesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        action: Literal[
            "on",
            "off",
            "allow",
            "block",
            "scan",
            "noscan",
            "safesearch",
            "ytrestricted",
            "isolate",
            "noisolate",
            "override",
            "l4_override",
            "egress",
            "resolve",
            "quarantine",
        ],
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        device_posture: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expiration: rule_create_params.Expiration | NotGiven = NOT_GIVEN,
        filters: List[GatewayFilter] | NotGiven = NOT_GIVEN,
        identity: str | NotGiven = NOT_GIVEN,
        precedence: int | NotGiven = NOT_GIVEN,
        rule_settings: RuleSettingParam | NotGiven = NOT_GIVEN,
        schedule: ScheduleParam | NotGiven = NOT_GIVEN,
        traffic: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GatewayRule]:
        """
        Creates a new Zero Trust Gateway rule.

        Args:
          action: The action to preform when the associated traffic, identity, and device posture
              expressions are either absent or evaluate to `true`.

          name: The name of the rule.

          description: The description of the rule.

          device_posture: The wirefilter expression used for device posture check matching.

          enabled: True if the rule is enabled.

          expiration: The expiration time stamp and default duration of a DNS policy. Takes precedence
              over the policy's `schedule` configuration, if any.

              This does not apply to HTTP or network policies.

          filters: The protocol or layer to evaluate the traffic, identity, and device posture
              expressions.

          identity: The wirefilter expression used for identity matching.

          precedence: Precedence sets the order of your rules. Lower values indicate higher
              precedence. At each processing phase, applicable rules are evaluated in
              ascending order of this value.

          rule_settings: Additional settings that modify the rule's action.

          schedule: The schedule for activating DNS policies. This does not apply to HTTP or network
              policies.

          traffic: The wirefilter expression used for traffic matching.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/gateway/rules",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "name": name,
                    "description": description,
                    "device_posture": device_posture,
                    "enabled": enabled,
                    "expiration": expiration,
                    "filters": filters,
                    "identity": identity,
                    "precedence": precedence,
                    "rule_settings": rule_settings,
                    "schedule": schedule,
                    "traffic": traffic,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[GatewayRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GatewayRule]], ResultWrapper[GatewayRule]),
        )

    async def update(
        self,
        rule_id: str,
        *,
        account_id: str,
        action: Literal[
            "on",
            "off",
            "allow",
            "block",
            "scan",
            "noscan",
            "safesearch",
            "ytrestricted",
            "isolate",
            "noisolate",
            "override",
            "l4_override",
            "egress",
            "resolve",
            "quarantine",
        ],
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        device_posture: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expiration: rule_update_params.Expiration | NotGiven = NOT_GIVEN,
        filters: List[GatewayFilter] | NotGiven = NOT_GIVEN,
        identity: str | NotGiven = NOT_GIVEN,
        precedence: int | NotGiven = NOT_GIVEN,
        rule_settings: RuleSettingParam | NotGiven = NOT_GIVEN,
        schedule: ScheduleParam | NotGiven = NOT_GIVEN,
        traffic: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GatewayRule]:
        """
        Updates a configured Zero Trust Gateway rule.

        Args:
          rule_id: The API resource UUID.

          action: The action to preform when the associated traffic, identity, and device posture
              expressions are either absent or evaluate to `true`.

          name: The name of the rule.

          description: The description of the rule.

          device_posture: The wirefilter expression used for device posture check matching.

          enabled: True if the rule is enabled.

          expiration: The expiration time stamp and default duration of a DNS policy. Takes precedence
              over the policy's `schedule` configuration, if any.

              This does not apply to HTTP or network policies.

          filters: The protocol or layer to evaluate the traffic, identity, and device posture
              expressions.

          identity: The wirefilter expression used for identity matching.

          precedence: Precedence sets the order of your rules. Lower values indicate higher
              precedence. At each processing phase, applicable rules are evaluated in
              ascending order of this value.

          rule_settings: Additional settings that modify the rule's action.

          schedule: The schedule for activating DNS policies. This does not apply to HTTP or network
              policies.

          traffic: The wirefilter expression used for traffic matching.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._put(
            f"/accounts/{account_id}/gateway/rules/{rule_id}",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "name": name,
                    "description": description,
                    "device_posture": device_posture,
                    "enabled": enabled,
                    "expiration": expiration,
                    "filters": filters,
                    "identity": identity,
                    "precedence": precedence,
                    "rule_settings": rule_settings,
                    "schedule": schedule,
                    "traffic": traffic,
                },
                rule_update_params.RuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[GatewayRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GatewayRule]], ResultWrapper[GatewayRule]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[GatewayRule, AsyncSinglePage[GatewayRule]]:
        """
        Fetches the Zero Trust Gateway rules for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/gateway/rules",
            page=AsyncSinglePage[GatewayRule],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=GatewayRule,
        )

    async def delete(
        self,
        rule_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes a Zero Trust Gateway rule.

        Args:
          rule_id: The API resource UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/gateway/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def get(
        self,
        rule_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GatewayRule]:
        """
        Fetches a single Zero Trust Gateway rule.

        Args:
          rule_id: The API resource UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._get(
            f"/accounts/{account_id}/gateway/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[GatewayRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GatewayRule]], ResultWrapper[GatewayRule]),
        )

    async def reset_expiration(
        self,
        rule_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GatewayRule]:
        """
        Resets the expiration of a Zero Trust Gateway Rule if its duration has elapsed
        and it has a default duration.

        The Zero Trust Gateway Rule must have values for both `expiration.expires_at`
        and `expiration.duration`.

        Args:
          rule_id: The API resource UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._post(
            f"/accounts/{account_id}/gateway/rules/{rule_id}/reset_expiration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[GatewayRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[GatewayRule]], ResultWrapper[GatewayRule]),
        )


class RulesResourceWithRawResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.create = to_raw_response_wrapper(
            rules.create,
        )
        self.update = to_raw_response_wrapper(
            rules.update,
        )
        self.list = to_raw_response_wrapper(
            rules.list,
        )
        self.delete = to_raw_response_wrapper(
            rules.delete,
        )
        self.get = to_raw_response_wrapper(
            rules.get,
        )
        self.reset_expiration = to_raw_response_wrapper(
            rules.reset_expiration,
        )


class AsyncRulesResourceWithRawResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.create = async_to_raw_response_wrapper(
            rules.create,
        )
        self.update = async_to_raw_response_wrapper(
            rules.update,
        )
        self.list = async_to_raw_response_wrapper(
            rules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            rules.delete,
        )
        self.get = async_to_raw_response_wrapper(
            rules.get,
        )
        self.reset_expiration = async_to_raw_response_wrapper(
            rules.reset_expiration,
        )


class RulesResourceWithStreamingResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.create = to_streamed_response_wrapper(
            rules.create,
        )
        self.update = to_streamed_response_wrapper(
            rules.update,
        )
        self.list = to_streamed_response_wrapper(
            rules.list,
        )
        self.delete = to_streamed_response_wrapper(
            rules.delete,
        )
        self.get = to_streamed_response_wrapper(
            rules.get,
        )
        self.reset_expiration = to_streamed_response_wrapper(
            rules.reset_expiration,
        )


class AsyncRulesResourceWithStreamingResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.create = async_to_streamed_response_wrapper(
            rules.create,
        )
        self.update = async_to_streamed_response_wrapper(
            rules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            rules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            rules.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            rules.get,
        )
        self.reset_expiration = async_to_streamed_response_wrapper(
            rules.reset_expiration,
        )
