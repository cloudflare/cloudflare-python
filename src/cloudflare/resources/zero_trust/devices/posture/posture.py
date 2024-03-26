# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from .integrations import (
    Integrations,
    AsyncIntegrations,
    IntegrationsWithRawResponse,
    AsyncIntegrationsWithRawResponse,
    IntegrationsWithStreamingResponse,
    AsyncIntegrationsWithStreamingResponse,
)
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
from .....types.zero_trust.devices import (
    PostureListResponse,
    PostureDeleteResponse,
    TeamsDevicesDevicePostureRules,
    posture_create_params,
    posture_update_params,
)

__all__ = ["Posture", "AsyncPosture"]


class Posture(SyncAPIResource):
    @cached_property
    def integrations(self) -> Integrations:
        return Integrations(self._client)

    @cached_property
    def with_raw_response(self) -> PostureWithRawResponse:
        return PostureWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PostureWithStreamingResponse:
        return PostureWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        type: Literal[
            "file",
            "application",
            "tanium",
            "gateway",
            "warp",
            "disk_encryption",
            "sentinelone",
            "carbonblack",
            "firewall",
            "os_version",
            "domain_joined",
            "client_certificate",
            "unique_client_id",
            "kolide",
            "tanium_s2s",
            "crowdstrike_s2s",
            "intune",
            "workspace_one",
            "sentinelone_s2s",
        ],
        description: str | NotGiven = NOT_GIVEN,
        expiration: str | NotGiven = NOT_GIVEN,
        input: posture_create_params.Input | NotGiven = NOT_GIVEN,
        match: Iterable[posture_create_params.Match] | NotGiven = NOT_GIVEN,
        schedule: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesDevicePostureRules]:
        """
        Creates a new device posture rule.

        Args:
          name: The name of the device posture rule.

          type: The type of device posture rule.

          description: The description of the device posture rule.

          expiration: Sets the expiration time for a posture check result. If empty, the result
              remains valid until it is overwritten by new data from the WARP client.

          input: The value to be checked against.

          match: The conditions that the client must match to run the rule.

          schedule: Polling frequency for the WARP client posture check. Default: `5m` (poll every
              five minutes). Minimum: `1m`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/devices/posture",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "description": description,
                    "expiration": expiration,
                    "input": input,
                    "match": match,
                    "schedule": schedule,
                },
                posture_create_params.PostureCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[TeamsDevicesDevicePostureRules]], ResultWrapper[TeamsDevicesDevicePostureRules]),
        )

    def update(
        self,
        rule_id: str,
        *,
        account_id: str,
        name: str,
        type: Literal[
            "file",
            "application",
            "tanium",
            "gateway",
            "warp",
            "disk_encryption",
            "sentinelone",
            "carbonblack",
            "firewall",
            "os_version",
            "domain_joined",
            "client_certificate",
            "unique_client_id",
            "kolide",
            "tanium_s2s",
            "crowdstrike_s2s",
            "intune",
            "workspace_one",
            "sentinelone_s2s",
        ],
        description: str | NotGiven = NOT_GIVEN,
        expiration: str | NotGiven = NOT_GIVEN,
        input: posture_update_params.Input | NotGiven = NOT_GIVEN,
        match: Iterable[posture_update_params.Match] | NotGiven = NOT_GIVEN,
        schedule: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesDevicePostureRules]:
        """
        Updates a device posture rule.

        Args:
          rule_id: API UUID.

          name: The name of the device posture rule.

          type: The type of device posture rule.

          description: The description of the device posture rule.

          expiration: Sets the expiration time for a posture check result. If empty, the result
              remains valid until it is overwritten by new data from the WARP client.

          input: The value to be checked against.

          match: The conditions that the client must match to run the rule.

          schedule: Polling frequency for the WARP client posture check. Default: `5m` (poll every
              five minutes). Minimum: `1m`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._put(
            f"/accounts/{account_id}/devices/posture/{rule_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "description": description,
                    "expiration": expiration,
                    "input": input,
                    "match": match,
                    "schedule": schedule,
                },
                posture_update_params.PostureUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[TeamsDevicesDevicePostureRules]], ResultWrapper[TeamsDevicesDevicePostureRules]),
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
    ) -> Optional[PostureListResponse]:
        """
        Fetches device posture rules for a Zero Trust account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/devices/posture",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PostureListResponse]], ResultWrapper[PostureListResponse]),
        )

    def delete(
        self,
        rule_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PostureDeleteResponse]:
        """
        Deletes a device posture rule.

        Args:
          rule_id: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._delete(
            f"/accounts/{account_id}/devices/posture/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PostureDeleteResponse]], ResultWrapper[PostureDeleteResponse]),
        )

    def get(
        self,
        rule_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesDevicePostureRules]:
        """
        Fetches a single device posture rule.

        Args:
          rule_id: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._get(
            f"/accounts/{account_id}/devices/posture/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[TeamsDevicesDevicePostureRules]], ResultWrapper[TeamsDevicesDevicePostureRules]),
        )


class AsyncPosture(AsyncAPIResource):
    @cached_property
    def integrations(self) -> AsyncIntegrations:
        return AsyncIntegrations(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPostureWithRawResponse:
        return AsyncPostureWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPostureWithStreamingResponse:
        return AsyncPostureWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        type: Literal[
            "file",
            "application",
            "tanium",
            "gateway",
            "warp",
            "disk_encryption",
            "sentinelone",
            "carbonblack",
            "firewall",
            "os_version",
            "domain_joined",
            "client_certificate",
            "unique_client_id",
            "kolide",
            "tanium_s2s",
            "crowdstrike_s2s",
            "intune",
            "workspace_one",
            "sentinelone_s2s",
        ],
        description: str | NotGiven = NOT_GIVEN,
        expiration: str | NotGiven = NOT_GIVEN,
        input: posture_create_params.Input | NotGiven = NOT_GIVEN,
        match: Iterable[posture_create_params.Match] | NotGiven = NOT_GIVEN,
        schedule: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesDevicePostureRules]:
        """
        Creates a new device posture rule.

        Args:
          name: The name of the device posture rule.

          type: The type of device posture rule.

          description: The description of the device posture rule.

          expiration: Sets the expiration time for a posture check result. If empty, the result
              remains valid until it is overwritten by new data from the WARP client.

          input: The value to be checked against.

          match: The conditions that the client must match to run the rule.

          schedule: Polling frequency for the WARP client posture check. Default: `5m` (poll every
              five minutes). Minimum: `1m`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/devices/posture",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "description": description,
                    "expiration": expiration,
                    "input": input,
                    "match": match,
                    "schedule": schedule,
                },
                posture_create_params.PostureCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[TeamsDevicesDevicePostureRules]], ResultWrapper[TeamsDevicesDevicePostureRules]),
        )

    async def update(
        self,
        rule_id: str,
        *,
        account_id: str,
        name: str,
        type: Literal[
            "file",
            "application",
            "tanium",
            "gateway",
            "warp",
            "disk_encryption",
            "sentinelone",
            "carbonblack",
            "firewall",
            "os_version",
            "domain_joined",
            "client_certificate",
            "unique_client_id",
            "kolide",
            "tanium_s2s",
            "crowdstrike_s2s",
            "intune",
            "workspace_one",
            "sentinelone_s2s",
        ],
        description: str | NotGiven = NOT_GIVEN,
        expiration: str | NotGiven = NOT_GIVEN,
        input: posture_update_params.Input | NotGiven = NOT_GIVEN,
        match: Iterable[posture_update_params.Match] | NotGiven = NOT_GIVEN,
        schedule: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesDevicePostureRules]:
        """
        Updates a device posture rule.

        Args:
          rule_id: API UUID.

          name: The name of the device posture rule.

          type: The type of device posture rule.

          description: The description of the device posture rule.

          expiration: Sets the expiration time for a posture check result. If empty, the result
              remains valid until it is overwritten by new data from the WARP client.

          input: The value to be checked against.

          match: The conditions that the client must match to run the rule.

          schedule: Polling frequency for the WARP client posture check. Default: `5m` (poll every
              five minutes). Minimum: `1m`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._put(
            f"/accounts/{account_id}/devices/posture/{rule_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "description": description,
                    "expiration": expiration,
                    "input": input,
                    "match": match,
                    "schedule": schedule,
                },
                posture_update_params.PostureUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[TeamsDevicesDevicePostureRules]], ResultWrapper[TeamsDevicesDevicePostureRules]),
        )

    async def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PostureListResponse]:
        """
        Fetches device posture rules for a Zero Trust account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/devices/posture",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PostureListResponse]], ResultWrapper[PostureListResponse]),
        )

    async def delete(
        self,
        rule_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PostureDeleteResponse]:
        """
        Deletes a device posture rule.

        Args:
          rule_id: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/devices/posture/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PostureDeleteResponse]], ResultWrapper[PostureDeleteResponse]),
        )

    async def get(
        self,
        rule_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[TeamsDevicesDevicePostureRules]:
        """
        Fetches a single device posture rule.

        Args:
          rule_id: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._get(
            f"/accounts/{account_id}/devices/posture/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[TeamsDevicesDevicePostureRules]], ResultWrapper[TeamsDevicesDevicePostureRules]),
        )


class PostureWithRawResponse:
    def __init__(self, posture: Posture) -> None:
        self._posture = posture

        self.create = to_raw_response_wrapper(
            posture.create,
        )
        self.update = to_raw_response_wrapper(
            posture.update,
        )
        self.list = to_raw_response_wrapper(
            posture.list,
        )
        self.delete = to_raw_response_wrapper(
            posture.delete,
        )
        self.get = to_raw_response_wrapper(
            posture.get,
        )

    @cached_property
    def integrations(self) -> IntegrationsWithRawResponse:
        return IntegrationsWithRawResponse(self._posture.integrations)


class AsyncPostureWithRawResponse:
    def __init__(self, posture: AsyncPosture) -> None:
        self._posture = posture

        self.create = async_to_raw_response_wrapper(
            posture.create,
        )
        self.update = async_to_raw_response_wrapper(
            posture.update,
        )
        self.list = async_to_raw_response_wrapper(
            posture.list,
        )
        self.delete = async_to_raw_response_wrapper(
            posture.delete,
        )
        self.get = async_to_raw_response_wrapper(
            posture.get,
        )

    @cached_property
    def integrations(self) -> AsyncIntegrationsWithRawResponse:
        return AsyncIntegrationsWithRawResponse(self._posture.integrations)


class PostureWithStreamingResponse:
    def __init__(self, posture: Posture) -> None:
        self._posture = posture

        self.create = to_streamed_response_wrapper(
            posture.create,
        )
        self.update = to_streamed_response_wrapper(
            posture.update,
        )
        self.list = to_streamed_response_wrapper(
            posture.list,
        )
        self.delete = to_streamed_response_wrapper(
            posture.delete,
        )
        self.get = to_streamed_response_wrapper(
            posture.get,
        )

    @cached_property
    def integrations(self) -> IntegrationsWithStreamingResponse:
        return IntegrationsWithStreamingResponse(self._posture.integrations)


class AsyncPostureWithStreamingResponse:
    def __init__(self, posture: AsyncPosture) -> None:
        self._posture = posture

        self.create = async_to_streamed_response_wrapper(
            posture.create,
        )
        self.update = async_to_streamed_response_wrapper(
            posture.update,
        )
        self.list = async_to_streamed_response_wrapper(
            posture.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            posture.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            posture.get,
        )

    @cached_property
    def integrations(self) -> AsyncIntegrationsWithStreamingResponse:
        return AsyncIntegrationsWithStreamingResponse(self._posture.integrations)
