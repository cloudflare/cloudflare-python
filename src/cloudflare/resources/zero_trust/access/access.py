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
from .tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
from .groups import (
    GroupsResource,
    AsyncGroupsResource,
    GroupsResourceWithRawResponse,
    AsyncGroupsResourceWithRawResponse,
    GroupsResourceWithStreamingResponse,
    AsyncGroupsResourceWithStreamingResponse,
)
from .policies import (
    PoliciesResource,
    AsyncPoliciesResource,
    PoliciesResourceWithRawResponse,
    AsyncPoliciesResourceWithRawResponse,
    PoliciesResourceWithStreamingResponse,
    AsyncPoliciesResourceWithStreamingResponse,
)
from .bookmarks import (
    BookmarksResource,
    AsyncBookmarksResource,
    BookmarksResourceWithRawResponse,
    AsyncBookmarksResourceWithRawResponse,
    BookmarksResourceWithStreamingResponse,
    AsyncBookmarksResourceWithStreamingResponse,
)
from .logs.logs import (
    LogsResource,
    AsyncLogsResource,
    LogsResourceWithRawResponse,
    AsyncLogsResourceWithRawResponse,
    LogsResourceWithStreamingResponse,
    AsyncLogsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .gateway_ca import (
    GatewayCAResource,
    AsyncGatewayCAResource,
    GatewayCAResourceWithRawResponse,
    AsyncGatewayCAResourceWithRawResponse,
    GatewayCAResourceWithStreamingResponse,
    AsyncGatewayCAResourceWithStreamingResponse,
)
from .users.users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
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
from .applications.applications import (
    ApplicationsResource,
    AsyncApplicationsResource,
    ApplicationsResourceWithRawResponse,
    AsyncApplicationsResourceWithRawResponse,
    ApplicationsResourceWithStreamingResponse,
    AsyncApplicationsResourceWithStreamingResponse,
)
from .certificates.certificates import (
    CertificatesResource,
    AsyncCertificatesResource,
    CertificatesResourceWithRawResponse,
    AsyncCertificatesResourceWithRawResponse,
    CertificatesResourceWithStreamingResponse,
    AsyncCertificatesResourceWithStreamingResponse,
)
from .infrastructure.infrastructure import (
    InfrastructureResource,
    AsyncInfrastructureResource,
    InfrastructureResourceWithRawResponse,
    AsyncInfrastructureResourceWithRawResponse,
    InfrastructureResourceWithStreamingResponse,
    AsyncInfrastructureResourceWithStreamingResponse,
)

__all__ = ["AccessResource", "AsyncAccessResource"]


class AccessResource(SyncAPIResource):
    @cached_property
    def gateway_ca(self) -> GatewayCAResource:
        return GatewayCAResource(self._client)

    @cached_property
    def infrastructure(self) -> InfrastructureResource:
        return InfrastructureResource(self._client)

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
    def policies(self) -> PoliciesResource:
        return PoliciesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccessResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AccessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AccessResourceWithStreamingResponse(self)


class AsyncAccessResource(AsyncAPIResource):
    @cached_property
    def gateway_ca(self) -> AsyncGatewayCAResource:
        return AsyncGatewayCAResource(self._client)

    @cached_property
    def infrastructure(self) -> AsyncInfrastructureResource:
        return AsyncInfrastructureResource(self._client)

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
    def policies(self) -> AsyncPoliciesResource:
        return AsyncPoliciesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccessResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccessResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAccessResourceWithStreamingResponse(self)


class AccessResourceWithRawResponse:
    def __init__(self, access: AccessResource) -> None:
        self._access = access

    @cached_property
    def gateway_ca(self) -> GatewayCAResourceWithRawResponse:
        return GatewayCAResourceWithRawResponse(self._access.gateway_ca)

    @cached_property
    def infrastructure(self) -> InfrastructureResourceWithRawResponse:
        return InfrastructureResourceWithRawResponse(self._access.infrastructure)

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

    @cached_property
    def policies(self) -> PoliciesResourceWithRawResponse:
        return PoliciesResourceWithRawResponse(self._access.policies)


class AsyncAccessResourceWithRawResponse:
    def __init__(self, access: AsyncAccessResource) -> None:
        self._access = access

    @cached_property
    def gateway_ca(self) -> AsyncGatewayCAResourceWithRawResponse:
        return AsyncGatewayCAResourceWithRawResponse(self._access.gateway_ca)

    @cached_property
    def infrastructure(self) -> AsyncInfrastructureResourceWithRawResponse:
        return AsyncInfrastructureResourceWithRawResponse(self._access.infrastructure)

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

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithRawResponse:
        return AsyncPoliciesResourceWithRawResponse(self._access.policies)


class AccessResourceWithStreamingResponse:
    def __init__(self, access: AccessResource) -> None:
        self._access = access

    @cached_property
    def gateway_ca(self) -> GatewayCAResourceWithStreamingResponse:
        return GatewayCAResourceWithStreamingResponse(self._access.gateway_ca)

    @cached_property
    def infrastructure(self) -> InfrastructureResourceWithStreamingResponse:
        return InfrastructureResourceWithStreamingResponse(self._access.infrastructure)

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

    @cached_property
    def policies(self) -> PoliciesResourceWithStreamingResponse:
        return PoliciesResourceWithStreamingResponse(self._access.policies)


class AsyncAccessResourceWithStreamingResponse:
    def __init__(self, access: AsyncAccessResource) -> None:
        self._access = access

    @cached_property
    def gateway_ca(self) -> AsyncGatewayCAResourceWithStreamingResponse:
        return AsyncGatewayCAResourceWithStreamingResponse(self._access.gateway_ca)

    @cached_property
    def infrastructure(self) -> AsyncInfrastructureResourceWithStreamingResponse:
        return AsyncInfrastructureResourceWithStreamingResponse(self._access.infrastructure)

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

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithStreamingResponse:
        return AsyncPoliciesResourceWithStreamingResponse(self._access.policies)
