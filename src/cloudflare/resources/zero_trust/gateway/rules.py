# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
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
            "redirect",
        ],
        name: str,
        description: str | Omit = omit,
        device_posture: str | Omit = omit,
        enabled: bool | Omit = omit,
        expiration: Optional[rule_create_params.Expiration] | Omit = omit,
        filters: List[GatewayFilter] | Omit = omit,
        identity: str | Omit = omit,
        precedence: int | Omit = omit,
        rule_settings: RuleSettingParam | Omit = omit,
        schedule: Optional[ScheduleParam] | Omit = omit,
        traffic: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[GatewayRule]:
        """
        Create a new Zero Trust Gateway rule.

        Args:
          action: Specify the action to perform when the associated traffic, identity, and device
              posture expressions either absent or evaluate to `true`.

          name: Specify the rule name.

          description: Specify the rule description.

          device_posture: Specify the wirefilter expression used for device posture check. The API
              automatically formats and sanitizes expressions before storing them. To prevent
              Terraform state drift, use the formatted expression returned in the API
              response.

          enabled: Specify whether the rule is enabled.

          expiration: Defines the expiration time stamp and default duration of a DNS policy. Takes
              precedence over the policy's `schedule` configuration, if any. This does not
              apply to HTTP or network policies. Settable only for `dns` rules.

          filters: Specify the protocol or layer to evaluate the traffic, identity, and device
              posture expressions.

          identity: Specify the wirefilter expression used for identity matching. The API
              automatically formats and sanitizes expressions before storing them. To prevent
              Terraform state drift, use the formatted expression returned in the API
              response.

          precedence: Set the order of your rules. Lower values indicate higher precedence. At each
              processing phase, evaluate applicable rules in ascending order of this value.
              Refer to
              [Order of enforcement](http://developers.cloudflare.com/learning-paths/secure-internet-traffic/understand-policies/order-of-enforcement/#manage-precedence-with-terraform)
              to manage precedence via Terraform.

          rule_settings: Set settings related to this rule. Each setting is only valid for specific rule
              types and can only be used with the appropriate selectors. If Terraform drift is
              observed in these setting values, verify that the setting is supported for the
              given rule type and that the API response reflects the requested value. If the
              API response returns sanitized or modified values that differ from the request,
              use the API-provided values in Terraform to ensure consistency.

          schedule: Defines the schedule for activating DNS policies. Settable only for `dns` and
              `dns_resolver` rules.

          traffic: Specify the wirefilter expression used for traffic matching. The API
              automatically formats and sanitizes expressions before storing them. To prevent
              Terraform state drift, use the formatted expression returned in the API
              response.

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
            "redirect",
        ],
        name: str,
        description: str | Omit = omit,
        device_posture: str | Omit = omit,
        enabled: bool | Omit = omit,
        expiration: Optional[rule_update_params.Expiration] | Omit = omit,
        filters: List[GatewayFilter] | Omit = omit,
        identity: str | Omit = omit,
        precedence: int | Omit = omit,
        rule_settings: RuleSettingParam | Omit = omit,
        schedule: Optional[ScheduleParam] | Omit = omit,
        traffic: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[GatewayRule]:
        """
        Update a configured Zero Trust Gateway rule.

        Args:
          rule_id: Identify the API resource with a UUID.

          action: Specify the action to perform when the associated traffic, identity, and device
              posture expressions either absent or evaluate to `true`.

          name: Specify the rule name.

          description: Specify the rule description.

          device_posture: Specify the wirefilter expression used for device posture check. The API
              automatically formats and sanitizes expressions before storing them. To prevent
              Terraform state drift, use the formatted expression returned in the API
              response.

          enabled: Specify whether the rule is enabled.

          expiration: Defines the expiration time stamp and default duration of a DNS policy. Takes
              precedence over the policy's `schedule` configuration, if any. This does not
              apply to HTTP or network policies. Settable only for `dns` rules.

          filters: Specify the protocol or layer to evaluate the traffic, identity, and device
              posture expressions.

          identity: Specify the wirefilter expression used for identity matching. The API
              automatically formats and sanitizes expressions before storing them. To prevent
              Terraform state drift, use the formatted expression returned in the API
              response.

          precedence: Set the order of your rules. Lower values indicate higher precedence. At each
              processing phase, evaluate applicable rules in ascending order of this value.
              Refer to
              [Order of enforcement](http://developers.cloudflare.com/learning-paths/secure-internet-traffic/understand-policies/order-of-enforcement/#manage-precedence-with-terraform)
              to manage precedence via Terraform.

          rule_settings: Set settings related to this rule. Each setting is only valid for specific rule
              types and can only be used with the appropriate selectors. If Terraform drift is
              observed in these setting values, verify that the setting is supported for the
              given rule type and that the API response reflects the requested value. If the
              API response returns sanitized or modified values that differ from the request,
              use the API-provided values in Terraform to ensure consistency.

          schedule: Defines the schedule for activating DNS policies. Settable only for `dns` and
              `dns_resolver` rules.

          traffic: Specify the wirefilter expression used for traffic matching. The API
              automatically formats and sanitizes expressions before storing them. To prevent
              Terraform state drift, use the formatted expression returned in the API
              response.

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[GatewayRule]:
        """
        List Zero Trust Gateway rules for an account.

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a Zero Trust Gateway rule.

        Args:
          rule_id: Identify the API resource with a UUID.

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[GatewayRule]:
        """
        Get a single Zero Trust Gateway rule.

        Args:
          rule_id: Identify the API resource with a UUID.

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

    def list_tenant(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[GatewayRule]:
        """
        List Zero Trust Gateway rules for the parent account of an account in the MSP
        configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/gateway/rules/tenant",
            page=SyncSinglePage[GatewayRule],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=GatewayRule,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[GatewayRule]:
        """
        Resets the expiration of a Zero Trust Gateway Rule if its duration elapsed and
        it has a default duration. The Zero Trust Gateway Rule must have values for both
        `expiration.expires_at` and `expiration.duration`.

        Args:
          rule_id: Identify the API resource with a UUID.

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
            "redirect",
        ],
        name: str,
        description: str | Omit = omit,
        device_posture: str | Omit = omit,
        enabled: bool | Omit = omit,
        expiration: Optional[rule_create_params.Expiration] | Omit = omit,
        filters: List[GatewayFilter] | Omit = omit,
        identity: str | Omit = omit,
        precedence: int | Omit = omit,
        rule_settings: RuleSettingParam | Omit = omit,
        schedule: Optional[ScheduleParam] | Omit = omit,
        traffic: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[GatewayRule]:
        """
        Create a new Zero Trust Gateway rule.

        Args:
          action: Specify the action to perform when the associated traffic, identity, and device
              posture expressions either absent or evaluate to `true`.

          name: Specify the rule name.

          description: Specify the rule description.

          device_posture: Specify the wirefilter expression used for device posture check. The API
              automatically formats and sanitizes expressions before storing them. To prevent
              Terraform state drift, use the formatted expression returned in the API
              response.

          enabled: Specify whether the rule is enabled.

          expiration: Defines the expiration time stamp and default duration of a DNS policy. Takes
              precedence over the policy's `schedule` configuration, if any. This does not
              apply to HTTP or network policies. Settable only for `dns` rules.

          filters: Specify the protocol or layer to evaluate the traffic, identity, and device
              posture expressions.

          identity: Specify the wirefilter expression used for identity matching. The API
              automatically formats and sanitizes expressions before storing them. To prevent
              Terraform state drift, use the formatted expression returned in the API
              response.

          precedence: Set the order of your rules. Lower values indicate higher precedence. At each
              processing phase, evaluate applicable rules in ascending order of this value.
              Refer to
              [Order of enforcement](http://developers.cloudflare.com/learning-paths/secure-internet-traffic/understand-policies/order-of-enforcement/#manage-precedence-with-terraform)
              to manage precedence via Terraform.

          rule_settings: Set settings related to this rule. Each setting is only valid for specific rule
              types and can only be used with the appropriate selectors. If Terraform drift is
              observed in these setting values, verify that the setting is supported for the
              given rule type and that the API response reflects the requested value. If the
              API response returns sanitized or modified values that differ from the request,
              use the API-provided values in Terraform to ensure consistency.

          schedule: Defines the schedule for activating DNS policies. Settable only for `dns` and
              `dns_resolver` rules.

          traffic: Specify the wirefilter expression used for traffic matching. The API
              automatically formats and sanitizes expressions before storing them. To prevent
              Terraform state drift, use the formatted expression returned in the API
              response.

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
            "redirect",
        ],
        name: str,
        description: str | Omit = omit,
        device_posture: str | Omit = omit,
        enabled: bool | Omit = omit,
        expiration: Optional[rule_update_params.Expiration] | Omit = omit,
        filters: List[GatewayFilter] | Omit = omit,
        identity: str | Omit = omit,
        precedence: int | Omit = omit,
        rule_settings: RuleSettingParam | Omit = omit,
        schedule: Optional[ScheduleParam] | Omit = omit,
        traffic: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[GatewayRule]:
        """
        Update a configured Zero Trust Gateway rule.

        Args:
          rule_id: Identify the API resource with a UUID.

          action: Specify the action to perform when the associated traffic, identity, and device
              posture expressions either absent or evaluate to `true`.

          name: Specify the rule name.

          description: Specify the rule description.

          device_posture: Specify the wirefilter expression used for device posture check. The API
              automatically formats and sanitizes expressions before storing them. To prevent
              Terraform state drift, use the formatted expression returned in the API
              response.

          enabled: Specify whether the rule is enabled.

          expiration: Defines the expiration time stamp and default duration of a DNS policy. Takes
              precedence over the policy's `schedule` configuration, if any. This does not
              apply to HTTP or network policies. Settable only for `dns` rules.

          filters: Specify the protocol or layer to evaluate the traffic, identity, and device
              posture expressions.

          identity: Specify the wirefilter expression used for identity matching. The API
              automatically formats and sanitizes expressions before storing them. To prevent
              Terraform state drift, use the formatted expression returned in the API
              response.

          precedence: Set the order of your rules. Lower values indicate higher precedence. At each
              processing phase, evaluate applicable rules in ascending order of this value.
              Refer to
              [Order of enforcement](http://developers.cloudflare.com/learning-paths/secure-internet-traffic/understand-policies/order-of-enforcement/#manage-precedence-with-terraform)
              to manage precedence via Terraform.

          rule_settings: Set settings related to this rule. Each setting is only valid for specific rule
              types and can only be used with the appropriate selectors. If Terraform drift is
              observed in these setting values, verify that the setting is supported for the
              given rule type and that the API response reflects the requested value. If the
              API response returns sanitized or modified values that differ from the request,
              use the API-provided values in Terraform to ensure consistency.

          schedule: Defines the schedule for activating DNS policies. Settable only for `dns` and
              `dns_resolver` rules.

          traffic: Specify the wirefilter expression used for traffic matching. The API
              automatically formats and sanitizes expressions before storing them. To prevent
              Terraform state drift, use the formatted expression returned in the API
              response.

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[GatewayRule, AsyncSinglePage[GatewayRule]]:
        """
        List Zero Trust Gateway rules for an account.

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a Zero Trust Gateway rule.

        Args:
          rule_id: Identify the API resource with a UUID.

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[GatewayRule]:
        """
        Get a single Zero Trust Gateway rule.

        Args:
          rule_id: Identify the API resource with a UUID.

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

    def list_tenant(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[GatewayRule, AsyncSinglePage[GatewayRule]]:
        """
        List Zero Trust Gateway rules for the parent account of an account in the MSP
        configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/gateway/rules/tenant",
            page=AsyncSinglePage[GatewayRule],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=GatewayRule,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[GatewayRule]:
        """
        Resets the expiration of a Zero Trust Gateway Rule if its duration elapsed and
        it has a default duration. The Zero Trust Gateway Rule must have values for both
        `expiration.expires_at` and `expiration.duration`.

        Args:
          rule_id: Identify the API resource with a UUID.

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
        self.list_tenant = to_raw_response_wrapper(
            rules.list_tenant,
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
        self.list_tenant = async_to_raw_response_wrapper(
            rules.list_tenant,
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
        self.list_tenant = to_streamed_response_wrapper(
            rules.list_tenant,
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
        self.list_tenant = async_to_streamed_response_wrapper(
            rules.list_tenant,
        )
        self.reset_expiration = async_to_streamed_response_wrapper(
            rules.reset_expiration,
        )
