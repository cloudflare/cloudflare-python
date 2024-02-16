# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.firewalls import (
    UaRuleUpdateResponse,
    UaRuleDeleteResponse,
    UaRuleGetResponse,
    UaRuleUserAgentBlockingRulesCreateAUserAgentBlockingRuleResponse,
    UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponse,
)

from typing import Optional, Type

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.firewalls import ua_rule_update_params
from ...types.firewalls import ua_rule_user_agent_blocking_rules_create_a_user_agent_blocking_rule_params
from ...types.firewalls import ua_rule_user_agent_blocking_rules_list_user_agent_blocking_rules_params
from ..._wrappers import ResultWrapper
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
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["UaRules", "AsyncUaRules"]


class UaRules(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UaRulesWithRawResponse:
        return UaRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UaRulesWithStreamingResponse:
        return UaRulesWithStreamingResponse(self)

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
    ) -> Optional[UaRuleUpdateResponse]:
        """
        Updates an existing User Agent Blocking rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the User Agent Blocking rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            Optional[UaRuleUpdateResponse],
            self._put(
                f"/zones/{zone_identifier}/firewall/ua_rules/{id}",
                body=maybe_transform(body, ua_rule_update_params.UaRuleUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UaRuleUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete(
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
    ) -> Optional[UaRuleDeleteResponse]:
        """
        Deletes an existing User Agent Blocking rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the User Agent Blocking rule.

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
            f"/zones/{zone_identifier}/firewall/ua_rules/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[UaRuleDeleteResponse]], ResultWrapper[UaRuleDeleteResponse]),
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
    ) -> Optional[UaRuleGetResponse]:
        """
        Fetches the details of a User Agent Blocking rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the User Agent Blocking rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            Optional[UaRuleGetResponse],
            self._get(
                f"/zones/{zone_identifier}/firewall/ua_rules/{id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UaRuleGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def user_agent_blocking_rules_create_a_user_agent_blocking_rule(
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
    ) -> Optional[UaRuleUserAgentBlockingRulesCreateAUserAgentBlockingRuleResponse]:
        """
        Creates a new User Agent Blocking rule in a zone.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return cast(
            Optional[UaRuleUserAgentBlockingRulesCreateAUserAgentBlockingRuleResponse],
            self._post(
                f"/zones/{zone_identifier}/firewall/ua_rules",
                body=maybe_transform(
                    body,
                    ua_rule_user_agent_blocking_rules_create_a_user_agent_blocking_rule_params.UaRuleUserAgentBlockingRulesCreateAUserAgentBlockingRuleParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UaRuleUserAgentBlockingRulesCreateAUserAgentBlockingRuleResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def user_agent_blocking_rules_list_user_agent_blocking_rules(
        self,
        zone_identifier: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        description_search: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        ua_search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponse]:
        """Fetches User Agent Blocking rules in a zone.

        You can filter the results using
        several optional parameters.

        Args:
          zone_identifier: Identifier

          description: A string to search for in the description of existing rules.

          description_search: A string to search for in the description of existing rules.

          page: Page number of paginated results.

          per_page: The maximum number of results per page. You can only set the value to `1` or to
              a multiple of 5 such as `5`, `10`, `15`, or `20`.

          ua_search: A string to search for in the user agent values of existing rules.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/firewall/ua_rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "description": description,
                        "description_search": description_search,
                        "page": page,
                        "per_page": per_page,
                        "ua_search": ua_search,
                    },
                    ua_rule_user_agent_blocking_rules_list_user_agent_blocking_rules_params.UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponse]],
                ResultWrapper[UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponse],
            ),
        )


class AsyncUaRules(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUaRulesWithRawResponse:
        return AsyncUaRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUaRulesWithStreamingResponse:
        return AsyncUaRulesWithStreamingResponse(self)

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
    ) -> Optional[UaRuleUpdateResponse]:
        """
        Updates an existing User Agent Blocking rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the User Agent Blocking rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            Optional[UaRuleUpdateResponse],
            await self._put(
                f"/zones/{zone_identifier}/firewall/ua_rules/{id}",
                body=maybe_transform(body, ua_rule_update_params.UaRuleUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UaRuleUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete(
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
    ) -> Optional[UaRuleDeleteResponse]:
        """
        Deletes an existing User Agent Blocking rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the User Agent Blocking rule.

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
            f"/zones/{zone_identifier}/firewall/ua_rules/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[UaRuleDeleteResponse]], ResultWrapper[UaRuleDeleteResponse]),
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
    ) -> Optional[UaRuleGetResponse]:
        """
        Fetches the details of a User Agent Blocking rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the User Agent Blocking rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            Optional[UaRuleGetResponse],
            await self._get(
                f"/zones/{zone_identifier}/firewall/ua_rules/{id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UaRuleGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def user_agent_blocking_rules_create_a_user_agent_blocking_rule(
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
    ) -> Optional[UaRuleUserAgentBlockingRulesCreateAUserAgentBlockingRuleResponse]:
        """
        Creates a new User Agent Blocking rule in a zone.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return cast(
            Optional[UaRuleUserAgentBlockingRulesCreateAUserAgentBlockingRuleResponse],
            await self._post(
                f"/zones/{zone_identifier}/firewall/ua_rules",
                body=maybe_transform(
                    body,
                    ua_rule_user_agent_blocking_rules_create_a_user_agent_blocking_rule_params.UaRuleUserAgentBlockingRulesCreateAUserAgentBlockingRuleParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UaRuleUserAgentBlockingRulesCreateAUserAgentBlockingRuleResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def user_agent_blocking_rules_list_user_agent_blocking_rules(
        self,
        zone_identifier: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        description_search: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        ua_search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponse]:
        """Fetches User Agent Blocking rules in a zone.

        You can filter the results using
        several optional parameters.

        Args:
          zone_identifier: Identifier

          description: A string to search for in the description of existing rules.

          description_search: A string to search for in the description of existing rules.

          page: Page number of paginated results.

          per_page: The maximum number of results per page. You can only set the value to `1` or to
              a multiple of 5 such as `5`, `10`, `15`, or `20`.

          ua_search: A string to search for in the user agent values of existing rules.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/firewall/ua_rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "description": description,
                        "description_search": description_search,
                        "page": page,
                        "per_page": per_page,
                        "ua_search": ua_search,
                    },
                    ua_rule_user_agent_blocking_rules_list_user_agent_blocking_rules_params.UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponse]],
                ResultWrapper[UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponse],
            ),
        )


class UaRulesWithRawResponse:
    def __init__(self, ua_rules: UaRules) -> None:
        self._ua_rules = ua_rules

        self.update = to_raw_response_wrapper(
            ua_rules.update,
        )
        self.delete = to_raw_response_wrapper(
            ua_rules.delete,
        )
        self.get = to_raw_response_wrapper(
            ua_rules.get,
        )
        self.user_agent_blocking_rules_create_a_user_agent_blocking_rule = to_raw_response_wrapper(
            ua_rules.user_agent_blocking_rules_create_a_user_agent_blocking_rule,
        )
        self.user_agent_blocking_rules_list_user_agent_blocking_rules = to_raw_response_wrapper(
            ua_rules.user_agent_blocking_rules_list_user_agent_blocking_rules,
        )


class AsyncUaRulesWithRawResponse:
    def __init__(self, ua_rules: AsyncUaRules) -> None:
        self._ua_rules = ua_rules

        self.update = async_to_raw_response_wrapper(
            ua_rules.update,
        )
        self.delete = async_to_raw_response_wrapper(
            ua_rules.delete,
        )
        self.get = async_to_raw_response_wrapper(
            ua_rules.get,
        )
        self.user_agent_blocking_rules_create_a_user_agent_blocking_rule = async_to_raw_response_wrapper(
            ua_rules.user_agent_blocking_rules_create_a_user_agent_blocking_rule,
        )
        self.user_agent_blocking_rules_list_user_agent_blocking_rules = async_to_raw_response_wrapper(
            ua_rules.user_agent_blocking_rules_list_user_agent_blocking_rules,
        )


class UaRulesWithStreamingResponse:
    def __init__(self, ua_rules: UaRules) -> None:
        self._ua_rules = ua_rules

        self.update = to_streamed_response_wrapper(
            ua_rules.update,
        )
        self.delete = to_streamed_response_wrapper(
            ua_rules.delete,
        )
        self.get = to_streamed_response_wrapper(
            ua_rules.get,
        )
        self.user_agent_blocking_rules_create_a_user_agent_blocking_rule = to_streamed_response_wrapper(
            ua_rules.user_agent_blocking_rules_create_a_user_agent_blocking_rule,
        )
        self.user_agent_blocking_rules_list_user_agent_blocking_rules = to_streamed_response_wrapper(
            ua_rules.user_agent_blocking_rules_list_user_agent_blocking_rules,
        )


class AsyncUaRulesWithStreamingResponse:
    def __init__(self, ua_rules: AsyncUaRules) -> None:
        self._ua_rules = ua_rules

        self.update = async_to_streamed_response_wrapper(
            ua_rules.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            ua_rules.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            ua_rules.get,
        )
        self.user_agent_blocking_rules_create_a_user_agent_blocking_rule = async_to_streamed_response_wrapper(
            ua_rules.user_agent_blocking_rules_create_a_user_agent_blocking_rule,
        )
        self.user_agent_blocking_rules_list_user_agent_blocking_rules = async_to_streamed_response_wrapper(
            ua_rules.user_agent_blocking_rules_list_user_agent_blocking_rules,
        )
