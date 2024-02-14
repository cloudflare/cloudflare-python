# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .catch_alls import CatchAlls, AsyncCatchAlls

from ....._compat import cached_property

from .....types.emails.routings import (
    RuleUpdateResponse,
    RuleDeleteResponse,
    RuleEmailRoutingRoutingRulesCreateRoutingRuleResponse,
    RuleEmailRoutingRoutingRulesListRoutingRulesResponse,
    RuleGetResponse,
    rule_update_params,
    rule_email_routing_routing_rules_create_routing_rule_params,
)

from typing import Type, Iterable, Optional

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
from .....types.emails.routings import rule_update_params
from .....types.emails.routings import rule_email_routing_routing_rules_create_routing_rule_params
from .....types.emails.routings import rule_email_routing_routing_rules_list_routing_rules_params
from .catch_alls import (
    CatchAlls,
    AsyncCatchAlls,
    CatchAllsWithRawResponse,
    AsyncCatchAllsWithRawResponse,
    CatchAllsWithStreamingResponse,
    AsyncCatchAllsWithStreamingResponse,
)
from ....._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Rules", "AsyncRules"]


class Rules(SyncAPIResource):
    @cached_property
    def catch_alls(self) -> CatchAlls:
        return CatchAlls(self._client)

    @cached_property
    def with_raw_response(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self)

    def update(
        self,
        rule_identifier: str,
        *,
        zone_identifier: str,
        actions: Iterable[rule_update_params.Action],
        matchers: Iterable[rule_update_params.Matcher],
        enabled: Literal[True, False] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleUpdateResponse:
        """
        Update actions and matches, or enable/disable specific routing rules.

        Args:
          zone_identifier: Identifier

          rule_identifier: Routing rule identifier.

          actions: List actions patterns.

          matchers: Matching patterns to forward to your actions.

          enabled: Routing rule status.

          name: Routing rule name.

          priority: Priority of the routing rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not rule_identifier:
            raise ValueError(f"Expected a non-empty value for `rule_identifier` but received {rule_identifier!r}")
        return self._put(
            f"/zones/{zone_identifier}/email/routing/rules/{rule_identifier}",
            body=maybe_transform(
                {
                    "actions": actions,
                    "matchers": matchers,
                    "enabled": enabled,
                    "name": name,
                    "priority": priority,
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
            cast_to=cast(Type[RuleUpdateResponse], ResultWrapper[RuleUpdateResponse]),
        )

    def delete(
        self,
        rule_identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleDeleteResponse:
        """
        Delete a specific routing rule.

        Args:
          zone_identifier: Identifier

          rule_identifier: Routing rule identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not rule_identifier:
            raise ValueError(f"Expected a non-empty value for `rule_identifier` but received {rule_identifier!r}")
        return self._delete(
            f"/zones/{zone_identifier}/email/routing/rules/{rule_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RuleDeleteResponse], ResultWrapper[RuleDeleteResponse]),
        )

    def email_routing_routing_rules_create_routing_rule(
        self,
        zone_identifier: str,
        *,
        actions: Iterable[rule_email_routing_routing_rules_create_routing_rule_params.Action],
        matchers: Iterable[rule_email_routing_routing_rules_create_routing_rule_params.Matcher],
        enabled: Literal[True, False] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleEmailRoutingRoutingRulesCreateRoutingRuleResponse:
        """
        Rules consist of a set of criteria for matching emails (such as an email being
        sent to a specific custom email address) plus a set of actions to take on the
        email (like forwarding it to a specific destination address).

        Args:
          zone_identifier: Identifier

          actions: List actions patterns.

          matchers: Matching patterns to forward to your actions.

          enabled: Routing rule status.

          name: Routing rule name.

          priority: Priority of the routing rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._post(
            f"/zones/{zone_identifier}/email/routing/rules",
            body=maybe_transform(
                {
                    "actions": actions,
                    "matchers": matchers,
                    "enabled": enabled,
                    "name": name,
                    "priority": priority,
                },
                rule_email_routing_routing_rules_create_routing_rule_params.RuleEmailRoutingRoutingRulesCreateRoutingRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[RuleEmailRoutingRoutingRulesCreateRoutingRuleResponse],
                ResultWrapper[RuleEmailRoutingRoutingRulesCreateRoutingRuleResponse],
            ),
        )

    def email_routing_routing_rules_list_routing_rules(
        self,
        zone_identifier: str,
        *,
        enabled: Literal[True, False] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleEmailRoutingRoutingRulesListRoutingRulesResponse]:
        """
        Lists existing routing rules.

        Args:
          zone_identifier: Identifier

          enabled: Filter by enabled routing rules.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/email/routing/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "enabled": enabled,
                        "page": page,
                        "per_page": per_page,
                    },
                    rule_email_routing_routing_rules_list_routing_rules_params.RuleEmailRoutingRoutingRulesListRoutingRulesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleEmailRoutingRoutingRulesListRoutingRulesResponse]],
                ResultWrapper[RuleEmailRoutingRoutingRulesListRoutingRulesResponse],
            ),
        )

    def get(
        self,
        rule_identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleGetResponse:
        """
        Get information for a specific routing rule already created.

        Args:
          zone_identifier: Identifier

          rule_identifier: Routing rule identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not rule_identifier:
            raise ValueError(f"Expected a non-empty value for `rule_identifier` but received {rule_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/email/routing/rules/{rule_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RuleGetResponse], ResultWrapper[RuleGetResponse]),
        )


class AsyncRules(AsyncAPIResource):
    @cached_property
    def catch_alls(self) -> AsyncCatchAlls:
        return AsyncCatchAlls(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self)

    async def update(
        self,
        rule_identifier: str,
        *,
        zone_identifier: str,
        actions: Iterable[rule_update_params.Action],
        matchers: Iterable[rule_update_params.Matcher],
        enabled: Literal[True, False] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleUpdateResponse:
        """
        Update actions and matches, or enable/disable specific routing rules.

        Args:
          zone_identifier: Identifier

          rule_identifier: Routing rule identifier.

          actions: List actions patterns.

          matchers: Matching patterns to forward to your actions.

          enabled: Routing rule status.

          name: Routing rule name.

          priority: Priority of the routing rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not rule_identifier:
            raise ValueError(f"Expected a non-empty value for `rule_identifier` but received {rule_identifier!r}")
        return await self._put(
            f"/zones/{zone_identifier}/email/routing/rules/{rule_identifier}",
            body=maybe_transform(
                {
                    "actions": actions,
                    "matchers": matchers,
                    "enabled": enabled,
                    "name": name,
                    "priority": priority,
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
            cast_to=cast(Type[RuleUpdateResponse], ResultWrapper[RuleUpdateResponse]),
        )

    async def delete(
        self,
        rule_identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleDeleteResponse:
        """
        Delete a specific routing rule.

        Args:
          zone_identifier: Identifier

          rule_identifier: Routing rule identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not rule_identifier:
            raise ValueError(f"Expected a non-empty value for `rule_identifier` but received {rule_identifier!r}")
        return await self._delete(
            f"/zones/{zone_identifier}/email/routing/rules/{rule_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RuleDeleteResponse], ResultWrapper[RuleDeleteResponse]),
        )

    async def email_routing_routing_rules_create_routing_rule(
        self,
        zone_identifier: str,
        *,
        actions: Iterable[rule_email_routing_routing_rules_create_routing_rule_params.Action],
        matchers: Iterable[rule_email_routing_routing_rules_create_routing_rule_params.Matcher],
        enabled: Literal[True, False] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleEmailRoutingRoutingRulesCreateRoutingRuleResponse:
        """
        Rules consist of a set of criteria for matching emails (such as an email being
        sent to a specific custom email address) plus a set of actions to take on the
        email (like forwarding it to a specific destination address).

        Args:
          zone_identifier: Identifier

          actions: List actions patterns.

          matchers: Matching patterns to forward to your actions.

          enabled: Routing rule status.

          name: Routing rule name.

          priority: Priority of the routing rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._post(
            f"/zones/{zone_identifier}/email/routing/rules",
            body=maybe_transform(
                {
                    "actions": actions,
                    "matchers": matchers,
                    "enabled": enabled,
                    "name": name,
                    "priority": priority,
                },
                rule_email_routing_routing_rules_create_routing_rule_params.RuleEmailRoutingRoutingRulesCreateRoutingRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[RuleEmailRoutingRoutingRulesCreateRoutingRuleResponse],
                ResultWrapper[RuleEmailRoutingRoutingRulesCreateRoutingRuleResponse],
            ),
        )

    async def email_routing_routing_rules_list_routing_rules(
        self,
        zone_identifier: str,
        *,
        enabled: Literal[True, False] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleEmailRoutingRoutingRulesListRoutingRulesResponse]:
        """
        Lists existing routing rules.

        Args:
          zone_identifier: Identifier

          enabled: Filter by enabled routing rules.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/email/routing/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "enabled": enabled,
                        "page": page,
                        "per_page": per_page,
                    },
                    rule_email_routing_routing_rules_list_routing_rules_params.RuleEmailRoutingRoutingRulesListRoutingRulesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleEmailRoutingRoutingRulesListRoutingRulesResponse]],
                ResultWrapper[RuleEmailRoutingRoutingRulesListRoutingRulesResponse],
            ),
        )

    async def get(
        self,
        rule_identifier: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleGetResponse:
        """
        Get information for a specific routing rule already created.

        Args:
          zone_identifier: Identifier

          rule_identifier: Routing rule identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not rule_identifier:
            raise ValueError(f"Expected a non-empty value for `rule_identifier` but received {rule_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/email/routing/rules/{rule_identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RuleGetResponse], ResultWrapper[RuleGetResponse]),
        )


class RulesWithRawResponse:
    def __init__(self, rules: Rules) -> None:
        self._rules = rules

        self.update = to_raw_response_wrapper(
            rules.update,
        )
        self.delete = to_raw_response_wrapper(
            rules.delete,
        )
        self.email_routing_routing_rules_create_routing_rule = to_raw_response_wrapper(
            rules.email_routing_routing_rules_create_routing_rule,
        )
        self.email_routing_routing_rules_list_routing_rules = to_raw_response_wrapper(
            rules.email_routing_routing_rules_list_routing_rules,
        )
        self.get = to_raw_response_wrapper(
            rules.get,
        )

    @cached_property
    def catch_alls(self) -> CatchAllsWithRawResponse:
        return CatchAllsWithRawResponse(self._rules.catch_alls)


class AsyncRulesWithRawResponse:
    def __init__(self, rules: AsyncRules) -> None:
        self._rules = rules

        self.update = async_to_raw_response_wrapper(
            rules.update,
        )
        self.delete = async_to_raw_response_wrapper(
            rules.delete,
        )
        self.email_routing_routing_rules_create_routing_rule = async_to_raw_response_wrapper(
            rules.email_routing_routing_rules_create_routing_rule,
        )
        self.email_routing_routing_rules_list_routing_rules = async_to_raw_response_wrapper(
            rules.email_routing_routing_rules_list_routing_rules,
        )
        self.get = async_to_raw_response_wrapper(
            rules.get,
        )

    @cached_property
    def catch_alls(self) -> AsyncCatchAllsWithRawResponse:
        return AsyncCatchAllsWithRawResponse(self._rules.catch_alls)


class RulesWithStreamingResponse:
    def __init__(self, rules: Rules) -> None:
        self._rules = rules

        self.update = to_streamed_response_wrapper(
            rules.update,
        )
        self.delete = to_streamed_response_wrapper(
            rules.delete,
        )
        self.email_routing_routing_rules_create_routing_rule = to_streamed_response_wrapper(
            rules.email_routing_routing_rules_create_routing_rule,
        )
        self.email_routing_routing_rules_list_routing_rules = to_streamed_response_wrapper(
            rules.email_routing_routing_rules_list_routing_rules,
        )
        self.get = to_streamed_response_wrapper(
            rules.get,
        )

    @cached_property
    def catch_alls(self) -> CatchAllsWithStreamingResponse:
        return CatchAllsWithStreamingResponse(self._rules.catch_alls)


class AsyncRulesWithStreamingResponse:
    def __init__(self, rules: AsyncRules) -> None:
        self._rules = rules

        self.update = async_to_streamed_response_wrapper(
            rules.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            rules.delete,
        )
        self.email_routing_routing_rules_create_routing_rule = async_to_streamed_response_wrapper(
            rules.email_routing_routing_rules_create_routing_rule,
        )
        self.email_routing_routing_rules_list_routing_rules = async_to_streamed_response_wrapper(
            rules.email_routing_routing_rules_list_routing_rules,
        )
        self.get = async_to_streamed_response_wrapper(
            rules.get,
        )

    @cached_property
    def catch_alls(self) -> AsyncCatchAllsWithStreamingResponse:
        return AsyncCatchAllsWithStreamingResponse(self._rules.catch_alls)
