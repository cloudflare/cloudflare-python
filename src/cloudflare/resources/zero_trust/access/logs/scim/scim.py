# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .updates import (
    UpdatesResource,
    AsyncUpdatesResource,
    UpdatesResourceWithRawResponse,
    AsyncUpdatesResourceWithRawResponse,
    UpdatesResourceWithStreamingResponse,
    AsyncUpdatesResourceWithStreamingResponse,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SCIMResource", "AsyncSCIMResource"]


class SCIMResource(SyncAPIResource):
    @cached_property
    def updates(self) -> UpdatesResource:
        return UpdatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> SCIMResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SCIMResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SCIMResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SCIMResourceWithStreamingResponse(self)


class AsyncSCIMResource(AsyncAPIResource):
    @cached_property
    def updates(self) -> AsyncUpdatesResource:
        return AsyncUpdatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSCIMResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSCIMResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSCIMResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSCIMResourceWithStreamingResponse(self)


class SCIMResourceWithRawResponse:
    def __init__(self, scim: SCIMResource) -> None:
        self._scim = scim

    @cached_property
    def updates(self) -> UpdatesResourceWithRawResponse:
        return UpdatesResourceWithRawResponse(self._scim.updates)


class AsyncSCIMResourceWithRawResponse:
    def __init__(self, scim: AsyncSCIMResource) -> None:
        self._scim = scim

    @cached_property
    def updates(self) -> AsyncUpdatesResourceWithRawResponse:
        return AsyncUpdatesResourceWithRawResponse(self._scim.updates)


class SCIMResourceWithStreamingResponse:
    def __init__(self, scim: SCIMResource) -> None:
        self._scim = scim

    @cached_property
    def updates(self) -> UpdatesResourceWithStreamingResponse:
        return UpdatesResourceWithStreamingResponse(self._scim.updates)


class AsyncSCIMResourceWithStreamingResponse:
    def __init__(self, scim: AsyncSCIMResource) -> None:
        self._scim = scim

    @cached_property
    def updates(self) -> AsyncUpdatesResourceWithStreamingResponse:
        return AsyncUpdatesResourceWithStreamingResponse(self._scim.updates)
