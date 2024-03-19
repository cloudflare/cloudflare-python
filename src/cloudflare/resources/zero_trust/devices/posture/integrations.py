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
from ....._base_client import (
    make_request_options,
)
from .....types.zero_trust.devices.posture import (
    IntegrationListResponse,
    IntegrationDeleteResponse,
    TeamsDevicesDevicePostureIntegrations,
    integration_edit_params,
    integration_create_params,
)

__all__ = ["Integrations", "AsyncIntegrations"]


class Integrations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IntegrationsWithRawResponse:
        return IntegrationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntegrationsWithStreamingResponse:
        return IntegrationsWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: object,
        config: integration_create_params.Config,
        interval: str,
        name: str,
        type: Literal["workspace_one", "crowdstrike_s2s", "uptycs", "intune", "kolide", "tanium", "sentinelone_s2s"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesDevicePostureIntegrations]:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TeamsDevicesDevicePostureIntegrations]],
                ResultWrapper[TeamsDevicesDevicePostureIntegrations],
            ),
        )

    def list(
        self,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IntegrationListResponse]:
        """
        Fetches the list of device posture integrations for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/devices/posture/integration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IntegrationListResponse]], ResultWrapper[IntegrationListResponse]),
        )

    def delete(
        self,
        integration_id: str,
        *,
        account_id: object,
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
                    post_parser=ResultWrapper._unwrapper,
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
        account_id: object,
        config: integration_edit_params.Config | NotGiven = NOT_GIVEN,
        interval: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        type: Literal["workspace_one", "crowdstrike_s2s", "uptycs", "intune", "kolide", "tanium", "sentinelone_s2s"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesDevicePostureIntegrations]:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TeamsDevicesDevicePostureIntegrations]],
                ResultWrapper[TeamsDevicesDevicePostureIntegrations],
            ),
        )

    def get(
        self,
        integration_id: str,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesDevicePostureIntegrations]:
        """
        Fetches details for a single device posture integration.

        Args:
          integration_id: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return self._get(
            f"/accounts/{account_id}/devices/posture/integration/{integration_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TeamsDevicesDevicePostureIntegrations]],
                ResultWrapper[TeamsDevicesDevicePostureIntegrations],
            ),
        )


class AsyncIntegrations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIntegrationsWithRawResponse:
        return AsyncIntegrationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntegrationsWithStreamingResponse:
        return AsyncIntegrationsWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: object,
        config: integration_create_params.Config,
        interval: str,
        name: str,
        type: Literal["workspace_one", "crowdstrike_s2s", "uptycs", "intune", "kolide", "tanium", "sentinelone_s2s"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesDevicePostureIntegrations]:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TeamsDevicesDevicePostureIntegrations]],
                ResultWrapper[TeamsDevicesDevicePostureIntegrations],
            ),
        )

    async def list(
        self,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IntegrationListResponse]:
        """
        Fetches the list of device posture integrations for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/devices/posture/integration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IntegrationListResponse]], ResultWrapper[IntegrationListResponse]),
        )

    async def delete(
        self,
        integration_id: str,
        *,
        account_id: object,
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
                    post_parser=ResultWrapper._unwrapper,
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
        account_id: object,
        config: integration_edit_params.Config | NotGiven = NOT_GIVEN,
        interval: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        type: Literal["workspace_one", "crowdstrike_s2s", "uptycs", "intune", "kolide", "tanium", "sentinelone_s2s"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesDevicePostureIntegrations]:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TeamsDevicesDevicePostureIntegrations]],
                ResultWrapper[TeamsDevicesDevicePostureIntegrations],
            ),
        )

    async def get(
        self,
        integration_id: str,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesDevicePostureIntegrations]:
        """
        Fetches details for a single device posture integration.

        Args:
          integration_id: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return await self._get(
            f"/accounts/{account_id}/devices/posture/integration/{integration_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[TeamsDevicesDevicePostureIntegrations]],
                ResultWrapper[TeamsDevicesDevicePostureIntegrations],
            ),
        )


class IntegrationsWithRawResponse:
    def __init__(self, integrations: Integrations) -> None:
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


class AsyncIntegrationsWithRawResponse:
    def __init__(self, integrations: AsyncIntegrations) -> None:
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


class IntegrationsWithStreamingResponse:
    def __init__(self, integrations: Integrations) -> None:
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


class AsyncIntegrationsWithStreamingResponse:
    def __init__(self, integrations: AsyncIntegrations) -> None:
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
