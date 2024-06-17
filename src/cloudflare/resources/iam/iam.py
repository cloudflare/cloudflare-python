# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .resource_groups import (
    ResourceGroupsResource,
    AsyncResourceGroupsResource,
    ResourceGroupsResourceWithRawResponse,
    AsyncResourceGroupsResourceWithRawResponse,
    ResourceGroupsResourceWithStreamingResponse,
    AsyncResourceGroupsResourceWithStreamingResponse,
)
from .permission_groups import (
    PermissionGroupsResource,
    AsyncPermissionGroupsResource,
    PermissionGroupsResourceWithRawResponse,
    AsyncPermissionGroupsResourceWithRawResponse,
    PermissionGroupsResourceWithStreamingResponse,
    AsyncPermissionGroupsResourceWithStreamingResponse,
)

__all__ = ["IamResource", "AsyncIamResource"]


class IamResource(SyncAPIResource):
    @cached_property
    def permission_groups(self) -> PermissionGroupsResource:
        return PermissionGroupsResource(self._client)

    @cached_property
    def resource_groups(self) -> ResourceGroupsResource:
        return ResourceGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> IamResourceWithRawResponse:
        return IamResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IamResourceWithStreamingResponse:
        return IamResourceWithStreamingResponse(self)


class AsyncIamResource(AsyncAPIResource):
    @cached_property
    def permission_groups(self) -> AsyncPermissionGroupsResource:
        return AsyncPermissionGroupsResource(self._client)

    @cached_property
    def resource_groups(self) -> AsyncResourceGroupsResource:
        return AsyncResourceGroupsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIamResourceWithRawResponse:
        return AsyncIamResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIamResourceWithStreamingResponse:
        return AsyncIamResourceWithStreamingResponse(self)


class IamResourceWithRawResponse:
    def __init__(self, iam: IamResource) -> None:
        self._iam = iam

    @cached_property
    def permission_groups(self) -> PermissionGroupsResourceWithRawResponse:
        return PermissionGroupsResourceWithRawResponse(self._iam.permission_groups)

    @cached_property
    def resource_groups(self) -> ResourceGroupsResourceWithRawResponse:
        return ResourceGroupsResourceWithRawResponse(self._iam.resource_groups)


class AsyncIamResourceWithRawResponse:
    def __init__(self, iam: AsyncIamResource) -> None:
        self._iam = iam

    @cached_property
    def permission_groups(self) -> AsyncPermissionGroupsResourceWithRawResponse:
        return AsyncPermissionGroupsResourceWithRawResponse(self._iam.permission_groups)

    @cached_property
    def resource_groups(self) -> AsyncResourceGroupsResourceWithRawResponse:
        return AsyncResourceGroupsResourceWithRawResponse(self._iam.resource_groups)


class IamResourceWithStreamingResponse:
    def __init__(self, iam: IamResource) -> None:
        self._iam = iam

    @cached_property
    def permission_groups(self) -> PermissionGroupsResourceWithStreamingResponse:
        return PermissionGroupsResourceWithStreamingResponse(self._iam.permission_groups)

    @cached_property
    def resource_groups(self) -> ResourceGroupsResourceWithStreamingResponse:
        return ResourceGroupsResourceWithStreamingResponse(self._iam.resource_groups)


class AsyncIamResourceWithStreamingResponse:
    def __init__(self, iam: AsyncIamResource) -> None:
        self._iam = iam

    @cached_property
    def permission_groups(self) -> AsyncPermissionGroupsResourceWithStreamingResponse:
        return AsyncPermissionGroupsResourceWithStreamingResponse(self._iam.permission_groups)

    @cached_property
    def resource_groups(self) -> AsyncResourceGroupsResourceWithStreamingResponse:
        return AsyncResourceGroupsResourceWithStreamingResponse(self._iam.resource_groups)
