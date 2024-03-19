# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ....._base_client import (
    AsyncPaginator,
    make_request_options,
)
from .....types.firewall.waf.packages import (
    GroupGetResponse,
    GroupEditResponse,
    WAFManagedRulesSchemasGroup,
    group_edit_params,
    group_list_params,
)

__all__ = ["Groups", "AsyncGroups"]


class Groups(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GroupsWithRawResponse:
        return GroupsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GroupsWithStreamingResponse:
        return GroupsWithStreamingResponse(self)

    def list(
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
    ) -> SyncV4PagePaginationArray[WAFManagedRulesSchemasGroup]:
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
        return self._get_api_list(
            f"/zones/{zone_id}/firewall/waf/packages/{package_id}/groups",
            page=SyncV4PagePaginationArray[WAFManagedRulesSchemasGroup],
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
                    group_list_params.GroupListParams,
                ),
            ),
            model=WAFManagedRulesSchemasGroup,
        )

    def edit(
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
    ) -> GroupEditResponse:
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
            GroupEditResponse,
            self._patch(
                f"/zones/{zone_id}/firewall/waf/packages/{package_id}/groups/{group_id}",
                body=maybe_transform({"mode": mode}, group_edit_params.GroupEditParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[GroupEditResponse]
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


class AsyncGroups(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGroupsWithRawResponse:
        return AsyncGroupsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGroupsWithStreamingResponse:
        return AsyncGroupsWithStreamingResponse(self)

    def list(
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
    ) -> AsyncPaginator[WAFManagedRulesSchemasGroup, AsyncV4PagePaginationArray[WAFManagedRulesSchemasGroup]]:
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
        return self._get_api_list(
            f"/zones/{zone_id}/firewall/waf/packages/{package_id}/groups",
            page=AsyncV4PagePaginationArray[WAFManagedRulesSchemasGroup],
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
                    group_list_params.GroupListParams,
                ),
            ),
            model=WAFManagedRulesSchemasGroup,
        )

    async def edit(
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
    ) -> GroupEditResponse:
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
            GroupEditResponse,
            await self._patch(
                f"/zones/{zone_id}/firewall/waf/packages/{package_id}/groups/{group_id}",
                body=await async_maybe_transform({"mode": mode}, group_edit_params.GroupEditParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[GroupEditResponse]
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


class GroupsWithRawResponse:
    def __init__(self, groups: Groups) -> None:
        self._groups = groups

        self.list = to_raw_response_wrapper(
            groups.list,
        )
        self.edit = to_raw_response_wrapper(
            groups.edit,
        )
        self.get = to_raw_response_wrapper(
            groups.get,
        )


class AsyncGroupsWithRawResponse:
    def __init__(self, groups: AsyncGroups) -> None:
        self._groups = groups

        self.list = async_to_raw_response_wrapper(
            groups.list,
        )
        self.edit = async_to_raw_response_wrapper(
            groups.edit,
        )
        self.get = async_to_raw_response_wrapper(
            groups.get,
        )


class GroupsWithStreamingResponse:
    def __init__(self, groups: Groups) -> None:
        self._groups = groups

        self.list = to_streamed_response_wrapper(
            groups.list,
        )
        self.edit = to_streamed_response_wrapper(
            groups.edit,
        )
        self.get = to_streamed_response_wrapper(
            groups.get,
        )


class AsyncGroupsWithStreamingResponse:
    def __init__(self, groups: AsyncGroups) -> None:
        self._groups = groups

        self.list = async_to_streamed_response_wrapper(
            groups.list,
        )
        self.edit = async_to_streamed_response_wrapper(
            groups.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            groups.get,
        )
