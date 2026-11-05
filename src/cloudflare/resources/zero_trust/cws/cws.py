# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .policies import (
    PoliciesResource,
    AsyncPoliciesResource,
    PoliciesResourceWithRawResponse,
    AsyncPoliciesResourceWithRawResponse,
    PoliciesResourceWithStreamingResponse,
    AsyncPoliciesResourceWithStreamingResponse,
)
from .workloads import (
    WorkloadsResource,
    AsyncWorkloadsResource,
    WorkloadsResourceWithRawResponse,
    AsyncWorkloadsResourceWithRawResponse,
    WorkloadsResourceWithStreamingResponse,
    AsyncWorkloadsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .deployments import (
    DeploymentsResource,
    AsyncDeploymentsResource,
    DeploymentsResourceWithRawResponse,
    AsyncDeploymentsResourceWithRawResponse,
    DeploymentsResourceWithStreamingResponse,
    AsyncDeploymentsResourceWithStreamingResponse,
)
from .domain_acls import (
    DomainACLsResource,
    AsyncDomainACLsResource,
    DomainACLsResourceWithRawResponse,
    AsyncDomainACLsResourceWithRawResponse,
    DomainACLsResourceWithStreamingResponse,
    AsyncDomainACLsResourceWithStreamingResponse,
)
from .policy_sets import (
    PolicySetsResource,
    AsyncPolicySetsResource,
    PolicySetsResourceWithRawResponse,
    AsyncPolicySetsResourceWithRawResponse,
    PolicySetsResourceWithStreamingResponse,
    AsyncPolicySetsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from .rego_modules import (
    RegoModulesResource,
    AsyncRegoModulesResource,
    RegoModulesResourceWithRawResponse,
    AsyncRegoModulesResourceWithRawResponse,
    RegoModulesResourceWithStreamingResponse,
    AsyncRegoModulesResourceWithStreamingResponse,
)
from .rego_metadata import (
    RegoMetadataResource,
    AsyncRegoMetadataResource,
    RegoMetadataResourceWithRawResponse,
    AsyncRegoMetadataResourceWithRawResponse,
    RegoMetadataResourceWithStreamingResponse,
    AsyncRegoMetadataResourceWithStreamingResponse,
)
from .tenant_structures.tenant_structures import (
    TenantStructuresResource,
    AsyncTenantStructuresResource,
    TenantStructuresResourceWithRawResponse,
    AsyncTenantStructuresResourceWithRawResponse,
    TenantStructuresResourceWithStreamingResponse,
    AsyncTenantStructuresResourceWithStreamingResponse,
)
from .basic_auth_credentials.basic_auth_credentials import (
    BasicAuthCredentialsResource,
    AsyncBasicAuthCredentialsResource,
    BasicAuthCredentialsResourceWithRawResponse,
    AsyncBasicAuthCredentialsResourceWithRawResponse,
    BasicAuthCredentialsResourceWithStreamingResponse,
    AsyncBasicAuthCredentialsResourceWithStreamingResponse,
)

__all__ = ["CWSResource", "AsyncCWSResource"]


class CWSResource(SyncAPIResource):
    @cached_property
    def basic_auth_credentials(self) -> BasicAuthCredentialsResource:
        return BasicAuthCredentialsResource(self._client)

    @cached_property
    def deployments(self) -> DeploymentsResource:
        return DeploymentsResource(self._client)

    @cached_property
    def domain_acls(self) -> DomainACLsResource:
        return DomainACLsResource(self._client)

    @cached_property
    def policies(self) -> PoliciesResource:
        return PoliciesResource(self._client)

    @cached_property
    def policy_sets(self) -> PolicySetsResource:
        return PolicySetsResource(self._client)

    @cached_property
    def rego_metadata(self) -> RegoMetadataResource:
        return RegoMetadataResource(self._client)

    @cached_property
    def rego_modules(self) -> RegoModulesResource:
        return RegoModulesResource(self._client)

    @cached_property
    def tenant_structures(self) -> TenantStructuresResource:
        return TenantStructuresResource(self._client)

    @cached_property
    def workloads(self) -> WorkloadsResource:
        return WorkloadsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CWSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CWSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CWSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CWSResourceWithStreamingResponse(self)


class AsyncCWSResource(AsyncAPIResource):
    @cached_property
    def basic_auth_credentials(self) -> AsyncBasicAuthCredentialsResource:
        return AsyncBasicAuthCredentialsResource(self._client)

    @cached_property
    def deployments(self) -> AsyncDeploymentsResource:
        return AsyncDeploymentsResource(self._client)

    @cached_property
    def domain_acls(self) -> AsyncDomainACLsResource:
        return AsyncDomainACLsResource(self._client)

    @cached_property
    def policies(self) -> AsyncPoliciesResource:
        return AsyncPoliciesResource(self._client)

    @cached_property
    def policy_sets(self) -> AsyncPolicySetsResource:
        return AsyncPolicySetsResource(self._client)

    @cached_property
    def rego_metadata(self) -> AsyncRegoMetadataResource:
        return AsyncRegoMetadataResource(self._client)

    @cached_property
    def rego_modules(self) -> AsyncRegoModulesResource:
        return AsyncRegoModulesResource(self._client)

    @cached_property
    def tenant_structures(self) -> AsyncTenantStructuresResource:
        return AsyncTenantStructuresResource(self._client)

    @cached_property
    def workloads(self) -> AsyncWorkloadsResource:
        return AsyncWorkloadsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCWSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCWSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCWSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCWSResourceWithStreamingResponse(self)


class CWSResourceWithRawResponse:
    def __init__(self, cws: CWSResource) -> None:
        self._cws = cws

    @cached_property
    def basic_auth_credentials(self) -> BasicAuthCredentialsResourceWithRawResponse:
        return BasicAuthCredentialsResourceWithRawResponse(self._cws.basic_auth_credentials)

    @cached_property
    def deployments(self) -> DeploymentsResourceWithRawResponse:
        return DeploymentsResourceWithRawResponse(self._cws.deployments)

    @cached_property
    def domain_acls(self) -> DomainACLsResourceWithRawResponse:
        return DomainACLsResourceWithRawResponse(self._cws.domain_acls)

    @cached_property
    def policies(self) -> PoliciesResourceWithRawResponse:
        return PoliciesResourceWithRawResponse(self._cws.policies)

    @cached_property
    def policy_sets(self) -> PolicySetsResourceWithRawResponse:
        return PolicySetsResourceWithRawResponse(self._cws.policy_sets)

    @cached_property
    def rego_metadata(self) -> RegoMetadataResourceWithRawResponse:
        return RegoMetadataResourceWithRawResponse(self._cws.rego_metadata)

    @cached_property
    def rego_modules(self) -> RegoModulesResourceWithRawResponse:
        return RegoModulesResourceWithRawResponse(self._cws.rego_modules)

    @cached_property
    def tenant_structures(self) -> TenantStructuresResourceWithRawResponse:
        return TenantStructuresResourceWithRawResponse(self._cws.tenant_structures)

    @cached_property
    def workloads(self) -> WorkloadsResourceWithRawResponse:
        return WorkloadsResourceWithRawResponse(self._cws.workloads)


class AsyncCWSResourceWithRawResponse:
    def __init__(self, cws: AsyncCWSResource) -> None:
        self._cws = cws

    @cached_property
    def basic_auth_credentials(self) -> AsyncBasicAuthCredentialsResourceWithRawResponse:
        return AsyncBasicAuthCredentialsResourceWithRawResponse(self._cws.basic_auth_credentials)

    @cached_property
    def deployments(self) -> AsyncDeploymentsResourceWithRawResponse:
        return AsyncDeploymentsResourceWithRawResponse(self._cws.deployments)

    @cached_property
    def domain_acls(self) -> AsyncDomainACLsResourceWithRawResponse:
        return AsyncDomainACLsResourceWithRawResponse(self._cws.domain_acls)

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithRawResponse:
        return AsyncPoliciesResourceWithRawResponse(self._cws.policies)

    @cached_property
    def policy_sets(self) -> AsyncPolicySetsResourceWithRawResponse:
        return AsyncPolicySetsResourceWithRawResponse(self._cws.policy_sets)

    @cached_property
    def rego_metadata(self) -> AsyncRegoMetadataResourceWithRawResponse:
        return AsyncRegoMetadataResourceWithRawResponse(self._cws.rego_metadata)

    @cached_property
    def rego_modules(self) -> AsyncRegoModulesResourceWithRawResponse:
        return AsyncRegoModulesResourceWithRawResponse(self._cws.rego_modules)

    @cached_property
    def tenant_structures(self) -> AsyncTenantStructuresResourceWithRawResponse:
        return AsyncTenantStructuresResourceWithRawResponse(self._cws.tenant_structures)

    @cached_property
    def workloads(self) -> AsyncWorkloadsResourceWithRawResponse:
        return AsyncWorkloadsResourceWithRawResponse(self._cws.workloads)


class CWSResourceWithStreamingResponse:
    def __init__(self, cws: CWSResource) -> None:
        self._cws = cws

    @cached_property
    def basic_auth_credentials(self) -> BasicAuthCredentialsResourceWithStreamingResponse:
        return BasicAuthCredentialsResourceWithStreamingResponse(self._cws.basic_auth_credentials)

    @cached_property
    def deployments(self) -> DeploymentsResourceWithStreamingResponse:
        return DeploymentsResourceWithStreamingResponse(self._cws.deployments)

    @cached_property
    def domain_acls(self) -> DomainACLsResourceWithStreamingResponse:
        return DomainACLsResourceWithStreamingResponse(self._cws.domain_acls)

    @cached_property
    def policies(self) -> PoliciesResourceWithStreamingResponse:
        return PoliciesResourceWithStreamingResponse(self._cws.policies)

    @cached_property
    def policy_sets(self) -> PolicySetsResourceWithStreamingResponse:
        return PolicySetsResourceWithStreamingResponse(self._cws.policy_sets)

    @cached_property
    def rego_metadata(self) -> RegoMetadataResourceWithStreamingResponse:
        return RegoMetadataResourceWithStreamingResponse(self._cws.rego_metadata)

    @cached_property
    def rego_modules(self) -> RegoModulesResourceWithStreamingResponse:
        return RegoModulesResourceWithStreamingResponse(self._cws.rego_modules)

    @cached_property
    def tenant_structures(self) -> TenantStructuresResourceWithStreamingResponse:
        return TenantStructuresResourceWithStreamingResponse(self._cws.tenant_structures)

    @cached_property
    def workloads(self) -> WorkloadsResourceWithStreamingResponse:
        return WorkloadsResourceWithStreamingResponse(self._cws.workloads)


class AsyncCWSResourceWithStreamingResponse:
    def __init__(self, cws: AsyncCWSResource) -> None:
        self._cws = cws

    @cached_property
    def basic_auth_credentials(self) -> AsyncBasicAuthCredentialsResourceWithStreamingResponse:
        return AsyncBasicAuthCredentialsResourceWithStreamingResponse(self._cws.basic_auth_credentials)

    @cached_property
    def deployments(self) -> AsyncDeploymentsResourceWithStreamingResponse:
        return AsyncDeploymentsResourceWithStreamingResponse(self._cws.deployments)

    @cached_property
    def domain_acls(self) -> AsyncDomainACLsResourceWithStreamingResponse:
        return AsyncDomainACLsResourceWithStreamingResponse(self._cws.domain_acls)

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithStreamingResponse:
        return AsyncPoliciesResourceWithStreamingResponse(self._cws.policies)

    @cached_property
    def policy_sets(self) -> AsyncPolicySetsResourceWithStreamingResponse:
        return AsyncPolicySetsResourceWithStreamingResponse(self._cws.policy_sets)

    @cached_property
    def rego_metadata(self) -> AsyncRegoMetadataResourceWithStreamingResponse:
        return AsyncRegoMetadataResourceWithStreamingResponse(self._cws.rego_metadata)

    @cached_property
    def rego_modules(self) -> AsyncRegoModulesResourceWithStreamingResponse:
        return AsyncRegoModulesResourceWithStreamingResponse(self._cws.rego_modules)

    @cached_property
    def tenant_structures(self) -> AsyncTenantStructuresResourceWithStreamingResponse:
        return AsyncTenantStructuresResourceWithStreamingResponse(self._cws.tenant_structures)

    @cached_property
    def workloads(self) -> AsyncWorkloadsResourceWithStreamingResponse:
        return AsyncWorkloadsResourceWithStreamingResponse(self._cws.workloads)
