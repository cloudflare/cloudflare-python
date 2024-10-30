# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast
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
from ...._base_client import make_request_options
from ....types.cloudforce_one.requests import priority_create_params, priority_update_params
from ....types.cloudforce_one.requests.priority_get_response import PriorityGetResponse
from ....types.cloudforce_one.requests.priority_quota_response import PriorityQuotaResponse
from ....types.cloudforce_one.requests.priority_create_response import PriorityCreateResponse
from ....types.cloudforce_one.requests.priority_delete_response import PriorityDeleteResponse
from ....types.cloudforce_one.requests.priority_update_response import PriorityUpdateResponse

__all__ = ["PriorityResource", "AsyncPriorityResource"]


class PriorityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PriorityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PriorityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PriorityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PriorityResourceWithStreamingResponse(self)

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
    ) -> Optional[PriorityCreateResponse]:
        """
        Create a New Priority Intelligence Requirement

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
                post_parser=ResultWrapper[Optional[PriorityCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PriorityCreateResponse]], ResultWrapper[PriorityCreateResponse]),
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
    ) -> Optional[PriorityUpdateResponse]:
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
                post_parser=ResultWrapper[Optional[PriorityUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PriorityUpdateResponse]], ResultWrapper[PriorityUpdateResponse]),
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
        Delete a Priority Intelligence Requirement

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
        return self._delete(
            f"/accounts/{account_identifier}/cloudforce-one/requests/priority/{priority_identifer}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PriorityDeleteResponse,
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
    ) -> Optional[PriorityGetResponse]:
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
                post_parser=ResultWrapper[Optional[PriorityGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PriorityGetResponse]], ResultWrapper[PriorityGetResponse]),
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
    ) -> Optional[PriorityQuotaResponse]:
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
                post_parser=ResultWrapper[Optional[PriorityQuotaResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PriorityQuotaResponse]], ResultWrapper[PriorityQuotaResponse]),
        )


class AsyncPriorityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPriorityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPriorityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPriorityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPriorityResourceWithStreamingResponse(self)

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
    ) -> Optional[PriorityCreateResponse]:
        """
        Create a New Priority Intelligence Requirement

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
                post_parser=ResultWrapper[Optional[PriorityCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PriorityCreateResponse]], ResultWrapper[PriorityCreateResponse]),
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
    ) -> Optional[PriorityUpdateResponse]:
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
                post_parser=ResultWrapper[Optional[PriorityUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PriorityUpdateResponse]], ResultWrapper[PriorityUpdateResponse]),
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
        Delete a Priority Intelligence Requirement

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
        return await self._delete(
            f"/accounts/{account_identifier}/cloudforce-one/requests/priority/{priority_identifer}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PriorityDeleteResponse,
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
    ) -> Optional[PriorityGetResponse]:
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
                post_parser=ResultWrapper[Optional[PriorityGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PriorityGetResponse]], ResultWrapper[PriorityGetResponse]),
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
    ) -> Optional[PriorityQuotaResponse]:
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
                post_parser=ResultWrapper[Optional[PriorityQuotaResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PriorityQuotaResponse]], ResultWrapper[PriorityQuotaResponse]),
        )


class PriorityResourceWithRawResponse:
    def __init__(self, priority: PriorityResource) -> None:
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
        self.get = to_raw_response_wrapper(
            priority.get,
        )
        self.quota = to_raw_response_wrapper(
            priority.quota,
        )


class AsyncPriorityResourceWithRawResponse:
    def __init__(self, priority: AsyncPriorityResource) -> None:
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
        self.get = async_to_raw_response_wrapper(
            priority.get,
        )
        self.quota = async_to_raw_response_wrapper(
            priority.quota,
        )


class PriorityResourceWithStreamingResponse:
    def __init__(self, priority: PriorityResource) -> None:
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
        self.get = to_streamed_response_wrapper(
            priority.get,
        )
        self.quota = to_streamed_response_wrapper(
            priority.quota,
        )


class AsyncPriorityResourceWithStreamingResponse:
    def __init__(self, priority: AsyncPriorityResource) -> None:
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
        self.get = async_to_streamed_response_wrapper(
            priority.get,
        )
        self.quota = async_to_streamed_response_wrapper(
            priority.quota,
        )
