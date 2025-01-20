# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Optional, cast
from typing_extensions import Literal

import httpx

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
from .....pagination import SyncSinglePage, AsyncSinglePage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.devices.posture import integration_edit_params, integration_create_params
from .....types.zero_trust.devices.posture.integration import Integration
from .....types.zero_trust.devices.posture.integration_delete_response import IntegrationDeleteResponse

__all__ = ["IntegrationsResource", "AsyncIntegrationsResource"]


class IntegrationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return IntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return IntegrationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        config: integration_create_params.Config,
        interval: str,
        name: str,
        type: Literal[
            "workspace_one", "crowdstrike_s2s", "uptycs", "intune", "kolide", "tanium", "sentinelone_s2s", "custom_s2s"
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Integration]:
        """
        Create a new device posture integration.

        Args:
          config: The configuration object containing third-party integration information.

          interval: The interval between each posture check with the third-party API. Use `m` for
              minutes (e.g. `5m`) and `h` for hours (e.g. `12h`).

          name: The name of the device posture integration.

          type: The type of device posture integration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/devices/posture/integration",
            body=maybe_transform(
                {
                    "config": config,
                    "interval": interval,
                    "name": name,
                    "type": type,
                },
                integration_create_params.IntegrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Integration]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Integration]], ResultWrapper[Integration]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[Integration]:
        """
        Fetches the list of device posture integrations for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/devices/posture/integration",
            page=SyncSinglePage[Integration],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Integration,
        )

    def delete(
        self,
        integration_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IntegrationDeleteResponse]:
        """
        Delete a configured device posture integration.

        Args:
          integration_id: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return cast(
            Optional[IntegrationDeleteResponse],
            self._delete(
                f"/accounts/{account_id}/devices/posture/integration/{integration_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[IntegrationDeleteResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IntegrationDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def edit(
        self,
        integration_id: str,
        *,
        account_id: str,
        config: integration_edit_params.Config | NotGiven = NOT_GIVEN,
        interval: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        type: Literal[
            "workspace_one", "crowdstrike_s2s", "uptycs", "intune", "kolide", "tanium", "sentinelone_s2s", "custom_s2s"
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Integration]:
        """
        Updates a configured device posture integration.

        Args:
          integration_id: API UUID.

          config: The configuration object containing third-party integration information.

          interval: The interval between each posture check with the third-party API. Use `m` for
              minutes (e.g. `5m`) and `h` for hours (e.g. `12h`).

          name: The name of the device posture integration.

          type: The type of device posture integration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return self._patch(
            f"/accounts/{account_id}/devices/posture/integration/{integration_id}",
            body=maybe_transform(
                {
                    "config": config,
                    "interval": interval,
                    "name": name,
                    "type": type,
                },
                integration_edit_params.IntegrationEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Integration]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Integration]], ResultWrapper[Integration]),
        )

    def get(
        self,
        integration_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Integration]:
        """
        Fetches details for a single device posture integration.

        Args:
          integration_id: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return self._get(
            f"/accounts/{account_id}/devices/posture/integration/{integration_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Integration]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Integration]], ResultWrapper[Integration]),
        )


class AsyncIntegrationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncIntegrationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        config: integration_create_params.Config,
        interval: str,
        name: str,
        type: Literal[
            "workspace_one", "crowdstrike_s2s", "uptycs", "intune", "kolide", "tanium", "sentinelone_s2s", "custom_s2s"
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Integration]:
        """
        Create a new device posture integration.

        Args:
          config: The configuration object containing third-party integration information.

          interval: The interval between each posture check with the third-party API. Use `m` for
              minutes (e.g. `5m`) and `h` for hours (e.g. `12h`).

          name: The name of the device posture integration.

          type: The type of device posture integration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/devices/posture/integration",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "interval": interval,
                    "name": name,
                    "type": type,
                },
                integration_create_params.IntegrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Integration]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Integration]], ResultWrapper[Integration]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Integration, AsyncSinglePage[Integration]]:
        """
        Fetches the list of device posture integrations for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/devices/posture/integration",
            page=AsyncSinglePage[Integration],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Integration,
        )

    async def delete(
        self,
        integration_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IntegrationDeleteResponse]:
        """
        Delete a configured device posture integration.

        Args:
          integration_id: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return cast(
            Optional[IntegrationDeleteResponse],
            await self._delete(
                f"/accounts/{account_id}/devices/posture/integration/{integration_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[IntegrationDeleteResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[IntegrationDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def edit(
        self,
        integration_id: str,
        *,
        account_id: str,
        config: integration_edit_params.Config | NotGiven = NOT_GIVEN,
        interval: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        type: Literal[
            "workspace_one", "crowdstrike_s2s", "uptycs", "intune", "kolide", "tanium", "sentinelone_s2s", "custom_s2s"
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Integration]:
        """
        Updates a configured device posture integration.

        Args:
          integration_id: API UUID.

          config: The configuration object containing third-party integration information.

          interval: The interval between each posture check with the third-party API. Use `m` for
              minutes (e.g. `5m`) and `h` for hours (e.g. `12h`).

          name: The name of the device posture integration.

          type: The type of device posture integration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/devices/posture/integration/{integration_id}",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "interval": interval,
                    "name": name,
                    "type": type,
                },
                integration_edit_params.IntegrationEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Integration]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Integration]], ResultWrapper[Integration]),
        )

    async def get(
        self,
        integration_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Integration]:
        """
        Fetches details for a single device posture integration.

        Args:
          integration_id: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return await self._get(
            f"/accounts/{account_id}/devices/posture/integration/{integration_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[Integration]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[Integration]], ResultWrapper[Integration]),
        )


class IntegrationsResourceWithRawResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

        self.create = to_raw_response_wrapper(
            integrations.create,
        )
        self.list = to_raw_response_wrapper(
            integrations.list,
        )
        self.delete = to_raw_response_wrapper(
            integrations.delete,
        )
        self.edit = to_raw_response_wrapper(
            integrations.edit,
        )
        self.get = to_raw_response_wrapper(
            integrations.get,
        )


class AsyncIntegrationsResourceWithRawResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

        self.create = async_to_raw_response_wrapper(
            integrations.create,
        )
        self.list = async_to_raw_response_wrapper(
            integrations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            integrations.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            integrations.edit,
        )
        self.get = async_to_raw_response_wrapper(
            integrations.get,
        )


class IntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

        self.create = to_streamed_response_wrapper(
            integrations.create,
        )
        self.list = to_streamed_response_wrapper(
            integrations.list,
        )
        self.delete = to_streamed_response_wrapper(
            integrations.delete,
        )
        self.edit = to_streamed_response_wrapper(
            integrations.edit,
        )
        self.get = to_streamed_response_wrapper(
            integrations.get,
        )


class AsyncIntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

        self.create = async_to_streamed_response_wrapper(
            integrations.create,
        )
        self.list = async_to_streamed_response_wrapper(
            integrations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            integrations.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            integrations.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            integrations.get,
        )
