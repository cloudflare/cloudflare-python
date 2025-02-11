# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Iterable, Optional, cast
from typing_extensions import overload

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
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
from .....types.zero_trust.dlp.profile import Profile
from .....types.zero_trust.dlp.profiles import custom_create_params, custom_update_params
from .....types.zero_trust.dlp.context_awareness_param import ContextAwarenessParam
from .....types.zero_trust.dlp.profiles.custom_create_response import CustomCreateResponse

__all__ = ["CustomResource", "AsyncCustomResource"]


class CustomResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CustomResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CustomResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        account_id: str,
        profiles: Iterable[custom_create_params.Variant0Profile],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomCreateResponse]:
        """
        Creates a DLP custom profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        account_id: str,
        entries: Iterable[custom_create_params.DLPNewCustomProfileEntry],
        name: str,
        ai_context_enabled: bool | NotGiven = NOT_GIVEN,
        allowed_match_count: int | NotGiven = NOT_GIVEN,
        confidence_threshold: Optional[str] | NotGiven = NOT_GIVEN,
        context_awareness: ContextAwarenessParam | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        ocr_enabled: bool | NotGiven = NOT_GIVEN,
        shared_entries: Iterable[custom_create_params.DLPNewCustomProfileSharedEntry] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomCreateResponse]:
        """
        Creates a DLP custom profile.

        Args:
          allowed_match_count: Related DLP policies will trigger when the match count exceeds the number set.

          context_awareness: Scan the context of predefined entries to only return matches surrounded by
              keywords.

          description: The description of the profile

          shared_entries: Entries from other profiles (e.g. pre-defined Cloudflare profiles, or your
              Microsoft Information Protection profiles).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "profiles"], ["account_id", "entries", "name"])
    def create(
        self,
        *,
        account_id: str,
        profiles: Iterable[custom_create_params.Variant0Profile] | NotGiven = NOT_GIVEN,
        entries: Iterable[custom_create_params.DLPNewCustomProfileEntry] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        ai_context_enabled: bool | NotGiven = NOT_GIVEN,
        allowed_match_count: int | NotGiven = NOT_GIVEN,
        confidence_threshold: Optional[str] | NotGiven = NOT_GIVEN,
        context_awareness: ContextAwarenessParam | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        ocr_enabled: bool | NotGiven = NOT_GIVEN,
        shared_entries: Iterable[custom_create_params.DLPNewCustomProfileSharedEntry] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomCreateResponse]:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            Optional[CustomCreateResponse],
            self._post(
                f"/accounts/{account_id}/dlp/profiles/custom",
                body=maybe_transform(
                    {
                        "profiles": profiles,
                        "entries": entries,
                        "name": name,
                        "ai_context_enabled": ai_context_enabled,
                        "allowed_match_count": allowed_match_count,
                        "confidence_threshold": confidence_threshold,
                        "context_awareness": context_awareness,
                        "description": description,
                        "ocr_enabled": ocr_enabled,
                        "shared_entries": shared_entries,
                    },
                    custom_create_params.CustomCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[CustomCreateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CustomCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def update(
        self,
        profile_id: str,
        *,
        account_id: str,
        name: str,
        ai_context_enabled: bool | NotGiven = NOT_GIVEN,
        allowed_match_count: Optional[int] | NotGiven = NOT_GIVEN,
        confidence_threshold: Optional[str] | NotGiven = NOT_GIVEN,
        context_awareness: ContextAwarenessParam | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        entries: Optional[Iterable[custom_update_params.Entry]] | NotGiven = NOT_GIVEN,
        ocr_enabled: bool | NotGiven = NOT_GIVEN,
        shared_entries: Iterable[custom_update_params.SharedEntry] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Profile]:
        """
        Updates a DLP custom profile.

        Args:
          context_awareness: Scan the context of predefined entries to only return matches surrounded by
              keywords.

          description: The description of the profile

          entries: Custom entries from this profile. If this field is omitted, entries owned by
              this profile will not be changed.

          shared_entries: Other entries, e.g. predefined or integration.

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
            Optional[Profile],
            self._put(
                f"/accounts/{account_id}/dlp/profiles/custom/{profile_id}",
                body=maybe_transform(
                    {
                        "name": name,
                        "ai_context_enabled": ai_context_enabled,
                        "allowed_match_count": allowed_match_count,
                        "confidence_threshold": confidence_threshold,
                        "context_awareness": context_awareness,
                        "description": description,
                        "entries": entries,
                        "ocr_enabled": ocr_enabled,
                        "shared_entries": shared_entries,
                    },
                    custom_update_params.CustomUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Profile]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Profile]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> object:
        """
        Deletes a DLP custom profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._delete(
            f"/accounts/{account_id}/dlp/profiles/custom/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
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
    ) -> Optional[Profile]:
        """
        Fetches a custom DLP profile by id.

        Args:
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
            Optional[Profile],
            self._get(
                f"/accounts/{account_id}/dlp/profiles/custom/{profile_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Profile]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Profile]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncCustomResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCustomResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        account_id: str,
        profiles: Iterable[custom_create_params.Variant0Profile],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomCreateResponse]:
        """
        Creates a DLP custom profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        account_id: str,
        entries: Iterable[custom_create_params.DLPNewCustomProfileEntry],
        name: str,
        ai_context_enabled: bool | NotGiven = NOT_GIVEN,
        allowed_match_count: int | NotGiven = NOT_GIVEN,
        confidence_threshold: Optional[str] | NotGiven = NOT_GIVEN,
        context_awareness: ContextAwarenessParam | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        ocr_enabled: bool | NotGiven = NOT_GIVEN,
        shared_entries: Iterable[custom_create_params.DLPNewCustomProfileSharedEntry] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomCreateResponse]:
        """
        Creates a DLP custom profile.

        Args:
          allowed_match_count: Related DLP policies will trigger when the match count exceeds the number set.

          context_awareness: Scan the context of predefined entries to only return matches surrounded by
              keywords.

          description: The description of the profile

          shared_entries: Entries from other profiles (e.g. pre-defined Cloudflare profiles, or your
              Microsoft Information Protection profiles).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "profiles"], ["account_id", "entries", "name"])
    async def create(
        self,
        *,
        account_id: str,
        profiles: Iterable[custom_create_params.Variant0Profile] | NotGiven = NOT_GIVEN,
        entries: Iterable[custom_create_params.DLPNewCustomProfileEntry] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        ai_context_enabled: bool | NotGiven = NOT_GIVEN,
        allowed_match_count: int | NotGiven = NOT_GIVEN,
        confidence_threshold: Optional[str] | NotGiven = NOT_GIVEN,
        context_awareness: ContextAwarenessParam | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        ocr_enabled: bool | NotGiven = NOT_GIVEN,
        shared_entries: Iterable[custom_create_params.DLPNewCustomProfileSharedEntry] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CustomCreateResponse]:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            Optional[CustomCreateResponse],
            await self._post(
                f"/accounts/{account_id}/dlp/profiles/custom",
                body=await async_maybe_transform(
                    {
                        "profiles": profiles,
                        "entries": entries,
                        "name": name,
                        "ai_context_enabled": ai_context_enabled,
                        "allowed_match_count": allowed_match_count,
                        "confidence_threshold": confidence_threshold,
                        "context_awareness": context_awareness,
                        "description": description,
                        "ocr_enabled": ocr_enabled,
                        "shared_entries": shared_entries,
                    },
                    custom_create_params.CustomCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[CustomCreateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CustomCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def update(
        self,
        profile_id: str,
        *,
        account_id: str,
        name: str,
        ai_context_enabled: bool | NotGiven = NOT_GIVEN,
        allowed_match_count: Optional[int] | NotGiven = NOT_GIVEN,
        confidence_threshold: Optional[str] | NotGiven = NOT_GIVEN,
        context_awareness: ContextAwarenessParam | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        entries: Optional[Iterable[custom_update_params.Entry]] | NotGiven = NOT_GIVEN,
        ocr_enabled: bool | NotGiven = NOT_GIVEN,
        shared_entries: Iterable[custom_update_params.SharedEntry] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Profile]:
        """
        Updates a DLP custom profile.

        Args:
          context_awareness: Scan the context of predefined entries to only return matches surrounded by
              keywords.

          description: The description of the profile

          entries: Custom entries from this profile. If this field is omitted, entries owned by
              this profile will not be changed.

          shared_entries: Other entries, e.g. predefined or integration.

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
            Optional[Profile],
            await self._put(
                f"/accounts/{account_id}/dlp/profiles/custom/{profile_id}",
                body=await async_maybe_transform(
                    {
                        "name": name,
                        "ai_context_enabled": ai_context_enabled,
                        "allowed_match_count": allowed_match_count,
                        "confidence_threshold": confidence_threshold,
                        "context_awareness": context_awareness,
                        "description": description,
                        "entries": entries,
                        "ocr_enabled": ocr_enabled,
                        "shared_entries": shared_entries,
                    },
                    custom_update_params.CustomUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Profile]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Profile]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
    ) -> object:
        """
        Deletes a DLP custom profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/dlp/profiles/custom/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
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
    ) -> Optional[Profile]:
        """
        Fetches a custom DLP profile by id.

        Args:
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
            Optional[Profile],
            await self._get(
                f"/accounts/{account_id}/dlp/profiles/custom/{profile_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[Profile]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[Profile]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class CustomResourceWithRawResponse:
    def __init__(self, custom: CustomResource) -> None:
        self._custom = custom

        self.create = to_raw_response_wrapper(
            custom.create,
        )
        self.update = to_raw_response_wrapper(
            custom.update,
        )
        self.delete = to_raw_response_wrapper(
            custom.delete,
        )
        self.get = to_raw_response_wrapper(
            custom.get,
        )


class AsyncCustomResourceWithRawResponse:
    def __init__(self, custom: AsyncCustomResource) -> None:
        self._custom = custom

        self.create = async_to_raw_response_wrapper(
            custom.create,
        )
        self.update = async_to_raw_response_wrapper(
            custom.update,
        )
        self.delete = async_to_raw_response_wrapper(
            custom.delete,
        )
        self.get = async_to_raw_response_wrapper(
            custom.get,
        )


class CustomResourceWithStreamingResponse:
    def __init__(self, custom: CustomResource) -> None:
        self._custom = custom

        self.create = to_streamed_response_wrapper(
            custom.create,
        )
        self.update = to_streamed_response_wrapper(
            custom.update,
        )
        self.delete = to_streamed_response_wrapper(
            custom.delete,
        )
        self.get = to_streamed_response_wrapper(
            custom.get,
        )


class AsyncCustomResourceWithStreamingResponse:
    def __init__(self, custom: AsyncCustomResource) -> None:
        self._custom = custom

        self.create = async_to_streamed_response_wrapper(
            custom.create,
        )
        self.update = async_to_streamed_response_wrapper(
            custom.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            custom.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            custom.get,
        )
