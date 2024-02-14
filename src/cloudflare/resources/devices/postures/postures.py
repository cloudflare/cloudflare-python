# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .integrations import Integrations, AsyncIntegrations

from ...._compat import cached_property

from ....types.devices import (
    PostureUpdateResponse,
    PostureDeleteResponse,
    PostureDevicePostureRulesCreateDevicePostureRuleResponse,
    PostureDevicePostureRulesListDevicePostureRulesResponse,
    PostureGetResponse,
    posture_update_params,
    posture_device_posture_rules_create_device_posture_rule_params,
)

from typing import Type, Optional, Iterable

from typing_extensions import Literal

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.devices import posture_update_params
from ....types.devices import posture_device_posture_rules_create_device_posture_rule_params
from .integrations import (
    Integrations,
    AsyncIntegrations,
    IntegrationsWithRawResponse,
    AsyncIntegrationsWithRawResponse,
    IntegrationsWithStreamingResponse,
    AsyncIntegrationsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Postures", "AsyncPostures"]


class Postures(SyncAPIResource):
    @cached_property
    def integrations(self) -> Integrations:
        return Integrations(self._client)

    @cached_property
    def with_raw_response(self) -> PosturesWithRawResponse:
        return PosturesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PosturesWithStreamingResponse:
        return PosturesWithStreamingResponse(self)

    def update(
        self,
        uuid: str,
        *,
        identifier: object,
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
    ) -> Optional[PostureUpdateResponse]:
        """
        Updates a device posture rule.

        Args:
          uuid: API UUID.

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
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._put(
            f"/accounts/{identifier}/devices/posture/{uuid}",
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
            cast_to=cast(Type[Optional[PostureUpdateResponse]], ResultWrapper[PostureUpdateResponse]),
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
    ) -> Optional[PostureDeleteResponse]:
        """
        Deletes a device posture rule.

        Args:
          uuid: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._delete(
            f"/accounts/{identifier}/devices/posture/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PostureDeleteResponse]], ResultWrapper[PostureDeleteResponse]),
        )

    def device_posture_rules_create_device_posture_rule(
        self,
        identifier: object,
        *,
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
        input: posture_device_posture_rules_create_device_posture_rule_params.Input | NotGiven = NOT_GIVEN,
        match: Iterable[posture_device_posture_rules_create_device_posture_rule_params.Match] | NotGiven = NOT_GIVEN,
        schedule: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PostureDevicePostureRulesCreateDevicePostureRuleResponse]:
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
        return self._post(
            f"/accounts/{identifier}/devices/posture",
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
                posture_device_posture_rules_create_device_posture_rule_params.PostureDevicePostureRulesCreateDevicePostureRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[PostureDevicePostureRulesCreateDevicePostureRuleResponse]],
                ResultWrapper[PostureDevicePostureRulesCreateDevicePostureRuleResponse],
            ),
        )

    def device_posture_rules_list_device_posture_rules(
        self,
        identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PostureDevicePostureRulesListDevicePostureRulesResponse]:
        """
        Fetches device posture rules for a Zero Trust account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{identifier}/devices/posture",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[PostureDevicePostureRulesListDevicePostureRulesResponse]],
                ResultWrapper[PostureDevicePostureRulesListDevicePostureRulesResponse],
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
    ) -> Optional[PostureGetResponse]:
        """
        Fetches a single device posture rule.

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
            f"/accounts/{identifier}/devices/posture/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PostureGetResponse]], ResultWrapper[PostureGetResponse]),
        )


class AsyncPostures(AsyncAPIResource):
    @cached_property
    def integrations(self) -> AsyncIntegrations:
        return AsyncIntegrations(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPosturesWithRawResponse:
        return AsyncPosturesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPosturesWithStreamingResponse:
        return AsyncPosturesWithStreamingResponse(self)

    async def update(
        self,
        uuid: str,
        *,
        identifier: object,
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
    ) -> Optional[PostureUpdateResponse]:
        """
        Updates a device posture rule.

        Args:
          uuid: API UUID.

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
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._put(
            f"/accounts/{identifier}/devices/posture/{uuid}",
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
            cast_to=cast(Type[Optional[PostureUpdateResponse]], ResultWrapper[PostureUpdateResponse]),
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
    ) -> Optional[PostureDeleteResponse]:
        """
        Deletes a device posture rule.

        Args:
          uuid: API UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._delete(
            f"/accounts/{identifier}/devices/posture/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PostureDeleteResponse]], ResultWrapper[PostureDeleteResponse]),
        )

    async def device_posture_rules_create_device_posture_rule(
        self,
        identifier: object,
        *,
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
        input: posture_device_posture_rules_create_device_posture_rule_params.Input | NotGiven = NOT_GIVEN,
        match: Iterable[posture_device_posture_rules_create_device_posture_rule_params.Match] | NotGiven = NOT_GIVEN,
        schedule: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PostureDevicePostureRulesCreateDevicePostureRuleResponse]:
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
        return await self._post(
            f"/accounts/{identifier}/devices/posture",
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
                posture_device_posture_rules_create_device_posture_rule_params.PostureDevicePostureRulesCreateDevicePostureRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[PostureDevicePostureRulesCreateDevicePostureRuleResponse]],
                ResultWrapper[PostureDevicePostureRulesCreateDevicePostureRuleResponse],
            ),
        )

    async def device_posture_rules_list_device_posture_rules(
        self,
        identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PostureDevicePostureRulesListDevicePostureRulesResponse]:
        """
        Fetches device posture rules for a Zero Trust account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{identifier}/devices/posture",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[PostureDevicePostureRulesListDevicePostureRulesResponse]],
                ResultWrapper[PostureDevicePostureRulesListDevicePostureRulesResponse],
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
    ) -> Optional[PostureGetResponse]:
        """
        Fetches a single device posture rule.

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
            f"/accounts/{identifier}/devices/posture/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PostureGetResponse]], ResultWrapper[PostureGetResponse]),
        )


class PosturesWithRawResponse:
    def __init__(self, postures: Postures) -> None:
        self._postures = postures

        self.update = to_raw_response_wrapper(
            postures.update,
        )
        self.delete = to_raw_response_wrapper(
            postures.delete,
        )
        self.device_posture_rules_create_device_posture_rule = to_raw_response_wrapper(
            postures.device_posture_rules_create_device_posture_rule,
        )
        self.device_posture_rules_list_device_posture_rules = to_raw_response_wrapper(
            postures.device_posture_rules_list_device_posture_rules,
        )
        self.get = to_raw_response_wrapper(
            postures.get,
        )

    @cached_property
    def integrations(self) -> IntegrationsWithRawResponse:
        return IntegrationsWithRawResponse(self._postures.integrations)


class AsyncPosturesWithRawResponse:
    def __init__(self, postures: AsyncPostures) -> None:
        self._postures = postures

        self.update = async_to_raw_response_wrapper(
            postures.update,
        )
        self.delete = async_to_raw_response_wrapper(
            postures.delete,
        )
        self.device_posture_rules_create_device_posture_rule = async_to_raw_response_wrapper(
            postures.device_posture_rules_create_device_posture_rule,
        )
        self.device_posture_rules_list_device_posture_rules = async_to_raw_response_wrapper(
            postures.device_posture_rules_list_device_posture_rules,
        )
        self.get = async_to_raw_response_wrapper(
            postures.get,
        )

    @cached_property
    def integrations(self) -> AsyncIntegrationsWithRawResponse:
        return AsyncIntegrationsWithRawResponse(self._postures.integrations)


class PosturesWithStreamingResponse:
    def __init__(self, postures: Postures) -> None:
        self._postures = postures

        self.update = to_streamed_response_wrapper(
            postures.update,
        )
        self.delete = to_streamed_response_wrapper(
            postures.delete,
        )
        self.device_posture_rules_create_device_posture_rule = to_streamed_response_wrapper(
            postures.device_posture_rules_create_device_posture_rule,
        )
        self.device_posture_rules_list_device_posture_rules = to_streamed_response_wrapper(
            postures.device_posture_rules_list_device_posture_rules,
        )
        self.get = to_streamed_response_wrapper(
            postures.get,
        )

    @cached_property
    def integrations(self) -> IntegrationsWithStreamingResponse:
        return IntegrationsWithStreamingResponse(self._postures.integrations)


class AsyncPosturesWithStreamingResponse:
    def __init__(self, postures: AsyncPostures) -> None:
        self._postures = postures

        self.update = async_to_streamed_response_wrapper(
            postures.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            postures.delete,
        )
        self.device_posture_rules_create_device_posture_rule = async_to_streamed_response_wrapper(
            postures.device_posture_rules_create_device_posture_rule,
        )
        self.device_posture_rules_list_device_posture_rules = async_to_streamed_response_wrapper(
            postures.device_posture_rules_list_device_posture_rules,
        )
        self.get = async_to_streamed_response_wrapper(
            postures.get,
        )

    @cached_property
    def integrations(self) -> AsyncIntegrationsWithStreamingResponse:
        return AsyncIntegrationsWithStreamingResponse(self._postures.integrations)
