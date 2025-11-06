# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncSinglePage, AsyncSinglePage, SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.token_validation import (
    rule_edit_params,
    rule_list_params,
    rule_create_params,
    rule_bulk_edit_params,
    rule_bulk_create_params,
)
from ...types.token_validation.token_validation_rule import TokenValidationRule

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

    def create(
        self,
        *,
        zone_id: str,
        action: Literal["log", "block"],
        description: str,
        enabled: bool,
        expression: str,
        selector: rule_create_params.Selector,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenValidationRule:
        """
        Create a token validation rule.

        Args:
          zone_id: Identifier.

          action: Action to take on requests that match operations included in `selector` and fail
              `expression`.

          description: A human-readable description that gives more details than `title`.

          enabled: Toggle rule on or off.

          expression: Rule expression. Requests that fail to match this expression will be subject to
              `action`.

              For details on expressions, see the
              [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/).

          selector: Select operations covered by this rule.

              For details on selectors, see the
              [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/).

          title: A human-readable name for the rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/token_validation/rules",
            body=maybe_transform(
                {
                    "action": action,
                    "description": description,
                    "enabled": enabled,
                    "expression": expression,
                    "selector": selector,
                    "title": title,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TokenValidationRule]._unwrapper,
            ),
            cast_to=cast(Type[TokenValidationRule], ResultWrapper[TokenValidationRule]),
        )

    def list(
        self,
        *,
        zone_id: str,
        id: str | Omit = omit,
        action: Literal["log", "block"] | Omit = omit,
        enabled: bool | Omit = omit,
        host: str | Omit = omit,
        hostname: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        rule_id: str | Omit = omit,
        token_configuration: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[TokenValidationRule]:
        """
        List token validation rules

        Args:
          zone_id: Identifier.

          id: Select rules with these IDs.

          action: Action to take on requests that match operations included in `selector` and fail
              `expression`.

          enabled: Toggle rule on or off.

          host: Select rules with this host in `include`.

          hostname: Select rules with this host in `include`.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          rule_id: Select rules with these IDs.

          token_configuration: Select rules using any of these token configurations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/token_validation/rules",
            page=SyncV4PagePaginationArray[TokenValidationRule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "action": action,
                        "enabled": enabled,
                        "host": host,
                        "hostname": hostname,
                        "page": page,
                        "per_page": per_page,
                        "rule_id": rule_id,
                        "token_configuration": token_configuration,
                    },
                    rule_list_params.RuleListParams,
                ),
            ),
            model=TokenValidationRule,
        )

    def delete(
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
    ) -> object:
        """
        Delete a zone token validation rule.

        Args:
          zone_id: Identifier.

          rule_id: UUID.

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
            f"/zones/{zone_id}/token_validation/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def bulk_create(
        self,
        *,
        zone_id: str,
        body: Iterable[rule_bulk_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[TokenValidationRule]:
        """
        Create zone token validation rules.

        A request can create multiple Token Validation Rules.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/token_validation/rules/bulk",
            page=SyncSinglePage[TokenValidationRule],
            body=maybe_transform(body, Iterable[rule_bulk_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=TokenValidationRule,
            method="post",
        )

    def bulk_edit(
        self,
        *,
        zone_id: str,
        body: Iterable[rule_bulk_edit_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[TokenValidationRule]:
        """
        Edit token validation rules.

        A request can update multiple Token Validation Rules.

        Rules can be re-ordered using the `position` field.

        Returns all updated rules.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/token_validation/rules/bulk",
            page=SyncSinglePage[TokenValidationRule],
            body=maybe_transform(body, Iterable[rule_bulk_edit_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=TokenValidationRule,
            method="patch",
        )

    def edit(
        self,
        rule_id: str,
        *,
        zone_id: str,
        action: Literal["log", "block"] | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        expression: str | Omit = omit,
        position: rule_edit_params.Position | Omit = omit,
        selector: rule_edit_params.Selector | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenValidationRule:
        """
        Edit a zone token validation rule.

        Args:
          zone_id: Identifier.

          rule_id: UUID.

          action: Action to take on requests that match operations included in `selector` and fail
              `expression`.

          description: A human-readable description that gives more details than `title`.

          enabled: Toggle rule on or off.

          expression: Rule expression. Requests that fail to match this expression will be subject to
              `action`.

              For details on expressions, see the
              [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/).

          position: Update rule order among zone rules.

          selector: Select operations covered by this rule.

              For details on selectors, see the
              [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/).

          title: A human-readable name for the rule.

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
            f"/zones/{zone_id}/token_validation/rules/{rule_id}",
            body=maybe_transform(
                {
                    "action": action,
                    "description": description,
                    "enabled": enabled,
                    "expression": expression,
                    "position": position,
                    "selector": selector,
                    "title": title,
                },
                rule_edit_params.RuleEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TokenValidationRule]._unwrapper,
            ),
            cast_to=cast(Type[TokenValidationRule], ResultWrapper[TokenValidationRule]),
        )

    def get(
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
    ) -> TokenValidationRule:
        """
        Get a zone token validation rule.

        Args:
          zone_id: Identifier.

          rule_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._get(
            f"/zones/{zone_id}/token_validation/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TokenValidationRule]._unwrapper,
            ),
            cast_to=cast(Type[TokenValidationRule], ResultWrapper[TokenValidationRule]),
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

    async def create(
        self,
        *,
        zone_id: str,
        action: Literal["log", "block"],
        description: str,
        enabled: bool,
        expression: str,
        selector: rule_create_params.Selector,
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenValidationRule:
        """
        Create a token validation rule.

        Args:
          zone_id: Identifier.

          action: Action to take on requests that match operations included in `selector` and fail
              `expression`.

          description: A human-readable description that gives more details than `title`.

          enabled: Toggle rule on or off.

          expression: Rule expression. Requests that fail to match this expression will be subject to
              `action`.

              For details on expressions, see the
              [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/).

          selector: Select operations covered by this rule.

              For details on selectors, see the
              [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/).

          title: A human-readable name for the rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/token_validation/rules",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "description": description,
                    "enabled": enabled,
                    "expression": expression,
                    "selector": selector,
                    "title": title,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TokenValidationRule]._unwrapper,
            ),
            cast_to=cast(Type[TokenValidationRule], ResultWrapper[TokenValidationRule]),
        )

    def list(
        self,
        *,
        zone_id: str,
        id: str | Omit = omit,
        action: Literal["log", "block"] | Omit = omit,
        enabled: bool | Omit = omit,
        host: str | Omit = omit,
        hostname: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        rule_id: str | Omit = omit,
        token_configuration: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TokenValidationRule, AsyncV4PagePaginationArray[TokenValidationRule]]:
        """
        List token validation rules

        Args:
          zone_id: Identifier.

          id: Select rules with these IDs.

          action: Action to take on requests that match operations included in `selector` and fail
              `expression`.

          enabled: Toggle rule on or off.

          host: Select rules with this host in `include`.

          hostname: Select rules with this host in `include`.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          rule_id: Select rules with these IDs.

          token_configuration: Select rules using any of these token configurations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/token_validation/rules",
            page=AsyncV4PagePaginationArray[TokenValidationRule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "action": action,
                        "enabled": enabled,
                        "host": host,
                        "hostname": hostname,
                        "page": page,
                        "per_page": per_page,
                        "rule_id": rule_id,
                        "token_configuration": token_configuration,
                    },
                    rule_list_params.RuleListParams,
                ),
            ),
            model=TokenValidationRule,
        )

    async def delete(
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
    ) -> object:
        """
        Delete a zone token validation rule.

        Args:
          zone_id: Identifier.

          rule_id: UUID.

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
            f"/zones/{zone_id}/token_validation/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def bulk_create(
        self,
        *,
        zone_id: str,
        body: Iterable[rule_bulk_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TokenValidationRule, AsyncSinglePage[TokenValidationRule]]:
        """
        Create zone token validation rules.

        A request can create multiple Token Validation Rules.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/token_validation/rules/bulk",
            page=AsyncSinglePage[TokenValidationRule],
            body=maybe_transform(body, Iterable[rule_bulk_create_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=TokenValidationRule,
            method="post",
        )

    def bulk_edit(
        self,
        *,
        zone_id: str,
        body: Iterable[rule_bulk_edit_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TokenValidationRule, AsyncSinglePage[TokenValidationRule]]:
        """
        Edit token validation rules.

        A request can update multiple Token Validation Rules.

        Rules can be re-ordered using the `position` field.

        Returns all updated rules.

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/token_validation/rules/bulk",
            page=AsyncSinglePage[TokenValidationRule],
            body=maybe_transform(body, Iterable[rule_bulk_edit_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=TokenValidationRule,
            method="patch",
        )

    async def edit(
        self,
        rule_id: str,
        *,
        zone_id: str,
        action: Literal["log", "block"] | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        expression: str | Omit = omit,
        position: rule_edit_params.Position | Omit = omit,
        selector: rule_edit_params.Selector | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenValidationRule:
        """
        Edit a zone token validation rule.

        Args:
          zone_id: Identifier.

          rule_id: UUID.

          action: Action to take on requests that match operations included in `selector` and fail
              `expression`.

          description: A human-readable description that gives more details than `title`.

          enabled: Toggle rule on or off.

          expression: Rule expression. Requests that fail to match this expression will be subject to
              `action`.

              For details on expressions, see the
              [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/).

          position: Update rule order among zone rules.

          selector: Select operations covered by this rule.

              For details on selectors, see the
              [Cloudflare Docs](https://developers.cloudflare.com/api-shield/security/jwt-validation/).

          title: A human-readable name for the rule.

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
            f"/zones/{zone_id}/token_validation/rules/{rule_id}",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "description": description,
                    "enabled": enabled,
                    "expression": expression,
                    "position": position,
                    "selector": selector,
                    "title": title,
                },
                rule_edit_params.RuleEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TokenValidationRule]._unwrapper,
            ),
            cast_to=cast(Type[TokenValidationRule], ResultWrapper[TokenValidationRule]),
        )

    async def get(
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
    ) -> TokenValidationRule:
        """
        Get a zone token validation rule.

        Args:
          zone_id: Identifier.

          rule_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._get(
            f"/zones/{zone_id}/token_validation/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TokenValidationRule]._unwrapper,
            ),
            cast_to=cast(Type[TokenValidationRule], ResultWrapper[TokenValidationRule]),
        )


class RulesResourceWithRawResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.create = to_raw_response_wrapper(
            rules.create,
        )
        self.list = to_raw_response_wrapper(
            rules.list,
        )
        self.delete = to_raw_response_wrapper(
            rules.delete,
        )
        self.bulk_create = to_raw_response_wrapper(
            rules.bulk_create,
        )
        self.bulk_edit = to_raw_response_wrapper(
            rules.bulk_edit,
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

        self.create = async_to_raw_response_wrapper(
            rules.create,
        )
        self.list = async_to_raw_response_wrapper(
            rules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            rules.delete,
        )
        self.bulk_create = async_to_raw_response_wrapper(
            rules.bulk_create,
        )
        self.bulk_edit = async_to_raw_response_wrapper(
            rules.bulk_edit,
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

        self.create = to_streamed_response_wrapper(
            rules.create,
        )
        self.list = to_streamed_response_wrapper(
            rules.list,
        )
        self.delete = to_streamed_response_wrapper(
            rules.delete,
        )
        self.bulk_create = to_streamed_response_wrapper(
            rules.bulk_create,
        )
        self.bulk_edit = to_streamed_response_wrapper(
            rules.bulk_edit,
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

        self.create = async_to_streamed_response_wrapper(
            rules.create,
        )
        self.list = async_to_streamed_response_wrapper(
            rules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            rules.delete,
        )
        self.bulk_create = async_to_streamed_response_wrapper(
            rules.bulk_create,
        )
        self.bulk_edit = async_to_streamed_response_wrapper(
            rules.bulk_edit,
        )
        self.edit = async_to_streamed_response_wrapper(
            rules.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            rules.get,
        )
