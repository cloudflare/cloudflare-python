# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .customs import Customs, AsyncCustoms

from ...._compat import cached_property

from .predefineds import Predefineds, AsyncPredefineds

from ....types.dlps import ProfileDLPProfilesListAllProfilesResponse, ProfileGetResponse

from typing import Type, Optional

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
from .customs import (
    Customs,
    AsyncCustoms,
    CustomsWithRawResponse,
    AsyncCustomsWithRawResponse,
    CustomsWithStreamingResponse,
    AsyncCustomsWithStreamingResponse,
)
from .predefineds import (
    Predefineds,
    AsyncPredefineds,
    PredefinedsWithRawResponse,
    AsyncPredefinedsWithRawResponse,
    PredefinedsWithStreamingResponse,
    AsyncPredefinedsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Profiles", "AsyncProfiles"]


class Profiles(SyncAPIResource):
    @cached_property
    def customs(self) -> Customs:
        return Customs(self._client)

    @cached_property
    def predefineds(self) -> Predefineds:
        return Predefineds(self._client)

    @cached_property
    def with_raw_response(self) -> ProfilesWithRawResponse:
        return ProfilesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfilesWithStreamingResponse:
        return ProfilesWithStreamingResponse(self)

    def dlp_profiles_list_all_profiles(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ProfileDLPProfilesListAllProfilesResponse]:
        """
        Lists all DLP profiles in an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/dlp/profiles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ProfileDLPProfilesListAllProfilesResponse]],
                ResultWrapper[ProfileDLPProfilesListAllProfilesResponse],
            ),
        )

    def get(
        self,
        profile_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProfileGetResponse:
        """Fetches a DLP profile by ID.

        Supports both predefined and custom profiles

        Args:
          account_id: Identifier

          profile_id: The ID for this profile

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return cast(
            ProfileGetResponse,
            self._get(
                f"/accounts/{account_id}/dlp/profiles/{profile_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ProfileGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncProfiles(AsyncAPIResource):
    @cached_property
    def customs(self) -> AsyncCustoms:
        return AsyncCustoms(self._client)

    @cached_property
    def predefineds(self) -> AsyncPredefineds:
        return AsyncPredefineds(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProfilesWithRawResponse:
        return AsyncProfilesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfilesWithStreamingResponse:
        return AsyncProfilesWithStreamingResponse(self)

    async def dlp_profiles_list_all_profiles(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ProfileDLPProfilesListAllProfilesResponse]:
        """
        Lists all DLP profiles in an account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/dlp/profiles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ProfileDLPProfilesListAllProfilesResponse]],
                ResultWrapper[ProfileDLPProfilesListAllProfilesResponse],
            ),
        )

    async def get(
        self,
        profile_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProfileGetResponse:
        """Fetches a DLP profile by ID.

        Supports both predefined and custom profiles

        Args:
          account_id: Identifier

          profile_id: The ID for this profile

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return cast(
            ProfileGetResponse,
            await self._get(
                f"/accounts/{account_id}/dlp/profiles/{profile_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ProfileGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ProfilesWithRawResponse:
    def __init__(self, profiles: Profiles) -> None:
        self._profiles = profiles

        self.dlp_profiles_list_all_profiles = to_raw_response_wrapper(
            profiles.dlp_profiles_list_all_profiles,
        )
        self.get = to_raw_response_wrapper(
            profiles.get,
        )

    @cached_property
    def customs(self) -> CustomsWithRawResponse:
        return CustomsWithRawResponse(self._profiles.customs)

    @cached_property
    def predefineds(self) -> PredefinedsWithRawResponse:
        return PredefinedsWithRawResponse(self._profiles.predefineds)


class AsyncProfilesWithRawResponse:
    def __init__(self, profiles: AsyncProfiles) -> None:
        self._profiles = profiles

        self.dlp_profiles_list_all_profiles = async_to_raw_response_wrapper(
            profiles.dlp_profiles_list_all_profiles,
        )
        self.get = async_to_raw_response_wrapper(
            profiles.get,
        )

    @cached_property
    def customs(self) -> AsyncCustomsWithRawResponse:
        return AsyncCustomsWithRawResponse(self._profiles.customs)

    @cached_property
    def predefineds(self) -> AsyncPredefinedsWithRawResponse:
        return AsyncPredefinedsWithRawResponse(self._profiles.predefineds)


class ProfilesWithStreamingResponse:
    def __init__(self, profiles: Profiles) -> None:
        self._profiles = profiles

        self.dlp_profiles_list_all_profiles = to_streamed_response_wrapper(
            profiles.dlp_profiles_list_all_profiles,
        )
        self.get = to_streamed_response_wrapper(
            profiles.get,
        )

    @cached_property
    def customs(self) -> CustomsWithStreamingResponse:
        return CustomsWithStreamingResponse(self._profiles.customs)

    @cached_property
    def predefineds(self) -> PredefinedsWithStreamingResponse:
        return PredefinedsWithStreamingResponse(self._profiles.predefineds)


class AsyncProfilesWithStreamingResponse:
    def __init__(self, profiles: AsyncProfiles) -> None:
        self._profiles = profiles

        self.dlp_profiles_list_all_profiles = async_to_streamed_response_wrapper(
            profiles.dlp_profiles_list_all_profiles,
        )
        self.get = async_to_streamed_response_wrapper(
            profiles.get,
        )

    @cached_property
    def customs(self) -> AsyncCustomsWithStreamingResponse:
        return AsyncCustomsWithStreamingResponse(self._profiles.customs)

    @cached_property
    def predefineds(self) -> AsyncPredefinedsWithStreamingResponse:
        return AsyncPredefinedsWithStreamingResponse(self._profiles.predefineds)
