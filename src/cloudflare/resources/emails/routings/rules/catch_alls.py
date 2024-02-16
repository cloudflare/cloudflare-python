# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.emails.routings.rules import (
    CatchAllEmailRoutingRoutingRulesGetCatchAllRuleResponse,
    CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleResponse,
    catch_all_email_routing_routing_rules_update_catch_all_rule_params,
)

from typing import Type, Iterable

from typing_extensions import Literal

from ....._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from .....types import shared_params
from .....types.emails.routings.rules import catch_all_email_routing_routing_rules_update_catch_all_rule_params
from ....._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["CatchAlls", "AsyncCatchAlls"]


class CatchAlls(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CatchAllsWithRawResponse:
        return CatchAllsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CatchAllsWithStreamingResponse:
        return CatchAllsWithStreamingResponse(self)

    def email_routing_routing_rules_get_catch_all_rule(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CatchAllEmailRoutingRoutingRulesGetCatchAllRuleResponse:
        """
        Get information on the default catch-all routing rule.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/email/routing/rules/catch_all",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[CatchAllEmailRoutingRoutingRulesGetCatchAllRuleResponse],
                ResultWrapper[CatchAllEmailRoutingRoutingRulesGetCatchAllRuleResponse],
            ),
        )

    def email_routing_routing_rules_update_catch_all_rule(
        self,
        zone_identifier: str,
        *,
        actions: Iterable[catch_all_email_routing_routing_rules_update_catch_all_rule_params.Action],
        matchers: Iterable[catch_all_email_routing_routing_rules_update_catch_all_rule_params.Matcher],
        enabled: Literal[True, False] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleResponse:
        """
        Enable or disable catch-all routing rule, or change action to forward to
        specific destination address.

        Args:
          zone_identifier: Identifier

          actions: List actions for the catch-all routing rule.

          matchers: List of matchers for the catch-all routing rule.

          enabled: Routing rule status.

          name: Routing rule name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._put(
            f"/zones/{zone_identifier}/email/routing/rules/catch_all",
            body=maybe_transform(
                {
                    "actions": actions,
                    "matchers": matchers,
                    "enabled": enabled,
                    "name": name,
                },
                catch_all_email_routing_routing_rules_update_catch_all_rule_params.CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleResponse],
                ResultWrapper[CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleResponse],
            ),
        )


class AsyncCatchAlls(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCatchAllsWithRawResponse:
        return AsyncCatchAllsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCatchAllsWithStreamingResponse:
        return AsyncCatchAllsWithStreamingResponse(self)

    async def email_routing_routing_rules_get_catch_all_rule(
        self,
        zone_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CatchAllEmailRoutingRoutingRulesGetCatchAllRuleResponse:
        """
        Get information on the default catch-all routing rule.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/email/routing/rules/catch_all",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[CatchAllEmailRoutingRoutingRulesGetCatchAllRuleResponse],
                ResultWrapper[CatchAllEmailRoutingRoutingRulesGetCatchAllRuleResponse],
            ),
        )

    async def email_routing_routing_rules_update_catch_all_rule(
        self,
        zone_identifier: str,
        *,
        actions: Iterable[catch_all_email_routing_routing_rules_update_catch_all_rule_params.Action],
        matchers: Iterable[catch_all_email_routing_routing_rules_update_catch_all_rule_params.Matcher],
        enabled: Literal[True, False] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleResponse:
        """
        Enable or disable catch-all routing rule, or change action to forward to
        specific destination address.

        Args:
          zone_identifier: Identifier

          actions: List actions for the catch-all routing rule.

          matchers: List of matchers for the catch-all routing rule.

          enabled: Routing rule status.

          name: Routing rule name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._put(
            f"/zones/{zone_identifier}/email/routing/rules/catch_all",
            body=maybe_transform(
                {
                    "actions": actions,
                    "matchers": matchers,
                    "enabled": enabled,
                    "name": name,
                },
                catch_all_email_routing_routing_rules_update_catch_all_rule_params.CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleResponse],
                ResultWrapper[CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleResponse],
            ),
        )


class CatchAllsWithRawResponse:
    def __init__(self, catch_alls: CatchAlls) -> None:
        self._catch_alls = catch_alls

        self.email_routing_routing_rules_get_catch_all_rule = to_raw_response_wrapper(
            catch_alls.email_routing_routing_rules_get_catch_all_rule,
        )
        self.email_routing_routing_rules_update_catch_all_rule = to_raw_response_wrapper(
            catch_alls.email_routing_routing_rules_update_catch_all_rule,
        )


class AsyncCatchAllsWithRawResponse:
    def __init__(self, catch_alls: AsyncCatchAlls) -> None:
        self._catch_alls = catch_alls

        self.email_routing_routing_rules_get_catch_all_rule = async_to_raw_response_wrapper(
            catch_alls.email_routing_routing_rules_get_catch_all_rule,
        )
        self.email_routing_routing_rules_update_catch_all_rule = async_to_raw_response_wrapper(
            catch_alls.email_routing_routing_rules_update_catch_all_rule,
        )


class CatchAllsWithStreamingResponse:
    def __init__(self, catch_alls: CatchAlls) -> None:
        self._catch_alls = catch_alls

        self.email_routing_routing_rules_get_catch_all_rule = to_streamed_response_wrapper(
            catch_alls.email_routing_routing_rules_get_catch_all_rule,
        )
        self.email_routing_routing_rules_update_catch_all_rule = to_streamed_response_wrapper(
            catch_alls.email_routing_routing_rules_update_catch_all_rule,
        )


class AsyncCatchAllsWithStreamingResponse:
    def __init__(self, catch_alls: AsyncCatchAlls) -> None:
        self._catch_alls = catch_alls

        self.email_routing_routing_rules_get_catch_all_rule = async_to_streamed_response_wrapper(
            catch_alls.email_routing_routing_rules_get_catch_all_rule,
        )
        self.email_routing_routing_rules_update_catch_all_rule = async_to_streamed_response_wrapper(
            catch_alls.email_routing_routing_rules_update_catch_all_rule,
        )
