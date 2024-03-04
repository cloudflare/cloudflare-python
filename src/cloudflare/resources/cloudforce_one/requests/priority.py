# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, List, Type, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.cloudforce_one.requests import (
    PriorityGetResponse,
    PriorityQuotaResponse,
    PriorityCreateResponse,
    PriorityDeleteResponse,
    PriorityUpdateResponse,
    PriorityDoSomethingUnknownResponse,
    priority_create_params,
    priority_update_params,
    priority_do_something_unknown_params,
)

__all__ = ["Priority", "AsyncPriority"]


class Priority(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PriorityWithRawResponse:
        return PriorityWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PriorityWithStreamingResponse:
        return PriorityWithStreamingResponse(self)

    def create(
        self,
        account_identifier: str,
        *,
        labels: List[str],
        priority: int,
        requirement: str,
        tlp: Literal["clear", "amber", "amber-strict", "green", "red"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriorityCreateResponse:
        """
        Create a New Priority Requirement

        Args:
          account_identifier: Identifier

          labels: List of labels

          priority: Priority

          requirement: Requirement

          tlp: The CISA defined Traffic Light Protocol (TLP)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._post(
            f"/accounts/{account_identifier}/cloudforce-one/requests/priority/new",
            body=maybe_transform(
                {
                    "labels": labels,
                    "priority": priority,
                    "requirement": requirement,
                    "tlp": tlp,
                },
                priority_create_params.PriorityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PriorityCreateResponse], ResultWrapper[PriorityCreateResponse]),
        )

    def update(
        self,
        priority_identifer: str,
        *,
        account_identifier: str,
        labels: List[str],
        priority: int,
        requirement: str,
        tlp: Literal["clear", "amber", "amber-strict", "green", "red"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriorityUpdateResponse:
        """
        Update a Priority Intelligence Requirement

        Args:
          account_identifier: Identifier

          priority_identifer: UUID

          labels: List of labels

          priority: Priority

          requirement: Requirement

          tlp: The CISA defined Traffic Light Protocol (TLP)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not priority_identifer:
            raise ValueError(f"Expected a non-empty value for `priority_identifer` but received {priority_identifer!r}")
        return self._put(
            f"/accounts/{account_identifier}/cloudforce-one/requests/priority/{priority_identifer}",
            body=maybe_transform(
                {
                    "labels": labels,
                    "priority": priority,
                    "requirement": requirement,
                    "tlp": tlp,
                },
                priority_update_params.PriorityUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PriorityUpdateResponse], ResultWrapper[PriorityUpdateResponse]),
        )

    def delete(
        self,
        priority_identifer: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriorityDeleteResponse:
        """
        Delete a Priority Intelligence Report

        Args:
          account_identifier: Identifier

          priority_identifer: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not priority_identifer:
            raise ValueError(f"Expected a non-empty value for `priority_identifer` but received {priority_identifer!r}")
        return cast(
            PriorityDeleteResponse,
            self._delete(
                f"/accounts/{account_identifier}/cloudforce-one/requests/priority/{priority_identifer}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PriorityDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def do_something_unknown(
        self,
        account_identifier: str,
        *,
        page: int,
        per_page: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriorityDoSomethingUnknownResponse:
        """
        List Priority Intelligence Requirements

        Args:
          account_identifier: Identifier

          page: Page number of results

          per_page: Number of results per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._post(
            f"/accounts/{account_identifier}/cloudforce-one/requests/priority",
            body=maybe_transform(
                {
                    "page": page,
                    "per_page": per_page,
                },
                priority_do_something_unknown_params.PriorityDoSomethingUnknownParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PriorityDoSomethingUnknownResponse], ResultWrapper[PriorityDoSomethingUnknownResponse]),
        )

    def get(
        self,
        priority_identifer: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriorityGetResponse:
        """
        Get a Priority Intelligence Requirement

        Args:
          account_identifier: Identifier

          priority_identifer: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not priority_identifer:
            raise ValueError(f"Expected a non-empty value for `priority_identifer` but received {priority_identifer!r}")
        return self._get(
            f"/accounts/{account_identifier}/cloudforce-one/requests/priority/{priority_identifer}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PriorityGetResponse], ResultWrapper[PriorityGetResponse]),
        )

    def quota(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriorityQuotaResponse:
        """
        Get Priority Intelligence Requirement Quota

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/cloudforce-one/requests/priority/quota",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PriorityQuotaResponse], ResultWrapper[PriorityQuotaResponse]),
        )


class AsyncPriority(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPriorityWithRawResponse:
        return AsyncPriorityWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPriorityWithStreamingResponse:
        return AsyncPriorityWithStreamingResponse(self)

    async def create(
        self,
        account_identifier: str,
        *,
        labels: List[str],
        priority: int,
        requirement: str,
        tlp: Literal["clear", "amber", "amber-strict", "green", "red"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriorityCreateResponse:
        """
        Create a New Priority Requirement

        Args:
          account_identifier: Identifier

          labels: List of labels

          priority: Priority

          requirement: Requirement

          tlp: The CISA defined Traffic Light Protocol (TLP)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._post(
            f"/accounts/{account_identifier}/cloudforce-one/requests/priority/new",
            body=await async_maybe_transform(
                {
                    "labels": labels,
                    "priority": priority,
                    "requirement": requirement,
                    "tlp": tlp,
                },
                priority_create_params.PriorityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PriorityCreateResponse], ResultWrapper[PriorityCreateResponse]),
        )

    async def update(
        self,
        priority_identifer: str,
        *,
        account_identifier: str,
        labels: List[str],
        priority: int,
        requirement: str,
        tlp: Literal["clear", "amber", "amber-strict", "green", "red"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriorityUpdateResponse:
        """
        Update a Priority Intelligence Requirement

        Args:
          account_identifier: Identifier

          priority_identifer: UUID

          labels: List of labels

          priority: Priority

          requirement: Requirement

          tlp: The CISA defined Traffic Light Protocol (TLP)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not priority_identifer:
            raise ValueError(f"Expected a non-empty value for `priority_identifer` but received {priority_identifer!r}")
        return await self._put(
            f"/accounts/{account_identifier}/cloudforce-one/requests/priority/{priority_identifer}",
            body=await async_maybe_transform(
                {
                    "labels": labels,
                    "priority": priority,
                    "requirement": requirement,
                    "tlp": tlp,
                },
                priority_update_params.PriorityUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PriorityUpdateResponse], ResultWrapper[PriorityUpdateResponse]),
        )

    async def delete(
        self,
        priority_identifer: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriorityDeleteResponse:
        """
        Delete a Priority Intelligence Report

        Args:
          account_identifier: Identifier

          priority_identifer: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not priority_identifer:
            raise ValueError(f"Expected a non-empty value for `priority_identifer` but received {priority_identifer!r}")
        return cast(
            PriorityDeleteResponse,
            await self._delete(
                f"/accounts/{account_identifier}/cloudforce-one/requests/priority/{priority_identifer}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PriorityDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def do_something_unknown(
        self,
        account_identifier: str,
        *,
        page: int,
        per_page: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriorityDoSomethingUnknownResponse:
        """
        List Priority Intelligence Requirements

        Args:
          account_identifier: Identifier

          page: Page number of results

          per_page: Number of results per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._post(
            f"/accounts/{account_identifier}/cloudforce-one/requests/priority",
            body=await async_maybe_transform(
                {
                    "page": page,
                    "per_page": per_page,
                },
                priority_do_something_unknown_params.PriorityDoSomethingUnknownParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PriorityDoSomethingUnknownResponse], ResultWrapper[PriorityDoSomethingUnknownResponse]),
        )

    async def get(
        self,
        priority_identifer: str,
        *,
        account_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriorityGetResponse:
        """
        Get a Priority Intelligence Requirement

        Args:
          account_identifier: Identifier

          priority_identifer: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        if not priority_identifer:
            raise ValueError(f"Expected a non-empty value for `priority_identifer` but received {priority_identifer!r}")
        return await self._get(
            f"/accounts/{account_identifier}/cloudforce-one/requests/priority/{priority_identifer}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PriorityGetResponse], ResultWrapper[PriorityGetResponse]),
        )

    async def quota(
        self,
        account_identifier: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PriorityQuotaResponse:
        """
        Get Priority Intelligence Requirement Quota

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/cloudforce-one/requests/priority/quota",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[PriorityQuotaResponse], ResultWrapper[PriorityQuotaResponse]),
        )


class PriorityWithRawResponse:
    def __init__(self, priority: Priority) -> None:
        self._priority = priority

        self.create = to_raw_response_wrapper(
            priority.create,
        )
        self.update = to_raw_response_wrapper(
            priority.update,
        )
        self.delete = to_raw_response_wrapper(
            priority.delete,
        )
        self.do_something_unknown = to_raw_response_wrapper(
            priority.do_something_unknown,
        )
        self.get = to_raw_response_wrapper(
            priority.get,
        )
        self.quota = to_raw_response_wrapper(
            priority.quota,
        )


class AsyncPriorityWithRawResponse:
    def __init__(self, priority: AsyncPriority) -> None:
        self._priority = priority

        self.create = async_to_raw_response_wrapper(
            priority.create,
        )
        self.update = async_to_raw_response_wrapper(
            priority.update,
        )
        self.delete = async_to_raw_response_wrapper(
            priority.delete,
        )
        self.do_something_unknown = async_to_raw_response_wrapper(
            priority.do_something_unknown,
        )
        self.get = async_to_raw_response_wrapper(
            priority.get,
        )
        self.quota = async_to_raw_response_wrapper(
            priority.quota,
        )


class PriorityWithStreamingResponse:
    def __init__(self, priority: Priority) -> None:
        self._priority = priority

        self.create = to_streamed_response_wrapper(
            priority.create,
        )
        self.update = to_streamed_response_wrapper(
            priority.update,
        )
        self.delete = to_streamed_response_wrapper(
            priority.delete,
        )
        self.do_something_unknown = to_streamed_response_wrapper(
            priority.do_something_unknown,
        )
        self.get = to_streamed_response_wrapper(
            priority.get,
        )
        self.quota = to_streamed_response_wrapper(
            priority.quota,
        )


class AsyncPriorityWithStreamingResponse:
    def __init__(self, priority: AsyncPriority) -> None:
        self._priority = priority

        self.create = async_to_streamed_response_wrapper(
            priority.create,
        )
        self.update = async_to_streamed_response_wrapper(
            priority.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            priority.delete,
        )
        self.do_something_unknown = async_to_streamed_response_wrapper(
            priority.do_something_unknown,
        )
        self.get = async_to_streamed_response_wrapper(
            priority.get,
        )
        self.quota = async_to_streamed_response_wrapper(
            priority.quota,
        )
