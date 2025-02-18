# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage, SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.email_security.settings import (
    DomainGetResponse,
    DomainEditResponse,
    DomainListResponse,
    DomainDeleteResponse,
    DomainBulkDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        domain = client.email_security.settings.domains.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[DomainListResponse], domain, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        domain = client.email_security.settings.domains.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            active_delivery_mode="DIRECT",
            allowed_delivery_mode="DIRECT",
            direction="asc",
            domain=["string"],
            order="domain",
            page=1,
            per_page=1,
            search="search",
        )
        assert_matches_type(SyncV4PagePaginationArray[DomainListResponse], domain, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.email_security.settings.domains.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[DomainListResponse], domain, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.email_security.settings.domains.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[DomainListResponse], domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.domains.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        domain = client.email_security.settings.domains.delete(
            domain_id=2400,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DomainDeleteResponse, domain, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.email_security.settings.domains.with_raw_response.delete(
            domain_id=2400,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainDeleteResponse, domain, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.email_security.settings.domains.with_streaming_response.delete(
            domain_id=2400,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainDeleteResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.domains.with_raw_response.delete(
                domain_id=2400,
                account_id="",
            )

    @parametrize
    def test_method_bulk_delete(self, client: Cloudflare) -> None:
        domain = client.email_security.settings.domains.bulk_delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[DomainBulkDeleteResponse], domain, path=["response"])

    @parametrize
    def test_raw_response_bulk_delete(self, client: Cloudflare) -> None:
        response = client.email_security.settings.domains.with_raw_response.bulk_delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(SyncSinglePage[DomainBulkDeleteResponse], domain, path=["response"])

    @parametrize
    def test_streaming_response_bulk_delete(self, client: Cloudflare) -> None:
        with client.email_security.settings.domains.with_streaming_response.bulk_delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(SyncSinglePage[DomainBulkDeleteResponse], domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.domains.with_raw_response.bulk_delete(
                account_id="",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        domain = client.email_security.settings.domains.edit(
            domain_id=2400,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ip_restrictions=["192.0.2.0/24", "2001:db8::/32"],
        )
        assert_matches_type(DomainEditResponse, domain, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        domain = client.email_security.settings.domains.edit(
            domain_id=2400,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ip_restrictions=["192.0.2.0/24", "2001:db8::/32"],
            domain="domain",
            drop_dispositions=["MALICIOUS"],
            folder="AllItems",
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            lookback_hops=1,
            require_tls_inbound=True,
            require_tls_outbound=True,
            transport="transport",
        )
        assert_matches_type(DomainEditResponse, domain, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.email_security.settings.domains.with_raw_response.edit(
            domain_id=2400,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ip_restrictions=["192.0.2.0/24", "2001:db8::/32"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainEditResponse, domain, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.email_security.settings.domains.with_streaming_response.edit(
            domain_id=2400,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ip_restrictions=["192.0.2.0/24", "2001:db8::/32"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainEditResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.domains.with_raw_response.edit(
                domain_id=2400,
                account_id="",
                ip_restrictions=["192.0.2.0/24", "2001:db8::/32"],
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        domain = client.email_security.settings.domains.get(
            domain_id=2400,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DomainGetResponse, domain, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.email_security.settings.domains.with_raw_response.get(
            domain_id=2400,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainGetResponse, domain, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.email_security.settings.domains.with_streaming_response.get(
            domain_id=2400,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainGetResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.settings.domains.with_raw_response.get(
                domain_id=2400,
                account_id="",
            )


class TestAsyncDomains:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.email_security.settings.domains.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[DomainListResponse], domain, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.email_security.settings.domains.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            active_delivery_mode="DIRECT",
            allowed_delivery_mode="DIRECT",
            direction="asc",
            domain=["string"],
            order="domain",
            page=1,
            per_page=1,
            search="search",
        )
        assert_matches_type(AsyncV4PagePaginationArray[DomainListResponse], domain, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.domains.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[DomainListResponse], domain, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.domains.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[DomainListResponse], domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.domains.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.email_security.settings.domains.delete(
            domain_id=2400,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DomainDeleteResponse, domain, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.domains.with_raw_response.delete(
            domain_id=2400,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainDeleteResponse, domain, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.domains.with_streaming_response.delete(
            domain_id=2400,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainDeleteResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.domains.with_raw_response.delete(
                domain_id=2400,
                account_id="",
            )

    @parametrize
    async def test_method_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.email_security.settings.domains.bulk_delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[DomainBulkDeleteResponse], domain, path=["response"])

    @parametrize
    async def test_raw_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.domains.with_raw_response.bulk_delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(AsyncSinglePage[DomainBulkDeleteResponse], domain, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.domains.with_streaming_response.bulk_delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(AsyncSinglePage[DomainBulkDeleteResponse], domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.domains.with_raw_response.bulk_delete(
                account_id="",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.email_security.settings.domains.edit(
            domain_id=2400,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ip_restrictions=["192.0.2.0/24", "2001:db8::/32"],
        )
        assert_matches_type(DomainEditResponse, domain, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.email_security.settings.domains.edit(
            domain_id=2400,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ip_restrictions=["192.0.2.0/24", "2001:db8::/32"],
            domain="domain",
            drop_dispositions=["MALICIOUS"],
            folder="AllItems",
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            lookback_hops=1,
            require_tls_inbound=True,
            require_tls_outbound=True,
            transport="transport",
        )
        assert_matches_type(DomainEditResponse, domain, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.domains.with_raw_response.edit(
            domain_id=2400,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ip_restrictions=["192.0.2.0/24", "2001:db8::/32"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainEditResponse, domain, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.domains.with_streaming_response.edit(
            domain_id=2400,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ip_restrictions=["192.0.2.0/24", "2001:db8::/32"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainEditResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.domains.with_raw_response.edit(
                domain_id=2400,
                account_id="",
                ip_restrictions=["192.0.2.0/24", "2001:db8::/32"],
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.email_security.settings.domains.get(
            domain_id=2400,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DomainGetResponse, domain, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.settings.domains.with_raw_response.get(
            domain_id=2400,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainGetResponse, domain, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.settings.domains.with_streaming_response.get(
            domain_id=2400,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainGetResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.settings.domains.with_raw_response.get(
                domain_id=2400,
                account_id="",
            )
