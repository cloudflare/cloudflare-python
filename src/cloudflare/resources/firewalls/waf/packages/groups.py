# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.firewalls.waf.packages import (
    GroupUpdateResponse,
    GroupGetResponse,
    GroupWAFRuleGroupsListWAFRuleGroupsResponse,
)

from typing_extensions import Literal

from typing import Type, Optional

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
from .....types.firewalls.waf.packages import group_update_params
from .....types.firewalls.waf.packages import group_waf_rule_groups_list_waf_rule_groups_params
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

__all__ = ["Groups", "AsyncGroups"]


class Groups(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GroupsWithRawResponse:
        return GroupsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GroupsWithStreamingResponse:
        return GroupsWithStreamingResponse(self)

    def update(
        self,
        group_id: str,
        *,
        zone_id: str,
        package_id: str,
        mode: Literal["on", "off"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupUpdateResponse:
        """Updates a WAF rule group.

        You can update the state (`mode` parameter) of a rule
        group.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_id: Identifier

          package_id: The unique identifier of a WAF package.

          group_id: The unique identifier of a WAF package.

          mode: The state of the rules contained in the rule group. When `on`, the rules in the
              group are configurable/usable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not package_id:
            raise ValueError(f"Expected a non-empty value for `package_id` but received {package_id!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return cast(
            GroupUpdateResponse,
            self._patch(
                f"/zones/{zone_id}/firewall/waf/packages/{package_id}/groups/{group_id}",
                body=maybe_transform({"mode": mode}, group_update_params.GroupUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[GroupUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        group_id: str,
        *,
        zone_id: str,
        package_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupGetResponse:
        """
        Fetches the details of a WAF rule group.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_id: Identifier

          package_id: The unique identifier of a WAF package.

          group_id: The unique identifier of a WAF package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not package_id:
            raise ValueError(f"Expected a non-empty value for `package_id` but received {package_id!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return cast(
            GroupGetResponse,
            self._get(
                f"/zones/{zone_id}/firewall/waf/packages/{package_id}/groups/{group_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[GroupGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def waf_rule_groups_list_waf_rule_groups(
        self,
        package_id: str,
        *,
        zone_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        mode: Literal["on", "off"] | NotGiven = NOT_GIVEN,
        order: Literal["mode", "rules_count"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GroupWAFRuleGroupsListWAFRuleGroupsResponse]:
        """
        Fetches the WAF rule groups in a WAF package.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_id: Identifier

          package_id: The unique identifier of a WAF package.

          direction: The direction used to sort returned rule groups.

          match: When set to `all`, all the search requirements must match. When set to `any`,
              only one of the search requirements has to match.

          mode: The state of the rules contained in the rule group. When `on`, the rules in the
              group are configurable/usable.

          order: The field used to sort returned rule groups.

          page: The page number of paginated results.

          per_page: The number of rule groups per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not package_id:
            raise ValueError(f"Expected a non-empty value for `package_id` but received {package_id!r}")
        return self._get(
            f"/zones/{zone_id}/firewall/waf/packages/{package_id}/groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "match": match,
                        "mode": mode,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    group_waf_rule_groups_list_waf_rule_groups_params.GroupWAFRuleGroupsListWAFRuleGroupsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[GroupWAFRuleGroupsListWAFRuleGroupsResponse]],
                ResultWrapper[GroupWAFRuleGroupsListWAFRuleGroupsResponse],
            ),
        )


class AsyncGroups(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGroupsWithRawResponse:
        return AsyncGroupsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGroupsWithStreamingResponse:
        return AsyncGroupsWithStreamingResponse(self)

    async def update(
        self,
        group_id: str,
        *,
        zone_id: str,
        package_id: str,
        mode: Literal["on", "off"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupUpdateResponse:
        """Updates a WAF rule group.

        You can update the state (`mode` parameter) of a rule
        group.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_id: Identifier

          package_id: The unique identifier of a WAF package.

          group_id: The unique identifier of a WAF package.

          mode: The state of the rules contained in the rule group. When `on`, the rules in the
              group are configurable/usable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not package_id:
            raise ValueError(f"Expected a non-empty value for `package_id` but received {package_id!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return cast(
            GroupUpdateResponse,
            await self._patch(
                f"/zones/{zone_id}/firewall/waf/packages/{package_id}/groups/{group_id}",
                body=maybe_transform({"mode": mode}, group_update_params.GroupUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[GroupUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        group_id: str,
        *,
        zone_id: str,
        package_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupGetResponse:
        """
        Fetches the details of a WAF rule group.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_id: Identifier

          package_id: The unique identifier of a WAF package.

          group_id: The unique identifier of a WAF package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not package_id:
            raise ValueError(f"Expected a non-empty value for `package_id` but received {package_id!r}")
        if not group_id:
            raise ValueError(f"Expected a non-empty value for `group_id` but received {group_id!r}")
        return cast(
            GroupGetResponse,
            await self._get(
                f"/zones/{zone_id}/firewall/waf/packages/{package_id}/groups/{group_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[GroupGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def waf_rule_groups_list_waf_rule_groups(
        self,
        package_id: str,
        *,
        zone_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        mode: Literal["on", "off"] | NotGiven = NOT_GIVEN,
        order: Literal["mode", "rules_count"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[GroupWAFRuleGroupsListWAFRuleGroupsResponse]:
        """
        Fetches the WAF rule groups in a WAF package.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_id: Identifier

          package_id: The unique identifier of a WAF package.

          direction: The direction used to sort returned rule groups.

          match: When set to `all`, all the search requirements must match. When set to `any`,
              only one of the search requirements has to match.

          mode: The state of the rules contained in the rule group. When `on`, the rules in the
              group are configurable/usable.

          order: The field used to sort returned rule groups.

          page: The page number of paginated results.

          per_page: The number of rule groups per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not package_id:
            raise ValueError(f"Expected a non-empty value for `package_id` but received {package_id!r}")
        return await self._get(
            f"/zones/{zone_id}/firewall/waf/packages/{package_id}/groups",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "match": match,
                        "mode": mode,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    group_waf_rule_groups_list_waf_rule_groups_params.GroupWAFRuleGroupsListWAFRuleGroupsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[GroupWAFRuleGroupsListWAFRuleGroupsResponse]],
                ResultWrapper[GroupWAFRuleGroupsListWAFRuleGroupsResponse],
            ),
        )


class GroupsWithRawResponse:
    def __init__(self, groups: Groups) -> None:
        self._groups = groups

        self.update = to_raw_response_wrapper(
            groups.update,
        )
        self.get = to_raw_response_wrapper(
            groups.get,
        )
        self.waf_rule_groups_list_waf_rule_groups = to_raw_response_wrapper(
            groups.waf_rule_groups_list_waf_rule_groups,
        )


class AsyncGroupsWithRawResponse:
    def __init__(self, groups: AsyncGroups) -> None:
        self._groups = groups

        self.update = async_to_raw_response_wrapper(
            groups.update,
        )
        self.get = async_to_raw_response_wrapper(
            groups.get,
        )
        self.waf_rule_groups_list_waf_rule_groups = async_to_raw_response_wrapper(
            groups.waf_rule_groups_list_waf_rule_groups,
        )


class GroupsWithStreamingResponse:
    def __init__(self, groups: Groups) -> None:
        self._groups = groups

        self.update = to_streamed_response_wrapper(
            groups.update,
        )
        self.get = to_streamed_response_wrapper(
            groups.get,
        )
        self.waf_rule_groups_list_waf_rule_groups = to_streamed_response_wrapper(
            groups.waf_rule_groups_list_waf_rule_groups,
        )


class AsyncGroupsWithStreamingResponse:
    def __init__(self, groups: AsyncGroups) -> None:
        self._groups = groups

        self.update = async_to_streamed_response_wrapper(
            groups.update,
        )
        self.get = async_to_streamed_response_wrapper(
            groups.get,
        )
        self.waf_rule_groups_list_waf_rule_groups = async_to_streamed_response_wrapper(
            groups.waf_rule_groups_list_waf_rule_groups,
        )
