# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.email_sending import (
    SubdomainGetResponse,
    SubdomainListResponse,
    SubdomainCreateResponse,
    SubdomainDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubdomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        subdomain = client.email_sending.subdomains.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="sub.example.com",
        )
        assert_matches_type(Optional[SubdomainCreateResponse], subdomain, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.email_sending.subdomains.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="sub.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subdomain = response.parse()
        assert_matches_type(Optional[SubdomainCreateResponse], subdomain, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.email_sending.subdomains.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="sub.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subdomain = response.parse()
            assert_matches_type(Optional[SubdomainCreateResponse], subdomain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.email_sending.subdomains.with_raw_response.create(
                zone_id="",
                name="sub.example.com",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        subdomain = client.email_sending.subdomains.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[SubdomainListResponse], subdomain, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.email_sending.subdomains.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subdomain = response.parse()
        assert_matches_type(SyncSinglePage[SubdomainListResponse], subdomain, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.email_sending.subdomains.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subdomain = response.parse()
            assert_matches_type(SyncSinglePage[SubdomainListResponse], subdomain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.email_sending.subdomains.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        subdomain = client.email_sending.subdomains.delete(
            subdomain_id="aabbccdd11223344aabbccdd11223344",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SubdomainDeleteResponse, subdomain, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.email_sending.subdomains.with_raw_response.delete(
            subdomain_id="aabbccdd11223344aabbccdd11223344",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subdomain = response.parse()
        assert_matches_type(SubdomainDeleteResponse, subdomain, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.email_sending.subdomains.with_streaming_response.delete(
            subdomain_id="aabbccdd11223344aabbccdd11223344",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subdomain = response.parse()
            assert_matches_type(SubdomainDeleteResponse, subdomain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.email_sending.subdomains.with_raw_response.delete(
                subdomain_id="aabbccdd11223344aabbccdd11223344",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subdomain_id` but received ''"):
            client.email_sending.subdomains.with_raw_response.delete(
                subdomain_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        subdomain = client.email_sending.subdomains.get(
            subdomain_id="aabbccdd11223344aabbccdd11223344",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SubdomainGetResponse], subdomain, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.email_sending.subdomains.with_raw_response.get(
            subdomain_id="aabbccdd11223344aabbccdd11223344",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subdomain = response.parse()
        assert_matches_type(Optional[SubdomainGetResponse], subdomain, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.email_sending.subdomains.with_streaming_response.get(
            subdomain_id="aabbccdd11223344aabbccdd11223344",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subdomain = response.parse()
            assert_matches_type(Optional[SubdomainGetResponse], subdomain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.email_sending.subdomains.with_raw_response.get(
                subdomain_id="aabbccdd11223344aabbccdd11223344",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subdomain_id` but received ''"):
            client.email_sending.subdomains.with_raw_response.get(
                subdomain_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncSubdomains:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        subdomain = await async_client.email_sending.subdomains.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="sub.example.com",
        )
        assert_matches_type(Optional[SubdomainCreateResponse], subdomain, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_sending.subdomains.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="sub.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subdomain = await response.parse()
        assert_matches_type(Optional[SubdomainCreateResponse], subdomain, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_sending.subdomains.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="sub.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subdomain = await response.parse()
            assert_matches_type(Optional[SubdomainCreateResponse], subdomain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.email_sending.subdomains.with_raw_response.create(
                zone_id="",
                name="sub.example.com",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        subdomain = await async_client.email_sending.subdomains.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[SubdomainListResponse], subdomain, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_sending.subdomains.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subdomain = await response.parse()
        assert_matches_type(AsyncSinglePage[SubdomainListResponse], subdomain, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_sending.subdomains.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subdomain = await response.parse()
            assert_matches_type(AsyncSinglePage[SubdomainListResponse], subdomain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.email_sending.subdomains.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        subdomain = await async_client.email_sending.subdomains.delete(
            subdomain_id="aabbccdd11223344aabbccdd11223344",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SubdomainDeleteResponse, subdomain, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_sending.subdomains.with_raw_response.delete(
            subdomain_id="aabbccdd11223344aabbccdd11223344",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subdomain = await response.parse()
        assert_matches_type(SubdomainDeleteResponse, subdomain, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_sending.subdomains.with_streaming_response.delete(
            subdomain_id="aabbccdd11223344aabbccdd11223344",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subdomain = await response.parse()
            assert_matches_type(SubdomainDeleteResponse, subdomain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.email_sending.subdomains.with_raw_response.delete(
                subdomain_id="aabbccdd11223344aabbccdd11223344",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subdomain_id` but received ''"):
            await async_client.email_sending.subdomains.with_raw_response.delete(
                subdomain_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        subdomain = await async_client.email_sending.subdomains.get(
            subdomain_id="aabbccdd11223344aabbccdd11223344",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SubdomainGetResponse], subdomain, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_sending.subdomains.with_raw_response.get(
            subdomain_id="aabbccdd11223344aabbccdd11223344",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subdomain = await response.parse()
        assert_matches_type(Optional[SubdomainGetResponse], subdomain, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_sending.subdomains.with_streaming_response.get(
            subdomain_id="aabbccdd11223344aabbccdd11223344",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subdomain = await response.parse()
            assert_matches_type(Optional[SubdomainGetResponse], subdomain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.email_sending.subdomains.with_raw_response.get(
                subdomain_id="aabbccdd11223344aabbccdd11223344",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subdomain_id` but received ''"):
            await async_client.email_sending.subdomains.with_raw_response.get(
                subdomain_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
