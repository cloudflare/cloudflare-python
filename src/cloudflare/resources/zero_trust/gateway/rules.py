# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Type, Optional, cast
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
from ...._base_client import (
    make_request_options,
)
from ....types.zero_trust.gateway import (
    RuleListResponse,
    RuleDeleteResponse,
    ZeroTrustGatewayRules,
    rule_create_params,
    rule_update_params,
)

__all__ = ["Rules", "AsyncRules"]


class Rules(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: object,
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
            "audit_ssh",
        ],
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        device_posture: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        filters: List[Literal["http", "dns", "l4", "egress"]] | NotGiven = NOT_GIVEN,
        identity: str | NotGiven = NOT_GIVEN,
        precedence: int | NotGiven = NOT_GIVEN,
        rule_settings: rule_create_params.RuleSettings | NotGiven = NOT_GIVEN,
        schedule: rule_create_params.Schedule | NotGiven = NOT_GIVEN,
        traffic: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ZeroTrustGatewayRules:
        """
        Creates a new Zero Trust Gateway rule.

        Args:
          action: The action to preform when the associated traffic, identity, and device posture
              expressions are either absent or evaluate to `true`.

          name: The name of the rule.

          description: The description of the rule.

          device_posture: The wirefilter expression used for device posture check matching.

          enabled: True if the rule is enabled.

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
        return self._post(
            f"/accounts/{account_id}/gateway/rules",
            body=maybe_transform(
                {
                    "action": action,
                    "name": name,
                    "description": description,
                    "device_posture": device_posture,
                    "enabled": enabled,
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ZeroTrustGatewayRules], ResultWrapper[ZeroTrustGatewayRules]),
        )

    def update(
        self,
        rule_id: str,
        *,
        account_id: object,
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
            "audit_ssh",
        ],
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        device_posture: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        filters: List[Literal["http", "dns", "l4", "egress"]] | NotGiven = NOT_GIVEN,
        identity: str | NotGiven = NOT_GIVEN,
        precedence: int | NotGiven = NOT_GIVEN,
        rule_settings: rule_update_params.RuleSettings | NotGiven = NOT_GIVEN,
        schedule: rule_update_params.Schedule | NotGiven = NOT_GIVEN,
        traffic: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ZeroTrustGatewayRules:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ZeroTrustGatewayRules], ResultWrapper[ZeroTrustGatewayRules]),
        )

    def list(
        self,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleListResponse]:
        """
        Fetches the Zero Trust Gateway rules for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/gateway/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleListResponse]], ResultWrapper[RuleListResponse]),
        )

    def delete(
        self,
        rule_id: str,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleDeleteResponse:
        """
        Deletes a Zero Trust Gateway rule.

        Args:
          rule_id: The API resource UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return cast(
            RuleDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/gateway/rules/{rule_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RuleDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        rule_id: str,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ZeroTrustGatewayRules:
        """
        Fetches a single Zero Trust Gateway rule.

        Args:
          rule_id: The API resource UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._get(
            f"/accounts/{account_id}/gateway/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ZeroTrustGatewayRules], ResultWrapper[ZeroTrustGatewayRules]),
        )


class AsyncRules(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: object,
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
            "audit_ssh",
        ],
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        device_posture: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        filters: List[Literal["http", "dns", "l4", "egress"]] | NotGiven = NOT_GIVEN,
        identity: str | NotGiven = NOT_GIVEN,
        precedence: int | NotGiven = NOT_GIVEN,
        rule_settings: rule_create_params.RuleSettings | NotGiven = NOT_GIVEN,
        schedule: rule_create_params.Schedule | NotGiven = NOT_GIVEN,
        traffic: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ZeroTrustGatewayRules:
        """
        Creates a new Zero Trust Gateway rule.

        Args:
          action: The action to preform when the associated traffic, identity, and device posture
              expressions are either absent or evaluate to `true`.

          name: The name of the rule.

          description: The description of the rule.

          device_posture: The wirefilter expression used for device posture check matching.

          enabled: True if the rule is enabled.

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
        return await self._post(
            f"/accounts/{account_id}/gateway/rules",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "name": name,
                    "description": description,
                    "device_posture": device_posture,
                    "enabled": enabled,
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ZeroTrustGatewayRules], ResultWrapper[ZeroTrustGatewayRules]),
        )

    async def update(
        self,
        rule_id: str,
        *,
        account_id: object,
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
            "audit_ssh",
        ],
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        device_posture: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        filters: List[Literal["http", "dns", "l4", "egress"]] | NotGiven = NOT_GIVEN,
        identity: str | NotGiven = NOT_GIVEN,
        precedence: int | NotGiven = NOT_GIVEN,
        rule_settings: rule_update_params.RuleSettings | NotGiven = NOT_GIVEN,
        schedule: rule_update_params.Schedule | NotGiven = NOT_GIVEN,
        traffic: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ZeroTrustGatewayRules:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ZeroTrustGatewayRules], ResultWrapper[ZeroTrustGatewayRules]),
        )

    async def list(
        self,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleListResponse]:
        """
        Fetches the Zero Trust Gateway rules for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/gateway/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleListResponse]], ResultWrapper[RuleListResponse]),
        )

    async def delete(
        self,
        rule_id: str,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleDeleteResponse:
        """
        Deletes a Zero Trust Gateway rule.

        Args:
          rule_id: The API resource UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return cast(
            RuleDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/gateway/rules/{rule_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RuleDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        rule_id: str,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ZeroTrustGatewayRules:
        """
        Fetches a single Zero Trust Gateway rule.

        Args:
          rule_id: The API resource UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._get(
            f"/accounts/{account_id}/gateway/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ZeroTrustGatewayRules], ResultWrapper[ZeroTrustGatewayRules]),
        )


class RulesWithRawResponse:
    def __init__(self, rules: Rules) -> None:
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


class AsyncRulesWithRawResponse:
    def __init__(self, rules: AsyncRules) -> None:
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


class RulesWithStreamingResponse:
    def __init__(self, rules: Rules) -> None:
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


class AsyncRulesWithStreamingResponse:
    def __init__(self, rules: AsyncRules) -> None:
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
