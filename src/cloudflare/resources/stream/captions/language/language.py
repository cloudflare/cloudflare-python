# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .vtt import (
    VttResource,
    AsyncVttResource,
    VttResourceWithRawResponse,
    AsyncVttResourceWithRawResponse,
    VttResourceWithStreamingResponse,
    AsyncVttResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
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
from .....types.stream.caption import Caption
from .....types.stream.captions import language_update_params
from .....types.stream.captions.language_delete_response import LanguageDeleteResponse

__all__ = ["LanguageResource", "AsyncLanguageResource"]


class LanguageResource(SyncAPIResource):
    @cached_property
    def vtt(self) -> VttResource:
        return VttResource(self._client)

    @cached_property
    def with_raw_response(self) -> LanguageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return LanguageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LanguageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return LanguageResourceWithStreamingResponse(self)

    def create(
        self,
        language: str,
        *,
        account_id: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Caption]:
        """
        Generate captions or subtitles for provided language via AI.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          language: The language tag in BCP 47 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not language:
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        return self._post(
            f"/accounts/{account_id}/stream/{identifier}/captions/{language}/generate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Caption]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Caption]], ResultWrapper[Caption]),
        )

    def update(
        self,
        language: str,
        *,
        account_id: str,
        identifier: str,
        file: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Caption]:
        """
        Uploads the caption or subtitle file to the endpoint for a specific BCP47
        language. One caption or subtitle file per language is allowed.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          language: The language tag in BCP 47 format.

          file: The WebVTT file containing the caption or subtitle content.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not language:
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._put(
            f"/accounts/{account_id}/stream/{identifier}/captions/{language}",
            body=maybe_transform({"file": file}, language_update_params.LanguageUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Caption]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Caption]], ResultWrapper[Caption]),
        )

    def delete(
        self,
        language: str,
        *,
        account_id: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Removes the captions or subtitles from a video.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          language: The language tag in BCP 47 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not language:
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        return self._delete(
            f"/accounts/{account_id}/stream/{identifier}/captions/{language}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[LanguageDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    def get(
        self,
        language: str,
        *,
        account_id: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Caption]:
        """
        Lists the captions or subtitles for provided language.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          language: The language tag in BCP 47 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not language:
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        return self._get(
            f"/accounts/{account_id}/stream/{identifier}/captions/{language}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Caption]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Caption]], ResultWrapper[Caption]),
        )


class AsyncLanguageResource(AsyncAPIResource):
    @cached_property
    def vtt(self) -> AsyncVttResource:
        return AsyncVttResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLanguageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLanguageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLanguageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncLanguageResourceWithStreamingResponse(self)

    async def create(
        self,
        language: str,
        *,
        account_id: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Caption]:
        """
        Generate captions or subtitles for provided language via AI.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          language: The language tag in BCP 47 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not language:
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        return await self._post(
            f"/accounts/{account_id}/stream/{identifier}/captions/{language}/generate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Caption]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Caption]], ResultWrapper[Caption]),
        )

    async def update(
        self,
        language: str,
        *,
        account_id: str,
        identifier: str,
        file: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Caption]:
        """
        Uploads the caption or subtitle file to the endpoint for a specific BCP47
        language. One caption or subtitle file per language is allowed.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          language: The language tag in BCP 47 format.

          file: The WebVTT file containing the caption or subtitle content.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not language:
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._put(
            f"/accounts/{account_id}/stream/{identifier}/captions/{language}",
            body=await async_maybe_transform({"file": file}, language_update_params.LanguageUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Caption]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Caption]], ResultWrapper[Caption]),
        )

    async def delete(
        self,
        language: str,
        *,
        account_id: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Removes the captions or subtitles from a video.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          language: The language tag in BCP 47 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not language:
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        return await self._delete(
            f"/accounts/{account_id}/stream/{identifier}/captions/{language}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[LanguageDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )

    async def get(
        self,
        language: str,
        *,
        account_id: str,
        identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Caption]:
        """
        Lists the captions or subtitles for provided language.

        Args:
          account_id: Identifier

          identifier: A Cloudflare-generated unique identifier for a media item.

          language: The language tag in BCP 47 format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        if not language:
            raise ValueError(f"Expected a non-empty value for `language` but received {language!r}")
        return await self._get(
            f"/accounts/{account_id}/stream/{identifier}/captions/{language}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Caption]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Caption]], ResultWrapper[Caption]),
        )


class LanguageResourceWithRawResponse:
    def __init__(self, language: LanguageResource) -> None:
        self._language = language

        self.create = to_raw_response_wrapper(
            language.create,
        )
        self.update = to_raw_response_wrapper(
            language.update,
        )
        self.delete = to_raw_response_wrapper(
            language.delete,
        )
        self.get = to_raw_response_wrapper(
            language.get,
        )

    @cached_property
    def vtt(self) -> VttResourceWithRawResponse:
        return VttResourceWithRawResponse(self._language.vtt)


class AsyncLanguageResourceWithRawResponse:
    def __init__(self, language: AsyncLanguageResource) -> None:
        self._language = language

        self.create = async_to_raw_response_wrapper(
            language.create,
        )
        self.update = async_to_raw_response_wrapper(
            language.update,
        )
        self.delete = async_to_raw_response_wrapper(
            language.delete,
        )
        self.get = async_to_raw_response_wrapper(
            language.get,
        )

    @cached_property
    def vtt(self) -> AsyncVttResourceWithRawResponse:
        return AsyncVttResourceWithRawResponse(self._language.vtt)


class LanguageResourceWithStreamingResponse:
    def __init__(self, language: LanguageResource) -> None:
        self._language = language

        self.create = to_streamed_response_wrapper(
            language.create,
        )
        self.update = to_streamed_response_wrapper(
            language.update,
        )
        self.delete = to_streamed_response_wrapper(
            language.delete,
        )
        self.get = to_streamed_response_wrapper(
            language.get,
        )

    @cached_property
    def vtt(self) -> VttResourceWithStreamingResponse:
        return VttResourceWithStreamingResponse(self._language.vtt)


class AsyncLanguageResourceWithStreamingResponse:
    def __init__(self, language: AsyncLanguageResource) -> None:
        self._language = language

        self.create = async_to_streamed_response_wrapper(
            language.create,
        )
        self.update = async_to_streamed_response_wrapper(
            language.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            language.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            language.get,
        )

    @cached_property
    def vtt(self) -> AsyncVttResourceWithStreamingResponse:
        return AsyncVttResourceWithStreamingResponse(self._language.vtt)
