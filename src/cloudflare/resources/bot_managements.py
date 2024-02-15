# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types import BotManagementUpdateResponse, BotManagementGetResponse

from typing_extensions import Literal

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ..types import shared_params
from ..types import bot_management_update_params
from .._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["BotManagements", "AsyncBotManagements"]


class BotManagements(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BotManagementsWithRawResponse:
        return BotManagementsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BotManagementsWithStreamingResponse:
        return BotManagementsWithStreamingResponse(self)

    @overload
    def update(
        self,
        zone_id: str,
        *,
        enable_js: bool | NotGiven = NOT_GIVEN,
        fight_mode: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BotManagementUpdateResponse:
        """
        Updates the Bot Management configuration for a zone.

        This API is used to update:

        - **Bot Fight Mode**
        - **Super Bot Fight Mode**
        - **Bot Management for Enterprise**

        See [Bot Plans](https://developers.cloudflare.com/bots/plans/) for more
        information on the different plans

        Args:
          zone_id: Identifier

          enable_js: Use lightweight, invisible JavaScript detections to improve Bot Management.
              [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).

          fight_mode: Whether to enable Bot Fight Mode.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        zone_id: str,
        *,
        enable_js: bool | NotGiven = NOT_GIVEN,
        optimize_wordpress: bool | NotGiven = NOT_GIVEN,
        sbfm_definitely_automated: Literal["allow", "block", "managed_challenge"] | NotGiven = NOT_GIVEN,
        sbfm_static_resource_protection: bool | NotGiven = NOT_GIVEN,
        sbfm_verified_bots: Literal["allow", "block"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BotManagementUpdateResponse:
        """
        Updates the Bot Management configuration for a zone.

        This API is used to update:

        - **Bot Fight Mode**
        - **Super Bot Fight Mode**
        - **Bot Management for Enterprise**

        See [Bot Plans](https://developers.cloudflare.com/bots/plans/) for more
        information on the different plans

        Args:
          zone_id: Identifier

          enable_js: Use lightweight, invisible JavaScript detections to improve Bot Management.
              [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).

          optimize_wordpress: Whether to optimize Super Bot Fight Mode protections for Wordpress.

          sbfm_definitely_automated: Super Bot Fight Mode (SBFM) action to take on definitely automated requests.

          sbfm_static_resource_protection: Super Bot Fight Mode (SBFM) to enable static resource protection. Enable if
              static resources on your application need bot protection. Note: Static resource
              protection can also result in legitimate traffic being blocked.

          sbfm_verified_bots: Super Bot Fight Mode (SBFM) action to take on verified bots requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        zone_id: str,
        *,
        enable_js: bool | NotGiven = NOT_GIVEN,
        optimize_wordpress: bool | NotGiven = NOT_GIVEN,
        sbfm_definitely_automated: Literal["allow", "block", "managed_challenge"] | NotGiven = NOT_GIVEN,
        sbfm_likely_automated: Literal["allow", "block", "managed_challenge"] | NotGiven = NOT_GIVEN,
        sbfm_static_resource_protection: bool | NotGiven = NOT_GIVEN,
        sbfm_verified_bots: Literal["allow", "block"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BotManagementUpdateResponse:
        """
        Updates the Bot Management configuration for a zone.

        This API is used to update:

        - **Bot Fight Mode**
        - **Super Bot Fight Mode**
        - **Bot Management for Enterprise**

        See [Bot Plans](https://developers.cloudflare.com/bots/plans/) for more
        information on the different plans

        Args:
          zone_id: Identifier

          enable_js: Use lightweight, invisible JavaScript detections to improve Bot Management.
              [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).

          optimize_wordpress: Whether to optimize Super Bot Fight Mode protections for Wordpress.

          sbfm_definitely_automated: Super Bot Fight Mode (SBFM) action to take on definitely automated requests.

          sbfm_likely_automated: Super Bot Fight Mode (SBFM) action to take on likely automated requests.

          sbfm_static_resource_protection: Super Bot Fight Mode (SBFM) to enable static resource protection. Enable if
              static resources on your application need bot protection. Note: Static resource
              protection can also result in legitimate traffic being blocked.

          sbfm_verified_bots: Super Bot Fight Mode (SBFM) action to take on verified bots requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        zone_id: str,
        *,
        auto_update_model: bool | NotGiven = NOT_GIVEN,
        enable_js: bool | NotGiven = NOT_GIVEN,
        suppress_session_score: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BotManagementUpdateResponse:
        """
        Updates the Bot Management configuration for a zone.

        This API is used to update:

        - **Bot Fight Mode**
        - **Super Bot Fight Mode**
        - **Bot Management for Enterprise**

        See [Bot Plans](https://developers.cloudflare.com/bots/plans/) for more
        information on the different plans

        Args:
          zone_id: Identifier

          auto_update_model: Automatically update to the newest bot detection models created by Cloudflare as
              they are released.
              [Learn more.](https://developers.cloudflare.com/bots/reference/machine-learning-models#model-versions-and-release-notes)

          enable_js: Use lightweight, invisible JavaScript detections to improve Bot Management.
              [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).

          suppress_session_score: Whether to disable tracking the highest bot score for a session in the Bot
              Management cookie.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    def update(
        self,
        zone_id: str,
        *,
        enable_js: bool | NotGiven = NOT_GIVEN,
        fight_mode: bool | NotGiven = NOT_GIVEN,
        optimize_wordpress: bool | NotGiven = NOT_GIVEN,
        sbfm_definitely_automated: Literal["allow", "block", "managed_challenge"] | NotGiven = NOT_GIVEN,
        sbfm_static_resource_protection: bool | NotGiven = NOT_GIVEN,
        sbfm_verified_bots: Literal["allow", "block"] | NotGiven = NOT_GIVEN,
        sbfm_likely_automated: Literal["allow", "block", "managed_challenge"] | NotGiven = NOT_GIVEN,
        auto_update_model: bool | NotGiven = NOT_GIVEN,
        suppress_session_score: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BotManagementUpdateResponse:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            BotManagementUpdateResponse,
            self._put(
                f"/zones/{zone_id}/bot_management",
                body=maybe_transform(
                    {
                        "enable_js": enable_js,
                        "fight_mode": fight_mode,
                        "optimize_wordpress": optimize_wordpress,
                        "sbfm_definitely_automated": sbfm_definitely_automated,
                        "sbfm_static_resource_protection": sbfm_static_resource_protection,
                        "sbfm_verified_bots": sbfm_verified_bots,
                        "sbfm_likely_automated": sbfm_likely_automated,
                        "auto_update_model": auto_update_model,
                        "suppress_session_score": suppress_session_score,
                    },
                    bot_management_update_params.BotManagementUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[BotManagementUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BotManagementGetResponse:
        """
        Retrieve a zone's Bot Management Config

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            BotManagementGetResponse,
            self._get(
                f"/zones/{zone_id}/bot_management",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[BotManagementGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncBotManagements(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBotManagementsWithRawResponse:
        return AsyncBotManagementsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBotManagementsWithStreamingResponse:
        return AsyncBotManagementsWithStreamingResponse(self)

    @overload
    async def update(
        self,
        zone_id: str,
        *,
        enable_js: bool | NotGiven = NOT_GIVEN,
        fight_mode: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BotManagementUpdateResponse:
        """
        Updates the Bot Management configuration for a zone.

        This API is used to update:

        - **Bot Fight Mode**
        - **Super Bot Fight Mode**
        - **Bot Management for Enterprise**

        See [Bot Plans](https://developers.cloudflare.com/bots/plans/) for more
        information on the different plans

        Args:
          zone_id: Identifier

          enable_js: Use lightweight, invisible JavaScript detections to improve Bot Management.
              [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).

          fight_mode: Whether to enable Bot Fight Mode.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        zone_id: str,
        *,
        enable_js: bool | NotGiven = NOT_GIVEN,
        optimize_wordpress: bool | NotGiven = NOT_GIVEN,
        sbfm_definitely_automated: Literal["allow", "block", "managed_challenge"] | NotGiven = NOT_GIVEN,
        sbfm_static_resource_protection: bool | NotGiven = NOT_GIVEN,
        sbfm_verified_bots: Literal["allow", "block"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BotManagementUpdateResponse:
        """
        Updates the Bot Management configuration for a zone.

        This API is used to update:

        - **Bot Fight Mode**
        - **Super Bot Fight Mode**
        - **Bot Management for Enterprise**

        See [Bot Plans](https://developers.cloudflare.com/bots/plans/) for more
        information on the different plans

        Args:
          zone_id: Identifier

          enable_js: Use lightweight, invisible JavaScript detections to improve Bot Management.
              [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).

          optimize_wordpress: Whether to optimize Super Bot Fight Mode protections for Wordpress.

          sbfm_definitely_automated: Super Bot Fight Mode (SBFM) action to take on definitely automated requests.

          sbfm_static_resource_protection: Super Bot Fight Mode (SBFM) to enable static resource protection. Enable if
              static resources on your application need bot protection. Note: Static resource
              protection can also result in legitimate traffic being blocked.

          sbfm_verified_bots: Super Bot Fight Mode (SBFM) action to take on verified bots requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        zone_id: str,
        *,
        enable_js: bool | NotGiven = NOT_GIVEN,
        optimize_wordpress: bool | NotGiven = NOT_GIVEN,
        sbfm_definitely_automated: Literal["allow", "block", "managed_challenge"] | NotGiven = NOT_GIVEN,
        sbfm_likely_automated: Literal["allow", "block", "managed_challenge"] | NotGiven = NOT_GIVEN,
        sbfm_static_resource_protection: bool | NotGiven = NOT_GIVEN,
        sbfm_verified_bots: Literal["allow", "block"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BotManagementUpdateResponse:
        """
        Updates the Bot Management configuration for a zone.

        This API is used to update:

        - **Bot Fight Mode**
        - **Super Bot Fight Mode**
        - **Bot Management for Enterprise**

        See [Bot Plans](https://developers.cloudflare.com/bots/plans/) for more
        information on the different plans

        Args:
          zone_id: Identifier

          enable_js: Use lightweight, invisible JavaScript detections to improve Bot Management.
              [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).

          optimize_wordpress: Whether to optimize Super Bot Fight Mode protections for Wordpress.

          sbfm_definitely_automated: Super Bot Fight Mode (SBFM) action to take on definitely automated requests.

          sbfm_likely_automated: Super Bot Fight Mode (SBFM) action to take on likely automated requests.

          sbfm_static_resource_protection: Super Bot Fight Mode (SBFM) to enable static resource protection. Enable if
              static resources on your application need bot protection. Note: Static resource
              protection can also result in legitimate traffic being blocked.

          sbfm_verified_bots: Super Bot Fight Mode (SBFM) action to take on verified bots requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        zone_id: str,
        *,
        auto_update_model: bool | NotGiven = NOT_GIVEN,
        enable_js: bool | NotGiven = NOT_GIVEN,
        suppress_session_score: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BotManagementUpdateResponse:
        """
        Updates the Bot Management configuration for a zone.

        This API is used to update:

        - **Bot Fight Mode**
        - **Super Bot Fight Mode**
        - **Bot Management for Enterprise**

        See [Bot Plans](https://developers.cloudflare.com/bots/plans/) for more
        information on the different plans

        Args:
          zone_id: Identifier

          auto_update_model: Automatically update to the newest bot detection models created by Cloudflare as
              they are released.
              [Learn more.](https://developers.cloudflare.com/bots/reference/machine-learning-models#model-versions-and-release-notes)

          enable_js: Use lightweight, invisible JavaScript detections to improve Bot Management.
              [Learn more about JavaScript Detections](https://developers.cloudflare.com/bots/reference/javascript-detections/).

          suppress_session_score: Whether to disable tracking the highest bot score for a session in the Bot
              Management cookie.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    async def update(
        self,
        zone_id: str,
        *,
        enable_js: bool | NotGiven = NOT_GIVEN,
        fight_mode: bool | NotGiven = NOT_GIVEN,
        optimize_wordpress: bool | NotGiven = NOT_GIVEN,
        sbfm_definitely_automated: Literal["allow", "block", "managed_challenge"] | NotGiven = NOT_GIVEN,
        sbfm_static_resource_protection: bool | NotGiven = NOT_GIVEN,
        sbfm_verified_bots: Literal["allow", "block"] | NotGiven = NOT_GIVEN,
        sbfm_likely_automated: Literal["allow", "block", "managed_challenge"] | NotGiven = NOT_GIVEN,
        auto_update_model: bool | NotGiven = NOT_GIVEN,
        suppress_session_score: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BotManagementUpdateResponse:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            BotManagementUpdateResponse,
            await self._put(
                f"/zones/{zone_id}/bot_management",
                body=maybe_transform(
                    {
                        "enable_js": enable_js,
                        "fight_mode": fight_mode,
                        "optimize_wordpress": optimize_wordpress,
                        "sbfm_definitely_automated": sbfm_definitely_automated,
                        "sbfm_static_resource_protection": sbfm_static_resource_protection,
                        "sbfm_verified_bots": sbfm_verified_bots,
                        "sbfm_likely_automated": sbfm_likely_automated,
                        "auto_update_model": auto_update_model,
                        "suppress_session_score": suppress_session_score,
                    },
                    bot_management_update_params.BotManagementUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[BotManagementUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BotManagementGetResponse:
        """
        Retrieve a zone's Bot Management Config

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            BotManagementGetResponse,
            await self._get(
                f"/zones/{zone_id}/bot_management",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[BotManagementGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class BotManagementsWithRawResponse:
    def __init__(self, bot_managements: BotManagements) -> None:
        self._bot_managements = bot_managements

        self.update = to_raw_response_wrapper(
            bot_managements.update,
        )
        self.get = to_raw_response_wrapper(
            bot_managements.get,
        )


class AsyncBotManagementsWithRawResponse:
    def __init__(self, bot_managements: AsyncBotManagements) -> None:
        self._bot_managements = bot_managements

        self.update = async_to_raw_response_wrapper(
            bot_managements.update,
        )
        self.get = async_to_raw_response_wrapper(
            bot_managements.get,
        )


class BotManagementsWithStreamingResponse:
    def __init__(self, bot_managements: BotManagements) -> None:
        self._bot_managements = bot_managements

        self.update = to_streamed_response_wrapper(
            bot_managements.update,
        )
        self.get = to_streamed_response_wrapper(
            bot_managements.get,
        )


class AsyncBotManagementsWithStreamingResponse:
    def __init__(self, bot_managements: AsyncBotManagements) -> None:
        self._bot_managements = bot_managements

        self.update = async_to_streamed_response_wrapper(
            bot_managements.update,
        )
        self.get = async_to_streamed_response_wrapper(
            bot_managements.get,
        )
