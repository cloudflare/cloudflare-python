# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.tenant_custom_nameservers import (
    TenantCustomNameserverGetResponse,
    TenantCustomNameserverCreateResponse,
    TenantCustomNameserverDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTenantCustomNameservers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        tenant_custom_nameserver = client.tenant_custom_nameservers.create(
            tenant_tag="699d98642c564d2e855e9661899b7252",
            ns_name="ns1.example.com",
        )
        assert_matches_type(Optional[TenantCustomNameserverCreateResponse], tenant_custom_nameserver, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        tenant_custom_nameserver = client.tenant_custom_nameservers.create(
            tenant_tag="699d98642c564d2e855e9661899b7252",
            ns_name="ns1.example.com",
            ns_set=1,
        )
        assert_matches_type(Optional[TenantCustomNameserverCreateResponse], tenant_custom_nameserver, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.tenant_custom_nameservers.with_raw_response.create(
            tenant_tag="699d98642c564d2e855e9661899b7252",
            ns_name="ns1.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant_custom_nameserver = response.parse()
        assert_matches_type(Optional[TenantCustomNameserverCreateResponse], tenant_custom_nameserver, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.tenant_custom_nameservers.with_streaming_response.create(
            tenant_tag="699d98642c564d2e855e9661899b7252",
            ns_name="ns1.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant_custom_nameserver = response.parse()
            assert_matches_type(
                Optional[TenantCustomNameserverCreateResponse], tenant_custom_nameserver, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_tag` but received ''"):
            client.tenant_custom_nameservers.with_raw_response.create(
                tenant_tag="",
                ns_name="ns1.example.com",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        tenant_custom_nameserver = client.tenant_custom_nameservers.delete(
            custom_ns_id="ns1.example.com",
            tenant_tag="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            SyncSinglePage[TenantCustomNameserverDeleteResponse], tenant_custom_nameserver, path=["response"]
        )

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.tenant_custom_nameservers.with_raw_response.delete(
            custom_ns_id="ns1.example.com",
            tenant_tag="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant_custom_nameserver = response.parse()
        assert_matches_type(
            SyncSinglePage[TenantCustomNameserverDeleteResponse], tenant_custom_nameserver, path=["response"]
        )

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.tenant_custom_nameservers.with_streaming_response.delete(
            custom_ns_id="ns1.example.com",
            tenant_tag="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant_custom_nameserver = response.parse()
            assert_matches_type(
                SyncSinglePage[TenantCustomNameserverDeleteResponse], tenant_custom_nameserver, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_tag` but received ''"):
            client.tenant_custom_nameservers.with_raw_response.delete(
                custom_ns_id="ns1.example.com",
                tenant_tag="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_ns_id` but received ''"):
            client.tenant_custom_nameservers.with_raw_response.delete(
                custom_ns_id="",
                tenant_tag="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        tenant_custom_nameserver = client.tenant_custom_nameservers.get(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            SyncSinglePage[TenantCustomNameserverGetResponse], tenant_custom_nameserver, path=["response"]
        )

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.tenant_custom_nameservers.with_raw_response.get(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant_custom_nameserver = response.parse()
        assert_matches_type(
            SyncSinglePage[TenantCustomNameserverGetResponse], tenant_custom_nameserver, path=["response"]
        )

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.tenant_custom_nameservers.with_streaming_response.get(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant_custom_nameserver = response.parse()
            assert_matches_type(
                SyncSinglePage[TenantCustomNameserverGetResponse], tenant_custom_nameserver, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_tag` but received ''"):
            client.tenant_custom_nameservers.with_raw_response.get(
                "",
            )


class TestAsyncTenantCustomNameservers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        tenant_custom_nameserver = await async_client.tenant_custom_nameservers.create(
            tenant_tag="699d98642c564d2e855e9661899b7252",
            ns_name="ns1.example.com",
        )
        assert_matches_type(Optional[TenantCustomNameserverCreateResponse], tenant_custom_nameserver, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        tenant_custom_nameserver = await async_client.tenant_custom_nameservers.create(
            tenant_tag="699d98642c564d2e855e9661899b7252",
            ns_name="ns1.example.com",
            ns_set=1,
        )
        assert_matches_type(Optional[TenantCustomNameserverCreateResponse], tenant_custom_nameserver, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.tenant_custom_nameservers.with_raw_response.create(
            tenant_tag="699d98642c564d2e855e9661899b7252",
            ns_name="ns1.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant_custom_nameserver = await response.parse()
        assert_matches_type(Optional[TenantCustomNameserverCreateResponse], tenant_custom_nameserver, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.tenant_custom_nameservers.with_streaming_response.create(
            tenant_tag="699d98642c564d2e855e9661899b7252",
            ns_name="ns1.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant_custom_nameserver = await response.parse()
            assert_matches_type(
                Optional[TenantCustomNameserverCreateResponse], tenant_custom_nameserver, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_tag` but received ''"):
            await async_client.tenant_custom_nameservers.with_raw_response.create(
                tenant_tag="",
                ns_name="ns1.example.com",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        tenant_custom_nameserver = await async_client.tenant_custom_nameservers.delete(
            custom_ns_id="ns1.example.com",
            tenant_tag="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            AsyncSinglePage[TenantCustomNameserverDeleteResponse], tenant_custom_nameserver, path=["response"]
        )

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.tenant_custom_nameservers.with_raw_response.delete(
            custom_ns_id="ns1.example.com",
            tenant_tag="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant_custom_nameserver = await response.parse()
        assert_matches_type(
            AsyncSinglePage[TenantCustomNameserverDeleteResponse], tenant_custom_nameserver, path=["response"]
        )

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.tenant_custom_nameservers.with_streaming_response.delete(
            custom_ns_id="ns1.example.com",
            tenant_tag="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant_custom_nameserver = await response.parse()
            assert_matches_type(
                AsyncSinglePage[TenantCustomNameserverDeleteResponse], tenant_custom_nameserver, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_tag` but received ''"):
            await async_client.tenant_custom_nameservers.with_raw_response.delete(
                custom_ns_id="ns1.example.com",
                tenant_tag="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_ns_id` but received ''"):
            await async_client.tenant_custom_nameservers.with_raw_response.delete(
                custom_ns_id="",
                tenant_tag="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        tenant_custom_nameserver = await async_client.tenant_custom_nameservers.get(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            AsyncSinglePage[TenantCustomNameserverGetResponse], tenant_custom_nameserver, path=["response"]
        )

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.tenant_custom_nameservers.with_raw_response.get(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tenant_custom_nameserver = await response.parse()
        assert_matches_type(
            AsyncSinglePage[TenantCustomNameserverGetResponse], tenant_custom_nameserver, path=["response"]
        )

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.tenant_custom_nameservers.with_streaming_response.get(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tenant_custom_nameserver = await response.parse()
            assert_matches_type(
                AsyncSinglePage[TenantCustomNameserverGetResponse], tenant_custom_nameserver, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tenant_tag` but received ''"):
            await async_client.tenant_custom_nameservers.with_raw_response.get(
                "",
            )
