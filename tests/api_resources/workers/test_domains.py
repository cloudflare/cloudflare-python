# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, cast

from cloudflare.types.workers import (
    DomainGetResponse,
    DomainWorkerDomainAttachToDomainResponse,
    DomainWorkerDomainListDomainsResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.workers import domain_worker_domain_attach_to_domain_params
from cloudflare.types.workers import domain_worker_domain_list_domains_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        domain = client.workers.domains.delete(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )
        assert domain is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.workers.domains.with_raw_response.delete(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert domain is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.workers.domains.with_streaming_response.delete(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert domain is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        domain = client.workers.domains.get(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )
        assert_matches_type(DomainGetResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.workers.domains.with_raw_response.get(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainGetResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.workers.domains.with_streaming_response.get(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainGetResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_worker_domain_attach_to_domain(self, client: Cloudflare) -> None:
        domain = client.workers.domains.worker_domain_attach_to_domain(
            "9a7806061c88ada191ed06f989cc3dac",
            environment="production",
            hostname="foo.example.com",
            service="foo",
            zone_id="593c9c94de529bbbfaac7c53ced0447d",
        )
        assert_matches_type(DomainWorkerDomainAttachToDomainResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_worker_domain_attach_to_domain(self, client: Cloudflare) -> None:
        response = client.workers.domains.with_raw_response.worker_domain_attach_to_domain(
            "9a7806061c88ada191ed06f989cc3dac",
            environment="production",
            hostname="foo.example.com",
            service="foo",
            zone_id="593c9c94de529bbbfaac7c53ced0447d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainWorkerDomainAttachToDomainResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_worker_domain_attach_to_domain(self, client: Cloudflare) -> None:
        with client.workers.domains.with_streaming_response.worker_domain_attach_to_domain(
            "9a7806061c88ada191ed06f989cc3dac",
            environment="production",
            hostname="foo.example.com",
            service="foo",
            zone_id="593c9c94de529bbbfaac7c53ced0447d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainWorkerDomainAttachToDomainResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_worker_domain_list_domains(self, client: Cloudflare) -> None:
        domain = client.workers.domains.worker_domain_list_domains(
            "9a7806061c88ada191ed06f989cc3dac",
        )
        assert_matches_type(DomainWorkerDomainListDomainsResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_worker_domain_list_domains_with_all_params(self, client: Cloudflare) -> None:
        domain = client.workers.domains.worker_domain_list_domains(
            "9a7806061c88ada191ed06f989cc3dac",
            environment="production",
            hostname="foo.example.com",
            service="foo",
            zone_id="593c9c94de529bbbfaac7c53ced0447d",
            zone_name="example.com",
        )
        assert_matches_type(DomainWorkerDomainListDomainsResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_worker_domain_list_domains(self, client: Cloudflare) -> None:
        response = client.workers.domains.with_raw_response.worker_domain_list_domains(
            "9a7806061c88ada191ed06f989cc3dac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainWorkerDomainListDomainsResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_worker_domain_list_domains(self, client: Cloudflare) -> None:
        with client.workers.domains.with_streaming_response.worker_domain_list_domains(
            "9a7806061c88ada191ed06f989cc3dac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainWorkerDomainListDomainsResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDomains:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.workers.domains.delete(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )
        assert domain is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.domains.with_raw_response.delete(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert domain is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.domains.with_streaming_response.delete(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert domain is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.workers.domains.get(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )
        assert_matches_type(DomainGetResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.domains.with_raw_response.get(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainGetResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.domains.with_streaming_response.get(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainGetResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_worker_domain_attach_to_domain(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.workers.domains.worker_domain_attach_to_domain(
            "9a7806061c88ada191ed06f989cc3dac",
            environment="production",
            hostname="foo.example.com",
            service="foo",
            zone_id="593c9c94de529bbbfaac7c53ced0447d",
        )
        assert_matches_type(DomainWorkerDomainAttachToDomainResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_worker_domain_attach_to_domain(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.domains.with_raw_response.worker_domain_attach_to_domain(
            "9a7806061c88ada191ed06f989cc3dac",
            environment="production",
            hostname="foo.example.com",
            service="foo",
            zone_id="593c9c94de529bbbfaac7c53ced0447d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainWorkerDomainAttachToDomainResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_worker_domain_attach_to_domain(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.domains.with_streaming_response.worker_domain_attach_to_domain(
            "9a7806061c88ada191ed06f989cc3dac",
            environment="production",
            hostname="foo.example.com",
            service="foo",
            zone_id="593c9c94de529bbbfaac7c53ced0447d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainWorkerDomainAttachToDomainResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_worker_domain_list_domains(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.workers.domains.worker_domain_list_domains(
            "9a7806061c88ada191ed06f989cc3dac",
        )
        assert_matches_type(DomainWorkerDomainListDomainsResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_worker_domain_list_domains_with_all_params(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.workers.domains.worker_domain_list_domains(
            "9a7806061c88ada191ed06f989cc3dac",
            environment="production",
            hostname="foo.example.com",
            service="foo",
            zone_id="593c9c94de529bbbfaac7c53ced0447d",
            zone_name="example.com",
        )
        assert_matches_type(DomainWorkerDomainListDomainsResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_worker_domain_list_domains(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.domains.with_raw_response.worker_domain_list_domains(
            "9a7806061c88ada191ed06f989cc3dac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainWorkerDomainListDomainsResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_worker_domain_list_domains(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.domains.with_streaming_response.worker_domain_list_domains(
            "9a7806061c88ada191ed06f989cc3dac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainWorkerDomainListDomainsResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True
