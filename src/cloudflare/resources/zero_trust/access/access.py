# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .keys import (
    KeysResource,
    AsyncKeysResource,
    KeysResourceWithRawResponse,
    AsyncKeysResourceWithRawResponse,
    KeysResourceWithStreamingResponse,
    AsyncKeysResourceWithStreamingResponse,
)
from .logs import (
    LogsResource,
    AsyncLogsResource,
    LogsResourceWithRawResponse,
    AsyncLogsResourceWithRawResponse,
    LogsResourceWithStreamingResponse,
    AsyncLogsResourceWithStreamingResponse,
)
from .tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
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
from .bookmarks import (
    BookmarksResource,
    AsyncBookmarksResource,
    BookmarksResourceWithRawResponse,
    AsyncBookmarksResourceWithRawResponse,
    BookmarksResourceWithStreamingResponse,
    AsyncBookmarksResourceWithStreamingResponse,
)
from .logs.logs import LogsResource, AsyncLogsResource
from ...._compat import cached_property
from .users.users import UsersResource, AsyncUsersResource
from ...._resource import SyncAPIResource, AsyncAPIResource
from .applications import (
    ApplicationsResource,
    AsyncApplicationsResource,
    ApplicationsResourceWithRawResponse,
    AsyncApplicationsResourceWithRawResponse,
    ApplicationsResourceWithStreamingResponse,
    AsyncApplicationsResourceWithStreamingResponse,
)
from .certificates import (
    CertificatesResource,
    AsyncCertificatesResource,
    CertificatesResourceWithRawResponse,
    AsyncCertificatesResourceWithRawResponse,
    CertificatesResourceWithStreamingResponse,
    AsyncCertificatesResourceWithStreamingResponse,
)
from .custom_pages import (
    CustomPagesResource,
    AsyncCustomPagesResource,
    CustomPagesResourceWithRawResponse,
    AsyncCustomPagesResourceWithRawResponse,
    CustomPagesResourceWithStreamingResponse,
    AsyncCustomPagesResourceWithStreamingResponse,
)
from .service_tokens import (
    ServiceTokensResource,
    AsyncServiceTokensResource,
    ServiceTokensResourceWithRawResponse,
    AsyncServiceTokensResourceWithRawResponse,
    ServiceTokensResourceWithStreamingResponse,
    AsyncServiceTokensResourceWithStreamingResponse,
)
from .applications.applications import ApplicationsResource, AsyncApplicationsResource
from .certificates.certificates import CertificatesResource, AsyncCertificatesResource

__all__ = ["AccessResource", "AsyncAccessResource"]


class AccessResource(SyncAPIResource):
    @cached_property
    def applications(self) -> ApplicationsResource:
        return ApplicationsResource(self._client)

    @cached_property
    def certificates(self) -> CertificatesResource:
        return CertificatesResource(self._client)

    @cached_property
    def groups(self) -> GroupsResource:
        return GroupsResource(self._client)

    @cached_property
    def service_tokens(self) -> ServiceTokensResource:
        return ServiceTokensResource(self._client)

    @cached_property
    def bookmarks(self) -> BookmarksResource:
        return BookmarksResource(self._client)

    @cached_property
    def keys(self) -> KeysResource:
        return KeysResource(self._client)

    @cached_property
    def logs(self) -> LogsResource:
        return LogsResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def custom_pages(self) -> CustomPagesResource:
        return CustomPagesResource(self._client)

    @cached_property
    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccessResourceWithRawResponse:
        return AccessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessResourceWithStreamingResponse:
        return AccessResourceWithStreamingResponse(self)


class AsyncAccessResource(AsyncAPIResource):
    @cached_property
    def applications(self) -> AsyncApplicationsResource:
        return AsyncApplicationsResource(self._client)

    @cached_property
    def certificates(self) -> AsyncCertificatesResource:
        return AsyncCertificatesResource(self._client)

    @cached_property
    def groups(self) -> AsyncGroupsResource:
        return AsyncGroupsResource(self._client)

    @cached_property
    def service_tokens(self) -> AsyncServiceTokensResource:
        return AsyncServiceTokensResource(self._client)

    @cached_property
    def bookmarks(self) -> AsyncBookmarksResource:
        return AsyncBookmarksResource(self._client)

    @cached_property
    def keys(self) -> AsyncKeysResource:
        return AsyncKeysResource(self._client)

    @cached_property
    def logs(self) -> AsyncLogsResource:
        return AsyncLogsResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def custom_pages(self) -> AsyncCustomPagesResource:
        return AsyncCustomPagesResource(self._client)

    @cached_property
    def tags(self) -> AsyncTagsResource:
        return AsyncTagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccessResourceWithRawResponse:
        return AsyncAccessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessResourceWithStreamingResponse:
        return AsyncAccessResourceWithStreamingResponse(self)


class AccessResourceWithRawResponse:
    def __init__(self, access: AccessResource) -> None:
        self._access = access

    @cached_property
    def applications(self) -> ApplicationsResourceWithRawResponse:
        return ApplicationsResourceWithRawResponse(self._access.applications)

    @cached_property
    def certificates(self) -> CertificatesResourceWithRawResponse:
        return CertificatesResourceWithRawResponse(self._access.certificates)

    @cached_property
    def groups(self) -> GroupsResourceWithRawResponse:
        return GroupsResourceWithRawResponse(self._access.groups)

    @cached_property
    def service_tokens(self) -> ServiceTokensResourceWithRawResponse:
        return ServiceTokensResourceWithRawResponse(self._access.service_tokens)

    @cached_property
    def bookmarks(self) -> BookmarksResourceWithRawResponse:
        return BookmarksResourceWithRawResponse(self._access.bookmarks)

    @cached_property
    def keys(self) -> KeysResourceWithRawResponse:
        return KeysResourceWithRawResponse(self._access.keys)

    @cached_property
    def logs(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self._access.logs)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._access.users)

    @cached_property
    def custom_pages(self) -> CustomPagesResourceWithRawResponse:
        return CustomPagesResourceWithRawResponse(self._access.custom_pages)

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self._access.tags)


class AsyncAccessResourceWithRawResponse:
    def __init__(self, access: AsyncAccessResource) -> None:
        self._access = access

    @cached_property
    def applications(self) -> AsyncApplicationsResourceWithRawResponse:
        return AsyncApplicationsResourceWithRawResponse(self._access.applications)

    @cached_property
    def certificates(self) -> AsyncCertificatesResourceWithRawResponse:
        return AsyncCertificatesResourceWithRawResponse(self._access.certificates)

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithRawResponse:
        return AsyncGroupsResourceWithRawResponse(self._access.groups)

    @cached_property
    def service_tokens(self) -> AsyncServiceTokensResourceWithRawResponse:
        return AsyncServiceTokensResourceWithRawResponse(self._access.service_tokens)

    @cached_property
    def bookmarks(self) -> AsyncBookmarksResourceWithRawResponse:
        return AsyncBookmarksResourceWithRawResponse(self._access.bookmarks)

    @cached_property
    def keys(self) -> AsyncKeysResourceWithRawResponse:
        return AsyncKeysResourceWithRawResponse(self._access.keys)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self._access.logs)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._access.users)

    @cached_property
    def custom_pages(self) -> AsyncCustomPagesResourceWithRawResponse:
        return AsyncCustomPagesResourceWithRawResponse(self._access.custom_pages)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self._access.tags)


class AccessResourceWithStreamingResponse:
    def __init__(self, access: AccessResource) -> None:
        self._access = access

    @cached_property
    def applications(self) -> ApplicationsResourceWithStreamingResponse:
        return ApplicationsResourceWithStreamingResponse(self._access.applications)

    @cached_property
    def certificates(self) -> CertificatesResourceWithStreamingResponse:
        return CertificatesResourceWithStreamingResponse(self._access.certificates)

    @cached_property
    def groups(self) -> GroupsResourceWithStreamingResponse:
        return GroupsResourceWithStreamingResponse(self._access.groups)

    @cached_property
    def service_tokens(self) -> ServiceTokensResourceWithStreamingResponse:
        return ServiceTokensResourceWithStreamingResponse(self._access.service_tokens)

    @cached_property
    def bookmarks(self) -> BookmarksResourceWithStreamingResponse:
        return BookmarksResourceWithStreamingResponse(self._access.bookmarks)

    @cached_property
    def keys(self) -> KeysResourceWithStreamingResponse:
        return KeysResourceWithStreamingResponse(self._access.keys)

    @cached_property
    def logs(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self._access.logs)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._access.users)

    @cached_property
    def custom_pages(self) -> CustomPagesResourceWithStreamingResponse:
        return CustomPagesResourceWithStreamingResponse(self._access.custom_pages)

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self._access.tags)


class AsyncAccessResourceWithStreamingResponse:
    def __init__(self, access: AsyncAccessResource) -> None:
        self._access = access

    @cached_property
    def applications(self) -> AsyncApplicationsResourceWithStreamingResponse:
        return AsyncApplicationsResourceWithStreamingResponse(self._access.applications)

    @cached_property
    def certificates(self) -> AsyncCertificatesResourceWithStreamingResponse:
        return AsyncCertificatesResourceWithStreamingResponse(self._access.certificates)

    @cached_property
    def groups(self) -> AsyncGroupsResourceWithStreamingResponse:
        return AsyncGroupsResourceWithStreamingResponse(self._access.groups)

    @cached_property
    def service_tokens(self) -> AsyncServiceTokensResourceWithStreamingResponse:
        return AsyncServiceTokensResourceWithStreamingResponse(self._access.service_tokens)

    @cached_property
    def bookmarks(self) -> AsyncBookmarksResourceWithStreamingResponse:
        return AsyncBookmarksResourceWithStreamingResponse(self._access.bookmarks)

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        return AsyncKeysResourceWithStreamingResponse(self._access.keys)

    @cached_property
    def logs(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self._access.logs)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._access.users)

    @cached_property
    def custom_pages(self) -> AsyncCustomPagesResourceWithStreamingResponse:
        return AsyncCustomPagesResourceWithStreamingResponse(self._access.custom_pages)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self._access.tags)
