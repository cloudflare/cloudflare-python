# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast

import httpx

from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ......types.zero_trust.access.applications import policy_test_get_params, policy_test_create_params
from ......types.zero_trust.access.applications.policy_test_get_response import PolicyTestGetResponse
from ......types.zero_trust.access.applications.policy_test_create_response import PolicyTestCreateResponse

__all__ = ["PolicyTestsResource", "AsyncPolicyTestsResource"]


class PolicyTestsResource(SyncAPIResource):
    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> PolicyTestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PolicyTestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PolicyTestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PolicyTestsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        policies: List[policy_test_create_params.Policy] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyTestCreateResponse]:
        """
        Starts an Access policy test.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/access/policy-tests",
            body=maybe_transform({"policies": policies}, policy_test_create_params.PolicyTestCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PolicyTestCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PolicyTestCreateResponse]], ResultWrapper[PolicyTestCreateResponse]),
        )

    def get(
        self,
        policy_test_id: str,
        *,
        account_id: str,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyTestGetResponse]:
        """
        Fetches the current status of a given Access policy test.

        Args:
          account_id: Identifier

          policy_test_id: The UUID of the policy test.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_test_id:
            raise ValueError(f"Expected a non-empty value for `policy_test_id` but received {policy_test_id!r}")
        return self._get(
            f"/accounts/{account_id}/access/policy-tests/{policy_test_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, policy_test_get_params.PolicyTestGetParams),
                post_parser=ResultWrapper[Optional[PolicyTestGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PolicyTestGetResponse]], ResultWrapper[PolicyTestGetResponse]),
        )


class AsyncPolicyTestsResource(AsyncAPIResource):
    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPolicyTestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPolicyTestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPolicyTestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPolicyTestsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        policies: List[policy_test_create_params.Policy] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyTestCreateResponse]:
        """
        Starts an Access policy test.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/access/policy-tests",
            body=await async_maybe_transform({"policies": policies}, policy_test_create_params.PolicyTestCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PolicyTestCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PolicyTestCreateResponse]], ResultWrapper[PolicyTestCreateResponse]),
        )

    async def get(
        self,
        policy_test_id: str,
        *,
        account_id: str,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PolicyTestGetResponse]:
        """
        Fetches the current status of a given Access policy test.

        Args:
          account_id: Identifier

          policy_test_id: The UUID of the policy test.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_test_id:
            raise ValueError(f"Expected a non-empty value for `policy_test_id` but received {policy_test_id!r}")
        return await self._get(
            f"/accounts/{account_id}/access/policy-tests/{policy_test_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"page": page}, policy_test_get_params.PolicyTestGetParams),
                post_parser=ResultWrapper[Optional[PolicyTestGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PolicyTestGetResponse]], ResultWrapper[PolicyTestGetResponse]),
        )


class PolicyTestsResourceWithRawResponse:
    def __init__(self, policy_tests: PolicyTestsResource) -> None:
        self._policy_tests = policy_tests

        self.create = to_raw_response_wrapper(
            policy_tests.create,
        )
        self.get = to_raw_response_wrapper(
            policy_tests.get,
        )

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._policy_tests.users)


class AsyncPolicyTestsResourceWithRawResponse:
    def __init__(self, policy_tests: AsyncPolicyTestsResource) -> None:
        self._policy_tests = policy_tests

        self.create = async_to_raw_response_wrapper(
            policy_tests.create,
        )
        self.get = async_to_raw_response_wrapper(
            policy_tests.get,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._policy_tests.users)


class PolicyTestsResourceWithStreamingResponse:
    def __init__(self, policy_tests: PolicyTestsResource) -> None:
        self._policy_tests = policy_tests

        self.create = to_streamed_response_wrapper(
            policy_tests.create,
        )
        self.get = to_streamed_response_wrapper(
            policy_tests.get,
        )

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._policy_tests.users)


class AsyncPolicyTestsResourceWithStreamingResponse:
    def __init__(self, policy_tests: AsyncPolicyTestsResource) -> None:
        self._policy_tests = policy_tests

        self.create = async_to_streamed_response_wrapper(
            policy_tests.create,
        )
        self.get = async_to_streamed_response_wrapper(
            policy_tests.get,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._policy_tests.users)
