# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.users.billings import ProfileUserBillingProfileBillingProfileDetailsResponse

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Profiles", "AsyncProfiles"]


class Profiles(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProfilesWithRawResponse:
        return ProfilesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfilesWithStreamingResponse:
        return ProfilesWithStreamingResponse(self)

    def user_billing_profile_billing_profile_details(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProfileUserBillingProfileBillingProfileDetailsResponse:
        """Accesses your billing profile object."""
        return cast(
            ProfileUserBillingProfileBillingProfileDetailsResponse,
            self._get(
                "/user/billing/profile",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ProfileUserBillingProfileBillingProfileDetailsResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncProfiles(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProfilesWithRawResponse:
        return AsyncProfilesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfilesWithStreamingResponse:
        return AsyncProfilesWithStreamingResponse(self)

    async def user_billing_profile_billing_profile_details(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProfileUserBillingProfileBillingProfileDetailsResponse:
        """Accesses your billing profile object."""
        return cast(
            ProfileUserBillingProfileBillingProfileDetailsResponse,
            await self._get(
                "/user/billing/profile",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ProfileUserBillingProfileBillingProfileDetailsResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ProfilesWithRawResponse:
    def __init__(self, profiles: Profiles) -> None:
        self._profiles = profiles

        self.user_billing_profile_billing_profile_details = to_raw_response_wrapper(
            profiles.user_billing_profile_billing_profile_details,
        )


class AsyncProfilesWithRawResponse:
    def __init__(self, profiles: AsyncProfiles) -> None:
        self._profiles = profiles

        self.user_billing_profile_billing_profile_details = async_to_raw_response_wrapper(
            profiles.user_billing_profile_billing_profile_details,
        )


class ProfilesWithStreamingResponse:
    def __init__(self, profiles: Profiles) -> None:
        self._profiles = profiles

        self.user_billing_profile_billing_profile_details = to_streamed_response_wrapper(
            profiles.user_billing_profile_billing_profile_details,
        )


class AsyncProfilesWithStreamingResponse:
    def __init__(self, profiles: AsyncProfiles) -> None:
        self._profiles = profiles

        self.user_billing_profile_billing_profile_details = async_to_streamed_response_wrapper(
            profiles.user_billing_profile_billing_profile_details,
        )
