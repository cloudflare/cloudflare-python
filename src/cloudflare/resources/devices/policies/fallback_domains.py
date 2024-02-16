# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.devices.policies import (
    FallbackDomainDevicesGetLocalDomainFallbackListResponse,
    FallbackDomainDevicesGetLocalDomainFallbackListForADeviceSettingsPolicyResponse,
    FallbackDomainDevicesSetLocalDomainFallbackListResponse,
    FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyResponse,
    fallback_domain_devices_set_local_domain_fallback_list_params,
    fallback_domain_devices_set_local_domain_fallback_list_for_a_device_settings_policy_params,
)

from typing import Type, Optional, Iterable

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
from ....types.devices.policies import fallback_domain_devices_set_local_domain_fallback_list_params
from ....types.devices.policies import (
    fallback_domain_devices_set_local_domain_fallback_list_for_a_device_settings_policy_params,
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

__all__ = ["FallbackDomains", "AsyncFallbackDomains"]


class FallbackDomains(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FallbackDomainsWithRawResponse:
        return FallbackDomainsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FallbackDomainsWithStreamingResponse:
        return FallbackDomainsWithStreamingResponse(self)

    def devices_get_local_domain_fallback_list(
        self,
        identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FallbackDomainDevicesGetLocalDomainFallbackListResponse]:
        """Fetches a list of domains to bypass Gateway DNS resolution.

        These domains will
        use the specified local DNS resolver instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{identifier}/devices/policy/fallback_domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[FallbackDomainDevicesGetLocalDomainFallbackListResponse]],
                ResultWrapper[FallbackDomainDevicesGetLocalDomainFallbackListResponse],
            ),
        )

    def devices_get_local_domain_fallback_list_for_a_device_settings_policy(
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
    ) -> Optional[FallbackDomainDevicesGetLocalDomainFallbackListForADeviceSettingsPolicyResponse]:
        """
        Fetches the list of domains to bypass Gateway DNS resolution from a specified
        device settings profile. These domains will use the specified local DNS resolver
        instead.

        Args:
          uuid: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._get(
            f"/accounts/{identifier}/devices/policy/{uuid}/fallback_domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[FallbackDomainDevicesGetLocalDomainFallbackListForADeviceSettingsPolicyResponse]],
                ResultWrapper[FallbackDomainDevicesGetLocalDomainFallbackListForADeviceSettingsPolicyResponse],
            ),
        )

    def devices_set_local_domain_fallback_list(
        self,
        identifier: object,
        *,
        body: Iterable[fallback_domain_devices_set_local_domain_fallback_list_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FallbackDomainDevicesSetLocalDomainFallbackListResponse]:
        """Sets the list of domains to bypass Gateway DNS resolution.

        These domains will
        use the specified local DNS resolver instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/accounts/{identifier}/devices/policy/fallback_domains",
            body=maybe_transform(
                body,
                fallback_domain_devices_set_local_domain_fallback_list_params.FallbackDomainDevicesSetLocalDomainFallbackListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[FallbackDomainDevicesSetLocalDomainFallbackListResponse]],
                ResultWrapper[FallbackDomainDevicesSetLocalDomainFallbackListResponse],
            ),
        )

    def devices_set_local_domain_fallback_list_for_a_device_settings_policy(
        self,
        uuid: str,
        *,
        identifier: object,
        body: Iterable[fallback_domain_devices_set_local_domain_fallback_list_for_a_device_settings_policy_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyResponse]:
        """Sets the list of domains to bypass Gateway DNS resolution.

        These domains will
        use the specified local DNS resolver instead. This will only apply to the
        specified device settings profile.

        Args:
          uuid: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._put(
            f"/accounts/{identifier}/devices/policy/{uuid}/fallback_domains",
            body=maybe_transform(
                body,
                fallback_domain_devices_set_local_domain_fallback_list_for_a_device_settings_policy_params.FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyResponse]],
                ResultWrapper[FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyResponse],
            ),
        )


class AsyncFallbackDomains(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFallbackDomainsWithRawResponse:
        return AsyncFallbackDomainsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFallbackDomainsWithStreamingResponse:
        return AsyncFallbackDomainsWithStreamingResponse(self)

    async def devices_get_local_domain_fallback_list(
        self,
        identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FallbackDomainDevicesGetLocalDomainFallbackListResponse]:
        """Fetches a list of domains to bypass Gateway DNS resolution.

        These domains will
        use the specified local DNS resolver instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{identifier}/devices/policy/fallback_domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[FallbackDomainDevicesGetLocalDomainFallbackListResponse]],
                ResultWrapper[FallbackDomainDevicesGetLocalDomainFallbackListResponse],
            ),
        )

    async def devices_get_local_domain_fallback_list_for_a_device_settings_policy(
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
    ) -> Optional[FallbackDomainDevicesGetLocalDomainFallbackListForADeviceSettingsPolicyResponse]:
        """
        Fetches the list of domains to bypass Gateway DNS resolution from a specified
        device settings profile. These domains will use the specified local DNS resolver
        instead.

        Args:
          uuid: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._get(
            f"/accounts/{identifier}/devices/policy/{uuid}/fallback_domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[FallbackDomainDevicesGetLocalDomainFallbackListForADeviceSettingsPolicyResponse]],
                ResultWrapper[FallbackDomainDevicesGetLocalDomainFallbackListForADeviceSettingsPolicyResponse],
            ),
        )

    async def devices_set_local_domain_fallback_list(
        self,
        identifier: object,
        *,
        body: Iterable[fallback_domain_devices_set_local_domain_fallback_list_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FallbackDomainDevicesSetLocalDomainFallbackListResponse]:
        """Sets the list of domains to bypass Gateway DNS resolution.

        These domains will
        use the specified local DNS resolver instead.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/accounts/{identifier}/devices/policy/fallback_domains",
            body=maybe_transform(
                body,
                fallback_domain_devices_set_local_domain_fallback_list_params.FallbackDomainDevicesSetLocalDomainFallbackListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[FallbackDomainDevicesSetLocalDomainFallbackListResponse]],
                ResultWrapper[FallbackDomainDevicesSetLocalDomainFallbackListResponse],
            ),
        )

    async def devices_set_local_domain_fallback_list_for_a_device_settings_policy(
        self,
        uuid: str,
        *,
        identifier: object,
        body: Iterable[fallback_domain_devices_set_local_domain_fallback_list_for_a_device_settings_policy_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyResponse]:
        """Sets the list of domains to bypass Gateway DNS resolution.

        These domains will
        use the specified local DNS resolver instead. This will only apply to the
        specified device settings profile.

        Args:
          uuid: Device ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._put(
            f"/accounts/{identifier}/devices/policy/{uuid}/fallback_domains",
            body=maybe_transform(
                body,
                fallback_domain_devices_set_local_domain_fallback_list_for_a_device_settings_policy_params.FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyResponse]],
                ResultWrapper[FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyResponse],
            ),
        )


class FallbackDomainsWithRawResponse:
    def __init__(self, fallback_domains: FallbackDomains) -> None:
        self._fallback_domains = fallback_domains

        self.devices_get_local_domain_fallback_list = to_raw_response_wrapper(
            fallback_domains.devices_get_local_domain_fallback_list,
        )
        self.devices_get_local_domain_fallback_list_for_a_device_settings_policy = to_raw_response_wrapper(
            fallback_domains.devices_get_local_domain_fallback_list_for_a_device_settings_policy,
        )
        self.devices_set_local_domain_fallback_list = to_raw_response_wrapper(
            fallback_domains.devices_set_local_domain_fallback_list,
        )
        self.devices_set_local_domain_fallback_list_for_a_device_settings_policy = to_raw_response_wrapper(
            fallback_domains.devices_set_local_domain_fallback_list_for_a_device_settings_policy,
        )


class AsyncFallbackDomainsWithRawResponse:
    def __init__(self, fallback_domains: AsyncFallbackDomains) -> None:
        self._fallback_domains = fallback_domains

        self.devices_get_local_domain_fallback_list = async_to_raw_response_wrapper(
            fallback_domains.devices_get_local_domain_fallback_list,
        )
        self.devices_get_local_domain_fallback_list_for_a_device_settings_policy = async_to_raw_response_wrapper(
            fallback_domains.devices_get_local_domain_fallback_list_for_a_device_settings_policy,
        )
        self.devices_set_local_domain_fallback_list = async_to_raw_response_wrapper(
            fallback_domains.devices_set_local_domain_fallback_list,
        )
        self.devices_set_local_domain_fallback_list_for_a_device_settings_policy = async_to_raw_response_wrapper(
            fallback_domains.devices_set_local_domain_fallback_list_for_a_device_settings_policy,
        )


class FallbackDomainsWithStreamingResponse:
    def __init__(self, fallback_domains: FallbackDomains) -> None:
        self._fallback_domains = fallback_domains

        self.devices_get_local_domain_fallback_list = to_streamed_response_wrapper(
            fallback_domains.devices_get_local_domain_fallback_list,
        )
        self.devices_get_local_domain_fallback_list_for_a_device_settings_policy = to_streamed_response_wrapper(
            fallback_domains.devices_get_local_domain_fallback_list_for_a_device_settings_policy,
        )
        self.devices_set_local_domain_fallback_list = to_streamed_response_wrapper(
            fallback_domains.devices_set_local_domain_fallback_list,
        )
        self.devices_set_local_domain_fallback_list_for_a_device_settings_policy = to_streamed_response_wrapper(
            fallback_domains.devices_set_local_domain_fallback_list_for_a_device_settings_policy,
        )


class AsyncFallbackDomainsWithStreamingResponse:
    def __init__(self, fallback_domains: AsyncFallbackDomains) -> None:
        self._fallback_domains = fallback_domains

        self.devices_get_local_domain_fallback_list = async_to_streamed_response_wrapper(
            fallback_domains.devices_get_local_domain_fallback_list,
        )
        self.devices_get_local_domain_fallback_list_for_a_device_settings_policy = async_to_streamed_response_wrapper(
            fallback_domains.devices_get_local_domain_fallback_list_for_a_device_settings_policy,
        )
        self.devices_set_local_domain_fallback_list = async_to_streamed_response_wrapper(
            fallback_domains.devices_set_local_domain_fallback_list,
        )
        self.devices_set_local_domain_fallback_list_for_a_device_settings_policy = async_to_streamed_response_wrapper(
            fallback_domains.devices_set_local_domain_fallback_list_for_a_device_settings_policy,
        )
