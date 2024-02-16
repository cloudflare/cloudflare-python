# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.zaraz import ConfigUpdateResponse, ConfigGetResponse, config_update_params

from typing import Type, Dict

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.zaraz import config_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Config", "AsyncConfig"]


class Config(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigWithRawResponse:
        return ConfigWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigWithStreamingResponse:
        return ConfigWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        data_layer: bool,
        debug_key: str,
        settings: config_update_params.Settings,
        tools: Dict[str, config_update_params.Tools],
        triggers: Dict[str, config_update_params.Triggers],
        variables: Dict[str, config_update_params.Variables],
        zaraz_version: int,
        consent: config_update_params.Consent | NotGiven = NOT_GIVEN,
        history_change: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigUpdateResponse:
        """
        Updates Zaraz configuration for a zone.

        Args:
          zone_id: Identifier

          data_layer: Data layer compatibility mode enabled.

          debug_key: The key for Zaraz debug mode.

          settings: General Zaraz settings.

          tools: Tools set up under Zaraz configuration, where key is the alpha-numeric tool ID
              and value is the tool configuration object.

          triggers: Triggers set up under Zaraz configuration, where key is the trigger
              alpha-numeric ID and value is the trigger configuration.

          variables: Variables set up under Zaraz configuration, where key is the variable
              alpha-numeric ID and value is the variable configuration. Values of variables of
              type secret are not included.

          zaraz_version: Zaraz internal version of the config.

          consent: Consent management configuration.

          history_change: Single Page Application support enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/settings/zaraz/config",
            body=maybe_transform(
                {
                    "data_layer": data_layer,
                    "debug_key": debug_key,
                    "settings": settings,
                    "tools": tools,
                    "triggers": triggers,
                    "variables": variables,
                    "zaraz_version": zaraz_version,
                    "consent": consent,
                    "history_change": history_change,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ConfigUpdateResponse], ResultWrapper[ConfigUpdateResponse]),
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
    ) -> ConfigGetResponse:
        """Gets latest Zaraz configuration for a zone.

        It can be preview or published
        configuration, whichever was the last updated. Secret variables values will not
        be included.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/settings/zaraz/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ConfigGetResponse], ResultWrapper[ConfigGetResponse]),
        )


class AsyncConfig(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigWithRawResponse:
        return AsyncConfigWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigWithStreamingResponse:
        return AsyncConfigWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        data_layer: bool,
        debug_key: str,
        settings: config_update_params.Settings,
        tools: Dict[str, config_update_params.Tools],
        triggers: Dict[str, config_update_params.Triggers],
        variables: Dict[str, config_update_params.Variables],
        zaraz_version: int,
        consent: config_update_params.Consent | NotGiven = NOT_GIVEN,
        history_change: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigUpdateResponse:
        """
        Updates Zaraz configuration for a zone.

        Args:
          zone_id: Identifier

          data_layer: Data layer compatibility mode enabled.

          debug_key: The key for Zaraz debug mode.

          settings: General Zaraz settings.

          tools: Tools set up under Zaraz configuration, where key is the alpha-numeric tool ID
              and value is the tool configuration object.

          triggers: Triggers set up under Zaraz configuration, where key is the trigger
              alpha-numeric ID and value is the trigger configuration.

          variables: Variables set up under Zaraz configuration, where key is the variable
              alpha-numeric ID and value is the variable configuration. Values of variables of
              type secret are not included.

          zaraz_version: Zaraz internal version of the config.

          consent: Consent management configuration.

          history_change: Single Page Application support enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/settings/zaraz/config",
            body=maybe_transform(
                {
                    "data_layer": data_layer,
                    "debug_key": debug_key,
                    "settings": settings,
                    "tools": tools,
                    "triggers": triggers,
                    "variables": variables,
                    "zaraz_version": zaraz_version,
                    "consent": consent,
                    "history_change": history_change,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ConfigUpdateResponse], ResultWrapper[ConfigUpdateResponse]),
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
    ) -> ConfigGetResponse:
        """Gets latest Zaraz configuration for a zone.

        It can be preview or published
        configuration, whichever was the last updated. Secret variables values will not
        be included.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/settings/zaraz/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ConfigGetResponse], ResultWrapper[ConfigGetResponse]),
        )


class ConfigWithRawResponse:
    def __init__(self, config: Config) -> None:
        self._config = config

        self.update = to_raw_response_wrapper(
            config.update,
        )
        self.get = to_raw_response_wrapper(
            config.get,
        )


class AsyncConfigWithRawResponse:
    def __init__(self, config: AsyncConfig) -> None:
        self._config = config

        self.update = async_to_raw_response_wrapper(
            config.update,
        )
        self.get = async_to_raw_response_wrapper(
            config.get,
        )


class ConfigWithStreamingResponse:
    def __init__(self, config: Config) -> None:
        self._config = config

        self.update = to_streamed_response_wrapper(
            config.update,
        )
        self.get = to_streamed_response_wrapper(
            config.get,
        )


class AsyncConfigWithStreamingResponse:
    def __init__(self, config: AsyncConfig) -> None:
        self._config = config

        self.update = async_to_streamed_response_wrapper(
            config.update,
        )
        self.get = async_to_streamed_response_wrapper(
            config.get,
        )
