# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.api_gateway.configuration_update_response import ConfigurationUpdateResponse

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options

from typing import Iterable, Type, List

from ...types.api_gateway.configuration import Configuration

from ..._wrappers import ResultWrapper

from typing_extensions import Literal

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from ...types.api_gateway import configuration_update_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.api_gateway import configuration_update_params
from ...types.api_gateway import configuration_get_params
from typing import cast
from typing import cast

__all__ = ["ConfigurationsResource", "AsyncConfigurationsResource"]

class ConfigurationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigurationsResourceWithRawResponse:
        return ConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigurationsResourceWithStreamingResponse:
        return ConfigurationsResourceWithStreamingResponse(self)

    def update(self,
    *,
    zone_id: str,
    auth_id_characteristics: Iterable[configuration_update_params.AuthIDCharacteristic],
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> ConfigurationUpdateResponse:
        """
        Set configuration properties

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        return self._put(
            f"/zones/{zone_id}/api_gateway/configuration",
            body=maybe_transform({
                "auth_id_characteristics": auth_id_characteristics
            }, configuration_update_params.ConfigurationUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ConfigurationUpdateResponse,
        )

    def get(self,
    *,
    zone_id: str,
    properties: List[Literal["auth_id_characteristics"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Configuration:
        """
        Retrieve information about specific configuration properties

        Args:
          zone_id: Identifier

          properties: Requests information about certain properties.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        return self._get(
            f"/zones/{zone_id}/api_gateway/configuration",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=maybe_transform({
                "properties": properties
            }, configuration_get_params.ConfigurationGetParams), post_parser=ResultWrapper[Configuration]._unwrapper),
            cast_to=cast(Type[Configuration], ResultWrapper[Configuration]),
        )

class AsyncConfigurationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigurationsResourceWithRawResponse:
        return AsyncConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigurationsResourceWithStreamingResponse:
        return AsyncConfigurationsResourceWithStreamingResponse(self)

    async def update(self,
    *,
    zone_id: str,
    auth_id_characteristics: Iterable[configuration_update_params.AuthIDCharacteristic],
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> ConfigurationUpdateResponse:
        """
        Set configuration properties

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        return await self._put(
            f"/zones/{zone_id}/api_gateway/configuration",
            body=await async_maybe_transform({
                "auth_id_characteristics": auth_id_characteristics
            }, configuration_update_params.ConfigurationUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ConfigurationUpdateResponse,
        )

    async def get(self,
    *,
    zone_id: str,
    properties: List[Literal["auth_id_characteristics"]] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Configuration:
        """
        Retrieve information about specific configuration properties

        Args:
          zone_id: Identifier

          properties: Requests information about certain properties.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        return await self._get(
            f"/zones/{zone_id}/api_gateway/configuration",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, query=await async_maybe_transform({
                "properties": properties
            }, configuration_get_params.ConfigurationGetParams), post_parser=ResultWrapper[Configuration]._unwrapper),
            cast_to=cast(Type[Configuration], ResultWrapper[Configuration]),
        )

class ConfigurationsResourceWithRawResponse:
    def __init__(self, configurations: ConfigurationsResource) -> None:
        self._configurations = configurations

        self.update = to_raw_response_wrapper(
            configurations.update,
        )
        self.get = to_raw_response_wrapper(
            configurations.get,
        )

class AsyncConfigurationsResourceWithRawResponse:
    def __init__(self, configurations: AsyncConfigurationsResource) -> None:
        self._configurations = configurations

        self.update = async_to_raw_response_wrapper(
            configurations.update,
        )
        self.get = async_to_raw_response_wrapper(
            configurations.get,
        )

class ConfigurationsResourceWithStreamingResponse:
    def __init__(self, configurations: ConfigurationsResource) -> None:
        self._configurations = configurations

        self.update = to_streamed_response_wrapper(
            configurations.update,
        )
        self.get = to_streamed_response_wrapper(
            configurations.get,
        )

class AsyncConfigurationsResourceWithStreamingResponse:
    def __init__(self, configurations: AsyncConfigurationsResource) -> None:
        self._configurations = configurations

        self.update = async_to_streamed_response_wrapper(
            configurations.update,
        )
        self.get = async_to_streamed_response_wrapper(
            configurations.get,
        )