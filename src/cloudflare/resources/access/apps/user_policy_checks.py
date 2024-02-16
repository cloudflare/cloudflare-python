# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Union, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.access.apps import UserPolicyCheckAccessApplicationsTestAccessPoliciesResponse

__all__ = ["UserPolicyChecks", "AsyncUserPolicyChecks"]


class UserPolicyChecks(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserPolicyChecksWithRawResponse:
        return UserPolicyChecksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserPolicyChecksWithStreamingResponse:
        return UserPolicyChecksWithStreamingResponse(self)

    def access_applications_test_access_policies(
        self,
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserPolicyCheckAccessApplicationsTestAccessPoliciesResponse:
        """
        Tests if a specific user has permission to access an application.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/user_policy_checks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[UserPolicyCheckAccessApplicationsTestAccessPoliciesResponse],
                ResultWrapper[UserPolicyCheckAccessApplicationsTestAccessPoliciesResponse],
            ),
        )


class AsyncUserPolicyChecks(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserPolicyChecksWithRawResponse:
        return AsyncUserPolicyChecksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserPolicyChecksWithStreamingResponse:
        return AsyncUserPolicyChecksWithStreamingResponse(self)

    async def access_applications_test_access_policies(
        self,
        app_id: Union[str, str],
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserPolicyCheckAccessApplicationsTestAccessPoliciesResponse:
        """
        Tests if a specific user has permission to access an application.

        Args:
          account_or_zone_id: Identifier

          app_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/user_policy_checks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[UserPolicyCheckAccessApplicationsTestAccessPoliciesResponse],
                ResultWrapper[UserPolicyCheckAccessApplicationsTestAccessPoliciesResponse],
            ),
        )


class UserPolicyChecksWithRawResponse:
    def __init__(self, user_policy_checks: UserPolicyChecks) -> None:
        self._user_policy_checks = user_policy_checks

        self.access_applications_test_access_policies = to_raw_response_wrapper(
            user_policy_checks.access_applications_test_access_policies,
        )


class AsyncUserPolicyChecksWithRawResponse:
    def __init__(self, user_policy_checks: AsyncUserPolicyChecks) -> None:
        self._user_policy_checks = user_policy_checks

        self.access_applications_test_access_policies = async_to_raw_response_wrapper(
            user_policy_checks.access_applications_test_access_policies,
        )


class UserPolicyChecksWithStreamingResponse:
    def __init__(self, user_policy_checks: UserPolicyChecks) -> None:
        self._user_policy_checks = user_policy_checks

        self.access_applications_test_access_policies = to_streamed_response_wrapper(
            user_policy_checks.access_applications_test_access_policies,
        )


class AsyncUserPolicyChecksWithStreamingResponse:
    def __init__(self, user_policy_checks: AsyncUserPolicyChecks) -> None:
        self._user_policy_checks = user_policy_checks

        self.access_applications_test_access_policies = async_to_streamed_response_wrapper(
            user_policy_checks.access_applications_test_access_policies,
        )
