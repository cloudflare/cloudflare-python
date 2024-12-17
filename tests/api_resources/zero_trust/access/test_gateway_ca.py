# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.access import GatewayCAListResponse, GatewayCACreateResponse, GatewayCADeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGatewayCA:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        gateway_ca = client.zero_trust.access.gateway_ca.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[GatewayCACreateResponse], gateway_ca, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.gateway_ca.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway_ca = response.parse()
        assert_matches_type(Optional[GatewayCACreateResponse], gateway_ca, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.access.gateway_ca.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway_ca = response.parse()
            assert_matches_type(Optional[GatewayCACreateResponse], gateway_ca, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.gateway_ca.with_raw_response.create(
                account_id="",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        gateway_ca = client.zero_trust.access.gateway_ca.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[GatewayCAListResponse], gateway_ca, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.gateway_ca.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway_ca = response.parse()
        assert_matches_type(SyncSinglePage[GatewayCAListResponse], gateway_ca, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.access.gateway_ca.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway_ca = response.parse()
            assert_matches_type(SyncSinglePage[GatewayCAListResponse], gateway_ca, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.gateway_ca.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        gateway_ca = client.zero_trust.access.gateway_ca.delete(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[GatewayCADeleteResponse], gateway_ca, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.gateway_ca.with_raw_response.delete(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway_ca = response.parse()
        assert_matches_type(Optional[GatewayCADeleteResponse], gateway_ca, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.access.gateway_ca.with_streaming_response.delete(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway_ca = response.parse()
            assert_matches_type(Optional[GatewayCADeleteResponse], gateway_ca, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.gateway_ca.with_raw_response.delete(
                certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            client.zero_trust.access.gateway_ca.with_raw_response.delete(
                certificate_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncGatewayCA:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        gateway_ca = await async_client.zero_trust.access.gateway_ca.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[GatewayCACreateResponse], gateway_ca, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.gateway_ca.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway_ca = await response.parse()
        assert_matches_type(Optional[GatewayCACreateResponse], gateway_ca, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.gateway_ca.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway_ca = await response.parse()
            assert_matches_type(Optional[GatewayCACreateResponse], gateway_ca, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.gateway_ca.with_raw_response.create(
                account_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        gateway_ca = await async_client.zero_trust.access.gateway_ca.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[GatewayCAListResponse], gateway_ca, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.gateway_ca.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway_ca = await response.parse()
        assert_matches_type(AsyncSinglePage[GatewayCAListResponse], gateway_ca, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.gateway_ca.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway_ca = await response.parse()
            assert_matches_type(AsyncSinglePage[GatewayCAListResponse], gateway_ca, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.gateway_ca.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        gateway_ca = await async_client.zero_trust.access.gateway_ca.delete(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[GatewayCADeleteResponse], gateway_ca, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.gateway_ca.with_raw_response.delete(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway_ca = await response.parse()
        assert_matches_type(Optional[GatewayCADeleteResponse], gateway_ca, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.gateway_ca.with_streaming_response.delete(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway_ca = await response.parse()
            assert_matches_type(Optional[GatewayCADeleteResponse], gateway_ca, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.gateway_ca.with_raw_response.delete(
                certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            await async_client.zero_trust.access.gateway_ca.with_raw_response.delete(
                certificate_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
