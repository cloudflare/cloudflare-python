# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .apps.apps import Apps, AsyncApps

from ..._compat import cached_property

from .certificates.certificates import Certificates, AsyncCertificates

from .groups import Groups, AsyncGroups

from .identity_providers import IdentityProviders, AsyncIdentityProviders

from .organizations.organizations import Organizations, AsyncOrganizations

from .service_tokens.service_tokens import ServiceTokens, AsyncServiceTokens

from .bookmarks import Bookmarks, AsyncBookmarks

from .keys.keys import Keys, AsyncKeys

from .logs.logs import Logs, AsyncLogs

from .seats import Seats, AsyncSeats

from .users.users import Users, AsyncUsers

from .custom_pages import CustomPages, AsyncCustomPages

from .tags import Tags, AsyncTags

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
from .apps import (
    Apps,
    AsyncApps,
    AppsWithRawResponse,
    AsyncAppsWithRawResponse,
    AppsWithStreamingResponse,
    AsyncAppsWithStreamingResponse,
)
from .certificates import (
    Certificates,
    AsyncCertificates,
    CertificatesWithRawResponse,
    AsyncCertificatesWithRawResponse,
    CertificatesWithStreamingResponse,
    AsyncCertificatesWithStreamingResponse,
)
from .groups import (
    Groups,
    AsyncGroups,
    GroupsWithRawResponse,
    AsyncGroupsWithRawResponse,
    GroupsWithStreamingResponse,
    AsyncGroupsWithStreamingResponse,
)
from .identity_providers import (
    IdentityProviders,
    AsyncIdentityProviders,
    IdentityProvidersWithRawResponse,
    AsyncIdentityProvidersWithRawResponse,
    IdentityProvidersWithStreamingResponse,
    AsyncIdentityProvidersWithStreamingResponse,
)
from .organizations import (
    Organizations,
    AsyncOrganizations,
    OrganizationsWithRawResponse,
    AsyncOrganizationsWithRawResponse,
    OrganizationsWithStreamingResponse,
    AsyncOrganizationsWithStreamingResponse,
)
from .service_tokens import (
    ServiceTokens,
    AsyncServiceTokens,
    ServiceTokensWithRawResponse,
    AsyncServiceTokensWithRawResponse,
    ServiceTokensWithStreamingResponse,
    AsyncServiceTokensWithStreamingResponse,
)
from .bookmarks import (
    Bookmarks,
    AsyncBookmarks,
    BookmarksWithRawResponse,
    AsyncBookmarksWithRawResponse,
    BookmarksWithStreamingResponse,
    AsyncBookmarksWithStreamingResponse,
)
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
from .seats import (
    Seats,
    AsyncSeats,
    SeatsWithRawResponse,
    AsyncSeatsWithRawResponse,
    SeatsWithStreamingResponse,
    AsyncSeatsWithStreamingResponse,
)
from .users import (
    Users,
    AsyncUsers,
    UsersWithRawResponse,
    AsyncUsersWithRawResponse,
    UsersWithStreamingResponse,
    AsyncUsersWithStreamingResponse,
)
from .custom_pages import (
    CustomPages,
    AsyncCustomPages,
    CustomPagesWithRawResponse,
    AsyncCustomPagesWithRawResponse,
    CustomPagesWithStreamingResponse,
    AsyncCustomPagesWithStreamingResponse,
)
from .tags import (
    Tags,
    AsyncTags,
    TagsWithRawResponse,
    AsyncTagsWithRawResponse,
    TagsWithStreamingResponse,
    AsyncTagsWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["Access", "AsyncAccess"]


class Access(SyncAPIResource):
    @cached_property
    def apps(self) -> Apps:
        return Apps(self._client)

    @cached_property
    def certificates(self) -> Certificates:
        return Certificates(self._client)

    @cached_property
    def groups(self) -> Groups:
        return Groups(self._client)

    @cached_property
    def identity_providers(self) -> IdentityProviders:
        return IdentityProviders(self._client)

    @cached_property
    def organizations(self) -> Organizations:
        return Organizations(self._client)

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
    def seats(self) -> Seats:
        return Seats(self._client)

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
    def apps(self) -> AsyncApps:
        return AsyncApps(self._client)

    @cached_property
    def certificates(self) -> AsyncCertificates:
        return AsyncCertificates(self._client)

    @cached_property
    def groups(self) -> AsyncGroups:
        return AsyncGroups(self._client)

    @cached_property
    def identity_providers(self) -> AsyncIdentityProviders:
        return AsyncIdentityProviders(self._client)

    @cached_property
    def organizations(self) -> AsyncOrganizations:
        return AsyncOrganizations(self._client)

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
    def seats(self) -> AsyncSeats:
        return AsyncSeats(self._client)

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
    def apps(self) -> AppsWithRawResponse:
        return AppsWithRawResponse(self._access.apps)

    @cached_property
    def certificates(self) -> CertificatesWithRawResponse:
        return CertificatesWithRawResponse(self._access.certificates)

    @cached_property
    def groups(self) -> GroupsWithRawResponse:
        return GroupsWithRawResponse(self._access.groups)

    @cached_property
    def identity_providers(self) -> IdentityProvidersWithRawResponse:
        return IdentityProvidersWithRawResponse(self._access.identity_providers)

    @cached_property
    def organizations(self) -> OrganizationsWithRawResponse:
        return OrganizationsWithRawResponse(self._access.organizations)

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
    def seats(self) -> SeatsWithRawResponse:
        return SeatsWithRawResponse(self._access.seats)

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
    def apps(self) -> AsyncAppsWithRawResponse:
        return AsyncAppsWithRawResponse(self._access.apps)

    @cached_property
    def certificates(self) -> AsyncCertificatesWithRawResponse:
        return AsyncCertificatesWithRawResponse(self._access.certificates)

    @cached_property
    def groups(self) -> AsyncGroupsWithRawResponse:
        return AsyncGroupsWithRawResponse(self._access.groups)

    @cached_property
    def identity_providers(self) -> AsyncIdentityProvidersWithRawResponse:
        return AsyncIdentityProvidersWithRawResponse(self._access.identity_providers)

    @cached_property
    def organizations(self) -> AsyncOrganizationsWithRawResponse:
        return AsyncOrganizationsWithRawResponse(self._access.organizations)

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
    def seats(self) -> AsyncSeatsWithRawResponse:
        return AsyncSeatsWithRawResponse(self._access.seats)

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
    def apps(self) -> AppsWithStreamingResponse:
        return AppsWithStreamingResponse(self._access.apps)

    @cached_property
    def certificates(self) -> CertificatesWithStreamingResponse:
        return CertificatesWithStreamingResponse(self._access.certificates)

    @cached_property
    def groups(self) -> GroupsWithStreamingResponse:
        return GroupsWithStreamingResponse(self._access.groups)

    @cached_property
    def identity_providers(self) -> IdentityProvidersWithStreamingResponse:
        return IdentityProvidersWithStreamingResponse(self._access.identity_providers)

    @cached_property
    def organizations(self) -> OrganizationsWithStreamingResponse:
        return OrganizationsWithStreamingResponse(self._access.organizations)

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
    def seats(self) -> SeatsWithStreamingResponse:
        return SeatsWithStreamingResponse(self._access.seats)

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
    def apps(self) -> AsyncAppsWithStreamingResponse:
        return AsyncAppsWithStreamingResponse(self._access.apps)

    @cached_property
    def certificates(self) -> AsyncCertificatesWithStreamingResponse:
        return AsyncCertificatesWithStreamingResponse(self._access.certificates)

    @cached_property
    def groups(self) -> AsyncGroupsWithStreamingResponse:
        return AsyncGroupsWithStreamingResponse(self._access.groups)

    @cached_property
    def identity_providers(self) -> AsyncIdentityProvidersWithStreamingResponse:
        return AsyncIdentityProvidersWithStreamingResponse(self._access.identity_providers)

    @cached_property
    def organizations(self) -> AsyncOrganizationsWithStreamingResponse:
        return AsyncOrganizationsWithStreamingResponse(self._access.organizations)

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
    def seats(self) -> AsyncSeatsWithStreamingResponse:
        return AsyncSeatsWithStreamingResponse(self._access.seats)

    @cached_property
    def users(self) -> AsyncUsersWithStreamingResponse:
        return AsyncUsersWithStreamingResponse(self._access.users)

    @cached_property
    def custom_pages(self) -> AsyncCustomPagesWithStreamingResponse:
        return AsyncCustomPagesWithStreamingResponse(self._access.custom_pages)

    @cached_property
    def tags(self) -> AsyncTagsWithStreamingResponse:
        return AsyncTagsWithStreamingResponse(self._access.tags)
