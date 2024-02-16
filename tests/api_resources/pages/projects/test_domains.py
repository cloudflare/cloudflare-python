# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.pages.projects import (
    DomainUpdateResponse,
    DomainGetResponse,
    DomainPagesDomainsAddDomainResponse,
    DomainPagesDomainsGetDomainsResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.pages.projects import domain_pages_domains_add_domain_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        domain = client.pages.projects.domains.update(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )
        assert_matches_type(Optional[DomainUpdateResponse], domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.pages.projects.domains.with_raw_response.update(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(Optional[DomainUpdateResponse], domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.pages.projects.domains.with_streaming_response.update(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(Optional[DomainUpdateResponse], domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.domains.with_raw_response.update(
                "string",
                account_id="",
                project_name="this-is-my-project-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            client.pages.projects.domains.with_raw_response.update(
                "string",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
            client.pages.projects.domains.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="this-is-my-project-01",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        domain = client.pages.projects.domains.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )
        assert_matches_type(object, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.pages.projects.domains.with_raw_response.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(object, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.pages.projects.domains.with_streaming_response.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(object, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.domains.with_raw_response.delete(
                "string",
                account_id="",
                project_name="this-is-my-project-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            client.pages.projects.domains.with_raw_response.delete(
                "string",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
            client.pages.projects.domains.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="this-is-my-project-01",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        domain = client.pages.projects.domains.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )
        assert_matches_type(Optional[DomainGetResponse], domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.pages.projects.domains.with_raw_response.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(Optional[DomainGetResponse], domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.pages.projects.domains.with_streaming_response.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(Optional[DomainGetResponse], domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.domains.with_raw_response.get(
                "string",
                account_id="",
                project_name="this-is-my-project-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            client.pages.projects.domains.with_raw_response.get(
                "string",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
            client.pages.projects.domains.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="this-is-my-project-01",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_pages_domains_add_domain(self, client: Cloudflare) -> None:
        domain = client.pages.projects.domains.pages_domains_add_domain(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={"name": "example.com"},
        )
        assert_matches_type(Optional[DomainPagesDomainsAddDomainResponse], domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_pages_domains_add_domain(self, client: Cloudflare) -> None:
        response = client.pages.projects.domains.with_raw_response.pages_domains_add_domain(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={"name": "example.com"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(Optional[DomainPagesDomainsAddDomainResponse], domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_pages_domains_add_domain(self, client: Cloudflare) -> None:
        with client.pages.projects.domains.with_streaming_response.pages_domains_add_domain(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={"name": "example.com"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(Optional[DomainPagesDomainsAddDomainResponse], domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_pages_domains_add_domain(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.domains.with_raw_response.pages_domains_add_domain(
                "this-is-my-project-01",
                account_id="",
                body={"name": "example.com"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            client.pages.projects.domains.with_raw_response.pages_domains_add_domain(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={"name": "example.com"},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_pages_domains_get_domains(self, client: Cloudflare) -> None:
        domain = client.pages.projects.domains.pages_domains_get_domains(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DomainPagesDomainsGetDomainsResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_pages_domains_get_domains(self, client: Cloudflare) -> None:
        response = client.pages.projects.domains.with_raw_response.pages_domains_get_domains(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainPagesDomainsGetDomainsResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_pages_domains_get_domains(self, client: Cloudflare) -> None:
        with client.pages.projects.domains.with_streaming_response.pages_domains_get_domains(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainPagesDomainsGetDomainsResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_pages_domains_get_domains(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.domains.with_raw_response.pages_domains_get_domains(
                "this-is-my-project-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            client.pages.projects.domains.with_raw_response.pages_domains_get_domains(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncDomains:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.pages.projects.domains.update(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )
        assert_matches_type(Optional[DomainUpdateResponse], domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pages.projects.domains.with_raw_response.update(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(Optional[DomainUpdateResponse], domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pages.projects.domains.with_streaming_response.update(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(Optional[DomainUpdateResponse], domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.update(
                "string",
                account_id="",
                project_name="this-is-my-project-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.update(
                "string",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="this-is-my-project-01",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.pages.projects.domains.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )
        assert_matches_type(object, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pages.projects.domains.with_raw_response.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(object, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pages.projects.domains.with_streaming_response.delete(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(object, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.delete(
                "string",
                account_id="",
                project_name="this-is-my-project-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.delete(
                "string",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="this-is-my-project-01",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.pages.projects.domains.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )
        assert_matches_type(Optional[DomainGetResponse], domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pages.projects.domains.with_raw_response.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(Optional[DomainGetResponse], domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pages.projects.domains.with_streaming_response.get(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            project_name="this-is-my-project-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(Optional[DomainGetResponse], domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.get(
                "string",
                account_id="",
                project_name="this-is-my-project-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.get(
                "string",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                project_name="this-is-my-project-01",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_pages_domains_add_domain(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.pages.projects.domains.pages_domains_add_domain(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={"name": "example.com"},
        )
        assert_matches_type(Optional[DomainPagesDomainsAddDomainResponse], domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_pages_domains_add_domain(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pages.projects.domains.with_raw_response.pages_domains_add_domain(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={"name": "example.com"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(Optional[DomainPagesDomainsAddDomainResponse], domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_pages_domains_add_domain(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pages.projects.domains.with_streaming_response.pages_domains_add_domain(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={"name": "example.com"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(Optional[DomainPagesDomainsAddDomainResponse], domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_pages_domains_add_domain(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.pages_domains_add_domain(
                "this-is-my-project-01",
                account_id="",
                body={"name": "example.com"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.pages_domains_add_domain(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={"name": "example.com"},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_pages_domains_get_domains(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.pages.projects.domains.pages_domains_get_domains(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DomainPagesDomainsGetDomainsResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_pages_domains_get_domains(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pages.projects.domains.with_raw_response.pages_domains_get_domains(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainPagesDomainsGetDomainsResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_pages_domains_get_domains(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pages.projects.domains.with_streaming_response.pages_domains_get_domains(
            "this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainPagesDomainsGetDomainsResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_pages_domains_get_domains(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.pages_domains_get_domains(
                "this-is-my-project-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            await async_client.pages.projects.domains.with_raw_response.pages_domains_get_domains(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
