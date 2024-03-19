# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .keys import (
    Keys,
    AsyncKeys,
    KeysWithRawResponse,
    AsyncKeysWithRawResponse,
    KeysWithStreamingResponse,
    AsyncKeysWithStreamingResponse,
)
from .logs import (
    Logs,
    AsyncLogs,
    LogsWithRawResponse,
    AsyncLogsWithRawResponse,
    LogsWithStreamingResponse,
    AsyncLogsWithStreamingResponse,
)
from .tags import (
    Tags,
    AsyncTags,
    TagsWithRawResponse,
    AsyncTagsWithRawResponse,
    TagsWithStreamingResponse,
    AsyncTagsWithStreamingResponse,
)
from .users import (
    Users,
    AsyncUsers,
    UsersWithRawResponse,
    AsyncUsersWithRawResponse,
    UsersWithStreamingResponse,
    AsyncUsersWithStreamingResponse,
)
from .groups import (
    Groups,
    AsyncGroups,
    GroupsWithRawResponse,
    AsyncGroupsWithRawResponse,
    GroupsWithStreamingResponse,
    AsyncGroupsWithStreamingResponse,
)
from .bookmarks import (
    Bookmarks,
    AsyncBookmarks,
    BookmarksWithRawResponse,
    AsyncBookmarksWithRawResponse,
    BookmarksWithStreamingResponse,
    AsyncBookmarksWithStreamingResponse,
)
from .logs.logs import Logs, AsyncLogs
from ...._compat import cached_property
from .users.users import Users, AsyncUsers
from ...._resource import SyncAPIResource, AsyncAPIResource
from .applications import (
    Applications,
    AsyncApplications,
    ApplicationsWithRawResponse,
    AsyncApplicationsWithRawResponse,
    ApplicationsWithStreamingResponse,
    AsyncApplicationsWithStreamingResponse,
)
from .certificates import (
    Certificates,
    AsyncCertificates,
    CertificatesWithRawResponse,
    AsyncCertificatesWithRawResponse,
    CertificatesWithStreamingResponse,
    AsyncCertificatesWithStreamingResponse,
)
from .custom_pages import (
    CustomPages,
    AsyncCustomPages,
    CustomPagesWithRawResponse,
    AsyncCustomPagesWithRawResponse,
    CustomPagesWithStreamingResponse,
    AsyncCustomPagesWithStreamingResponse,
)
from .service_tokens import (
    ServiceTokens,
    AsyncServiceTokens,
    ServiceTokensWithRawResponse,
    AsyncServiceTokensWithRawResponse,
    ServiceTokensWithStreamingResponse,
    AsyncServiceTokensWithStreamingResponse,
)
from .applications.applications import Applications, AsyncApplications
from .certificates.certificates import Certificates, AsyncCertificates

__all__ = ["Access", "AsyncAccess"]


class Access(SyncAPIResource):
    @cached_property
    def applications(self) -> Applications:
        return Applications(self._client)

    @cached_property
    def certificates(self) -> Certificates:
        return Certificates(self._client)

    @cached_property
    def groups(self) -> Groups:
        return Groups(self._client)

    @cached_property
    def service_tokens(self) -> ServiceTokens:
        return ServiceTokens(self._client)

    @cached_property
    def bookmarks(self) -> Bookmarks:
        return Bookmarks(self._client)

    @cached_property
    def keys(self) -> Keys:
        return Keys(self._client)

    @cached_property
    def logs(self) -> Logs:
        return Logs(self._client)

    @cached_property
    def users(self) -> Users:
        return Users(self._client)

    @cached_property
    def custom_pages(self) -> CustomPages:
        return CustomPages(self._client)

    @cached_property
    def tags(self) -> Tags:
        return Tags(self._client)

    @cached_property
    def with_raw_response(self) -> AccessWithRawResponse:
        return AccessWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessWithStreamingResponse:
        return AccessWithStreamingResponse(self)


class AsyncAccess(AsyncAPIResource):
    @cached_property
    def applications(self) -> AsyncApplications:
        return AsyncApplications(self._client)

    @cached_property
    def certificates(self) -> AsyncCertificates:
        return AsyncCertificates(self._client)

    @cached_property
    def groups(self) -> AsyncGroups:
        return AsyncGroups(self._client)

    @cached_property
    def service_tokens(self) -> AsyncServiceTokens:
        return AsyncServiceTokens(self._client)

    @cached_property
    def bookmarks(self) -> AsyncBookmarks:
        return AsyncBookmarks(self._client)

    @cached_property
    def keys(self) -> AsyncKeys:
        return AsyncKeys(self._client)

    @cached_property
    def logs(self) -> AsyncLogs:
        return AsyncLogs(self._client)

    @cached_property
    def users(self) -> AsyncUsers:
        return AsyncUsers(self._client)

    @cached_property
    def custom_pages(self) -> AsyncCustomPages:
        return AsyncCustomPages(self._client)

    @cached_property
    def tags(self) -> AsyncTags:
        return AsyncTags(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccessWithRawResponse:
        return AsyncAccessWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessWithStreamingResponse:
        return AsyncAccessWithStreamingResponse(self)


class AccessWithRawResponse:
    def __init__(self, access: Access) -> None:
        self._access = access

    @cached_property
    def applications(self) -> ApplicationsWithRawResponse:
        return ApplicationsWithRawResponse(self._access.applications)

    @cached_property
    def certificates(self) -> CertificatesWithRawResponse:
        return CertificatesWithRawResponse(self._access.certificates)

    @cached_property
    def groups(self) -> GroupsWithRawResponse:
        return GroupsWithRawResponse(self._access.groups)

    @cached_property
    def service_tokens(self) -> ServiceTokensWithRawResponse:
        return ServiceTokensWithRawResponse(self._access.service_tokens)

    @cached_property
    def bookmarks(self) -> BookmarksWithRawResponse:
        return BookmarksWithRawResponse(self._access.bookmarks)

    @cached_property
    def keys(self) -> KeysWithRawResponse:
        return KeysWithRawResponse(self._access.keys)

    @cached_property
    def logs(self) -> LogsWithRawResponse:
        return LogsWithRawResponse(self._access.logs)

    @cached_property
    def users(self) -> UsersWithRawResponse:
        return UsersWithRawResponse(self._access.users)

    @cached_property
    def custom_pages(self) -> CustomPagesWithRawResponse:
        return CustomPagesWithRawResponse(self._access.custom_pages)

    @cached_property
    def tags(self) -> TagsWithRawResponse:
        return TagsWithRawResponse(self._access.tags)


class AsyncAccessWithRawResponse:
    def __init__(self, access: AsyncAccess) -> None:
        self._access = access

    @cached_property
    def applications(self) -> AsyncApplicationsWithRawResponse:
        return AsyncApplicationsWithRawResponse(self._access.applications)

    @cached_property
    def certificates(self) -> AsyncCertificatesWithRawResponse:
        return AsyncCertificatesWithRawResponse(self._access.certificates)

    @cached_property
    def groups(self) -> AsyncGroupsWithRawResponse:
        return AsyncGroupsWithRawResponse(self._access.groups)

    @cached_property
    def service_tokens(self) -> AsyncServiceTokensWithRawResponse:
        return AsyncServiceTokensWithRawResponse(self._access.service_tokens)

    @cached_property
    def bookmarks(self) -> AsyncBookmarksWithRawResponse:
        return AsyncBookmarksWithRawResponse(self._access.bookmarks)

    @cached_property
    def keys(self) -> AsyncKeysWithRawResponse:
        return AsyncKeysWithRawResponse(self._access.keys)

    @cached_property
    def logs(self) -> AsyncLogsWithRawResponse:
        return AsyncLogsWithRawResponse(self._access.logs)

    @cached_property
    def users(self) -> AsyncUsersWithRawResponse:
        return AsyncUsersWithRawResponse(self._access.users)

    @cached_property
    def custom_pages(self) -> AsyncCustomPagesWithRawResponse:
        return AsyncCustomPagesWithRawResponse(self._access.custom_pages)

    @cached_property
    def tags(self) -> AsyncTagsWithRawResponse:
        return AsyncTagsWithRawResponse(self._access.tags)


class AccessWithStreamingResponse:
    def __init__(self, access: Access) -> None:
        self._access = access

    @cached_property
    def applications(self) -> ApplicationsWithStreamingResponse:
        return ApplicationsWithStreamingResponse(self._access.applications)

    @cached_property
    def certificates(self) -> CertificatesWithStreamingResponse:
        return CertificatesWithStreamingResponse(self._access.certificates)

    @cached_property
    def groups(self) -> GroupsWithStreamingResponse:
        return GroupsWithStreamingResponse(self._access.groups)

    @cached_property
    def service_tokens(self) -> ServiceTokensWithStreamingResponse:
        return ServiceTokensWithStreamingResponse(self._access.service_tokens)

    @cached_property
    def bookmarks(self) -> BookmarksWithStreamingResponse:
        return BookmarksWithStreamingResponse(self._access.bookmarks)

    @cached_property
    def keys(self) -> KeysWithStreamingResponse:
        return KeysWithStreamingResponse(self._access.keys)

    @cached_property
    def logs(self) -> LogsWithStreamingResponse:
        return LogsWithStreamingResponse(self._access.logs)

    @cached_property
    def users(self) -> UsersWithStreamingResponse:
        return UsersWithStreamingResponse(self._access.users)

    @cached_property
    def custom_pages(self) -> CustomPagesWithStreamingResponse:
        return CustomPagesWithStreamingResponse(self._access.custom_pages)

    @cached_property
    def tags(self) -> TagsWithStreamingResponse:
        return TagsWithStreamingResponse(self._access.tags)


class AsyncAccessWithStreamingResponse:
    def __init__(self, access: AsyncAccess) -> None:
        self._access = access

    @cached_property
    def applications(self) -> AsyncApplicationsWithStreamingResponse:
        return AsyncApplicationsWithStreamingResponse(self._access.applications)

    @cached_property
    def certificates(self) -> AsyncCertificatesWithStreamingResponse:
        return AsyncCertificatesWithStreamingResponse(self._access.certificates)

    @cached_property
    def groups(self) -> AsyncGroupsWithStreamingResponse:
        return AsyncGroupsWithStreamingResponse(self._access.groups)

    @cached_property
    def service_tokens(self) -> AsyncServiceTokensWithStreamingResponse:
        return AsyncServiceTokensWithStreamingResponse(self._access.service_tokens)

    @cached_property
    def bookmarks(self) -> AsyncBookmarksWithStreamingResponse:
        return AsyncBookmarksWithStreamingResponse(self._access.bookmarks)

    @cached_property
    def keys(self) -> AsyncKeysWithStreamingResponse:
        return AsyncKeysWithStreamingResponse(self._access.keys)

    @cached_property
    def logs(self) -> AsyncLogsWithStreamingResponse:
        return AsyncLogsWithStreamingResponse(self._access.logs)

    @cached_property
    def users(self) -> AsyncUsersWithStreamingResponse:
        return AsyncUsersWithStreamingResponse(self._access.users)

    @cached_property
    def custom_pages(self) -> AsyncCustomPagesWithStreamingResponse:
        return AsyncCustomPagesWithStreamingResponse(self._access.custom_pages)

    @cached_property
    def tags(self) -> AsyncTagsWithStreamingResponse:
        return AsyncTagsWithStreamingResponse(self._access.tags)
