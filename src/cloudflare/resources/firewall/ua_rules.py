# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.firewall import ua_rule_list_params, ua_rule_create_params, ua_rule_update_params
from ...types.firewall.ua_rule_get_response import UARuleGetResponse
from ...types.firewall.ua_rule_list_response import UARuleListResponse
from ...types.firewall.ua_rule_create_response import UARuleCreateResponse
from ...types.firewall.ua_rule_delete_response import UARuleDeleteResponse
from ...types.firewall.ua_rule_update_response import UARuleUpdateResponse

__all__ = ["UARulesResource", "AsyncUARulesResource"]


class UARulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UARulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return UARulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UARulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return UARulesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        configuration: ua_rule_create_params.Configuration,
        mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"],
        description: str | Omit = omit,
        paused: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UARuleCreateResponse:
        """
        Creates a new User Agent Blocking rule in a zone.

        Args:
          zone_id: Defines an identifier.

          mode: The action to apply to a matched request.

          description: An informative summary of the rule. This value is sanitized and any tags will be
              removed.

          paused: When true, indicates that the rule is currently paused.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/firewall/ua_rules",
            body=maybe_transform(
                {
                    "configuration": configuration,
                    "mode": mode,
                    "description": description,
                    "paused": paused,
                },
                ua_rule_create_params.UARuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[UARuleCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[UARuleCreateResponse], ResultWrapper[UARuleCreateResponse]),
        )

    def update(
        self,
        ua_rule_id: str,
        *,
        zone_id: str,
        configuration: ua_rule_update_params.Configuration,
        mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"],
        description: str | Omit = omit,
        paused: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UARuleUpdateResponse:
        """
        Updates an existing User Agent Blocking rule.

        Args:
          zone_id: Defines an identifier.

          ua_rule_id: The unique identifier of the User Agent Blocking rule.

          configuration: The rule configuration.

          mode: The action to apply to a matched request.

          description: An informative summary of the rule. This value is sanitized and any tags will be
              removed.

          paused: When true, indicates that the rule is currently paused.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not ua_rule_id:
            raise ValueError(f"Expected a non-empty value for `ua_rule_id` but received {ua_rule_id!r}")
        return self._put(
            f"/zones/{zone_id}/firewall/ua_rules/{ua_rule_id}",
            body=maybe_transform(
                {
                    "configuration": configuration,
                    "mode": mode,
                    "description": description,
                    "paused": paused,
                },
                ua_rule_update_params.UARuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[UARuleUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[UARuleUpdateResponse], ResultWrapper[UARuleUpdateResponse]),
        )

    def list(
        self,
        *,
        zone_id: str,
        description: str | Omit = omit,
        page: float | Omit = omit,
        paused: bool | Omit = omit,
        per_page: float | Omit = omit,
        user_agent: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[UARuleListResponse]:
        """Fetches User Agent Blocking rules in a zone.

        You can filter the results using
        several optional parameters.

        Args:
          zone_id: Defines an identifier.

          description: A string to search for in the description of existing rules.

          page: Page number of paginated results.

          paused: When true, indicates that the rule is currently paused.

          per_page: The maximum number of results per page. You can only set the value to `1` or to
              a multiple of 5 such as `5`, `10`, `15`, or `20`.

          user_agent: A string to search for in the user agent values of existing rules.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/firewall/ua_rules",
            page=SyncV4PagePaginationArray[UARuleListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "description": description,
                        "page": page,
                        "paused": paused,
                        "per_page": per_page,
                        "user_agent": user_agent,
                    },
                    ua_rule_list_params.UARuleListParams,
                ),
            ),
            model=UARuleListResponse,
        )

    def delete(
        self,
        ua_rule_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UARuleDeleteResponse:
        """
        Deletes an existing User Agent Blocking rule.

        Args:
          zone_id: Defines an identifier.

          ua_rule_id: The unique identifier of the User Agent Blocking rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not ua_rule_id:
            raise ValueError(f"Expected a non-empty value for `ua_rule_id` but received {ua_rule_id!r}")
        return self._delete(
            f"/zones/{zone_id}/firewall/ua_rules/{ua_rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[UARuleDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[UARuleDeleteResponse], ResultWrapper[UARuleDeleteResponse]),
        )

    def get(
        self,
        ua_rule_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UARuleGetResponse:
        """
        Fetches the details of a User Agent Blocking rule.

        Args:
          zone_id: Defines an identifier.

          ua_rule_id: The unique identifier of the User Agent Blocking rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not ua_rule_id:
            raise ValueError(f"Expected a non-empty value for `ua_rule_id` but received {ua_rule_id!r}")
        return self._get(
            f"/zones/{zone_id}/firewall/ua_rules/{ua_rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[UARuleGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[UARuleGetResponse], ResultWrapper[UARuleGetResponse]),
        )


class AsyncUARulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUARulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUARulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUARulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncUARulesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        configuration: ua_rule_create_params.Configuration,
        mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"],
        description: str | Omit = omit,
        paused: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UARuleCreateResponse:
        """
        Creates a new User Agent Blocking rule in a zone.

        Args:
          zone_id: Defines an identifier.

          mode: The action to apply to a matched request.

          description: An informative summary of the rule. This value is sanitized and any tags will be
              removed.

          paused: When true, indicates that the rule is currently paused.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/firewall/ua_rules",
            body=await async_maybe_transform(
                {
                    "configuration": configuration,
                    "mode": mode,
                    "description": description,
                    "paused": paused,
                },
                ua_rule_create_params.UARuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[UARuleCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[UARuleCreateResponse], ResultWrapper[UARuleCreateResponse]),
        )

    async def update(
        self,
        ua_rule_id: str,
        *,
        zone_id: str,
        configuration: ua_rule_update_params.Configuration,
        mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"],
        description: str | Omit = omit,
        paused: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UARuleUpdateResponse:
        """
        Updates an existing User Agent Blocking rule.

        Args:
          zone_id: Defines an identifier.

          ua_rule_id: The unique identifier of the User Agent Blocking rule.

          configuration: The rule configuration.

          mode: The action to apply to a matched request.

          description: An informative summary of the rule. This value is sanitized and any tags will be
              removed.

          paused: When true, indicates that the rule is currently paused.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not ua_rule_id:
            raise ValueError(f"Expected a non-empty value for `ua_rule_id` but received {ua_rule_id!r}")
        return await self._put(
            f"/zones/{zone_id}/firewall/ua_rules/{ua_rule_id}",
            body=await async_maybe_transform(
                {
                    "configuration": configuration,
                    "mode": mode,
                    "description": description,
                    "paused": paused,
                },
                ua_rule_update_params.UARuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[UARuleUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[UARuleUpdateResponse], ResultWrapper[UARuleUpdateResponse]),
        )

    def list(
        self,
        *,
        zone_id: str,
        description: str | Omit = omit,
        page: float | Omit = omit,
        paused: bool | Omit = omit,
        per_page: float | Omit = omit,
        user_agent: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[UARuleListResponse, AsyncV4PagePaginationArray[UARuleListResponse]]:
        """Fetches User Agent Blocking rules in a zone.

        You can filter the results using
        several optional parameters.

        Args:
          zone_id: Defines an identifier.

          description: A string to search for in the description of existing rules.

          page: Page number of paginated results.

          paused: When true, indicates that the rule is currently paused.

          per_page: The maximum number of results per page. You can only set the value to `1` or to
              a multiple of 5 such as `5`, `10`, `15`, or `20`.

          user_agent: A string to search for in the user agent values of existing rules.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/firewall/ua_rules",
            page=AsyncV4PagePaginationArray[UARuleListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "description": description,
                        "page": page,
                        "paused": paused,
                        "per_page": per_page,
                        "user_agent": user_agent,
                    },
                    ua_rule_list_params.UARuleListParams,
                ),
            ),
            model=UARuleListResponse,
        )

    async def delete(
        self,
        ua_rule_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UARuleDeleteResponse:
        """
        Deletes an existing User Agent Blocking rule.

        Args:
          zone_id: Defines an identifier.

          ua_rule_id: The unique identifier of the User Agent Blocking rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not ua_rule_id:
            raise ValueError(f"Expected a non-empty value for `ua_rule_id` but received {ua_rule_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/firewall/ua_rules/{ua_rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[UARuleDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[UARuleDeleteResponse], ResultWrapper[UARuleDeleteResponse]),
        )

    async def get(
        self,
        ua_rule_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UARuleGetResponse:
        """
        Fetches the details of a User Agent Blocking rule.

        Args:
          zone_id: Defines an identifier.

          ua_rule_id: The unique identifier of the User Agent Blocking rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not ua_rule_id:
            raise ValueError(f"Expected a non-empty value for `ua_rule_id` but received {ua_rule_id!r}")
        return await self._get(
            f"/zones/{zone_id}/firewall/ua_rules/{ua_rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[UARuleGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[UARuleGetResponse], ResultWrapper[UARuleGetResponse]),
        )


class UARulesResourceWithRawResponse:
    def __init__(self, ua_rules: UARulesResource) -> None:
        self._ua_rules = ua_rules

        self.create = to_raw_response_wrapper(
            ua_rules.create,
        )
        self.update = to_raw_response_wrapper(
            ua_rules.update,
        )
        self.list = to_raw_response_wrapper(
            ua_rules.list,
        )
        self.delete = to_raw_response_wrapper(
            ua_rules.delete,
        )
        self.get = to_raw_response_wrapper(
            ua_rules.get,
        )


class AsyncUARulesResourceWithRawResponse:
    def __init__(self, ua_rules: AsyncUARulesResource) -> None:
        self._ua_rules = ua_rules

        self.create = async_to_raw_response_wrapper(
            ua_rules.create,
        )
        self.update = async_to_raw_response_wrapper(
            ua_rules.update,
        )
        self.list = async_to_raw_response_wrapper(
            ua_rules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            ua_rules.delete,
        )
        self.get = async_to_raw_response_wrapper(
            ua_rules.get,
        )


class UARulesResourceWithStreamingResponse:
    def __init__(self, ua_rules: UARulesResource) -> None:
        self._ua_rules = ua_rules

        self.create = to_streamed_response_wrapper(
            ua_rules.create,
        )
        self.update = to_streamed_response_wrapper(
            ua_rules.update,
        )
        self.list = to_streamed_response_wrapper(
            ua_rules.list,
        )
        self.delete = to_streamed_response_wrapper(
            ua_rules.delete,
        )
        self.get = to_streamed_response_wrapper(
            ua_rules.get,
        )


class AsyncUARulesResourceWithStreamingResponse:
    def __init__(self, ua_rules: AsyncUARulesResource) -> None:
        self._ua_rules = ua_rules

        self.create = async_to_streamed_response_wrapper(
            ua_rules.create,
        )
        self.update = async_to_streamed_response_wrapper(
            ua_rules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ua_rules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ua_rules.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            ua_rules.get,
        )
