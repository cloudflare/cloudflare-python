# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.firewall import access_rule_list_params, access_rule_create_params
from ...types.firewall.access_rule_create_response import AccessRuleCreateResponse

__all__ = ["AccessRulesResource", "AsyncAccessRulesResource"]


class AccessRulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccessRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AccessRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AccessRulesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        configuration: access_rule_create_params.Configuration,
        mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"],
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessRuleCreateResponse:
        """Creates a new IP Access rule for an account or zone.

        The rule will apply to all
        zones in the account or zone.

        Note: To create an IP Access rule that applies to a single zone, refer to the
        [IP Access rules for a zone](#ip-access-rules-for-a-zone) endpoints.

        Args:
          configuration: The rule configuration.

          mode: The action to apply to a matched request.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          notes: An informative summary of the rule, typically used as a reminder or explanation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return cast(
            AccessRuleCreateResponse,
            self._post(
                f"/{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules",
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
                    post_parser=ResultWrapper[AccessRuleCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AccessRuleCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        configuration: access_rule_list_params.Configuration | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"] | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        order: Literal["configuration.target", "configuration.value", "mode"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[object]:
        """Fetches IP Access rules of an account or zone.

        These rules apply to all the
        zones in the account or zone. You can filter the results using several optional
        parameters.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          direction: The direction used to sort returned rules.

          match: When set to `all`, all the search requirements must match. When set to `any`,
              only one of the search requirements has to match.

          mode: The action to apply to a matched request.

          notes: The string to search for in the notes of existing IP Access rules. Notes: For
              example, the string 'attack' would match IP Access rules with notes 'Attack
              26/02' and 'Attack 27/02'. The search is case insensitive.

          order: The field used to sort returned rules.

          page: Requested page within paginated list of results.

          per_page: Maximum number of results requested.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get_api_list(
            f"/{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules",
            page=SyncV4PagePaginationArray[object],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "configuration": configuration,
                        "direction": direction,
                        "match": match,
                        "mode": mode,
                        "notes": notes,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    access_rule_list_params.AccessRuleListParams,
                ),
            ),
            model=object,
        )


class AsyncAccessRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccessRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccessRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAccessRulesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        configuration: access_rule_create_params.Configuration,
        mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"],
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccessRuleCreateResponse:
        """Creates a new IP Access rule for an account or zone.

        The rule will apply to all
        zones in the account or zone.

        Note: To create an IP Access rule that applies to a single zone, refer to the
        [IP Access rules for a zone](#ip-access-rules-for-a-zone) endpoints.

        Args:
          configuration: The rule configuration.

          mode: The action to apply to a matched request.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          notes: An informative summary of the rule, typically used as a reminder or explanation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return cast(
            AccessRuleCreateResponse,
            await self._post(
                f"/{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules",
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
                    post_parser=ResultWrapper[AccessRuleCreateResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AccessRuleCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        configuration: access_rule_list_params.Configuration | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"] | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        order: Literal["configuration.target", "configuration.value", "mode"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[object, AsyncV4PagePaginationArray[object]]:
        """Fetches IP Access rules of an account or zone.

        These rules apply to all the
        zones in the account or zone. You can filter the results using several optional
        parameters.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          direction: The direction used to sort returned rules.

          match: When set to `all`, all the search requirements must match. When set to `any`,
              only one of the search requirements has to match.

          mode: The action to apply to a matched request.

          notes: The string to search for in the notes of existing IP Access rules. Notes: For
              example, the string 'attack' would match IP Access rules with notes 'Attack
              26/02' and 'Attack 27/02'. The search is case insensitive.

          order: The field used to sort returned rules.

          page: Requested page within paginated list of results.

          per_page: Maximum number of results requested.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get_api_list(
            f"/{account_or_zone}/{account_or_zone_id}/firewall/access_rules/rules",
            page=AsyncV4PagePaginationArray[object],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "configuration": configuration,
                        "direction": direction,
                        "match": match,
                        "mode": mode,
                        "notes": notes,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    access_rule_list_params.AccessRuleListParams,
                ),
            ),
            model=object,
        )


class AccessRulesResourceWithRawResponse:
    def __init__(self, access_rules: AccessRulesResource) -> None:
        self._access_rules = access_rules

        self.create = to_raw_response_wrapper(
            access_rules.create,
        )
        self.list = to_raw_response_wrapper(
            access_rules.list,
        )


class AsyncAccessRulesResourceWithRawResponse:
    def __init__(self, access_rules: AsyncAccessRulesResource) -> None:
        self._access_rules = access_rules

        self.create = async_to_raw_response_wrapper(
            access_rules.create,
        )
        self.list = async_to_raw_response_wrapper(
            access_rules.list,
        )


class AccessRulesResourceWithStreamingResponse:
    def __init__(self, access_rules: AccessRulesResource) -> None:
        self._access_rules = access_rules

        self.create = to_streamed_response_wrapper(
            access_rules.create,
        )
        self.list = to_streamed_response_wrapper(
            access_rules.list,
        )


class AsyncAccessRulesResourceWithStreamingResponse:
    def __init__(self, access_rules: AsyncAccessRulesResource) -> None:
        self._access_rules = access_rules

        self.create = async_to_streamed_response_wrapper(
            access_rules.create,
        )
        self.list = async_to_streamed_response_wrapper(
            access_rules.list,
        )
