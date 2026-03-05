# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import required_args, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from ...types.resource_tagging import zone_tag_get_params, zone_tag_update_params
from ...types.resource_tagging.zone_tag_get_response import ZoneTagGetResponse
from ...types.resource_tagging.zone_tag_update_response import ZoneTagUpdateResponse

__all__ = ["ZoneTagsResource", "AsyncZoneTagsResource"]


class ZoneTagsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ZoneTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ZoneTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZoneTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ZoneTagsResourceWithStreamingResponse(self)

    @overload
    def update(
        self,
        *,
        zone_id: str,
        resource_id: str,
        resource_type: Literal[
            "api_gateway_operation",
            "custom_certificate",
            "custom_hostname",
            "dns_record",
            "managed_client_certificate",
            "zone",
        ],
        tags: Dict[str, str] | Omit = omit,
        if_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ZoneTagUpdateResponse]:
        """Creates or updates tags for a specific zone-level resource.

        Replaces all
        existing tags for the resource.

        Args:
          zone_id: Zone ID is required only for zone-level resources

          resource_id: Identifies the unique resource.

          resource_type: Enum for base zone-level resource types (those with no extra required fields).

          tags: Contains key-value pairs of tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        *,
        zone_id: str,
        access_application_id: str,
        resource_id: str,
        resource_type: Literal[
            "api_gateway_operation",
            "custom_certificate",
            "custom_hostname",
            "dns_record",
            "managed_client_certificate",
            "zone",
            "access_application_policy",
        ],
        tags: Dict[str, str] | Omit = omit,
        if_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ZoneTagUpdateResponse]:
        """Creates or updates tags for a specific zone-level resource.

        Replaces all
        existing tags for the resource.

        Args:
          zone_id: Zone ID is required only for zone-level resources

          access_application_id: Access application ID is required only for access_application_policy resources

          resource_id: Identifies the unique resource.

          resource_type: Enum for base zone-level resource types (those with no extra required fields).

          tags: Contains key-value pairs of tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["zone_id", "resource_id", "resource_type"],
        ["zone_id", "access_application_id", "resource_id", "resource_type"],
    )
    def update(
        self,
        *,
        zone_id: str,
        resource_id: str,
        resource_type: Literal[
            "api_gateway_operation",
            "custom_certificate",
            "custom_hostname",
            "dns_record",
            "managed_client_certificate",
            "zone",
        ]
        | Literal[
            "api_gateway_operation",
            "custom_certificate",
            "custom_hostname",
            "dns_record",
            "managed_client_certificate",
            "zone",
            "access_application_policy",
        ],
        tags: Dict[str, str] | Omit = omit,
        if_match: str | Omit = omit,
        access_application_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ZoneTagUpdateResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {**strip_not_given({"If-Match": if_match}), **(extra_headers or {})}
        return cast(
            Optional[ZoneTagUpdateResponse],
            self._put(
                f"/zones/{zone_id}/tags",
                body=maybe_transform(
                    {
                        "resource_id": resource_id,
                        "resource_type": resource_type,
                        "tags": tags,
                        "access_application_id": access_application_id,
                    },
                    zone_tag_update_params.ZoneTagUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[ZoneTagUpdateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ZoneTagUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete(
        self,
        *,
        zone_id: str,
        if_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes all tags from a specific zone-level resource.

        Args:
          zone_id: Zone ID is required only for zone-level resources

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"If-Match": if_match}), **(extra_headers or {})}
        return self._delete(
            f"/zones/{zone_id}/tags",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        *,
        zone_id: str,
        resource_id: str,
        resource_type: Literal[
            "access_application_policy",
            "api_gateway_operation",
            "custom_certificate",
            "custom_hostname",
            "dns_record",
            "managed_client_certificate",
            "zone",
        ],
        access_application_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ZoneTagGetResponse]:
        """
        Retrieves tags for a specific zone-level resource.

        Args:
          zone_id: Zone ID is required only for zone-level resources

          resource_id: The ID of the resource to retrieve tags for.

          resource_type: The type of the resource.

          access_application_id: Access application ID identifier. Required for access_application_policy
              resources.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            Optional[ZoneTagGetResponse],
            self._get(
                f"/zones/{zone_id}/tags",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "resource_id": resource_id,
                            "resource_type": resource_type,
                            "access_application_id": access_application_id,
                        },
                        zone_tag_get_params.ZoneTagGetParams,
                    ),
                    post_parser=ResultWrapper[Optional[ZoneTagGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ZoneTagGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncZoneTagsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncZoneTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncZoneTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZoneTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncZoneTagsResourceWithStreamingResponse(self)

    @overload
    async def update(
        self,
        *,
        zone_id: str,
        resource_id: str,
        resource_type: Literal[
            "api_gateway_operation",
            "custom_certificate",
            "custom_hostname",
            "dns_record",
            "managed_client_certificate",
            "zone",
        ],
        tags: Dict[str, str] | Omit = omit,
        if_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ZoneTagUpdateResponse]:
        """Creates or updates tags for a specific zone-level resource.

        Replaces all
        existing tags for the resource.

        Args:
          zone_id: Zone ID is required only for zone-level resources

          resource_id: Identifies the unique resource.

          resource_type: Enum for base zone-level resource types (those with no extra required fields).

          tags: Contains key-value pairs of tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        *,
        zone_id: str,
        access_application_id: str,
        resource_id: str,
        resource_type: Literal[
            "api_gateway_operation",
            "custom_certificate",
            "custom_hostname",
            "dns_record",
            "managed_client_certificate",
            "zone",
            "access_application_policy",
        ],
        tags: Dict[str, str] | Omit = omit,
        if_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ZoneTagUpdateResponse]:
        """Creates or updates tags for a specific zone-level resource.

        Replaces all
        existing tags for the resource.

        Args:
          zone_id: Zone ID is required only for zone-level resources

          access_application_id: Access application ID is required only for access_application_policy resources

          resource_id: Identifies the unique resource.

          resource_type: Enum for base zone-level resource types (those with no extra required fields).

          tags: Contains key-value pairs of tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["zone_id", "resource_id", "resource_type"],
        ["zone_id", "access_application_id", "resource_id", "resource_type"],
    )
    async def update(
        self,
        *,
        zone_id: str,
        resource_id: str,
        resource_type: Literal[
            "api_gateway_operation",
            "custom_certificate",
            "custom_hostname",
            "dns_record",
            "managed_client_certificate",
            "zone",
        ]
        | Literal[
            "api_gateway_operation",
            "custom_certificate",
            "custom_hostname",
            "dns_record",
            "managed_client_certificate",
            "zone",
            "access_application_policy",
        ],
        tags: Dict[str, str] | Omit = omit,
        if_match: str | Omit = omit,
        access_application_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ZoneTagUpdateResponse]:
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {**strip_not_given({"If-Match": if_match}), **(extra_headers or {})}
        return cast(
            Optional[ZoneTagUpdateResponse],
            await self._put(
                f"/zones/{zone_id}/tags",
                body=await async_maybe_transform(
                    {
                        "resource_id": resource_id,
                        "resource_type": resource_type,
                        "tags": tags,
                        "access_application_id": access_application_id,
                    },
                    zone_tag_update_params.ZoneTagUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[ZoneTagUpdateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ZoneTagUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete(
        self,
        *,
        zone_id: str,
        if_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes all tags from a specific zone-level resource.

        Args:
          zone_id: Zone ID is required only for zone-level resources

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"If-Match": if_match}), **(extra_headers or {})}
        return await self._delete(
            f"/zones/{zone_id}/tags",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        *,
        zone_id: str,
        resource_id: str,
        resource_type: Literal[
            "access_application_policy",
            "api_gateway_operation",
            "custom_certificate",
            "custom_hostname",
            "dns_record",
            "managed_client_certificate",
            "zone",
        ],
        access_application_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[ZoneTagGetResponse]:
        """
        Retrieves tags for a specific zone-level resource.

        Args:
          zone_id: Zone ID is required only for zone-level resources

          resource_id: The ID of the resource to retrieve tags for.

          resource_type: The type of the resource.

          access_application_id: Access application ID identifier. Required for access_application_policy
              resources.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            Optional[ZoneTagGetResponse],
            await self._get(
                f"/zones/{zone_id}/tags",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "resource_id": resource_id,
                            "resource_type": resource_type,
                            "access_application_id": access_application_id,
                        },
                        zone_tag_get_params.ZoneTagGetParams,
                    ),
                    post_parser=ResultWrapper[Optional[ZoneTagGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[ZoneTagGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ZoneTagsResourceWithRawResponse:
    def __init__(self, zone_tags: ZoneTagsResource) -> None:
        self._zone_tags = zone_tags

        self.update = to_raw_response_wrapper(
            zone_tags.update,
        )
        self.delete = to_raw_response_wrapper(
            zone_tags.delete,
        )
        self.get = to_raw_response_wrapper(
            zone_tags.get,
        )


class AsyncZoneTagsResourceWithRawResponse:
    def __init__(self, zone_tags: AsyncZoneTagsResource) -> None:
        self._zone_tags = zone_tags

        self.update = async_to_raw_response_wrapper(
            zone_tags.update,
        )
        self.delete = async_to_raw_response_wrapper(
            zone_tags.delete,
        )
        self.get = async_to_raw_response_wrapper(
            zone_tags.get,
        )


class ZoneTagsResourceWithStreamingResponse:
    def __init__(self, zone_tags: ZoneTagsResource) -> None:
        self._zone_tags = zone_tags

        self.update = to_streamed_response_wrapper(
            zone_tags.update,
        )
        self.delete = to_streamed_response_wrapper(
            zone_tags.delete,
        )
        self.get = to_streamed_response_wrapper(
            zone_tags.get,
        )


class AsyncZoneTagsResourceWithStreamingResponse:
    def __init__(self, zone_tags: AsyncZoneTagsResource) -> None:
        self._zone_tags = zone_tags

        self.update = async_to_streamed_response_wrapper(
            zone_tags.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            zone_tags.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            zone_tags.get,
        )
