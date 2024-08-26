# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.zero_trust.access.applications.user_policy_check_list_response import UserPolicyCheckListResponse

from ....._wrappers import ResultWrapper

from typing import Optional, Type

from ....._base_client import make_request_options

from .....types.zero_trust.access.app_id import AppID

from ....._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .....types.zero_trust.access import AppID
from typing import cast
from typing import cast

__all__ = ["UserPolicyChecksResource", "AsyncUserPolicyChecksResource"]

class UserPolicyChecksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserPolicyChecksResourceWithRawResponse:
        return UserPolicyChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserPolicyChecksResourceWithStreamingResponse:
        return UserPolicyChecksResourceWithStreamingResponse(self)

    def list(self,
    app_id: AppID,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[UserPolicyCheckListResponse]:
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
          raise ValueError(
            f'Expected a non-empty value for `app_id` but received {app_id!r}'
          )
        if account_id and zone_id:
          raise ValueError('You cannot provide both account_id and zone_id');

        if account_id:
          account_or_zone = "accounts"
          account_or_zone_id = account_id
        else:
          if not zone_id:
            raise ValueError('You must provide either account_id or zone_id');

          account_or_zone = "zones"
          account_or_zone_id = zone_id
        return self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/user_policy_checks",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[UserPolicyCheckListResponse]]._unwrapper),
            cast_to=cast(Type[Optional[UserPolicyCheckListResponse]], ResultWrapper[UserPolicyCheckListResponse]),
        )

class AsyncUserPolicyChecksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserPolicyChecksResourceWithRawResponse:
        return AsyncUserPolicyChecksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserPolicyChecksResourceWithStreamingResponse:
        return AsyncUserPolicyChecksResourceWithStreamingResponse(self)

    async def list(self,
    app_id: AppID,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[UserPolicyCheckListResponse]:
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
          raise ValueError(
            f'Expected a non-empty value for `app_id` but received {app_id!r}'
          )
        if account_id and zone_id:
          raise ValueError('You cannot provide both account_id and zone_id');

        if account_id:
          account_or_zone = "accounts"
          account_or_zone_id = account_id
        else:
          if not zone_id:
            raise ValueError('You must provide either account_id or zone_id');

          account_or_zone = "zones"
          account_or_zone_id = zone_id
        return await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/apps/{app_id}/user_policy_checks",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[UserPolicyCheckListResponse]]._unwrapper),
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