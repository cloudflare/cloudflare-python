# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
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
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ....types.user.firewall import (
    LegacyJhsRule,
    AccessRuleDeleteResponse,
    access_rule_edit_params,
    access_rule_list_params,
    access_rule_create_params,
)

__all__ = ["AccessRules", "AsyncAccessRules"]


class AccessRules(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccessRulesWithRawResponse:
        return AccessRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessRulesWithStreamingResponse:
        return AccessRulesWithStreamingResponse(self)

    def create(
        self,
        *,
        configuration: access_rule_create_params.Configuration,
        mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"],
        notes: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LegacyJhsRule]:
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
                access_rule_create_params.AccessRuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[LegacyJhsRule]], ResultWrapper[LegacyJhsRule]),
        )

    def list(
        self,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        egs_pagination: access_rule_list_params.EgsPagination | NotGiven = NOT_GIVEN,
        filters: access_rule_list_params.Filters | NotGiven = NOT_GIVEN,
        order: Literal["configuration.target", "configuration.value", "mode"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[LegacyJhsRule]:
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
        return self._get_api_list(
            "/user/firewall/access_rules/rules",
            page=SyncV4PagePaginationArray[LegacyJhsRule],
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
                    access_rule_list_params.AccessRuleListParams,
                ),
            ),
            model=LegacyJhsRule,
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
    ) -> Optional[AccessRuleDeleteResponse]:
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
            cast_to=cast(Type[Optional[AccessRuleDeleteResponse]], ResultWrapper[AccessRuleDeleteResponse]),
        )

    def edit(
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
    ) -> Optional[LegacyJhsRule]:
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
                access_rule_edit_params.AccessRuleEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[LegacyJhsRule]], ResultWrapper[LegacyJhsRule]),
        )


class AsyncAccessRules(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccessRulesWithRawResponse:
        return AsyncAccessRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessRulesWithStreamingResponse:
        return AsyncAccessRulesWithStreamingResponse(self)

    async def create(
        self,
        *,
        configuration: access_rule_create_params.Configuration,
        mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"],
        notes: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LegacyJhsRule]:
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
            body=await async_maybe_transform(
                {
                    "configuration": configuration,
                    "mode": mode,
                    "notes": notes,
                },
                access_rule_create_params.AccessRuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[LegacyJhsRule]], ResultWrapper[LegacyJhsRule]),
        )

    def list(
        self,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        egs_pagination: access_rule_list_params.EgsPagination | NotGiven = NOT_GIVEN,
        filters: access_rule_list_params.Filters | NotGiven = NOT_GIVEN,
        order: Literal["configuration.target", "configuration.value", "mode"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[LegacyJhsRule, AsyncV4PagePaginationArray[LegacyJhsRule]]:
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
        return self._get_api_list(
            "/user/firewall/access_rules/rules",
            page=AsyncV4PagePaginationArray[LegacyJhsRule],
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
                    access_rule_list_params.AccessRuleListParams,
                ),
            ),
            model=LegacyJhsRule,
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
    ) -> Optional[AccessRuleDeleteResponse]:
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
            cast_to=cast(Type[Optional[AccessRuleDeleteResponse]], ResultWrapper[AccessRuleDeleteResponse]),
        )

    async def edit(
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
    ) -> Optional[LegacyJhsRule]:
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
            body=await async_maybe_transform(
                {
                    "mode": mode,
                    "notes": notes,
                },
                access_rule_edit_params.AccessRuleEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[LegacyJhsRule]], ResultWrapper[LegacyJhsRule]),
        )


class AccessRulesWithRawResponse:
    def __init__(self, access_rules: AccessRules) -> None:
        self._access_rules = access_rules

        self.create = to_raw_response_wrapper(
            access_rules.create,
        )
        self.list = to_raw_response_wrapper(
            access_rules.list,
        )
        self.delete = to_raw_response_wrapper(
            access_rules.delete,
        )
        self.edit = to_raw_response_wrapper(
            access_rules.edit,
        )


class AsyncAccessRulesWithRawResponse:
    def __init__(self, access_rules: AsyncAccessRules) -> None:
        self._access_rules = access_rules

        self.create = async_to_raw_response_wrapper(
            access_rules.create,
        )
        self.list = async_to_raw_response_wrapper(
            access_rules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            access_rules.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            access_rules.edit,
        )


class AccessRulesWithStreamingResponse:
    def __init__(self, access_rules: AccessRules) -> None:
        self._access_rules = access_rules

        self.create = to_streamed_response_wrapper(
            access_rules.create,
        )
        self.list = to_streamed_response_wrapper(
            access_rules.list,
        )
        self.delete = to_streamed_response_wrapper(
            access_rules.delete,
        )
        self.edit = to_streamed_response_wrapper(
            access_rules.edit,
        )


class AsyncAccessRulesWithStreamingResponse:
    def __init__(self, access_rules: AsyncAccessRules) -> None:
        self._access_rules = access_rules

        self.create = async_to_streamed_response_wrapper(
            access_rules.create,
        )
        self.list = async_to_streamed_response_wrapper(
            access_rules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            access_rules.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            access_rules.edit,
        )
