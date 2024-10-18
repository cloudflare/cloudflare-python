# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .rules import (
    RulesResource,
    AsyncRulesResource,
    RulesResourceWithRawResponse,
    AsyncRulesResourceWithRawResponse,
    RulesResourceWithStreamingResponse,
    AsyncRulesResourceWithStreamingResponse,
)
from .groups import (
    GroupsResource,
    AsyncGroupsResource,
    GroupsResourceWithRawResponse,
    AsyncGroupsResourceWithRawResponse,
    GroupsResourceWithStreamingResponse,
    AsyncGroupsResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["PackagesResource", "AsyncPackagesResource"]


class PackagesResource(SyncAPIResource):
    @cached_property
    def groups(self) -> GroupsResource:
        return GroupsResource(self._client)

    @cached_property
    def rules(self) -> RulesResource:
        return RulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> PackagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PackagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PackagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PackagesResourceWithStreamingResponse(self)


class AsyncPackagesResource(AsyncAPIResource):
    @cached_property
    def groups(self) -> AsyncGroupsResource:
        return AsyncGroupsResource(self._client)

    @cached_property
    def rules(self) -> AsyncRulesResource:
        return AsyncRulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPackagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPackagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPackagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPackagesResourceWithStreamingResponse(self)


class PackagesResourceWithRawResponse:
    def __init__(self, packages: PackagesResource) -> None:
        self._packages = packages

    @cached_property
    def groups(self) -> GroupsResourceWithRawResponse:
        return GroupsResourceWithRawResponse(self._packages.groups)

    @cached_property
    def rules(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self._packages.rules)


class AsyncPackagesResourceWithRawResponse:
    def __init__(self, packages: AsyncPackagesResource) -> None:
        self._packages = packages

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithRawResponse:
        return AsyncGroupsResourceWithRawResponse(self._packages.groups)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self._packages.rules)


class PackagesResourceWithStreamingResponse:
    def __init__(self, packages: PackagesResource) -> None:
        self._packages = packages

    @cached_property
    def groups(self) -> GroupsResourceWithStreamingResponse:
        return GroupsResourceWithStreamingResponse(self._packages.groups)

    @cached_property
    def rules(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self._packages.rules)


class AsyncPackagesResourceWithStreamingResponse:
    def __init__(self, packages: AsyncPackagesResource) -> None:
        self._packages = packages

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithStreamingResponse:
        return AsyncGroupsResourceWithStreamingResponse(self._packages.groups)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self._packages.rules)
