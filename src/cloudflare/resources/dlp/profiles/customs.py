# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, Type, Iterable, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
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
from ....types.dlp.profiles import (
    CustomGetResponse,
    CustomCreateResponse,
    CustomDeleteResponse,
    CustomUpdateResponse,
    custom_create_params,
    custom_update_params,
)

__all__ = ["Customs", "AsyncCustoms"]


class Customs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomsWithRawResponse:
        return CustomsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomsWithStreamingResponse:
        return CustomsWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        profiles: Iterable[custom_create_params.Profile],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomCreateResponse]:
        """
        Creates a set of DLP custom profiles.

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
            f"/accounts/{account_id}/dlp/profiles/custom",
            body=maybe_transform({"profiles": profiles}, custom_create_params.CustomCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomCreateResponse]], ResultWrapper[CustomCreateResponse]),
        )

    def update(
        self,
        profile_id: str,
        *,
        account_id: str,
        allowed_match_count: float | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        entries: Iterable[custom_update_params.Entry] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        shared_entries: Iterable[custom_update_params.SharedEntry] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomUpdateResponse:
        """
        Updates a DLP custom profile.

        Args:
          account_id: Identifier

          profile_id: The ID for this profile

          allowed_match_count: Related DLP policies will trigger when the match count exceeds the number set.

          description: The description of the profile.

          entries: The custom entries for this profile. Array elements with IDs are modifying the
              existing entry with that ID. Elements without ID will create new entries. Any
              entry not in the list will be deleted.

          name: The name of the profile.

          shared_entries: Entries from other profiles (e.g. pre-defined Cloudflare profiles, or your
              Microsoft Information Protection profiles).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._put(
            f"/accounts/{account_id}/dlp/profiles/custom/{profile_id}",
            body=maybe_transform(
                {
                    "allowed_match_count": allowed_match_count,
                    "description": description,
                    "entries": entries,
                    "name": name,
                    "shared_entries": shared_entries,
                },
                custom_update_params.CustomUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomUpdateResponse,
        )

    def delete(
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
    ) -> CustomDeleteResponse:
        """
        Deletes a DLP custom profile.

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
            CustomDeleteResponse,
            self._delete(
                f"/accounts/{account_id}/dlp/profiles/custom/{profile_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CustomDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
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
    ) -> CustomGetResponse:
        """
        Fetches a custom DLP profile.

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
        return self._get(
            f"/accounts/{account_id}/dlp/profiles/custom/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CustomGetResponse], ResultWrapper[CustomGetResponse]),
        )


class AsyncCustoms(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomsWithRawResponse:
        return AsyncCustomsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomsWithStreamingResponse:
        return AsyncCustomsWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        profiles: Iterable[custom_create_params.Profile],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomCreateResponse]:
        """
        Creates a set of DLP custom profiles.

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
            f"/accounts/{account_id}/dlp/profiles/custom",
            body=maybe_transform({"profiles": profiles}, custom_create_params.CustomCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[CustomCreateResponse]], ResultWrapper[CustomCreateResponse]),
        )

    async def update(
        self,
        profile_id: str,
        *,
        account_id: str,
        allowed_match_count: float | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        entries: Iterable[custom_update_params.Entry] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        shared_entries: Iterable[custom_update_params.SharedEntry] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomUpdateResponse:
        """
        Updates a DLP custom profile.

        Args:
          account_id: Identifier

          profile_id: The ID for this profile

          allowed_match_count: Related DLP policies will trigger when the match count exceeds the number set.

          description: The description of the profile.

          entries: The custom entries for this profile. Array elements with IDs are modifying the
              existing entry with that ID. Elements without ID will create new entries. Any
              entry not in the list will be deleted.

          name: The name of the profile.

          shared_entries: Entries from other profiles (e.g. pre-defined Cloudflare profiles, or your
              Microsoft Information Protection profiles).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._put(
            f"/accounts/{account_id}/dlp/profiles/custom/{profile_id}",
            body=maybe_transform(
                {
                    "allowed_match_count": allowed_match_count,
                    "description": description,
                    "entries": entries,
                    "name": name,
                    "shared_entries": shared_entries,
                },
                custom_update_params.CustomUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomUpdateResponse,
        )

    async def delete(
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
    ) -> CustomDeleteResponse:
        """
        Deletes a DLP custom profile.

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
            CustomDeleteResponse,
            await self._delete(
                f"/accounts/{account_id}/dlp/profiles/custom/{profile_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CustomDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
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
    ) -> CustomGetResponse:
        """
        Fetches a custom DLP profile.

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
        return await self._get(
            f"/accounts/{account_id}/dlp/profiles/custom/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CustomGetResponse], ResultWrapper[CustomGetResponse]),
        )


class CustomsWithRawResponse:
    def __init__(self, customs: Customs) -> None:
        self._customs = customs

        self.create = to_raw_response_wrapper(
            customs.create,
        )
        self.update = to_raw_response_wrapper(
            customs.update,
        )
        self.delete = to_raw_response_wrapper(
            customs.delete,
        )
        self.get = to_raw_response_wrapper(
            customs.get,
        )


class AsyncCustomsWithRawResponse:
    def __init__(self, customs: AsyncCustoms) -> None:
        self._customs = customs

        self.create = async_to_raw_response_wrapper(
            customs.create,
        )
        self.update = async_to_raw_response_wrapper(
            customs.update,
        )
        self.delete = async_to_raw_response_wrapper(
            customs.delete,
        )
        self.get = async_to_raw_response_wrapper(
            customs.get,
        )


class CustomsWithStreamingResponse:
    def __init__(self, customs: Customs) -> None:
        self._customs = customs

        self.create = to_streamed_response_wrapper(
            customs.create,
        )
        self.update = to_streamed_response_wrapper(
            customs.update,
        )
        self.delete = to_streamed_response_wrapper(
            customs.delete,
        )
        self.get = to_streamed_response_wrapper(
            customs.get,
        )


class AsyncCustomsWithStreamingResponse:
    def __init__(self, customs: AsyncCustoms) -> None:
        self._customs = customs

        self.create = async_to_streamed_response_wrapper(
            customs.create,
        )
        self.update = async_to_streamed_response_wrapper(
            customs.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            customs.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            customs.get,
        )
