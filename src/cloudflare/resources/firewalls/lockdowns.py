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
    LockdownGetResponse,
    LockdownDeleteResponse,
    LockdownUpdateResponse,
    LockdownZoneLockdownListZoneLockdownRulesResponse,
    LockdownZoneLockdownCreateAZoneLockdownRuleResponse,
    lockdown_update_params,
    lockdown_zone_lockdown_list_zone_lockdown_rules_params,
    lockdown_zone_lockdown_create_a_zone_lockdown_rule_params,
)

__all__ = ["Lockdowns", "AsyncLockdowns"]


class Lockdowns(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LockdownsWithRawResponse:
        return LockdownsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LockdownsWithStreamingResponse:
        return LockdownsWithStreamingResponse(self)

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
    ) -> Optional[LockdownUpdateResponse]:
        """
        Updates an existing Zone Lockdown rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the Zone Lockdown rule.

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
            f"/zones/{zone_identifier}/firewall/lockdowns/{id}",
            body=maybe_transform(body, lockdown_update_params.LockdownUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[LockdownUpdateResponse]], ResultWrapper[LockdownUpdateResponse]),
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
    ) -> Optional[LockdownDeleteResponse]:
        """
        Deletes an existing Zone Lockdown rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the Zone Lockdown rule.

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
            f"/zones/{zone_identifier}/firewall/lockdowns/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[LockdownDeleteResponse]], ResultWrapper[LockdownDeleteResponse]),
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
    ) -> Optional[LockdownGetResponse]:
        """
        Fetches the details of a Zone Lockdown rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the Zone Lockdown rule.

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
            f"/zones/{zone_identifier}/firewall/lockdowns/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[LockdownGetResponse]], ResultWrapper[LockdownGetResponse]),
        )

    def zone_lockdown_create_a_zone_lockdown_rule(
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
    ) -> Optional[LockdownZoneLockdownCreateAZoneLockdownRuleResponse]:
        """
        Creates a new Zone Lockdown rule.

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
            f"/zones/{zone_identifier}/firewall/lockdowns",
            body=maybe_transform(
                body,
                lockdown_zone_lockdown_create_a_zone_lockdown_rule_params.LockdownZoneLockdownCreateAZoneLockdownRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[LockdownZoneLockdownCreateAZoneLockdownRuleResponse]],
                ResultWrapper[LockdownZoneLockdownCreateAZoneLockdownRuleResponse],
            ),
        )

    def zone_lockdown_list_zone_lockdown_rules(
        self,
        zone_identifier: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        description_search: str | NotGiven = NOT_GIVEN,
        ip: str | NotGiven = NOT_GIVEN,
        ip_range_search: str | NotGiven = NOT_GIVEN,
        ip_search: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        uri_search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LockdownZoneLockdownListZoneLockdownRulesResponse]:
        """Fetches Zone Lockdown rules.

        You can filter the results using several optional
        parameters.

        Args:
          zone_identifier: Identifier

          description: A string to search for in the description of existing rules.

          description_search: A string to search for in the description of existing rules.

          ip: A single IP address to search for in existing rules.

          ip_range_search: A single IP address range to search for in existing rules.

          ip_search: A single IP address to search for in existing rules.

          page: Page number of paginated results.

          per_page: The maximum number of results per page. You can only set the value to `1` or to
              a multiple of 5 such as `5`, `10`, `15`, or `20`.

          priority: The priority of the rule to control the processing order. A lower number
              indicates higher priority. If not provided, any rules with a configured priority
              will be processed before rules without a priority.

          uri_search: A single URI to search for in the list of URLs of existing rules.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/firewall/lockdowns",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "description": description,
                        "description_search": description_search,
                        "ip": ip,
                        "ip_range_search": ip_range_search,
                        "ip_search": ip_search,
                        "page": page,
                        "per_page": per_page,
                        "priority": priority,
                        "uri_search": uri_search,
                    },
                    lockdown_zone_lockdown_list_zone_lockdown_rules_params.LockdownZoneLockdownListZoneLockdownRulesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[LockdownZoneLockdownListZoneLockdownRulesResponse]],
                ResultWrapper[LockdownZoneLockdownListZoneLockdownRulesResponse],
            ),
        )


class AsyncLockdowns(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLockdownsWithRawResponse:
        return AsyncLockdownsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLockdownsWithStreamingResponse:
        return AsyncLockdownsWithStreamingResponse(self)

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
    ) -> Optional[LockdownUpdateResponse]:
        """
        Updates an existing Zone Lockdown rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the Zone Lockdown rule.

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
            f"/zones/{zone_identifier}/firewall/lockdowns/{id}",
            body=maybe_transform(body, lockdown_update_params.LockdownUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[LockdownUpdateResponse]], ResultWrapper[LockdownUpdateResponse]),
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
    ) -> Optional[LockdownDeleteResponse]:
        """
        Deletes an existing Zone Lockdown rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the Zone Lockdown rule.

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
            f"/zones/{zone_identifier}/firewall/lockdowns/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[LockdownDeleteResponse]], ResultWrapper[LockdownDeleteResponse]),
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
    ) -> Optional[LockdownGetResponse]:
        """
        Fetches the details of a Zone Lockdown rule.

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the Zone Lockdown rule.

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
            f"/zones/{zone_identifier}/firewall/lockdowns/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[LockdownGetResponse]], ResultWrapper[LockdownGetResponse]),
        )

    async def zone_lockdown_create_a_zone_lockdown_rule(
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
    ) -> Optional[LockdownZoneLockdownCreateAZoneLockdownRuleResponse]:
        """
        Creates a new Zone Lockdown rule.

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
            f"/zones/{zone_identifier}/firewall/lockdowns",
            body=maybe_transform(
                body,
                lockdown_zone_lockdown_create_a_zone_lockdown_rule_params.LockdownZoneLockdownCreateAZoneLockdownRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[LockdownZoneLockdownCreateAZoneLockdownRuleResponse]],
                ResultWrapper[LockdownZoneLockdownCreateAZoneLockdownRuleResponse],
            ),
        )

    async def zone_lockdown_list_zone_lockdown_rules(
        self,
        zone_identifier: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        description_search: str | NotGiven = NOT_GIVEN,
        ip: str | NotGiven = NOT_GIVEN,
        ip_range_search: str | NotGiven = NOT_GIVEN,
        ip_search: str | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        priority: float | NotGiven = NOT_GIVEN,
        uri_search: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[LockdownZoneLockdownListZoneLockdownRulesResponse]:
        """Fetches Zone Lockdown rules.

        You can filter the results using several optional
        parameters.

        Args:
          zone_identifier: Identifier

          description: A string to search for in the description of existing rules.

          description_search: A string to search for in the description of existing rules.

          ip: A single IP address to search for in existing rules.

          ip_range_search: A single IP address range to search for in existing rules.

          ip_search: A single IP address to search for in existing rules.

          page: Page number of paginated results.

          per_page: The maximum number of results per page. You can only set the value to `1` or to
              a multiple of 5 such as `5`, `10`, `15`, or `20`.

          priority: The priority of the rule to control the processing order. A lower number
              indicates higher priority. If not provided, any rules with a configured priority
              will be processed before rules without a priority.

          uri_search: A single URI to search for in the list of URLs of existing rules.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/firewall/lockdowns",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "description": description,
                        "description_search": description_search,
                        "ip": ip,
                        "ip_range_search": ip_range_search,
                        "ip_search": ip_search,
                        "page": page,
                        "per_page": per_page,
                        "priority": priority,
                        "uri_search": uri_search,
                    },
                    lockdown_zone_lockdown_list_zone_lockdown_rules_params.LockdownZoneLockdownListZoneLockdownRulesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[LockdownZoneLockdownListZoneLockdownRulesResponse]],
                ResultWrapper[LockdownZoneLockdownListZoneLockdownRulesResponse],
            ),
        )


class LockdownsWithRawResponse:
    def __init__(self, lockdowns: Lockdowns) -> None:
        self._lockdowns = lockdowns

        self.update = to_raw_response_wrapper(
            lockdowns.update,
        )
        self.delete = to_raw_response_wrapper(
            lockdowns.delete,
        )
        self.get = to_raw_response_wrapper(
            lockdowns.get,
        )
        self.zone_lockdown_create_a_zone_lockdown_rule = to_raw_response_wrapper(
            lockdowns.zone_lockdown_create_a_zone_lockdown_rule,
        )
        self.zone_lockdown_list_zone_lockdown_rules = to_raw_response_wrapper(
            lockdowns.zone_lockdown_list_zone_lockdown_rules,
        )


class AsyncLockdownsWithRawResponse:
    def __init__(self, lockdowns: AsyncLockdowns) -> None:
        self._lockdowns = lockdowns

        self.update = async_to_raw_response_wrapper(
            lockdowns.update,
        )
        self.delete = async_to_raw_response_wrapper(
            lockdowns.delete,
        )
        self.get = async_to_raw_response_wrapper(
            lockdowns.get,
        )
        self.zone_lockdown_create_a_zone_lockdown_rule = async_to_raw_response_wrapper(
            lockdowns.zone_lockdown_create_a_zone_lockdown_rule,
        )
        self.zone_lockdown_list_zone_lockdown_rules = async_to_raw_response_wrapper(
            lockdowns.zone_lockdown_list_zone_lockdown_rules,
        )


class LockdownsWithStreamingResponse:
    def __init__(self, lockdowns: Lockdowns) -> None:
        self._lockdowns = lockdowns

        self.update = to_streamed_response_wrapper(
            lockdowns.update,
        )
        self.delete = to_streamed_response_wrapper(
            lockdowns.delete,
        )
        self.get = to_streamed_response_wrapper(
            lockdowns.get,
        )
        self.zone_lockdown_create_a_zone_lockdown_rule = to_streamed_response_wrapper(
            lockdowns.zone_lockdown_create_a_zone_lockdown_rule,
        )
        self.zone_lockdown_list_zone_lockdown_rules = to_streamed_response_wrapper(
            lockdowns.zone_lockdown_list_zone_lockdown_rules,
        )


class AsyncLockdownsWithStreamingResponse:
    def __init__(self, lockdowns: AsyncLockdowns) -> None:
        self._lockdowns = lockdowns

        self.update = async_to_streamed_response_wrapper(
            lockdowns.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            lockdowns.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            lockdowns.get,
        )
        self.zone_lockdown_create_a_zone_lockdown_rule = async_to_streamed_response_wrapper(
            lockdowns.zone_lockdown_create_a_zone_lockdown_rule,
        )
        self.zone_lockdown_list_zone_lockdown_rules = async_to_streamed_response_wrapper(
            lockdowns.zone_lockdown_list_zone_lockdown_rules,
        )
