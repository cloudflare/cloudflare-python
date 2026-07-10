# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
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

__all__ = ["SCIMResource", "AsyncSCIMResource"]


class SCIMResource(SyncAPIResource):
    @cached_property
    def groups(self) -> GroupsResource:
        return GroupsResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

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
    def groups(self) -> AsyncGroupsResource:
        return AsyncGroupsResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

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
    def groups(self) -> GroupsResourceWithRawResponse:
        return GroupsResourceWithRawResponse(self._scim.groups)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._scim.users)


class AsyncSCIMResourceWithRawResponse:
    def __init__(self, scim: AsyncSCIMResource) -> None:
        self._scim = scim

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithRawResponse:
        return AsyncGroupsResourceWithRawResponse(self._scim.groups)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._scim.users)


class SCIMResourceWithStreamingResponse:
    def __init__(self, scim: SCIMResource) -> None:
        self._scim = scim

    @cached_property
    def groups(self) -> GroupsResourceWithStreamingResponse:
        return GroupsResourceWithStreamingResponse(self._scim.groups)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._scim.users)


class AsyncSCIMResourceWithStreamingResponse:
    def __init__(self, scim: AsyncSCIMResource) -> None:
        self._scim = scim

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithStreamingResponse:
        return AsyncGroupsResourceWithStreamingResponse(self._scim.groups)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._scim.users)
