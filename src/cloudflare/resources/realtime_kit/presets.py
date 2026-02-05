# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.realtime_kit import preset_get_params, preset_create_params, preset_update_params
from ...types.realtime_kit.preset_get_response import PresetGetResponse
from ...types.realtime_kit.preset_create_response import PresetCreateResponse
from ...types.realtime_kit.preset_delete_response import PresetDeleteResponse
from ...types.realtime_kit.preset_update_response import PresetUpdateResponse
from ...types.realtime_kit.preset_get_preset_by_id_response import PresetGetPresetByIDResponse

__all__ = ["PresetsResource", "AsyncPresetsResource"]


class PresetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PresetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PresetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PresetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PresetsResourceWithStreamingResponse(self)

    def create(
        self,
        app_id: str,
        *,
        account_id: str,
        config: preset_create_params.Config,
        name: str,
        ui: preset_create_params.UI,
        permissions: preset_create_params.Permissions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresetCreateResponse:
        """
        Creates a preset belonging to the current App

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          name: Name of the preset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._post(
            f"/accounts/{account_id}/realtime/kit/{app_id}/presets",
            body=maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "ui": ui,
                    "permissions": permissions,
                },
                preset_create_params.PresetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PresetCreateResponse,
        )

    def update(
        self,
        preset_id: str,
        *,
        account_id: str,
        app_id: str,
        config: preset_update_params.Config | Omit = omit,
        name: str | Omit = omit,
        permissions: preset_update_params.Permissions | Omit = omit,
        ui: preset_update_params.UI | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresetUpdateResponse:
        """
        Update a preset by the provided preset ID

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          name: Name of the preset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not preset_id:
            raise ValueError(f"Expected a non-empty value for `preset_id` but received {preset_id!r}")
        return self._patch(
            f"/accounts/{account_id}/realtime/kit/{app_id}/presets/{preset_id}",
            body=maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "permissions": permissions,
                    "ui": ui,
                },
                preset_update_params.PresetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PresetUpdateResponse,
        )

    def delete(
        self,
        preset_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresetDeleteResponse:
        """
        Deletes a preset using the provided preset ID

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not preset_id:
            raise ValueError(f"Expected a non-empty value for `preset_id` but received {preset_id!r}")
        return self._delete(
            f"/accounts/{account_id}/realtime/kit/{app_id}/presets/{preset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PresetDeleteResponse,
        )

    def get(
        self,
        app_id: str,
        *,
        account_id: str,
        page_no: float | Omit = omit,
        per_page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresetGetResponse:
        """
        Fetches all the presets belonging to an App.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          page_no: The page number from which you want your page search results to be displayed.

          per_page: Number of results per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/presets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_no": page_no,
                        "per_page": per_page,
                    },
                    preset_get_params.PresetGetParams,
                ),
            ),
            cast_to=PresetGetResponse,
        )

    def get_preset_by_id(
        self,
        preset_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresetGetPresetByIDResponse:
        """
        Fetches details of a preset using the provided preset ID

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not preset_id:
            raise ValueError(f"Expected a non-empty value for `preset_id` but received {preset_id!r}")
        return self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/presets/{preset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PresetGetPresetByIDResponse,
        )


class AsyncPresetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPresetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPresetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPresetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPresetsResourceWithStreamingResponse(self)

    async def create(
        self,
        app_id: str,
        *,
        account_id: str,
        config: preset_create_params.Config,
        name: str,
        ui: preset_create_params.UI,
        permissions: preset_create_params.Permissions | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresetCreateResponse:
        """
        Creates a preset belonging to the current App

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          name: Name of the preset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._post(
            f"/accounts/{account_id}/realtime/kit/{app_id}/presets",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "ui": ui,
                    "permissions": permissions,
                },
                preset_create_params.PresetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PresetCreateResponse,
        )

    async def update(
        self,
        preset_id: str,
        *,
        account_id: str,
        app_id: str,
        config: preset_update_params.Config | Omit = omit,
        name: str | Omit = omit,
        permissions: preset_update_params.Permissions | Omit = omit,
        ui: preset_update_params.UI | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresetUpdateResponse:
        """
        Update a preset by the provided preset ID

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          name: Name of the preset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not preset_id:
            raise ValueError(f"Expected a non-empty value for `preset_id` but received {preset_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/realtime/kit/{app_id}/presets/{preset_id}",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "permissions": permissions,
                    "ui": ui,
                },
                preset_update_params.PresetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PresetUpdateResponse,
        )

    async def delete(
        self,
        preset_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresetDeleteResponse:
        """
        Deletes a preset using the provided preset ID

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not preset_id:
            raise ValueError(f"Expected a non-empty value for `preset_id` but received {preset_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/realtime/kit/{app_id}/presets/{preset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PresetDeleteResponse,
        )

    async def get(
        self,
        app_id: str,
        *,
        account_id: str,
        page_no: float | Omit = omit,
        per_page: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresetGetResponse:
        """
        Fetches all the presets belonging to an App.

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          page_no: The page number from which you want your page search results to be displayed.

          per_page: Number of results per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/presets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_no": page_no,
                        "per_page": per_page,
                    },
                    preset_get_params.PresetGetParams,
                ),
            ),
            cast_to=PresetGetResponse,
        )

    async def get_preset_by_id(
        self,
        preset_id: str,
        *,
        account_id: str,
        app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresetGetPresetByIDResponse:
        """
        Fetches details of a preset using the provided preset ID

        Args:
          account_id: The account identifier tag.

          app_id: The app identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        if not preset_id:
            raise ValueError(f"Expected a non-empty value for `preset_id` but received {preset_id!r}")
        return await self._get(
            f"/accounts/{account_id}/realtime/kit/{app_id}/presets/{preset_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PresetGetPresetByIDResponse,
        )


class PresetsResourceWithRawResponse:
    def __init__(self, presets: PresetsResource) -> None:
        self._presets = presets

        self.create = to_raw_response_wrapper(
            presets.create,
        )
        self.update = to_raw_response_wrapper(
            presets.update,
        )
        self.delete = to_raw_response_wrapper(
            presets.delete,
        )
        self.get = to_raw_response_wrapper(
            presets.get,
        )
        self.get_preset_by_id = to_raw_response_wrapper(
            presets.get_preset_by_id,
        )


class AsyncPresetsResourceWithRawResponse:
    def __init__(self, presets: AsyncPresetsResource) -> None:
        self._presets = presets

        self.create = async_to_raw_response_wrapper(
            presets.create,
        )
        self.update = async_to_raw_response_wrapper(
            presets.update,
        )
        self.delete = async_to_raw_response_wrapper(
            presets.delete,
        )
        self.get = async_to_raw_response_wrapper(
            presets.get,
        )
        self.get_preset_by_id = async_to_raw_response_wrapper(
            presets.get_preset_by_id,
        )


class PresetsResourceWithStreamingResponse:
    def __init__(self, presets: PresetsResource) -> None:
        self._presets = presets

        self.create = to_streamed_response_wrapper(
            presets.create,
        )
        self.update = to_streamed_response_wrapper(
            presets.update,
        )
        self.delete = to_streamed_response_wrapper(
            presets.delete,
        )
        self.get = to_streamed_response_wrapper(
            presets.get,
        )
        self.get_preset_by_id = to_streamed_response_wrapper(
            presets.get_preset_by_id,
        )


class AsyncPresetsResourceWithStreamingResponse:
    def __init__(self, presets: AsyncPresetsResource) -> None:
        self._presets = presets

        self.create = async_to_streamed_response_wrapper(
            presets.create,
        )
        self.update = async_to_streamed_response_wrapper(
            presets.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            presets.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            presets.get,
        )
        self.get_preset_by_id = async_to_streamed_response_wrapper(
            presets.get_preset_by_id,
        )
