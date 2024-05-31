# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .groups import (
    GroupsResource,
    AsyncGroupsResource,
    GroupsResourceWithRawResponse,
    AsyncGroupsResourceWithRawResponse,
    GroupsResourceWithStreamingResponse,
    AsyncGroupsResourceWithStreamingResponse,
)
from ...._compat import cached_property
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
