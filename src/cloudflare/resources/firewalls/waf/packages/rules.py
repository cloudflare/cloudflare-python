# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.firewalls.waf.packages import RuleUpdateResponse, RuleGetResponse, RuleWAFRulesListWAFRulesResponse

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
from .....types.firewalls.waf.packages import rule_update_params
from .....types.firewalls.waf.packages import rule_waf_rules_list_waf_rules_params
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
    def with_raw_response(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self)

    def update(
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
    ) -> RuleUpdateResponse:
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
            RuleUpdateResponse,
            self._patch(
                f"/zones/{zone_id}/firewall/waf/packages/{package_id}/rules/{rule_id}",
                body=maybe_transform({"mode": mode}, rule_update_params.RuleUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RuleUpdateResponse]
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
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RuleGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def waf_rules_list_waf_rules(
        self,
        package_id: str,
        *,
        zone_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        mode: Literal["DIS", "CHL", "BLK", "SIM"] | NotGiven = NOT_GIVEN,
        order: Literal["priority", "group_id", "description"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleWAFRulesListWAFRulesResponse]:
        """
        Fetches WAF rules in a WAF package.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_id: Identifier

          package_id: The unique identifier of a WAF package.

          direction: The direction used to sort returned rules.

          match: When set to `all`, all the search requirements must match. When set to `any`,
              only one of the search requirements has to match.

          mode: The action/mode a rule has been overridden to perform.

          order: The field used to sort returned rules.

          page: The page number of paginated results.

          per_page: The number of rules per page.

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
            f"/zones/{zone_id}/firewall/waf/packages/{package_id}/rules",
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
                    rule_waf_rules_list_waf_rules_params.RuleWAFRulesListWAFRulesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleWAFRulesListWAFRulesResponse]], ResultWrapper[RuleWAFRulesListWAFRulesResponse]
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
    ) -> RuleUpdateResponse:
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
            RuleUpdateResponse,
            await self._patch(
                f"/zones/{zone_id}/firewall/waf/packages/{package_id}/rules/{rule_id}",
                body=maybe_transform({"mode": mode}, rule_update_params.RuleUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RuleUpdateResponse]
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
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[RuleGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def waf_rules_list_waf_rules(
        self,
        package_id: str,
        *,
        zone_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        mode: Literal["DIS", "CHL", "BLK", "SIM"] | NotGiven = NOT_GIVEN,
        order: Literal["priority", "group_id", "description"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleWAFRulesListWAFRulesResponse]:
        """
        Fetches WAF rules in a WAF package.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_id: Identifier

          package_id: The unique identifier of a WAF package.

          direction: The direction used to sort returned rules.

          match: When set to `all`, all the search requirements must match. When set to `any`,
              only one of the search requirements has to match.

          mode: The action/mode a rule has been overridden to perform.

          order: The field used to sort returned rules.

          page: The page number of paginated results.

          per_page: The number of rules per page.

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
            f"/zones/{zone_id}/firewall/waf/packages/{package_id}/rules",
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
                    rule_waf_rules_list_waf_rules_params.RuleWAFRulesListWAFRulesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleWAFRulesListWAFRulesResponse]], ResultWrapper[RuleWAFRulesListWAFRulesResponse]
            ),
        )


class RulesWithRawResponse:
    def __init__(self, rules: Rules) -> None:
        self._rules = rules

        self.update = to_raw_response_wrapper(
            rules.update,
        )
        self.get = to_raw_response_wrapper(
            rules.get,
        )
        self.waf_rules_list_waf_rules = to_raw_response_wrapper(
            rules.waf_rules_list_waf_rules,
        )


class AsyncRulesWithRawResponse:
    def __init__(self, rules: AsyncRules) -> None:
        self._rules = rules

        self.update = async_to_raw_response_wrapper(
            rules.update,
        )
        self.get = async_to_raw_response_wrapper(
            rules.get,
        )
        self.waf_rules_list_waf_rules = async_to_raw_response_wrapper(
            rules.waf_rules_list_waf_rules,
        )


class RulesWithStreamingResponse:
    def __init__(self, rules: Rules) -> None:
        self._rules = rules

        self.update = to_streamed_response_wrapper(
            rules.update,
        )
        self.get = to_streamed_response_wrapper(
            rules.get,
        )
        self.waf_rules_list_waf_rules = to_streamed_response_wrapper(
            rules.waf_rules_list_waf_rules,
        )


class AsyncRulesWithStreamingResponse:
    def __init__(self, rules: AsyncRules) -> None:
        self._rules = rules

        self.update = async_to_streamed_response_wrapper(
            rules.update,
        )
        self.get = async_to_streamed_response_wrapper(
            rules.get,
        )
        self.waf_rules_list_waf_rules = async_to_streamed_response_wrapper(
            rules.waf_rules_list_waf_rules,
        )
