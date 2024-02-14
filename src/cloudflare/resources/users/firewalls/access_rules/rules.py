# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.users.firewalls.access_rules import (
    RuleUpdateResponse,
    RuleDeleteResponse,
    RuleIPAccessRulesForAUserCreateAnIPAccessRuleResponse,
    RuleIPAccessRulesForAUserListIPAccessRulesResponse,
    rule_ip_access_rules_for_a_user_create_an_ip_access_rule_params,
    rule_ip_access_rules_for_a_user_list_ip_access_rules_params,
)

from typing import Type, Optional

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
from .....types.users.firewalls.access_rules import rule_update_params
from .....types.users.firewalls.access_rules import rule_ip_access_rules_for_a_user_create_an_ip_access_rule_params
from .....types.users.firewalls.access_rules import rule_ip_access_rules_for_a_user_list_ip_access_rules_params
from ....._wrappers import ResultWrapper
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
    def with_raw_response(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self)

    def update(
        self,
        identifier: str,
        *,
        mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"] | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleUpdateResponse]:
        """Updates an IP Access rule defined at the user level.

        You can only update the
        rule action (`mode` parameter) and notes.

        Args:
          identifier: The unique identifier of the IP Access rule.

          mode: The action to apply to a matched request.

          notes: An informative summary of the rule, typically used as a reminder or explanation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._patch(
            f"/user/firewall/access_rules/rules/{identifier}",
            body=maybe_transform(
                {
                    "mode": mode,
                    "notes": notes,
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
            cast_to=cast(Type[Optional[RuleUpdateResponse]], ResultWrapper[RuleUpdateResponse]),
        )

    def delete(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleDeleteResponse]:
        """
        Deletes an IP Access rule at the user level.

        Note: Deleting a user-level rule will affect all zones owned by the user.

        Args:
          identifier: The unique identifier of the IP Access rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._delete(
            f"/user/firewall/access_rules/rules/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleDeleteResponse]], ResultWrapper[RuleDeleteResponse]),
        )

    def ip_access_rules_for_a_user_create_an_ip_access_rule(
        self,
        *,
        configuration: rule_ip_access_rules_for_a_user_create_an_ip_access_rule_params.Configuration,
        mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"],
        notes: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleIPAccessRulesForAUserCreateAnIPAccessRuleResponse]:
        """
        Creates a new IP Access rule for all zones owned by the current user.

        Note: To create an IP Access rule that applies to a specific zone, refer to the
        [IP Access rules for a zone](#ip-access-rules-for-a-zone) endpoints.

        Args:
          configuration: The rule configuration.

          mode: The action to apply to a matched request.

          notes: An informative summary of the rule, typically used as a reminder or explanation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/user/firewall/access_rules/rules",
            body=maybe_transform(
                {
                    "configuration": configuration,
                    "mode": mode,
                    "notes": notes,
                },
                rule_ip_access_rules_for_a_user_create_an_ip_access_rule_params.RuleIPAccessRulesForAUserCreateAnIPAccessRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleIPAccessRulesForAUserCreateAnIPAccessRuleResponse]],
                ResultWrapper[RuleIPAccessRulesForAUserCreateAnIPAccessRuleResponse],
            ),
        )

    def ip_access_rules_for_a_user_list_ip_access_rules(
        self,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        egs_pagination: rule_ip_access_rules_for_a_user_list_ip_access_rules_params.EgsPagination
        | NotGiven = NOT_GIVEN,
        filters: rule_ip_access_rules_for_a_user_list_ip_access_rules_params.Filters | NotGiven = NOT_GIVEN,
        order: Literal["configuration.target", "configuration.value", "mode"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleIPAccessRulesForAUserListIPAccessRulesResponse]:
        """Fetches IP Access rules of the user.

        You can filter the results using several
        optional parameters.

        Args:
          direction: The direction used to sort returned rules.

          order: The field used to sort returned rules.

          page: Requested page within paginated list of results.

          per_page: Maximum number of results requested.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/user/firewall/access_rules/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "egs_pagination": egs_pagination,
                        "filters": filters,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    rule_ip_access_rules_for_a_user_list_ip_access_rules_params.RuleIPAccessRulesForAUserListIPAccessRulesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleIPAccessRulesForAUserListIPAccessRulesResponse]],
                ResultWrapper[RuleIPAccessRulesForAUserListIPAccessRulesResponse],
            ),
        )


class AsyncRules(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self)

    async def update(
        self,
        identifier: str,
        *,
        mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"] | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleUpdateResponse]:
        """Updates an IP Access rule defined at the user level.

        You can only update the
        rule action (`mode` parameter) and notes.

        Args:
          identifier: The unique identifier of the IP Access rule.

          mode: The action to apply to a matched request.

          notes: An informative summary of the rule, typically used as a reminder or explanation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._patch(
            f"/user/firewall/access_rules/rules/{identifier}",
            body=maybe_transform(
                {
                    "mode": mode,
                    "notes": notes,
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
            cast_to=cast(Type[Optional[RuleUpdateResponse]], ResultWrapper[RuleUpdateResponse]),
        )

    async def delete(
        self,
        identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleDeleteResponse]:
        """
        Deletes an IP Access rule at the user level.

        Note: Deleting a user-level rule will affect all zones owned by the user.

        Args:
          identifier: The unique identifier of the IP Access rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._delete(
            f"/user/firewall/access_rules/rules/{identifier}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleDeleteResponse]], ResultWrapper[RuleDeleteResponse]),
        )

    async def ip_access_rules_for_a_user_create_an_ip_access_rule(
        self,
        *,
        configuration: rule_ip_access_rules_for_a_user_create_an_ip_access_rule_params.Configuration,
        mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"],
        notes: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleIPAccessRulesForAUserCreateAnIPAccessRuleResponse]:
        """
        Creates a new IP Access rule for all zones owned by the current user.

        Note: To create an IP Access rule that applies to a specific zone, refer to the
        [IP Access rules for a zone](#ip-access-rules-for-a-zone) endpoints.

        Args:
          configuration: The rule configuration.

          mode: The action to apply to a matched request.

          notes: An informative summary of the rule, typically used as a reminder or explanation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/user/firewall/access_rules/rules",
            body=maybe_transform(
                {
                    "configuration": configuration,
                    "mode": mode,
                    "notes": notes,
                },
                rule_ip_access_rules_for_a_user_create_an_ip_access_rule_params.RuleIPAccessRulesForAUserCreateAnIPAccessRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleIPAccessRulesForAUserCreateAnIPAccessRuleResponse]],
                ResultWrapper[RuleIPAccessRulesForAUserCreateAnIPAccessRuleResponse],
            ),
        )

    async def ip_access_rules_for_a_user_list_ip_access_rules(
        self,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        egs_pagination: rule_ip_access_rules_for_a_user_list_ip_access_rules_params.EgsPagination
        | NotGiven = NOT_GIVEN,
        filters: rule_ip_access_rules_for_a_user_list_ip_access_rules_params.Filters | NotGiven = NOT_GIVEN,
        order: Literal["configuration.target", "configuration.value", "mode"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleIPAccessRulesForAUserListIPAccessRulesResponse]:
        """Fetches IP Access rules of the user.

        You can filter the results using several
        optional parameters.

        Args:
          direction: The direction used to sort returned rules.

          order: The field used to sort returned rules.

          page: Requested page within paginated list of results.

          per_page: Maximum number of results requested.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/user/firewall/access_rules/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "egs_pagination": egs_pagination,
                        "filters": filters,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    rule_ip_access_rules_for_a_user_list_ip_access_rules_params.RuleIPAccessRulesForAUserListIPAccessRulesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleIPAccessRulesForAUserListIPAccessRulesResponse]],
                ResultWrapper[RuleIPAccessRulesForAUserListIPAccessRulesResponse],
            ),
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
        self.ip_access_rules_for_a_user_create_an_ip_access_rule = to_raw_response_wrapper(
            rules.ip_access_rules_for_a_user_create_an_ip_access_rule,
        )
        self.ip_access_rules_for_a_user_list_ip_access_rules = to_raw_response_wrapper(
            rules.ip_access_rules_for_a_user_list_ip_access_rules,
        )


class AsyncRulesWithRawResponse:
    def __init__(self, rules: AsyncRules) -> None:
        self._rules = rules

        self.update = async_to_raw_response_wrapper(
            rules.update,
        )
        self.delete = async_to_raw_response_wrapper(
            rules.delete,
        )
        self.ip_access_rules_for_a_user_create_an_ip_access_rule = async_to_raw_response_wrapper(
            rules.ip_access_rules_for_a_user_create_an_ip_access_rule,
        )
        self.ip_access_rules_for_a_user_list_ip_access_rules = async_to_raw_response_wrapper(
            rules.ip_access_rules_for_a_user_list_ip_access_rules,
        )


class RulesWithStreamingResponse:
    def __init__(self, rules: Rules) -> None:
        self._rules = rules

        self.update = to_streamed_response_wrapper(
            rules.update,
        )
        self.delete = to_streamed_response_wrapper(
            rules.delete,
        )
        self.ip_access_rules_for_a_user_create_an_ip_access_rule = to_streamed_response_wrapper(
            rules.ip_access_rules_for_a_user_create_an_ip_access_rule,
        )
        self.ip_access_rules_for_a_user_list_ip_access_rules = to_streamed_response_wrapper(
            rules.ip_access_rules_for_a_user_list_ip_access_rules,
        )


class AsyncRulesWithStreamingResponse:
    def __init__(self, rules: AsyncRules) -> None:
        self._rules = rules

        self.update = async_to_streamed_response_wrapper(
            rules.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            rules.delete,
        )
        self.ip_access_rules_for_a_user_create_an_ip_access_rule = async_to_streamed_response_wrapper(
            rules.ip_access_rules_for_a_user_create_an_ip_access_rule,
        )
        self.ip_access_rules_for_a_user_list_ip_access_rules = async_to_streamed_response_wrapper(
            rules.ip_access_rules_for_a_user_list_ip_access_rules,
        )
