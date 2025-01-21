# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import make_request_options
from .....types.zero_trust.access import AppID
from .....types.zero_trust.access.app_id import AppID
from .....types.zero_trust.access.applications.user_policy_check_list_response import UserPolicyCheckListResponse

__all__ = ["UserPolicyChecksResource", "AsyncUserPolicyChecksResource"]


class UserPolicyChecksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserPolicyChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return UserPolicyChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserPolicyChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return UserPolicyChecksResourceWithStreamingResponse(self)

    def list(
        self,
        app_id: AppID,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UserPolicyCheckListResponse]:
        """
        Tests if a specific user has permission to access an application.

        Args:
          app_id: Identifier

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/user_policy_checks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserPolicyCheckListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserPolicyCheckListResponse]], ResultWrapper[UserPolicyCheckListResponse]),
        )


class AsyncUserPolicyChecksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserPolicyChecksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserPolicyChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserPolicyChecksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncUserPolicyChecksResourceWithStreamingResponse(self)

    async def list(
        self,
        app_id: AppID,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[UserPolicyCheckListResponse]:
        """
        Tests if a specific user has permission to access an application.

        Args:
          app_id: Identifier

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/user_policy_checks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserPolicyCheckListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserPolicyCheckListResponse]], ResultWrapper[UserPolicyCheckListResponse]),
        )


class UserPolicyChecksResourceWithRawResponse:
    def __init__(self, user_policy_checks: UserPolicyChecksResource) -> None:
        self._user_policy_checks = user_policy_checks

        self.list = to_raw_response_wrapper(
            user_policy_checks.list,
        )


class AsyncUserPolicyChecksResourceWithRawResponse:
    def __init__(self, user_policy_checks: AsyncUserPolicyChecksResource) -> None:
        self._user_policy_checks = user_policy_checks

        self.list = async_to_raw_response_wrapper(
            user_policy_checks.list,
        )


class UserPolicyChecksResourceWithStreamingResponse:
    def __init__(self, user_policy_checks: UserPolicyChecksResource) -> None:
        self._user_policy_checks = user_policy_checks

        self.list = to_streamed_response_wrapper(
            user_policy_checks.list,
        )


class AsyncUserPolicyChecksResourceWithStreamingResponse:
    def __init__(self, user_policy_checks: AsyncUserPolicyChecksResource) -> None:
        self._user_policy_checks = user_policy_checks

        self.list = async_to_streamed_response_wrapper(
            user_policy_checks.list,
        )
