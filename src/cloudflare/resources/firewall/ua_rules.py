# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Optional, cast

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
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ...types.firewall import (
    UARuleGetResponse,
    UARuleListResponse,
    UARuleCreateResponse,
    UARuleDeleteResponse,
    UARuleUpdateResponse,
    ua_rule_list_params,
    ua_rule_create_params,
    ua_rule_update_params,
)

__all__ = ["UARules", "AsyncUARules"]


class UARules(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UARulesWithRawResponse:
        return UARulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UARulesWithStreamingResponse:
        return UARulesWithStreamingResponse(self)

    def create(
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
    ) -> Optional[UARuleCreateResponse]:
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
            Optional[UARuleCreateResponse],
            self._post(
                f"/zones/{zone_identifier}/firewall/ua_rules",
                body=maybe_transform(body, ua_rule_create_params.UARuleCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UARuleCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

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
    ) -> Optional[UARuleUpdateResponse]:
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
            Optional[UARuleUpdateResponse],
            self._put(
                f"/zones/{zone_identifier}/firewall/ua_rules/{id}",
                body=maybe_transform(body, ua_rule_update_params.UARuleUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UARuleUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
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
    ) -> SyncV4PagePaginationArray[UARuleListResponse]:
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
        return self._get_api_list(
            f"/zones/{zone_identifier}/firewall/ua_rules",
            page=SyncV4PagePaginationArray[UARuleListResponse],
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
                    ua_rule_list_params.UARuleListParams,
                ),
            ),
            model=UARuleListResponse,
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
    ) -> Optional[UARuleDeleteResponse]:
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
            cast_to=cast(Type[Optional[UARuleDeleteResponse]], ResultWrapper[UARuleDeleteResponse]),
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
    ) -> Optional[UARuleGetResponse]:
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
            Optional[UARuleGetResponse],
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
                    Any, ResultWrapper[UARuleGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncUARules(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUARulesWithRawResponse:
        return AsyncUARulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUARulesWithStreamingResponse:
        return AsyncUARulesWithStreamingResponse(self)

    async def create(
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
    ) -> Optional[UARuleCreateResponse]:
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
            Optional[UARuleCreateResponse],
            await self._post(
                f"/zones/{zone_identifier}/firewall/ua_rules",
                body=await async_maybe_transform(body, ua_rule_create_params.UARuleCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UARuleCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

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
    ) -> Optional[UARuleUpdateResponse]:
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
            Optional[UARuleUpdateResponse],
            await self._put(
                f"/zones/{zone_identifier}/firewall/ua_rules/{id}",
                body=await async_maybe_transform(body, ua_rule_update_params.UARuleUpdateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[UARuleUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
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
    ) -> AsyncPaginator[UARuleListResponse, AsyncV4PagePaginationArray[UARuleListResponse]]:
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
        return self._get_api_list(
            f"/zones/{zone_identifier}/firewall/ua_rules",
            page=AsyncV4PagePaginationArray[UARuleListResponse],
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
                    ua_rule_list_params.UARuleListParams,
                ),
            ),
            model=UARuleListResponse,
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
    ) -> Optional[UARuleDeleteResponse]:
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
            cast_to=cast(Type[Optional[UARuleDeleteResponse]], ResultWrapper[UARuleDeleteResponse]),
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
    ) -> Optional[UARuleGetResponse]:
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
            Optional[UARuleGetResponse],
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
                    Any, ResultWrapper[UARuleGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class UARulesWithRawResponse:
    def __init__(self, ua_rules: UARules) -> None:
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


class AsyncUARulesWithRawResponse:
    def __init__(self, ua_rules: AsyncUARules) -> None:
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


class UARulesWithStreamingResponse:
    def __init__(self, ua_rules: UARules) -> None:
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


class AsyncUARulesWithStreamingResponse:
    def __init__(self, ua_rules: AsyncUARules) -> None:
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
