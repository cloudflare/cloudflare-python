# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.firewalls import (
    RuleGetResponse,
    RuleDeleteResponse,
    RuleUpdateResponse,
    RuleFirewallRulesListFirewallRulesResponse,
    RuleFirewallRulesCreateFirewallRulesResponse,
    RuleFirewallRulesUpdateFirewallRulesResponse,
    RuleFirewallRulesUpdatePriorityOfFirewallRulesResponse,
    rule_delete_params,
    rule_update_params,
    rule_firewall_rules_list_firewall_rules_params,
    rule_firewall_rules_create_firewall_rules_params,
    rule_firewall_rules_update_firewall_rules_params,
    rule_firewall_rules_update_priority_of_firewall_rules_params,
)

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
        id: str,
        *,
        zone_identifier: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleUpdateResponse]:
        """
        Updates an existing firewall rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the firewall rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/zones/{zone_identifier}/firewall/rules/{id}",
            body=maybe_transform(body, rule_update_params.RuleUpdateParams),
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
        id: str,
        *,
        zone_identifier: str,
        delete_filter_if_unused: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleDeleteResponse]:
        """
        Deletes an existing firewall rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the firewall rule.

          delete_filter_if_unused: When true, indicates that Cloudflare should also delete the associated filter if
              there are no other firewall rules referencing the filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/zones/{zone_identifier}/firewall/rules/{id}",
            body=maybe_transform(
                {"delete_filter_if_unused": delete_filter_if_unused}, rule_delete_params.RuleDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleDeleteResponse]], ResultWrapper[RuleDeleteResponse]),
        )

    def firewall_rules_create_firewall_rules(
        self,
        zone_identifier: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleFirewallRulesCreateFirewallRulesResponse]:
        """
        Create one or more firewall rules.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._post(
            f"/zones/{zone_identifier}/firewall/rules",
            body=maybe_transform(
                body, rule_firewall_rules_create_firewall_rules_params.RuleFirewallRulesCreateFirewallRulesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleFirewallRulesCreateFirewallRulesResponse]],
                ResultWrapper[RuleFirewallRulesCreateFirewallRulesResponse],
            ),
        )

    def firewall_rules_list_firewall_rules(
        self,
        zone_identifier: str,
        *,
        action: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        paused: bool | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleFirewallRulesListFirewallRulesResponse]:
        """Fetches firewall rules in a zone.

        You can filter the results using several
        optional parameters.

        Args:
          zone_identifier: Identifier

          action: The action to search for. Must be an exact match.

          description: A case-insensitive string to find in the description.

          page: Page number of paginated results.

          paused: When true, indicates that the firewall rule is currently paused.

          per_page: Number of firewall rules per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/firewall/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action": action,
                        "description": description,
                        "page": page,
                        "paused": paused,
                        "per_page": per_page,
                    },
                    rule_firewall_rules_list_firewall_rules_params.RuleFirewallRulesListFirewallRulesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleFirewallRulesListFirewallRulesResponse]],
                ResultWrapper[RuleFirewallRulesListFirewallRulesResponse],
            ),
        )

    def firewall_rules_update_firewall_rules(
        self,
        zone_identifier: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleFirewallRulesUpdateFirewallRulesResponse]:
        """
        Updates one or more existing firewall rules.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._put(
            f"/zones/{zone_identifier}/firewall/rules",
            body=maybe_transform(
                body, rule_firewall_rules_update_firewall_rules_params.RuleFirewallRulesUpdateFirewallRulesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleFirewallRulesUpdateFirewallRulesResponse]],
                ResultWrapper[RuleFirewallRulesUpdateFirewallRulesResponse],
            ),
        )

    def firewall_rules_update_priority_of_firewall_rules(
        self,
        zone_identifier: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleFirewallRulesUpdatePriorityOfFirewallRulesResponse]:
        """
        Updates the priority of existing firewall rules.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._patch(
            f"/zones/{zone_identifier}/firewall/rules",
            body=maybe_transform(
                body,
                rule_firewall_rules_update_priority_of_firewall_rules_params.RuleFirewallRulesUpdatePriorityOfFirewallRulesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleFirewallRulesUpdatePriorityOfFirewallRulesResponse]],
                ResultWrapper[RuleFirewallRulesUpdatePriorityOfFirewallRulesResponse],
            ),
        )

    def get(
        self,
        id: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleGetResponse]:
        """
        Fetches the details of a firewall rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the firewall rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/zones/{zone_identifier}/firewall/rules/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleGetResponse]], ResultWrapper[RuleGetResponse]),
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
        id: str,
        *,
        zone_identifier: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleUpdateResponse]:
        """
        Updates an existing firewall rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the firewall rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/zones/{zone_identifier}/firewall/rules/{id}",
            body=maybe_transform(body, rule_update_params.RuleUpdateParams),
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
        id: str,
        *,
        zone_identifier: str,
        delete_filter_if_unused: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleDeleteResponse]:
        """
        Deletes an existing firewall rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the firewall rule.

          delete_filter_if_unused: When true, indicates that Cloudflare should also delete the associated filter if
              there are no other firewall rules referencing the filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/zones/{zone_identifier}/firewall/rules/{id}",
            body=maybe_transform(
                {"delete_filter_if_unused": delete_filter_if_unused}, rule_delete_params.RuleDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleDeleteResponse]], ResultWrapper[RuleDeleteResponse]),
        )

    async def firewall_rules_create_firewall_rules(
        self,
        zone_identifier: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleFirewallRulesCreateFirewallRulesResponse]:
        """
        Create one or more firewall rules.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._post(
            f"/zones/{zone_identifier}/firewall/rules",
            body=maybe_transform(
                body, rule_firewall_rules_create_firewall_rules_params.RuleFirewallRulesCreateFirewallRulesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleFirewallRulesCreateFirewallRulesResponse]],
                ResultWrapper[RuleFirewallRulesCreateFirewallRulesResponse],
            ),
        )

    async def firewall_rules_list_firewall_rules(
        self,
        zone_identifier: str,
        *,
        action: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        paused: bool | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleFirewallRulesListFirewallRulesResponse]:
        """Fetches firewall rules in a zone.

        You can filter the results using several
        optional parameters.

        Args:
          zone_identifier: Identifier

          action: The action to search for. Must be an exact match.

          description: A case-insensitive string to find in the description.

          page: Page number of paginated results.

          paused: When true, indicates that the firewall rule is currently paused.

          per_page: Number of firewall rules per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/firewall/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "action": action,
                        "description": description,
                        "page": page,
                        "paused": paused,
                        "per_page": per_page,
                    },
                    rule_firewall_rules_list_firewall_rules_params.RuleFirewallRulesListFirewallRulesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleFirewallRulesListFirewallRulesResponse]],
                ResultWrapper[RuleFirewallRulesListFirewallRulesResponse],
            ),
        )

    async def firewall_rules_update_firewall_rules(
        self,
        zone_identifier: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleFirewallRulesUpdateFirewallRulesResponse]:
        """
        Updates one or more existing firewall rules.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._put(
            f"/zones/{zone_identifier}/firewall/rules",
            body=maybe_transform(
                body, rule_firewall_rules_update_firewall_rules_params.RuleFirewallRulesUpdateFirewallRulesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleFirewallRulesUpdateFirewallRulesResponse]],
                ResultWrapper[RuleFirewallRulesUpdateFirewallRulesResponse],
            ),
        )

    async def firewall_rules_update_priority_of_firewall_rules(
        self,
        zone_identifier: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleFirewallRulesUpdatePriorityOfFirewallRulesResponse]:
        """
        Updates the priority of existing firewall rules.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._patch(
            f"/zones/{zone_identifier}/firewall/rules",
            body=maybe_transform(
                body,
                rule_firewall_rules_update_priority_of_firewall_rules_params.RuleFirewallRulesUpdatePriorityOfFirewallRulesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleFirewallRulesUpdatePriorityOfFirewallRulesResponse]],
                ResultWrapper[RuleFirewallRulesUpdatePriorityOfFirewallRulesResponse],
            ),
        )

    async def get(
        self,
        id: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleGetResponse]:
        """
        Fetches the details of a firewall rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the firewall rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/zones/{zone_identifier}/firewall/rules/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleGetResponse]], ResultWrapper[RuleGetResponse]),
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
        self.firewall_rules_create_firewall_rules = to_raw_response_wrapper(
            rules.firewall_rules_create_firewall_rules,
        )
        self.firewall_rules_list_firewall_rules = to_raw_response_wrapper(
            rules.firewall_rules_list_firewall_rules,
        )
        self.firewall_rules_update_firewall_rules = to_raw_response_wrapper(
            rules.firewall_rules_update_firewall_rules,
        )
        self.firewall_rules_update_priority_of_firewall_rules = to_raw_response_wrapper(
            rules.firewall_rules_update_priority_of_firewall_rules,
        )
        self.get = to_raw_response_wrapper(
            rules.get,
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
        self.firewall_rules_create_firewall_rules = async_to_raw_response_wrapper(
            rules.firewall_rules_create_firewall_rules,
        )
        self.firewall_rules_list_firewall_rules = async_to_raw_response_wrapper(
            rules.firewall_rules_list_firewall_rules,
        )
        self.firewall_rules_update_firewall_rules = async_to_raw_response_wrapper(
            rules.firewall_rules_update_firewall_rules,
        )
        self.firewall_rules_update_priority_of_firewall_rules = async_to_raw_response_wrapper(
            rules.firewall_rules_update_priority_of_firewall_rules,
        )
        self.get = async_to_raw_response_wrapper(
            rules.get,
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
        self.firewall_rules_create_firewall_rules = to_streamed_response_wrapper(
            rules.firewall_rules_create_firewall_rules,
        )
        self.firewall_rules_list_firewall_rules = to_streamed_response_wrapper(
            rules.firewall_rules_list_firewall_rules,
        )
        self.firewall_rules_update_firewall_rules = to_streamed_response_wrapper(
            rules.firewall_rules_update_firewall_rules,
        )
        self.firewall_rules_update_priority_of_firewall_rules = to_streamed_response_wrapper(
            rules.firewall_rules_update_priority_of_firewall_rules,
        )
        self.get = to_streamed_response_wrapper(
            rules.get,
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
        self.firewall_rules_create_firewall_rules = async_to_streamed_response_wrapper(
            rules.firewall_rules_create_firewall_rules,
        )
        self.firewall_rules_list_firewall_rules = async_to_streamed_response_wrapper(
            rules.firewall_rules_list_firewall_rules,
        )
        self.firewall_rules_update_firewall_rules = async_to_streamed_response_wrapper(
            rules.firewall_rules_update_firewall_rules,
        )
        self.firewall_rules_update_priority_of_firewall_rules = async_to_streamed_response_wrapper(
            rules.firewall_rules_update_priority_of_firewall_rules,
        )
        self.get = async_to_streamed_response_wrapper(
            rules.get,
        )
