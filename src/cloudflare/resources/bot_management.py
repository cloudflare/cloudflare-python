# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast
from typing_extensions import Literal, overload

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from .._base_client import make_request_options
from ..types.bot_management import bot_management_update_params
from ..types.bot_management.bot_management_get_response import BotManagementGetResponse
from ..types.bot_management.bot_management_update_response import BotManagementUpdateResponse

__all__ = ["BotManagementResource", "AsyncBotManagementResource"]


class BotManagementResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BotManagementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BotManagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BotManagementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BotManagementResourceWithStreamingResponse(self)

    @overload
    def update(
        self,
        *,
        zone_id: str,
        ai_bots_protection: Literal["block", "disabled"] | NotGiven = NOT_GIVEN,
        enable_js: bool | NotGiven = NOT_GIVEN,
        fight_mode: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BotManagementUpdateResponse]:
        """
        Updates the Bot Management configuration for a zone.

        This API is used to update:

        - **Bot Fight Mode**
        - **Super Bot Fight Mode**
        - **Bot Management for Enterprise**

        See [Bot Plans](https://developers.cloudflare.com/bots/plans/) for more
        information on the different plans \\
        If you recently upgraded or downgraded your plan, refer to the following examples
        to clean up old configurations. Copy and paste the example body to remove old zone
        configurations based on your current plan.

        #### Clean up configuration for Bot Fight Mode plan

        ```json
        {
          "sbfm_likely_automated": "allow",
          "sbfm_definitely_automated": "allow",
          "sbfm_verified_bots": "allow",
          "sbfm_static_resource_protection": false,
          "optimize_wordpress": false,
          "suppress_session_score": false
        }
        ```

        #### Clean up configuration for SBFM Pro plan

        ```json
        {
          "sbfm_likely_automated": "allow",
          "fight_mode": false
        }
        ```

        #### Clean up configuration for SBFM Biz plan

        ```json
        {
          "fight_mode": false
        }
        ```

        #### Clean up configuration for BM Enterprise Subscription plan

        It is strongly recommended that you ensure you have
        [custom rules](https://developers.cloudflare.com/waf/custom-rules/) in place to
        protect your zone before disabling the SBFM rules. Without these protections,
        your zone is vulnerable to attacks.

        ```json
        {
          "sbfm_likely_automated": "allow",
          "sbfm_definitely_automated": "allow",
          "sbfm_verified_bots": "allow",
          "sbfm_static_resource_protection": false,
          "optimize_wordpress": false,
          "fight_mode": false
        }
        ```

        Args:
          zone_id: Identifier

          ai_bots_protection: Enable rule to block AI Scrapers and Crawlers.

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
        *,
        zone_id: str,
        ai_bots_protection: Literal["block", "disabled"] | NotGiven = NOT_GIVEN,
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
    ) -> Optional[BotManagementUpdateResponse]:
        """
        Updates the Bot Management configuration for a zone.

        This API is used to update:

        - **Bot Fight Mode**
        - **Super Bot Fight Mode**
        - **Bot Management for Enterprise**

        See [Bot Plans](https://developers.cloudflare.com/bots/plans/) for more
        information on the different plans \\
        If you recently upgraded or downgraded your plan, refer to the following examples
        to clean up old configurations. Copy and paste the example body to remove old zone
        configurations based on your current plan.

        #### Clean up configuration for Bot Fight Mode plan

        ```json
        {
          "sbfm_likely_automated": "allow",
          "sbfm_definitely_automated": "allow",
          "sbfm_verified_bots": "allow",
          "sbfm_static_resource_protection": false,
          "optimize_wordpress": false,
          "suppress_session_score": false
        }
        ```

        #### Clean up configuration for SBFM Pro plan

        ```json
        {
          "sbfm_likely_automated": "allow",
          "fight_mode": false
        }
        ```

        #### Clean up configuration for SBFM Biz plan

        ```json
        {
          "fight_mode": false
        }
        ```

        #### Clean up configuration for BM Enterprise Subscription plan

        It is strongly recommended that you ensure you have
        [custom rules](https://developers.cloudflare.com/waf/custom-rules/) in place to
        protect your zone before disabling the SBFM rules. Without these protections,
        your zone is vulnerable to attacks.

        ```json
        {
          "sbfm_likely_automated": "allow",
          "sbfm_definitely_automated": "allow",
          "sbfm_verified_bots": "allow",
          "sbfm_static_resource_protection": false,
          "optimize_wordpress": false,
          "fight_mode": false
        }
        ```

        Args:
          zone_id: Identifier

          ai_bots_protection: Enable rule to block AI Scrapers and Crawlers.

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
        *,
        zone_id: str,
        ai_bots_protection: Literal["block", "disabled"] | NotGiven = NOT_GIVEN,
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
    ) -> Optional[BotManagementUpdateResponse]:
        """
        Updates the Bot Management configuration for a zone.

        This API is used to update:

        - **Bot Fight Mode**
        - **Super Bot Fight Mode**
        - **Bot Management for Enterprise**

        See [Bot Plans](https://developers.cloudflare.com/bots/plans/) for more
        information on the different plans \\
        If you recently upgraded or downgraded your plan, refer to the following examples
        to clean up old configurations. Copy and paste the example body to remove old zone
        configurations based on your current plan.

        #### Clean up configuration for Bot Fight Mode plan

        ```json
        {
          "sbfm_likely_automated": "allow",
          "sbfm_definitely_automated": "allow",
          "sbfm_verified_bots": "allow",
          "sbfm_static_resource_protection": false,
          "optimize_wordpress": false,
          "suppress_session_score": false
        }
        ```

        #### Clean up configuration for SBFM Pro plan

        ```json
        {
          "sbfm_likely_automated": "allow",
          "fight_mode": false
        }
        ```

        #### Clean up configuration for SBFM Biz plan

        ```json
        {
          "fight_mode": false
        }
        ```

        #### Clean up configuration for BM Enterprise Subscription plan

        It is strongly recommended that you ensure you have
        [custom rules](https://developers.cloudflare.com/waf/custom-rules/) in place to
        protect your zone before disabling the SBFM rules. Without these protections,
        your zone is vulnerable to attacks.

        ```json
        {
          "sbfm_likely_automated": "allow",
          "sbfm_definitely_automated": "allow",
          "sbfm_verified_bots": "allow",
          "sbfm_static_resource_protection": false,
          "optimize_wordpress": false,
          "fight_mode": false
        }
        ```

        Args:
          zone_id: Identifier

          ai_bots_protection: Enable rule to block AI Scrapers and Crawlers.

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
        *,
        zone_id: str,
        ai_bots_protection: Literal["block", "disabled"] | NotGiven = NOT_GIVEN,
        auto_update_model: bool | NotGiven = NOT_GIVEN,
        enable_js: bool | NotGiven = NOT_GIVEN,
        suppress_session_score: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BotManagementUpdateResponse]:
        """
        Updates the Bot Management configuration for a zone.

        This API is used to update:

        - **Bot Fight Mode**
        - **Super Bot Fight Mode**
        - **Bot Management for Enterprise**

        See [Bot Plans](https://developers.cloudflare.com/bots/plans/) for more
        information on the different plans \\
        If you recently upgraded or downgraded your plan, refer to the following examples
        to clean up old configurations. Copy and paste the example body to remove old zone
        configurations based on your current plan.

        #### Clean up configuration for Bot Fight Mode plan

        ```json
        {
          "sbfm_likely_automated": "allow",
          "sbfm_definitely_automated": "allow",
          "sbfm_verified_bots": "allow",
          "sbfm_static_resource_protection": false,
          "optimize_wordpress": false,
          "suppress_session_score": false
        }
        ```

        #### Clean up configuration for SBFM Pro plan

        ```json
        {
          "sbfm_likely_automated": "allow",
          "fight_mode": false
        }
        ```

        #### Clean up configuration for SBFM Biz plan

        ```json
        {
          "fight_mode": false
        }
        ```

        #### Clean up configuration for BM Enterprise Subscription plan

        It is strongly recommended that you ensure you have
        [custom rules](https://developers.cloudflare.com/waf/custom-rules/) in place to
        protect your zone before disabling the SBFM rules. Without these protections,
        your zone is vulnerable to attacks.

        ```json
        {
          "sbfm_likely_automated": "allow",
          "sbfm_definitely_automated": "allow",
          "sbfm_verified_bots": "allow",
          "sbfm_static_resource_protection": false,
          "optimize_wordpress": false,
          "fight_mode": false
        }
        ```

        Args:
          zone_id: Identifier

          ai_bots_protection: Enable rule to block AI Scrapers and Crawlers.

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

    @required_args(["zone_id"])
    def update(
        self,
        *,
        zone_id: str,
        ai_bots_protection: Literal["block", "disabled"] | NotGiven = NOT_GIVEN,
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
    ) -> Optional[BotManagementUpdateResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            Optional[BotManagementUpdateResponse],
            self._put(
                f"/zones/{zone_id}/bot_management",
                body=maybe_transform(
                    {
                        "ai_bots_protection": ai_bots_protection,
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
                    post_parser=ResultWrapper[Optional[BotManagementUpdateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[BotManagementUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BotManagementGetResponse]:
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
            Optional[BotManagementGetResponse],
            self._get(
                f"/zones/{zone_id}/bot_management",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[BotManagementGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[BotManagementGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncBotManagementResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBotManagementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBotManagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBotManagementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBotManagementResourceWithStreamingResponse(self)

    @overload
    async def update(
        self,
        *,
        zone_id: str,
        ai_bots_protection: Literal["block", "disabled"] | NotGiven = NOT_GIVEN,
        enable_js: bool | NotGiven = NOT_GIVEN,
        fight_mode: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BotManagementUpdateResponse]:
        """
        Updates the Bot Management configuration for a zone.

        This API is used to update:

        - **Bot Fight Mode**
        - **Super Bot Fight Mode**
        - **Bot Management for Enterprise**

        See [Bot Plans](https://developers.cloudflare.com/bots/plans/) for more
        information on the different plans \\
        If you recently upgraded or downgraded your plan, refer to the following examples
        to clean up old configurations. Copy and paste the example body to remove old zone
        configurations based on your current plan.

        #### Clean up configuration for Bot Fight Mode plan

        ```json
        {
          "sbfm_likely_automated": "allow",
          "sbfm_definitely_automated": "allow",
          "sbfm_verified_bots": "allow",
          "sbfm_static_resource_protection": false,
          "optimize_wordpress": false,
          "suppress_session_score": false
        }
        ```

        #### Clean up configuration for SBFM Pro plan

        ```json
        {
          "sbfm_likely_automated": "allow",
          "fight_mode": false
        }
        ```

        #### Clean up configuration for SBFM Biz plan

        ```json
        {
          "fight_mode": false
        }
        ```

        #### Clean up configuration for BM Enterprise Subscription plan

        It is strongly recommended that you ensure you have
        [custom rules](https://developers.cloudflare.com/waf/custom-rules/) in place to
        protect your zone before disabling the SBFM rules. Without these protections,
        your zone is vulnerable to attacks.

        ```json
        {
          "sbfm_likely_automated": "allow",
          "sbfm_definitely_automated": "allow",
          "sbfm_verified_bots": "allow",
          "sbfm_static_resource_protection": false,
          "optimize_wordpress": false,
          "fight_mode": false
        }
        ```

        Args:
          zone_id: Identifier

          ai_bots_protection: Enable rule to block AI Scrapers and Crawlers.

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
        *,
        zone_id: str,
        ai_bots_protection: Literal["block", "disabled"] | NotGiven = NOT_GIVEN,
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
    ) -> Optional[BotManagementUpdateResponse]:
        """
        Updates the Bot Management configuration for a zone.

        This API is used to update:

        - **Bot Fight Mode**
        - **Super Bot Fight Mode**
        - **Bot Management for Enterprise**

        See [Bot Plans](https://developers.cloudflare.com/bots/plans/) for more
        information on the different plans \\
        If you recently upgraded or downgraded your plan, refer to the following examples
        to clean up old configurations. Copy and paste the example body to remove old zone
        configurations based on your current plan.

        #### Clean up configuration for Bot Fight Mode plan

        ```json
        {
          "sbfm_likely_automated": "allow",
          "sbfm_definitely_automated": "allow",
          "sbfm_verified_bots": "allow",
          "sbfm_static_resource_protection": false,
          "optimize_wordpress": false,
          "suppress_session_score": false
        }
        ```

        #### Clean up configuration for SBFM Pro plan

        ```json
        {
          "sbfm_likely_automated": "allow",
          "fight_mode": false
        }
        ```

        #### Clean up configuration for SBFM Biz plan

        ```json
        {
          "fight_mode": false
        }
        ```

        #### Clean up configuration for BM Enterprise Subscription plan

        It is strongly recommended that you ensure you have
        [custom rules](https://developers.cloudflare.com/waf/custom-rules/) in place to
        protect your zone before disabling the SBFM rules. Without these protections,
        your zone is vulnerable to attacks.

        ```json
        {
          "sbfm_likely_automated": "allow",
          "sbfm_definitely_automated": "allow",
          "sbfm_verified_bots": "allow",
          "sbfm_static_resource_protection": false,
          "optimize_wordpress": false,
          "fight_mode": false
        }
        ```

        Args:
          zone_id: Identifier

          ai_bots_protection: Enable rule to block AI Scrapers and Crawlers.

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
        *,
        zone_id: str,
        ai_bots_protection: Literal["block", "disabled"] | NotGiven = NOT_GIVEN,
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
    ) -> Optional[BotManagementUpdateResponse]:
        """
        Updates the Bot Management configuration for a zone.

        This API is used to update:

        - **Bot Fight Mode**
        - **Super Bot Fight Mode**
        - **Bot Management for Enterprise**

        See [Bot Plans](https://developers.cloudflare.com/bots/plans/) for more
        information on the different plans \\
        If you recently upgraded or downgraded your plan, refer to the following examples
        to clean up old configurations. Copy and paste the example body to remove old zone
        configurations based on your current plan.

        #### Clean up configuration for Bot Fight Mode plan

        ```json
        {
          "sbfm_likely_automated": "allow",
          "sbfm_definitely_automated": "allow",
          "sbfm_verified_bots": "allow",
          "sbfm_static_resource_protection": false,
          "optimize_wordpress": false,
          "suppress_session_score": false
        }
        ```

        #### Clean up configuration for SBFM Pro plan

        ```json
        {
          "sbfm_likely_automated": "allow",
          "fight_mode": false
        }
        ```

        #### Clean up configuration for SBFM Biz plan

        ```json
        {
          "fight_mode": false
        }
        ```

        #### Clean up configuration for BM Enterprise Subscription plan

        It is strongly recommended that you ensure you have
        [custom rules](https://developers.cloudflare.com/waf/custom-rules/) in place to
        protect your zone before disabling the SBFM rules. Without these protections,
        your zone is vulnerable to attacks.

        ```json
        {
          "sbfm_likely_automated": "allow",
          "sbfm_definitely_automated": "allow",
          "sbfm_verified_bots": "allow",
          "sbfm_static_resource_protection": false,
          "optimize_wordpress": false,
          "fight_mode": false
        }
        ```

        Args:
          zone_id: Identifier

          ai_bots_protection: Enable rule to block AI Scrapers and Crawlers.

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
        *,
        zone_id: str,
        ai_bots_protection: Literal["block", "disabled"] | NotGiven = NOT_GIVEN,
        auto_update_model: bool | NotGiven = NOT_GIVEN,
        enable_js: bool | NotGiven = NOT_GIVEN,
        suppress_session_score: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BotManagementUpdateResponse]:
        """
        Updates the Bot Management configuration for a zone.

        This API is used to update:

        - **Bot Fight Mode**
        - **Super Bot Fight Mode**
        - **Bot Management for Enterprise**

        See [Bot Plans](https://developers.cloudflare.com/bots/plans/) for more
        information on the different plans \\
        If you recently upgraded or downgraded your plan, refer to the following examples
        to clean up old configurations. Copy and paste the example body to remove old zone
        configurations based on your current plan.

        #### Clean up configuration for Bot Fight Mode plan

        ```json
        {
          "sbfm_likely_automated": "allow",
          "sbfm_definitely_automated": "allow",
          "sbfm_verified_bots": "allow",
          "sbfm_static_resource_protection": false,
          "optimize_wordpress": false,
          "suppress_session_score": false
        }
        ```

        #### Clean up configuration for SBFM Pro plan

        ```json
        {
          "sbfm_likely_automated": "allow",
          "fight_mode": false
        }
        ```

        #### Clean up configuration for SBFM Biz plan

        ```json
        {
          "fight_mode": false
        }
        ```

        #### Clean up configuration for BM Enterprise Subscription plan

        It is strongly recommended that you ensure you have
        [custom rules](https://developers.cloudflare.com/waf/custom-rules/) in place to
        protect your zone before disabling the SBFM rules. Without these protections,
        your zone is vulnerable to attacks.

        ```json
        {
          "sbfm_likely_automated": "allow",
          "sbfm_definitely_automated": "allow",
          "sbfm_verified_bots": "allow",
          "sbfm_static_resource_protection": false,
          "optimize_wordpress": false,
          "fight_mode": false
        }
        ```

        Args:
          zone_id: Identifier

          ai_bots_protection: Enable rule to block AI Scrapers and Crawlers.

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

    @required_args(["zone_id"])
    async def update(
        self,
        *,
        zone_id: str,
        ai_bots_protection: Literal["block", "disabled"] | NotGiven = NOT_GIVEN,
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
    ) -> Optional[BotManagementUpdateResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            Optional[BotManagementUpdateResponse],
            await self._put(
                f"/zones/{zone_id}/bot_management",
                body=await async_maybe_transform(
                    {
                        "ai_bots_protection": ai_bots_protection,
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
                    post_parser=ResultWrapper[Optional[BotManagementUpdateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[BotManagementUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[BotManagementGetResponse]:
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
            Optional[BotManagementGetResponse],
            await self._get(
                f"/zones/{zone_id}/bot_management",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[BotManagementGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[BotManagementGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class BotManagementResourceWithRawResponse:
    def __init__(self, bot_management: BotManagementResource) -> None:
        self._bot_management = bot_management

        self.update = to_raw_response_wrapper(
            bot_management.update,
        )
        self.get = to_raw_response_wrapper(
            bot_management.get,
        )


class AsyncBotManagementResourceWithRawResponse:
    def __init__(self, bot_management: AsyncBotManagementResource) -> None:
        self._bot_management = bot_management

        self.update = async_to_raw_response_wrapper(
            bot_management.update,
        )
        self.get = async_to_raw_response_wrapper(
            bot_management.get,
        )


class BotManagementResourceWithStreamingResponse:
    def __init__(self, bot_management: BotManagementResource) -> None:
        self._bot_management = bot_management

        self.update = to_streamed_response_wrapper(
            bot_management.update,
        )
        self.get = to_streamed_response_wrapper(
            bot_management.get,
        )


class AsyncBotManagementResourceWithStreamingResponse:
    def __init__(self, bot_management: AsyncBotManagementResource) -> None:
        self._bot_management = bot_management

        self.update = async_to_streamed_response_wrapper(
            bot_management.update,
        )
        self.get = async_to_streamed_response_wrapper(
            bot_management.get,
        )
