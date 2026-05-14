# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

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
from ......_base_client import make_request_options
from ......types.ddos_protection.advanced_tcp_protection.syn_protection.rules import item_edit_params
from ......types.ddos_protection.advanced_tcp_protection.syn_protection.rules.item_get_response import ItemGetResponse
from ......types.ddos_protection.advanced_tcp_protection.syn_protection.rules.item_edit_response import ItemEditResponse
from ......types.ddos_protection.advanced_tcp_protection.syn_protection.rules.item_delete_response import (
    ItemDeleteResponse,
)

__all__ = ["ItemsResource", "AsyncItemsResource"]


class ItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ItemsResourceWithStreamingResponse(self)

    def delete(
        self,
        rule_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemDeleteResponse:
        """
        Delete a SYN Protection rule specified by the given UUID.

        Args:
          account_id: Identifier.

          rule_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules/{rule_id}",
                account_id=account_id,
                rule_id=rule_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemDeleteResponse,
        )

    def edit(
        self,
        rule_id: str,
        *,
        account_id: str,
        burst_sensitivity: str | Omit = omit,
        mitigation_type: str | Omit = omit,
        mode: str | Omit = omit,
        rate_sensitivity: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ItemEditResponse]:
        """
        Update a SYN Protection rule specified by the given UUID.

        Args:
          account_id: Identifier.

          rule_id: UUID.

          burst_sensitivity: The new burst sensitivity. Optional. Must be one of 'low', 'medium', 'high'.

          mitigation_type: The new mitigation type. Optional. Must be one of 'challenge' or 'retransmit'.

          mode: The new mode for SYN Protection. Optional. Must be one of 'enabled', 'disabled',
              'monitoring'.

          rate_sensitivity: The new rate sensitivity. Optional. Must be one of 'low', 'medium', 'high'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules/{rule_id}",
                account_id=account_id,
                rule_id=rule_id,
            ),
            body=maybe_transform(
                {
                    "burst_sensitivity": burst_sensitivity,
                    "mitigation_type": mitigation_type,
                    "mode": mode,
                    "rate_sensitivity": rate_sensitivity,
                },
                item_edit_params.ItemEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ItemEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ItemEditResponse]], ResultWrapper[ItemEditResponse]),
        )

    def get(
        self,
        rule_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ItemGetResponse]:
        """
        Get a SYN Protection rule specified by the given UUID.

        Args:
          account_id: Identifier.

          rule_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules/{rule_id}",
                account_id=account_id,
                rule_id=rule_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ItemGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ItemGetResponse]], ResultWrapper[ItemGetResponse]),
        )


class AsyncItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncItemsResourceWithStreamingResponse(self)

    async def delete(
        self,
        rule_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ItemDeleteResponse:
        """
        Delete a SYN Protection rule specified by the given UUID.

        Args:
          account_id: Identifier.

          rule_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules/{rule_id}",
                account_id=account_id,
                rule_id=rule_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ItemDeleteResponse,
        )

    async def edit(
        self,
        rule_id: str,
        *,
        account_id: str,
        burst_sensitivity: str | Omit = omit,
        mitigation_type: str | Omit = omit,
        mode: str | Omit = omit,
        rate_sensitivity: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ItemEditResponse]:
        """
        Update a SYN Protection rule specified by the given UUID.

        Args:
          account_id: Identifier.

          rule_id: UUID.

          burst_sensitivity: The new burst sensitivity. Optional. Must be one of 'low', 'medium', 'high'.

          mitigation_type: The new mitigation type. Optional. Must be one of 'challenge' or 'retransmit'.

          mode: The new mode for SYN Protection. Optional. Must be one of 'enabled', 'disabled',
              'monitoring'.

          rate_sensitivity: The new rate sensitivity. Optional. Must be one of 'low', 'medium', 'high'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules/{rule_id}",
                account_id=account_id,
                rule_id=rule_id,
            ),
            body=await async_maybe_transform(
                {
                    "burst_sensitivity": burst_sensitivity,
                    "mitigation_type": mitigation_type,
                    "mode": mode,
                    "rate_sensitivity": rate_sensitivity,
                },
                item_edit_params.ItemEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ItemEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ItemEditResponse]], ResultWrapper[ItemEditResponse]),
        )

    async def get(
        self,
        rule_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ItemGetResponse]:
        """
        Get a SYN Protection rule specified by the given UUID.

        Args:
          account_id: Identifier.

          rule_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/magic/advanced_tcp_protection/configs/syn_protection/rules/{rule_id}",
                account_id=account_id,
                rule_id=rule_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ItemGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ItemGetResponse]], ResultWrapper[ItemGetResponse]),
        )


class ItemsResourceWithRawResponse:
    def __init__(self, items: ItemsResource) -> None:
        self._items = items

        self.delete = to_raw_response_wrapper(
            items.delete,
        )
        self.edit = to_raw_response_wrapper(
            items.edit,
        )
        self.get = to_raw_response_wrapper(
            items.get,
        )


class AsyncItemsResourceWithRawResponse:
    def __init__(self, items: AsyncItemsResource) -> None:
        self._items = items

        self.delete = async_to_raw_response_wrapper(
            items.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            items.edit,
        )
        self.get = async_to_raw_response_wrapper(
            items.get,
        )


class ItemsResourceWithStreamingResponse:
    def __init__(self, items: ItemsResource) -> None:
        self._items = items

        self.delete = to_streamed_response_wrapper(
            items.delete,
        )
        self.edit = to_streamed_response_wrapper(
            items.edit,
        )
        self.get = to_streamed_response_wrapper(
            items.get,
        )


class AsyncItemsResourceWithStreamingResponse:
    def __init__(self, items: AsyncItemsResource) -> None:
        self._items = items

        self.delete = async_to_streamed_response_wrapper(
            items.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            items.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            items.get,
        )
