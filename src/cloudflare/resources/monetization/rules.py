# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Iterable, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from ...types.monetization import rule_update_params, rule_edit_rule_params
from ...types.monetization.monetization_rule import MonetizationRule
from ...types.monetization.monetization_rule_collection import MonetizationRuleCollection
from ...types.monetization.monetization_rule_input_param import MonetizationRuleInputParam

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

    def update(
        self,
        *,
        zone_id: str,
        rules: Iterable[MonetizationRuleInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonetizationRuleCollection:
        """
        Replaces the zone's Payment Required ruleset with the submitted desired state.
        Submit an empty rules array to clear all payment rules.

        Args:
          zone_id: The unique ID of the zone.

          rules: Full desired Payment Required ruleset. An empty array clears all payment rules.
              The ruleset may contain at most 40 unique wallet addresses; address comparison
              is case-insensitive. Every address must pass wallet screening before deployment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            path_template("/zones/{zone_id}/monetization/rules", zone_id=zone_id),
            body=maybe_transform({"rules": rules}, rule_update_params.RuleUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[MonetizationRuleCollection]._unwrapper,
            ),
            cast_to=cast(Type[MonetizationRuleCollection], ResultWrapper[MonetizationRuleCollection]),
        )

    def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonetizationRuleCollection:
        """Removes every Payment Required rule from the zone.

        Any rules the service does
        not own are preserved. Deleting a zone with no payment rules is a no-op. Returns
        the resulting (empty) rule collection.

        Args:
          zone_id: The unique ID of the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._delete(
            path_template("/zones/{zone_id}/monetization/rules", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[MonetizationRuleCollection]._unwrapper,
            ),
            cast_to=cast(Type[MonetizationRuleCollection], ResultWrapper[MonetizationRuleCollection]),
        )

    def delete_rule(
        self,
        rule_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonetizationRuleCollection:
        """Removes a single Payment Required rule identified by its ID.

        Every other rule is
        preserved. Returns the resulting rule collection.

        Args:
          zone_id: The unique ID of the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._delete(
            path_template("/zones/{zone_id}/monetization/rules/{rule_id}", zone_id=zone_id, rule_id=rule_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[MonetizationRuleCollection]._unwrapper,
            ),
            cast_to=cast(Type[MonetizationRuleCollection], ResultWrapper[MonetizationRuleCollection]),
        )

    def edit_rule(
        self,
        rule_id: str,
        *,
        zone_id: str,
        address: str | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        expression: str | Omit = omit,
        price: str | Omit = omit,
        scheme: Literal["exact", "upto", "origin_controlled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonetizationRuleCollection:
        """Applies a partial update to a single Payment Required rule.

        Only the fields
        present in the request body are changed; omitted fields keep their current
        values. Returns the full resulting rule collection.

        Args:
          zone_id: The unique ID of the zone.

          address: 0x-prefixed 20-byte hexadecimal Ethereum address. Mixed-case addresses must
              carry a valid EIP-55 checksum; all-lowercase or all-uppercase addresses are also
              accepted. The effective address must pass wallet screening whenever the rule is
              patched.

          expression: Wirefilter expression identifying the requests that require payment. Forwarded
              verbatim to the Rulesets API, which validates its syntax.

          price: Price in the smallest indivisible unit of the configured payment token, encoded
              as a decimal string. Must be a canonical decimal integer in [1000, 100000000]:
              no leading zeros, and a bare JSON number is rejected. The price is required for
              the fixed-price schemes ("exact" and "upto") and must be at least 1000, the
              smallest amount the payment facilitator can settle ($0.001 for a 6-decimal token
              such as USDC), and at most 100000000 ($100 for a 6-decimal token). When the
              scheme is "origin_controlled" the origin server sets pricing dynamically and the
              rule carries no price: the field must be omitted — any provided value, including
              "0", is rejected because it would not be enforced. Responses always encode this
              as a string and omit it for "origin_controlled" rules; the pattern matches
              exactly the set of values the server accepts.

          scheme: X402 payment scheme. "exact" requires the specified payment amount; "upto"
              permits a payment up to the specified amount; "origin_controlled" lets the
              origin server set pricing dynamically, in which case the rule carries no price
              and the price field must be omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._patch(
            path_template("/zones/{zone_id}/monetization/rules/{rule_id}", zone_id=zone_id, rule_id=rule_id),
            body=maybe_transform(
                {
                    "address": address,
                    "description": description,
                    "enabled": enabled,
                    "expression": expression,
                    "price": price,
                    "scheme": scheme,
                },
                rule_edit_rule_params.RuleEditRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[MonetizationRuleCollection]._unwrapper,
            ),
            cast_to=cast(Type[MonetizationRuleCollection], ResultWrapper[MonetizationRuleCollection]),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonetizationRuleCollection:
        """Returns the currently deployed Payment Required rules for a zone.

        A zone with no
        Payment Required ruleset returns 404.

        Args:
          zone_id: The unique ID of the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            path_template("/zones/{zone_id}/monetization/rules", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[MonetizationRuleCollection]._unwrapper,
            ),
            cast_to=cast(Type[MonetizationRuleCollection], ResultWrapper[MonetizationRuleCollection]),
        )

    def get_rule(
        self,
        rule_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonetizationRule:
        """
        Returns a single Payment Required rule identified by its ID.

        Args:
          zone_id: The unique ID of the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return cast(
            MonetizationRule,
            self._get(
                path_template("/zones/{zone_id}/monetization/rules/{rule_id}", zone_id=zone_id, rule_id=rule_id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[MonetizationRule]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[MonetizationRule]
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

    async def update(
        self,
        *,
        zone_id: str,
        rules: Iterable[MonetizationRuleInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonetizationRuleCollection:
        """
        Replaces the zone's Payment Required ruleset with the submitted desired state.
        Submit an empty rules array to clear all payment rules.

        Args:
          zone_id: The unique ID of the zone.

          rules: Full desired Payment Required ruleset. An empty array clears all payment rules.
              The ruleset may contain at most 40 unique wallet addresses; address comparison
              is case-insensitive. Every address must pass wallet screening before deployment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            path_template("/zones/{zone_id}/monetization/rules", zone_id=zone_id),
            body=await async_maybe_transform({"rules": rules}, rule_update_params.RuleUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[MonetizationRuleCollection]._unwrapper,
            ),
            cast_to=cast(Type[MonetizationRuleCollection], ResultWrapper[MonetizationRuleCollection]),
        )

    async def delete(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonetizationRuleCollection:
        """Removes every Payment Required rule from the zone.

        Any rules the service does
        not own are preserved. Deleting a zone with no payment rules is a no-op. Returns
        the resulting (empty) rule collection.

        Args:
          zone_id: The unique ID of the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._delete(
            path_template("/zones/{zone_id}/monetization/rules", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[MonetizationRuleCollection]._unwrapper,
            ),
            cast_to=cast(Type[MonetizationRuleCollection], ResultWrapper[MonetizationRuleCollection]),
        )

    async def delete_rule(
        self,
        rule_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonetizationRuleCollection:
        """Removes a single Payment Required rule identified by its ID.

        Every other rule is
        preserved. Returns the resulting rule collection.

        Args:
          zone_id: The unique ID of the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._delete(
            path_template("/zones/{zone_id}/monetization/rules/{rule_id}", zone_id=zone_id, rule_id=rule_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[MonetizationRuleCollection]._unwrapper,
            ),
            cast_to=cast(Type[MonetizationRuleCollection], ResultWrapper[MonetizationRuleCollection]),
        )

    async def edit_rule(
        self,
        rule_id: str,
        *,
        zone_id: str,
        address: str | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        expression: str | Omit = omit,
        price: str | Omit = omit,
        scheme: Literal["exact", "upto", "origin_controlled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonetizationRuleCollection:
        """Applies a partial update to a single Payment Required rule.

        Only the fields
        present in the request body are changed; omitted fields keep their current
        values. Returns the full resulting rule collection.

        Args:
          zone_id: The unique ID of the zone.

          address: 0x-prefixed 20-byte hexadecimal Ethereum address. Mixed-case addresses must
              carry a valid EIP-55 checksum; all-lowercase or all-uppercase addresses are also
              accepted. The effective address must pass wallet screening whenever the rule is
              patched.

          expression: Wirefilter expression identifying the requests that require payment. Forwarded
              verbatim to the Rulesets API, which validates its syntax.

          price: Price in the smallest indivisible unit of the configured payment token, encoded
              as a decimal string. Must be a canonical decimal integer in [1000, 100000000]:
              no leading zeros, and a bare JSON number is rejected. The price is required for
              the fixed-price schemes ("exact" and "upto") and must be at least 1000, the
              smallest amount the payment facilitator can settle ($0.001 for a 6-decimal token
              such as USDC), and at most 100000000 ($100 for a 6-decimal token). When the
              scheme is "origin_controlled" the origin server sets pricing dynamically and the
              rule carries no price: the field must be omitted — any provided value, including
              "0", is rejected because it would not be enforced. Responses always encode this
              as a string and omit it for "origin_controlled" rules; the pattern matches
              exactly the set of values the server accepts.

          scheme: X402 payment scheme. "exact" requires the specified payment amount; "upto"
              permits a payment up to the specified amount; "origin_controlled" lets the
              origin server set pricing dynamically, in which case the rule carries no price
              and the price field must be omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._patch(
            path_template("/zones/{zone_id}/monetization/rules/{rule_id}", zone_id=zone_id, rule_id=rule_id),
            body=await async_maybe_transform(
                {
                    "address": address,
                    "description": description,
                    "enabled": enabled,
                    "expression": expression,
                    "price": price,
                    "scheme": scheme,
                },
                rule_edit_rule_params.RuleEditRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[MonetizationRuleCollection]._unwrapper,
            ),
            cast_to=cast(Type[MonetizationRuleCollection], ResultWrapper[MonetizationRuleCollection]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonetizationRuleCollection:
        """Returns the currently deployed Payment Required rules for a zone.

        A zone with no
        Payment Required ruleset returns 404.

        Args:
          zone_id: The unique ID of the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            path_template("/zones/{zone_id}/monetization/rules", zone_id=zone_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[MonetizationRuleCollection]._unwrapper,
            ),
            cast_to=cast(Type[MonetizationRuleCollection], ResultWrapper[MonetizationRuleCollection]),
        )

    async def get_rule(
        self,
        rule_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonetizationRule:
        """
        Returns a single Payment Required rule identified by its ID.

        Args:
          zone_id: The unique ID of the zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return cast(
            MonetizationRule,
            await self._get(
                path_template("/zones/{zone_id}/monetization/rules/{rule_id}", zone_id=zone_id, rule_id=rule_id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[MonetizationRule]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[MonetizationRule]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class RulesResourceWithRawResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.update = to_raw_response_wrapper(
            rules.update,
        )
        self.delete = to_raw_response_wrapper(
            rules.delete,
        )
        self.delete_rule = to_raw_response_wrapper(
            rules.delete_rule,
        )
        self.edit_rule = to_raw_response_wrapper(
            rules.edit_rule,
        )
        self.get = to_raw_response_wrapper(
            rules.get,
        )
        self.get_rule = to_raw_response_wrapper(
            rules.get_rule,
        )


class AsyncRulesResourceWithRawResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.update = async_to_raw_response_wrapper(
            rules.update,
        )
        self.delete = async_to_raw_response_wrapper(
            rules.delete,
        )
        self.delete_rule = async_to_raw_response_wrapper(
            rules.delete_rule,
        )
        self.edit_rule = async_to_raw_response_wrapper(
            rules.edit_rule,
        )
        self.get = async_to_raw_response_wrapper(
            rules.get,
        )
        self.get_rule = async_to_raw_response_wrapper(
            rules.get_rule,
        )


class RulesResourceWithStreamingResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.update = to_streamed_response_wrapper(
            rules.update,
        )
        self.delete = to_streamed_response_wrapper(
            rules.delete,
        )
        self.delete_rule = to_streamed_response_wrapper(
            rules.delete_rule,
        )
        self.edit_rule = to_streamed_response_wrapper(
            rules.edit_rule,
        )
        self.get = to_streamed_response_wrapper(
            rules.get,
        )
        self.get_rule = to_streamed_response_wrapper(
            rules.get_rule,
        )


class AsyncRulesResourceWithStreamingResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.update = async_to_streamed_response_wrapper(
            rules.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            rules.delete,
        )
        self.delete_rule = async_to_streamed_response_wrapper(
            rules.delete_rule,
        )
        self.edit_rule = async_to_streamed_response_wrapper(
            rules.edit_rule,
        )
        self.get = async_to_streamed_response_wrapper(
            rules.get,
        )
        self.get_rule = async_to_streamed_response_wrapper(
            rules.get_rule,
        )
