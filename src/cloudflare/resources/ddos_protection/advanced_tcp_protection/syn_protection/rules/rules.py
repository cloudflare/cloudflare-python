# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .items import (
    ItemsResource,
    AsyncItemsResource,
    ItemsResourceWithRawResponse,
    AsyncItemsResourceWithRawResponse,
    ItemsResourceWithStreamingResponse,
    AsyncItemsResourceWithStreamingResponse,
)
from ......_types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ......_utils import path_template, maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_wrappers import ResultWrapper
from ......pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ......_base_client import AsyncPaginator, make_request_options
from ......types.ddos_protection.advanced_tcp_protection.syn_protection import rule_list_params, rule_create_params
from ......types.ddos_protection.advanced_tcp_protection.syn_protection.rule_list_response import RuleListResponse
from ......types.ddos_protection.advanced_tcp_protection.syn_protection.rule_create_response import RuleCreateResponse
from ......types.ddos_protection.advanced_tcp_protection.syn_protection.rule_bulk_delete_response import (
    RuleBulkDeleteResponse,
)

__all__ = ["RulesResource", "AsyncRulesResource"]


class RulesResource(SyncAPIResource):
    @cached_property
    def items(self) -> ItemsResource:
        return ItemsResource(self._client)

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
        account_id: str,
        burst_sensitivity: str,
        mode: str,
        name: str,
        rate_sensitivity: str,
        scope: str,
        mitigation_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[RuleCreateResponse]:
        """
        Create a SYN Protection rule for an account.

        Args:
          account_id: Identifier.

          burst_sensitivity: The burst sensitivity. Must be one of 'low', 'medium', 'high'.

          mode: The mode for SYN Protection. Must be one of 'enabled', 'disabled', 'monitoring'.

          name: The name of the SYN Protection rule. Value is relative to the 'scope' setting.
              For 'global' scope, name should be 'global'. For either the 'region' or
              'datacenter' scope, name should be the actual name of the region or datacenter,
              e.g., 'wnam' or 'lax'.

          rate_sensitivity: The rate sensitivity. Must be one of 'low', 'medium', 'high'.

          scope: The scope for the SYN Protection rule. Must be one of 'global', 'region', or
              'datacenter'.

          mitigation_type: The type of mitigation. Must be one of 'challenge' or 'retransmit'. Optional.
              Defaults to 'challenge'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules",
                account_id=account_id,
            ),
            body=maybe_transform(
                {
                    "burst_sensitivity": burst_sensitivity,
                    "mode": mode,
                    "name": name,
                    "rate_sensitivity": rate_sensitivity,
                    "scope": scope,
                    "mitigation_type": mitigation_type,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RuleCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleCreateResponse]], ResultWrapper[RuleCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: str | Omit = omit,
        order: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[RuleListResponse]:
        """
        List all SYN Protection rules for an account.

        Args:
          account_id: Identifier.

          direction: The direction of ordering (ASC or DESC). Defaults to 'ASC'.

          order: The field to order by. Defaults to 'prefix'.

          page: The page number for pagination. Defaults to 1.

          per_page: The number of items per page. Must be between 10 and 1000. Defaults to 25.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules",
                account_id=account_id,
            ),
            page=SyncV4PagePaginationArray[RuleListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    rule_list_params.RuleListParams,
                ),
            ),
            model=RuleListResponse,
        )

    def bulk_delete(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleBulkDeleteResponse:
        """
        Delete all SYN Protection rules for an account.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules",
                account_id=account_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleBulkDeleteResponse,
        )


class AsyncRulesResource(AsyncAPIResource):
    @cached_property
    def items(self) -> AsyncItemsResource:
        return AsyncItemsResource(self._client)

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
        account_id: str,
        burst_sensitivity: str,
        mode: str,
        name: str,
        rate_sensitivity: str,
        scope: str,
        mitigation_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[RuleCreateResponse]:
        """
        Create a SYN Protection rule for an account.

        Args:
          account_id: Identifier.

          burst_sensitivity: The burst sensitivity. Must be one of 'low', 'medium', 'high'.

          mode: The mode for SYN Protection. Must be one of 'enabled', 'disabled', 'monitoring'.

          name: The name of the SYN Protection rule. Value is relative to the 'scope' setting.
              For 'global' scope, name should be 'global'. For either the 'region' or
              'datacenter' scope, name should be the actual name of the region or datacenter,
              e.g., 'wnam' or 'lax'.

          rate_sensitivity: The rate sensitivity. Must be one of 'low', 'medium', 'high'.

          scope: The scope for the SYN Protection rule. Must be one of 'global', 'region', or
              'datacenter'.

          mitigation_type: The type of mitigation. Must be one of 'challenge' or 'retransmit'. Optional.
              Defaults to 'challenge'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules",
                account_id=account_id,
            ),
            body=await async_maybe_transform(
                {
                    "burst_sensitivity": burst_sensitivity,
                    "mode": mode,
                    "name": name,
                    "rate_sensitivity": rate_sensitivity,
                    "scope": scope,
                    "mitigation_type": mitigation_type,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RuleCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleCreateResponse]], ResultWrapper[RuleCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        direction: str | Omit = omit,
        order: str | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RuleListResponse, AsyncV4PagePaginationArray[RuleListResponse]]:
        """
        List all SYN Protection rules for an account.

        Args:
          account_id: Identifier.

          direction: The direction of ordering (ASC or DESC). Defaults to 'ASC'.

          order: The field to order by. Defaults to 'prefix'.

          page: The page number for pagination. Defaults to 1.

          per_page: The number of items per page. Must be between 10 and 1000. Defaults to 25.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules",
                account_id=account_id,
            ),
            page=AsyncV4PagePaginationArray[RuleListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    rule_list_params.RuleListParams,
                ),
            ),
            model=RuleListResponse,
        )

    async def bulk_delete(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleBulkDeleteResponse:
        """
        Delete all SYN Protection rules for an account.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules",
                account_id=account_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuleBulkDeleteResponse,
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
        self.bulk_delete = to_raw_response_wrapper(
            rules.bulk_delete,
        )

    @cached_property
    def items(self) -> ItemsResourceWithRawResponse:
        return ItemsResourceWithRawResponse(self._rules.items)


class AsyncRulesResourceWithRawResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.create = async_to_raw_response_wrapper(
            rules.create,
        )
        self.list = async_to_raw_response_wrapper(
            rules.list,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            rules.bulk_delete,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithRawResponse:
        return AsyncItemsResourceWithRawResponse(self._rules.items)


class RulesResourceWithStreamingResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.create = to_streamed_response_wrapper(
            rules.create,
        )
        self.list = to_streamed_response_wrapper(
            rules.list,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            rules.bulk_delete,
        )

    @cached_property
    def items(self) -> ItemsResourceWithStreamingResponse:
        return ItemsResourceWithStreamingResponse(self._rules.items)


class AsyncRulesResourceWithStreamingResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.create = async_to_streamed_response_wrapper(
            rules.create,
        )
        self.list = async_to_streamed_response_wrapper(
            rules.list,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            rules.bulk_delete,
        )

    @cached_property
    def items(self) -> AsyncItemsResourceWithStreamingResponse:
        return AsyncItemsResourceWithStreamingResponse(self._rules.items)
