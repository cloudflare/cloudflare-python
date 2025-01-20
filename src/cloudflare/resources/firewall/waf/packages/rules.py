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
from ....._base_client import AsyncPaginator, make_request_options
from .....types.firewall.waf.packages import rule_edit_params, rule_list_params
from .....types.firewall.waf.packages.rule_get_response import RuleGetResponse
from .....types.firewall.waf.packages.rule_edit_response import RuleEditResponse
from .....types.firewall.waf.packages.rule_list_response import RuleListResponse

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

    def list(
        self,
        package_id: str,
        *,
        zone_id: str,
        description: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        group_id: str | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        mode: Literal["DIS", "CHL", "BLK", "SIM"] | NotGiven = NOT_GIVEN,
        order: Literal["priority", "group_id", "description"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        priority: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[RuleListResponse]:
        """
        Fetches WAF rules in a WAF package.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_id: Identifier

          package_id: The unique identifier of a WAF package.

          description: The public description of the WAF rule.

          direction: The direction used to sort returned rules.

          group_id: The unique identifier of the rule group.

          match: When set to `all`, all the search requirements must match. When set to `any`,
              only one of the search requirements has to match.

          mode: The action/mode a rule has been overridden to perform.

          order: The field used to sort returned rules.

          page: The page number of paginated results.

          per_page: The number of rules per page.

          priority: The order in which the individual WAF rule is executed within its rule group.

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
            f"/zones/{zone_id}/firewall/waf/packages/{package_id}/rules",
            page=SyncV4PagePaginationArray[RuleListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "description": description,
                        "direction": direction,
                        "group_id": group_id,
                        "match": match,
                        "mode": mode,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "priority": priority,
                    },
                    rule_list_params.RuleListParams,
                ),
            ),
            model=cast(Any, RuleListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    def edit(
        self,
        rule_id: str,
        *,
        zone_id: str,
        package_id: str,
        mode: Literal["default", "disable", "simulate", "block", "challenge", "on", "off"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleEditResponse:
        """Updates a WAF rule.

        You can only update the mode/action of the rule.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_id: Identifier

          package_id: The unique identifier of a WAF package.

          rule_id: The unique identifier of a WAF package.

          mode: The mode/action of the rule when triggered. You must use a value from the
              `allowed_modes` array of the current rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not package_id:
            raise ValueError(f"Expected a non-empty value for `package_id` but received {package_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return cast(
            RuleEditResponse,
            self._patch(
                f"/zones/{zone_id}/firewall/waf/packages/{package_id}/rules/{rule_id}",
                body=maybe_transform({"mode": mode}, rule_edit_params.RuleEditParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[RuleEditResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RuleEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        rule_id: str,
        *,
        zone_id: str,
        package_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleGetResponse:
        """
        Fetches the details of a WAF rule in a WAF package.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_id: Identifier

          package_id: The unique identifier of a WAF package.

          rule_id: The unique identifier of a WAF package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not package_id:
            raise ValueError(f"Expected a non-empty value for `package_id` but received {package_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return cast(
            RuleGetResponse,
            self._get(
                f"/zones/{zone_id}/firewall/waf/packages/{package_id}/rules/{rule_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[RuleGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RuleGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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

    def list(
        self,
        package_id: str,
        *,
        zone_id: str,
        description: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        group_id: str | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        mode: Literal["DIS", "CHL", "BLK", "SIM"] | NotGiven = NOT_GIVEN,
        order: Literal["priority", "group_id", "description"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        priority: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[RuleListResponse, AsyncV4PagePaginationArray[RuleListResponse]]:
        """
        Fetches WAF rules in a WAF package.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_id: Identifier

          package_id: The unique identifier of a WAF package.

          description: The public description of the WAF rule.

          direction: The direction used to sort returned rules.

          group_id: The unique identifier of the rule group.

          match: When set to `all`, all the search requirements must match. When set to `any`,
              only one of the search requirements has to match.

          mode: The action/mode a rule has been overridden to perform.

          order: The field used to sort returned rules.

          page: The page number of paginated results.

          per_page: The number of rules per page.

          priority: The order in which the individual WAF rule is executed within its rule group.

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
            f"/zones/{zone_id}/firewall/waf/packages/{package_id}/rules",
            page=AsyncV4PagePaginationArray[RuleListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "description": description,
                        "direction": direction,
                        "group_id": group_id,
                        "match": match,
                        "mode": mode,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "priority": priority,
                    },
                    rule_list_params.RuleListParams,
                ),
            ),
            model=cast(Any, RuleListResponse),  # Union types cannot be passed in as arguments in the type system
        )

    async def edit(
        self,
        rule_id: str,
        *,
        zone_id: str,
        package_id: str,
        mode: Literal["default", "disable", "simulate", "block", "challenge", "on", "off"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleEditResponse:
        """Updates a WAF rule.

        You can only update the mode/action of the rule.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_id: Identifier

          package_id: The unique identifier of a WAF package.

          rule_id: The unique identifier of a WAF package.

          mode: The mode/action of the rule when triggered. You must use a value from the
              `allowed_modes` array of the current rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not package_id:
            raise ValueError(f"Expected a non-empty value for `package_id` but received {package_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return cast(
            RuleEditResponse,
            await self._patch(
                f"/zones/{zone_id}/firewall/waf/packages/{package_id}/rules/{rule_id}",
                body=await async_maybe_transform({"mode": mode}, rule_edit_params.RuleEditParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[RuleEditResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RuleEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        rule_id: str,
        *,
        zone_id: str,
        package_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleGetResponse:
        """
        Fetches the details of a WAF rule in a WAF package.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_id: Identifier

          package_id: The unique identifier of a WAF package.

          rule_id: The unique identifier of a WAF package.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not package_id:
            raise ValueError(f"Expected a non-empty value for `package_id` but received {package_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return cast(
            RuleGetResponse,
            await self._get(
                f"/zones/{zone_id}/firewall/waf/packages/{package_id}/rules/{rule_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[RuleGetResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RuleGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class RulesResourceWithRawResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.list = to_raw_response_wrapper(
            rules.list,
        )
        self.edit = to_raw_response_wrapper(
            rules.edit,
        )
        self.get = to_raw_response_wrapper(
            rules.get,
        )


class AsyncRulesResourceWithRawResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.list = async_to_raw_response_wrapper(
            rules.list,
        )
        self.edit = async_to_raw_response_wrapper(
            rules.edit,
        )
        self.get = async_to_raw_response_wrapper(
            rules.get,
        )


class RulesResourceWithStreamingResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.list = to_streamed_response_wrapper(
            rules.list,
        )
        self.edit = to_streamed_response_wrapper(
            rules.edit,
        )
        self.get = to_streamed_response_wrapper(
            rules.get,
        )


class AsyncRulesResourceWithStreamingResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.list = async_to_streamed_response_wrapper(
            rules.list,
        )
        self.edit = async_to_streamed_response_wrapper(
            rules.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            rules.get,
        )
