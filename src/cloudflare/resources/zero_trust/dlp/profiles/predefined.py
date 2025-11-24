# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
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
from .....types.zero_trust.dlp.profiles import predefined_update_params
from .....types.zero_trust.dlp.profiles.predefined_get_response import PredefinedGetResponse
from .....types.zero_trust.dlp.profiles.predefined_update_response import PredefinedUpdateResponse

__all__ = ["PredefinedResource", "AsyncPredefinedResource"]


class PredefinedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PredefinedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PredefinedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PredefinedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PredefinedResourceWithStreamingResponse(self)

    def update(
        self,
        profile_id: str,
        *,
        account_id: str,
        ai_context_enabled: bool | Omit = omit,
        allowed_match_count: Optional[int] | Omit = omit,
        confidence_threshold: Optional[str] | Omit = omit,
        enabled_entries: Optional[SequenceNotStr[str]] | Omit = omit,
        entries: Iterable[predefined_update_params.Entry] | Omit = omit,
        ocr_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[PredefinedUpdateResponse]:
        """This is similar to `update_predefined` but only returns entries that are
        enabled.

        This is needed for our terraform API Updates a DLP predefined profile.
        Only supports enabling/disabling entries.

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
        return self._put(
            f"/accounts/{account_id}/dlp/profiles/predefined/{profile_id}/config",
            body=maybe_transform(
                {
                    "ai_context_enabled": ai_context_enabled,
                    "allowed_match_count": allowed_match_count,
                    "confidence_threshold": confidence_threshold,
                    "enabled_entries": enabled_entries,
                    "entries": entries,
                    "ocr_enabled": ocr_enabled,
                },
                predefined_update_params.PredefinedUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PredefinedUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PredefinedUpdateResponse]], ResultWrapper[PredefinedUpdateResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        This is a no-op as predefined profiles can't be deleted but is needed for our
        generated terraform API.

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
            f"/accounts/{account_id}/dlp/profiles/predefined/{profile_id}",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[PredefinedGetResponse]:
        """
        This is similar to `get_predefined` but only returns entries that are enabled.
        This is needed for our terraform API Fetches a predefined DLP profile by id.

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
        return self._get(
            f"/accounts/{account_id}/dlp/profiles/predefined/{profile_id}/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PredefinedGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PredefinedGetResponse]], ResultWrapper[PredefinedGetResponse]),
        )


class AsyncPredefinedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPredefinedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPredefinedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPredefinedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPredefinedResourceWithStreamingResponse(self)

    async def update(
        self,
        profile_id: str,
        *,
        account_id: str,
        ai_context_enabled: bool | Omit = omit,
        allowed_match_count: Optional[int] | Omit = omit,
        confidence_threshold: Optional[str] | Omit = omit,
        enabled_entries: Optional[SequenceNotStr[str]] | Omit = omit,
        entries: Iterable[predefined_update_params.Entry] | Omit = omit,
        ocr_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[PredefinedUpdateResponse]:
        """This is similar to `update_predefined` but only returns entries that are
        enabled.

        This is needed for our terraform API Updates a DLP predefined profile.
        Only supports enabling/disabling entries.

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
        return await self._put(
            f"/accounts/{account_id}/dlp/profiles/predefined/{profile_id}/config",
            body=await async_maybe_transform(
                {
                    "ai_context_enabled": ai_context_enabled,
                    "allowed_match_count": allowed_match_count,
                    "confidence_threshold": confidence_threshold,
                    "enabled_entries": enabled_entries,
                    "entries": entries,
                    "ocr_enabled": ocr_enabled,
                },
                predefined_update_params.PredefinedUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PredefinedUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PredefinedUpdateResponse]], ResultWrapper[PredefinedUpdateResponse]),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        This is a no-op as predefined profiles can't be deleted but is needed for our
        generated terraform API.

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
            f"/accounts/{account_id}/dlp/profiles/predefined/{profile_id}",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[PredefinedGetResponse]:
        """
        This is similar to `get_predefined` but only returns entries that are enabled.
        This is needed for our terraform API Fetches a predefined DLP profile by id.

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
        return await self._get(
            f"/accounts/{account_id}/dlp/profiles/predefined/{profile_id}/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PredefinedGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PredefinedGetResponse]], ResultWrapper[PredefinedGetResponse]),
        )


class PredefinedResourceWithRawResponse:
    def __init__(self, predefined: PredefinedResource) -> None:
        self._predefined = predefined

        self.update = to_raw_response_wrapper(
            predefined.update,
        )
        self.delete = to_raw_response_wrapper(
            predefined.delete,
        )
        self.get = to_raw_response_wrapper(
            predefined.get,
        )


class AsyncPredefinedResourceWithRawResponse:
    def __init__(self, predefined: AsyncPredefinedResource) -> None:
        self._predefined = predefined

        self.update = async_to_raw_response_wrapper(
            predefined.update,
        )
        self.delete = async_to_raw_response_wrapper(
            predefined.delete,
        )
        self.get = async_to_raw_response_wrapper(
            predefined.get,
        )


class PredefinedResourceWithStreamingResponse:
    def __init__(self, predefined: PredefinedResource) -> None:
        self._predefined = predefined

        self.update = to_streamed_response_wrapper(
            predefined.update,
        )
        self.delete = to_streamed_response_wrapper(
            predefined.delete,
        )
        self.get = to_streamed_response_wrapper(
            predefined.get,
        )


class AsyncPredefinedResourceWithStreamingResponse:
    def __init__(self, predefined: AsyncPredefinedResource) -> None:
        self._predefined = predefined

        self.update = async_to_streamed_response_wrapper(
            predefined.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            predefined.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            predefined.get,
        )
