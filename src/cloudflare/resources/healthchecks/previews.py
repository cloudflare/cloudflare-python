# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.healthchecks.healthcheck import Healthcheck

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options

from typing import Type, Optional, List

from ...types.healthchecks.check_region import CheckRegion

from ...types.healthchecks.http_configuration_param import HTTPConfigurationParam

from ...types.healthchecks.tcp_configuration_param import TCPConfigurationParam

from ...types.healthchecks.preview_delete_response import PreviewDeleteResponse

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.healthchecks import preview_create_params
from ...types.healthchecks import HTTPConfiguration
from ...types.healthchecks import TCPConfiguration
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["PreviewsResource", "AsyncPreviewsResource"]

class PreviewsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PreviewsResourceWithRawResponse:
        return PreviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreviewsResourceWithStreamingResponse:
        return PreviewsResourceWithStreamingResponse(self)

    def create(self,
    *,
    zone_id: str,
    address: str,
    name: str,
    check_regions: Optional[List[CheckRegion]] | NotGiven = NOT_GIVEN,
    consecutive_fails: int | NotGiven = NOT_GIVEN,
    consecutive_successes: int | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    http_config: Optional[HTTPConfigurationParam] | NotGiven = NOT_GIVEN,
    interval: int | NotGiven = NOT_GIVEN,
    retries: int | NotGiven = NOT_GIVEN,
    suspended: bool | NotGiven = NOT_GIVEN,
    tcp_config: Optional[TCPConfigurationParam] | NotGiven = NOT_GIVEN,
    healthcheck_timeout: int | NotGiven = NOT_GIVEN,
    type: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Healthcheck:
        """
        Create a new preview health check.

        Args:
          zone_id: Identifier

          address: The hostname or IP address of the origin server to run health checks on.

          name: A short name to identify the health check. Only alphanumeric characters, hyphens
              and underscores are allowed.

          check_regions: A list of regions from which to run health checks. Null means Cloudflare will
              pick a default region.

          consecutive_fails: The number of consecutive fails required from a health check before changing the
              health to unhealthy.

          consecutive_successes: The number of consecutive successes required from a health check before changing
              the health to healthy.

          description: A human-readable description of the health check.

          http_config: Parameters specific to an HTTP or HTTPS health check.

          interval: The interval between each health check. Shorter intervals may give quicker
              notifications if the origin status changes, but will increase load on the origin
              as we check from multiple locations.

          retries: The number of retries to attempt in case of a timeout before marking the origin
              as unhealthy. Retries are attempted immediately.

          suspended: If suspended, no health checks are sent to the origin.

          tcp_config: Parameters specific to TCP health check.

          healthcheck_timeout: The timeout (in seconds) before marking the health check as failed.

          type: The protocol to use for the health check. Currently supported protocols are
              'HTTP', 'HTTPS' and 'TCP'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        return self._post(
            f"/zones/{zone_id}/healthchecks/preview",
            body=maybe_transform({
                "address": address,
                "name": name,
                "check_regions": check_regions,
                "consecutive_fails": consecutive_fails,
                "consecutive_successes": consecutive_successes,
                "description": description,
                "http_config": http_config,
                "interval": interval,
                "retries": retries,
                "suspended": suspended,
                "tcp_config": tcp_config,
                "timeout": healthcheck_timeout,
                "type": type,
            }, preview_create_params.PreviewCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Healthcheck]._unwrapper),
            cast_to=cast(Type[Healthcheck], ResultWrapper[Healthcheck]),
        )

    def delete(self,
    healthcheck_id: str,
    *,
    zone_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> PreviewDeleteResponse:
        """
        Delete a health check.

        Args:
          zone_id: Identifier

          healthcheck_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not healthcheck_id:
          raise ValueError(
            f'Expected a non-empty value for `healthcheck_id` but received {healthcheck_id!r}'
          )
        return self._delete(
            f"/zones/{zone_id}/healthchecks/preview/{healthcheck_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[PreviewDeleteResponse]._unwrapper),
            cast_to=cast(Type[PreviewDeleteResponse], ResultWrapper[PreviewDeleteResponse]),
        )

    def get(self,
    healthcheck_id: str,
    *,
    zone_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Healthcheck:
        """
        Fetch a single configured health check preview.

        Args:
          zone_id: Identifier

          healthcheck_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not healthcheck_id:
          raise ValueError(
            f'Expected a non-empty value for `healthcheck_id` but received {healthcheck_id!r}'
          )
        return self._get(
            f"/zones/{zone_id}/healthchecks/preview/{healthcheck_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Healthcheck]._unwrapper),
            cast_to=cast(Type[Healthcheck], ResultWrapper[Healthcheck]),
        )

class AsyncPreviewsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPreviewsResourceWithRawResponse:
        return AsyncPreviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreviewsResourceWithStreamingResponse:
        return AsyncPreviewsResourceWithStreamingResponse(self)

    async def create(self,
    *,
    zone_id: str,
    address: str,
    name: str,
    check_regions: Optional[List[CheckRegion]] | NotGiven = NOT_GIVEN,
    consecutive_fails: int | NotGiven = NOT_GIVEN,
    consecutive_successes: int | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    http_config: Optional[HTTPConfigurationParam] | NotGiven = NOT_GIVEN,
    interval: int | NotGiven = NOT_GIVEN,
    retries: int | NotGiven = NOT_GIVEN,
    suspended: bool | NotGiven = NOT_GIVEN,
    tcp_config: Optional[TCPConfigurationParam] | NotGiven = NOT_GIVEN,
    healthcheck_timeout: int | NotGiven = NOT_GIVEN,
    type: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Healthcheck:
        """
        Create a new preview health check.

        Args:
          zone_id: Identifier

          address: The hostname or IP address of the origin server to run health checks on.

          name: A short name to identify the health check. Only alphanumeric characters, hyphens
              and underscores are allowed.

          check_regions: A list of regions from which to run health checks. Null means Cloudflare will
              pick a default region.

          consecutive_fails: The number of consecutive fails required from a health check before changing the
              health to unhealthy.

          consecutive_successes: The number of consecutive successes required from a health check before changing
              the health to healthy.

          description: A human-readable description of the health check.

          http_config: Parameters specific to an HTTP or HTTPS health check.

          interval: The interval between each health check. Shorter intervals may give quicker
              notifications if the origin status changes, but will increase load on the origin
              as we check from multiple locations.

          retries: The number of retries to attempt in case of a timeout before marking the origin
              as unhealthy. Retries are attempted immediately.

          suspended: If suspended, no health checks are sent to the origin.

          tcp_config: Parameters specific to TCP health check.

          healthcheck_timeout: The timeout (in seconds) before marking the health check as failed.

          type: The protocol to use for the health check. Currently supported protocols are
              'HTTP', 'HTTPS' and 'TCP'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        return await self._post(
            f"/zones/{zone_id}/healthchecks/preview",
            body=await async_maybe_transform({
                "address": address,
                "name": name,
                "check_regions": check_regions,
                "consecutive_fails": consecutive_fails,
                "consecutive_successes": consecutive_successes,
                "description": description,
                "http_config": http_config,
                "interval": interval,
                "retries": retries,
                "suspended": suspended,
                "tcp_config": tcp_config,
                "timeout": healthcheck_timeout,
                "type": type,
            }, preview_create_params.PreviewCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Healthcheck]._unwrapper),
            cast_to=cast(Type[Healthcheck], ResultWrapper[Healthcheck]),
        )

    async def delete(self,
    healthcheck_id: str,
    *,
    zone_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> PreviewDeleteResponse:
        """
        Delete a health check.

        Args:
          zone_id: Identifier

          healthcheck_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not healthcheck_id:
          raise ValueError(
            f'Expected a non-empty value for `healthcheck_id` but received {healthcheck_id!r}'
          )
        return await self._delete(
            f"/zones/{zone_id}/healthchecks/preview/{healthcheck_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[PreviewDeleteResponse]._unwrapper),
            cast_to=cast(Type[PreviewDeleteResponse], ResultWrapper[PreviewDeleteResponse]),
        )

    async def get(self,
    healthcheck_id: str,
    *,
    zone_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Healthcheck:
        """
        Fetch a single configured health check preview.

        Args:
          zone_id: Identifier

          healthcheck_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not healthcheck_id:
          raise ValueError(
            f'Expected a non-empty value for `healthcheck_id` but received {healthcheck_id!r}'
          )
        return await self._get(
            f"/zones/{zone_id}/healthchecks/preview/{healthcheck_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Healthcheck]._unwrapper),
            cast_to=cast(Type[Healthcheck], ResultWrapper[Healthcheck]),
        )

class PreviewsResourceWithRawResponse:
    def __init__(self, previews: PreviewsResource) -> None:
        self._previews = previews

        self.create = to_raw_response_wrapper(
            previews.create,
        )
        self.delete = to_raw_response_wrapper(
            previews.delete,
        )
        self.get = to_raw_response_wrapper(
            previews.get,
        )

class AsyncPreviewsResourceWithRawResponse:
    def __init__(self, previews: AsyncPreviewsResource) -> None:
        self._previews = previews

        self.create = async_to_raw_response_wrapper(
            previews.create,
        )
        self.delete = async_to_raw_response_wrapper(
            previews.delete,
        )
        self.get = async_to_raw_response_wrapper(
            previews.get,
        )

class PreviewsResourceWithStreamingResponse:
    def __init__(self, previews: PreviewsResource) -> None:
        self._previews = previews

        self.create = to_streamed_response_wrapper(
            previews.create,
        )
        self.delete = to_streamed_response_wrapper(
            previews.delete,
        )
        self.get = to_streamed_response_wrapper(
            previews.get,
        )

class AsyncPreviewsResourceWithStreamingResponse:
    def __init__(self, previews: AsyncPreviewsResource) -> None:
        self._previews = previews

        self.create = async_to_streamed_response_wrapper(
            previews.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            previews.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            previews.get,
        )