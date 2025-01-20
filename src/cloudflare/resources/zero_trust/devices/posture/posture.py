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
    IntegrationsResource,
    AsyncIntegrationsResource,
    IntegrationsResourceWithRawResponse,
    AsyncIntegrationsResourceWithRawResponse,
    IntegrationsResourceWithStreamingResponse,
    AsyncIntegrationsResourceWithStreamingResponse,
)
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
from .....types.zero_trust.devices import posture_create_params, posture_update_params
from .....types.zero_trust.devices.device_input_param import DeviceInputParam
from .....types.zero_trust.devices.device_match_param import DeviceMatchParam
from .....types.zero_trust.devices.device_posture_rule import DevicePostureRule
from .....types.zero_trust.devices.posture_delete_response import PostureDeleteResponse

__all__ = ["PostureResource", "AsyncPostureResource"]


class PostureResource(SyncAPIResource):
    @cached_property
    def integrations(self) -> IntegrationsResource:
        return IntegrationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PostureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PostureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PostureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PostureResourceWithStreamingResponse(self)

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
            "client_certificate_v2",
            "unique_client_id",
            "kolide",
            "tanium_s2s",
            "crowdstrike_s2s",
            "intune",
            "workspace_one",
            "sentinelone_s2s",
            "custom_s2s",
        ],
        description: str | NotGiven = NOT_GIVEN,
        expiration: str | NotGiven = NOT_GIVEN,
        input: DeviceInputParam | NotGiven = NOT_GIVEN,
        match: Iterable[DeviceMatchParam] | NotGiven = NOT_GIVEN,
        schedule: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DevicePostureRule]:
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
                post_parser=ResultWrapper[Optional[DevicePostureRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DevicePostureRule]], ResultWrapper[DevicePostureRule]),
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
            "client_certificate_v2",
            "unique_client_id",
            "kolide",
            "tanium_s2s",
            "crowdstrike_s2s",
            "intune",
            "workspace_one",
            "sentinelone_s2s",
            "custom_s2s",
        ],
        description: str | NotGiven = NOT_GIVEN,
        expiration: str | NotGiven = NOT_GIVEN,
        input: DeviceInputParam | NotGiven = NOT_GIVEN,
        match: Iterable[DeviceMatchParam] | NotGiven = NOT_GIVEN,
        schedule: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DevicePostureRule]:
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
                post_parser=ResultWrapper[Optional[DevicePostureRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DevicePostureRule]], ResultWrapper[DevicePostureRule]),
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
    ) -> SyncSinglePage[DevicePostureRule]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/devices/posture",
            page=SyncSinglePage[DevicePostureRule],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=DevicePostureRule,
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
                post_parser=ResultWrapper[Optional[PostureDeleteResponse]]._unwrapper,
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
    ) -> Optional[DevicePostureRule]:
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
                post_parser=ResultWrapper[Optional[DevicePostureRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DevicePostureRule]], ResultWrapper[DevicePostureRule]),
        )


class AsyncPostureResource(AsyncAPIResource):
    @cached_property
    def integrations(self) -> AsyncIntegrationsResource:
        return AsyncIntegrationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPostureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPostureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPostureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPostureResourceWithStreamingResponse(self)

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
            "client_certificate_v2",
            "unique_client_id",
            "kolide",
            "tanium_s2s",
            "crowdstrike_s2s",
            "intune",
            "workspace_one",
            "sentinelone_s2s",
            "custom_s2s",
        ],
        description: str | NotGiven = NOT_GIVEN,
        expiration: str | NotGiven = NOT_GIVEN,
        input: DeviceInputParam | NotGiven = NOT_GIVEN,
        match: Iterable[DeviceMatchParam] | NotGiven = NOT_GIVEN,
        schedule: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DevicePostureRule]:
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
                post_parser=ResultWrapper[Optional[DevicePostureRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DevicePostureRule]], ResultWrapper[DevicePostureRule]),
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
            "client_certificate_v2",
            "unique_client_id",
            "kolide",
            "tanium_s2s",
            "crowdstrike_s2s",
            "intune",
            "workspace_one",
            "sentinelone_s2s",
            "custom_s2s",
        ],
        description: str | NotGiven = NOT_GIVEN,
        expiration: str | NotGiven = NOT_GIVEN,
        input: DeviceInputParam | NotGiven = NOT_GIVEN,
        match: Iterable[DeviceMatchParam] | NotGiven = NOT_GIVEN,
        schedule: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DevicePostureRule]:
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
                post_parser=ResultWrapper[Optional[DevicePostureRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DevicePostureRule]], ResultWrapper[DevicePostureRule]),
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
    ) -> AsyncPaginator[DevicePostureRule, AsyncSinglePage[DevicePostureRule]]:
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
        return self._get_api_list(
            f"/accounts/{account_id}/devices/posture",
            page=AsyncSinglePage[DevicePostureRule],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=DevicePostureRule,
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
                post_parser=ResultWrapper[Optional[PostureDeleteResponse]]._unwrapper,
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
    ) -> Optional[DevicePostureRule]:
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
                post_parser=ResultWrapper[Optional[DevicePostureRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DevicePostureRule]], ResultWrapper[DevicePostureRule]),
        )


class PostureResourceWithRawResponse:
    def __init__(self, posture: PostureResource) -> None:
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
    def integrations(self) -> IntegrationsResourceWithRawResponse:
        return IntegrationsResourceWithRawResponse(self._posture.integrations)


class AsyncPostureResourceWithRawResponse:
    def __init__(self, posture: AsyncPostureResource) -> None:
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
    def integrations(self) -> AsyncIntegrationsResourceWithRawResponse:
        return AsyncIntegrationsResourceWithRawResponse(self._posture.integrations)


class PostureResourceWithStreamingResponse:
    def __init__(self, posture: PostureResource) -> None:
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
    def integrations(self) -> IntegrationsResourceWithStreamingResponse:
        return IntegrationsResourceWithStreamingResponse(self._posture.integrations)


class AsyncPostureResourceWithStreamingResponse:
    def __init__(self, posture: AsyncPostureResource) -> None:
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
    def integrations(self) -> AsyncIntegrationsResourceWithStreamingResponse:
        return AsyncIntegrationsResourceWithStreamingResponse(self._posture.integrations)
