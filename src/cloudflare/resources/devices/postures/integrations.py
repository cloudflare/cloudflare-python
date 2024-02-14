# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, Type, Optional, cast
from typing_extensions import Literal

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
from ....types.devices.postures import (
    IntegrationGetResponse,
    IntegrationDeleteResponse,
    IntegrationUpdateResponse,
    IntegrationDevicePostureIntegrationsListDevicePostureIntegrationsResponse,
    IntegrationDevicePostureIntegrationsCreateDevicePostureIntegrationResponse,
    integration_update_params,
    integration_device_posture_integrations_create_device_posture_integration_params,
)

__all__ = ["Integrations", "AsyncIntegrations"]


class Integrations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IntegrationsWithRawResponse:
        return IntegrationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntegrationsWithStreamingResponse:
        return IntegrationsWithStreamingResponse(self)

    def update(
        self,
        uuid: str,
        *,
        identifier: object,
        config: integration_update_params.Config | NotGiven = NOT_GIVEN,
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
    ) -> Optional[IntegrationUpdateResponse]:
        """
        Updates a configured device posture integration.

        Args:
          uuid: API UUID.

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
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._patch(
            f"/accounts/{identifier}/devices/posture/integration/{uuid}",
            body=maybe_transform(
                {
                    "config": config,
                    "interval": interval,
                    "name": name,
                    "type": type,
                },
                integration_update_params.IntegrationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IntegrationUpdateResponse]], ResultWrapper[IntegrationUpdateResponse]),
        )

    def delete(
        self,
        uuid: str,
        *,
        identifier: object,
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
          uuid: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return cast(
            Optional[IntegrationDeleteResponse],
            self._delete(
                f"/accounts/{identifier}/devices/posture/integration/{uuid}",
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

    def device_posture_integrations_create_device_posture_integration(
        self,
        identifier: object,
        *,
        config: integration_device_posture_integrations_create_device_posture_integration_params.Config,
        interval: str,
        name: str,
        type: Literal["workspace_one", "crowdstrike_s2s", "uptycs", "intune", "kolide", "tanium", "sentinelone_s2s"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IntegrationDevicePostureIntegrationsCreateDevicePostureIntegrationResponse]:
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
            f"/accounts/{identifier}/devices/posture/integration",
            body=maybe_transform(
                {
                    "config": config,
                    "interval": interval,
                    "name": name,
                    "type": type,
                },
                integration_device_posture_integrations_create_device_posture_integration_params.IntegrationDevicePostureIntegrationsCreateDevicePostureIntegrationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[IntegrationDevicePostureIntegrationsCreateDevicePostureIntegrationResponse]],
                ResultWrapper[IntegrationDevicePostureIntegrationsCreateDevicePostureIntegrationResponse],
            ),
        )

    def device_posture_integrations_list_device_posture_integrations(
        self,
        identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IntegrationDevicePostureIntegrationsListDevicePostureIntegrationsResponse]:
        """
        Fetches the list of device posture integrations for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{identifier}/devices/posture/integration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[IntegrationDevicePostureIntegrationsListDevicePostureIntegrationsResponse]],
                ResultWrapper[IntegrationDevicePostureIntegrationsListDevicePostureIntegrationsResponse],
            ),
        )

    def get(
        self,
        uuid: str,
        *,
        identifier: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IntegrationGetResponse]:
        """
        Fetches details for a single device posture integration.

        Args:
          uuid: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._get(
            f"/accounts/{identifier}/devices/posture/integration/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IntegrationGetResponse]], ResultWrapper[IntegrationGetResponse]),
        )


class AsyncIntegrations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIntegrationsWithRawResponse:
        return AsyncIntegrationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntegrationsWithStreamingResponse:
        return AsyncIntegrationsWithStreamingResponse(self)

    async def update(
        self,
        uuid: str,
        *,
        identifier: object,
        config: integration_update_params.Config | NotGiven = NOT_GIVEN,
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
    ) -> Optional[IntegrationUpdateResponse]:
        """
        Updates a configured device posture integration.

        Args:
          uuid: API UUID.

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
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._patch(
            f"/accounts/{identifier}/devices/posture/integration/{uuid}",
            body=maybe_transform(
                {
                    "config": config,
                    "interval": interval,
                    "name": name,
                    "type": type,
                },
                integration_update_params.IntegrationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IntegrationUpdateResponse]], ResultWrapper[IntegrationUpdateResponse]),
        )

    async def delete(
        self,
        uuid: str,
        *,
        identifier: object,
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
          uuid: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return cast(
            Optional[IntegrationDeleteResponse],
            await self._delete(
                f"/accounts/{identifier}/devices/posture/integration/{uuid}",
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

    async def device_posture_integrations_create_device_posture_integration(
        self,
        identifier: object,
        *,
        config: integration_device_posture_integrations_create_device_posture_integration_params.Config,
        interval: str,
        name: str,
        type: Literal["workspace_one", "crowdstrike_s2s", "uptycs", "intune", "kolide", "tanium", "sentinelone_s2s"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IntegrationDevicePostureIntegrationsCreateDevicePostureIntegrationResponse]:
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
            f"/accounts/{identifier}/devices/posture/integration",
            body=maybe_transform(
                {
                    "config": config,
                    "interval": interval,
                    "name": name,
                    "type": type,
                },
                integration_device_posture_integrations_create_device_posture_integration_params.IntegrationDevicePostureIntegrationsCreateDevicePostureIntegrationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[IntegrationDevicePostureIntegrationsCreateDevicePostureIntegrationResponse]],
                ResultWrapper[IntegrationDevicePostureIntegrationsCreateDevicePostureIntegrationResponse],
            ),
        )

    async def device_posture_integrations_list_device_posture_integrations(
        self,
        identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IntegrationDevicePostureIntegrationsListDevicePostureIntegrationsResponse]:
        """
        Fetches the list of device posture integrations for an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{identifier}/devices/posture/integration",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[IntegrationDevicePostureIntegrationsListDevicePostureIntegrationsResponse]],
                ResultWrapper[IntegrationDevicePostureIntegrationsListDevicePostureIntegrationsResponse],
            ),
        )

    async def get(
        self,
        uuid: str,
        *,
        identifier: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[IntegrationGetResponse]:
        """
        Fetches details for a single device posture integration.

        Args:
          uuid: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._get(
            f"/accounts/{identifier}/devices/posture/integration/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[IntegrationGetResponse]], ResultWrapper[IntegrationGetResponse]),
        )


class IntegrationsWithRawResponse:
    def __init__(self, integrations: Integrations) -> None:
        self._integrations = integrations

        self.update = to_raw_response_wrapper(
            integrations.update,
        )
        self.delete = to_raw_response_wrapper(
            integrations.delete,
        )
        self.device_posture_integrations_create_device_posture_integration = to_raw_response_wrapper(
            integrations.device_posture_integrations_create_device_posture_integration,
        )
        self.device_posture_integrations_list_device_posture_integrations = to_raw_response_wrapper(
            integrations.device_posture_integrations_list_device_posture_integrations,
        )
        self.get = to_raw_response_wrapper(
            integrations.get,
        )


class AsyncIntegrationsWithRawResponse:
    def __init__(self, integrations: AsyncIntegrations) -> None:
        self._integrations = integrations

        self.update = async_to_raw_response_wrapper(
            integrations.update,
        )
        self.delete = async_to_raw_response_wrapper(
            integrations.delete,
        )
        self.device_posture_integrations_create_device_posture_integration = async_to_raw_response_wrapper(
            integrations.device_posture_integrations_create_device_posture_integration,
        )
        self.device_posture_integrations_list_device_posture_integrations = async_to_raw_response_wrapper(
            integrations.device_posture_integrations_list_device_posture_integrations,
        )
        self.get = async_to_raw_response_wrapper(
            integrations.get,
        )


class IntegrationsWithStreamingResponse:
    def __init__(self, integrations: Integrations) -> None:
        self._integrations = integrations

        self.update = to_streamed_response_wrapper(
            integrations.update,
        )
        self.delete = to_streamed_response_wrapper(
            integrations.delete,
        )
        self.device_posture_integrations_create_device_posture_integration = to_streamed_response_wrapper(
            integrations.device_posture_integrations_create_device_posture_integration,
        )
        self.device_posture_integrations_list_device_posture_integrations = to_streamed_response_wrapper(
            integrations.device_posture_integrations_list_device_posture_integrations,
        )
        self.get = to_streamed_response_wrapper(
            integrations.get,
        )


class AsyncIntegrationsWithStreamingResponse:
    def __init__(self, integrations: AsyncIntegrations) -> None:
        self._integrations = integrations

        self.update = async_to_streamed_response_wrapper(
            integrations.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            integrations.delete,
        )
        self.device_posture_integrations_create_device_posture_integration = async_to_streamed_response_wrapper(
            integrations.device_posture_integrations_create_device_posture_integration,
        )
        self.device_posture_integrations_list_device_posture_integrations = async_to_streamed_response_wrapper(
            integrations.device_posture_integrations_list_device_posture_integrations,
        )
        self.get = async_to_streamed_response_wrapper(
            integrations.get,
        )
