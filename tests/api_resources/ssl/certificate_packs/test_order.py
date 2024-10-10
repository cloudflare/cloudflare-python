# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.ssl.certificate_packs import OrderCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrder:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        order = client.ssl.certificate_packs.order.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate_authority="google",
            hosts=["example.com", "*.example.com", "www.example.com"],
            type="advanced",
            validation_method="txt",
            validity_days=14,
        )
        assert_matches_type(Optional[OrderCreateResponse], order, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        order = client.ssl.certificate_packs.order.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate_authority="google",
            hosts=["example.com", "*.example.com", "www.example.com"],
            type="advanced",
            validation_method="txt",
            validity_days=14,
            cloudflare_branding=False,
        )
        assert_matches_type(Optional[OrderCreateResponse], order, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.ssl.certificate_packs.order.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate_authority="google",
            hosts=["example.com", "*.example.com", "www.example.com"],
            type="advanced",
            validation_method="txt",
            validity_days=14,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(Optional[OrderCreateResponse], order, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.ssl.certificate_packs.order.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate_authority="google",
            hosts=["example.com", "*.example.com", "www.example.com"],
            type="advanced",
            validation_method="txt",
            validity_days=14,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(Optional[OrderCreateResponse], order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.ssl.certificate_packs.order.with_raw_response.create(
                zone_id="",
                certificate_authority="google",
                hosts=["example.com", "*.example.com", "www.example.com"],
                type="advanced",
                validation_method="txt",
                validity_days=14,
            )


class TestAsyncOrder:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        order = await async_client.ssl.certificate_packs.order.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate_authority="google",
            hosts=["example.com", "*.example.com", "www.example.com"],
            type="advanced",
            validation_method="txt",
            validity_days=14,
        )
        assert_matches_type(Optional[OrderCreateResponse], order, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        order = await async_client.ssl.certificate_packs.order.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate_authority="google",
            hosts=["example.com", "*.example.com", "www.example.com"],
            type="advanced",
            validation_method="txt",
            validity_days=14,
            cloudflare_branding=False,
        )
        assert_matches_type(Optional[OrderCreateResponse], order, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ssl.certificate_packs.order.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate_authority="google",
            hosts=["example.com", "*.example.com", "www.example.com"],
            type="advanced",
            validation_method="txt",
            validity_days=14,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(Optional[OrderCreateResponse], order, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ssl.certificate_packs.order.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate_authority="google",
            hosts=["example.com", "*.example.com", "www.example.com"],
            type="advanced",
            validation_method="txt",
            validity_days=14,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(Optional[OrderCreateResponse], order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.ssl.certificate_packs.order.with_raw_response.create(
                zone_id="",
                certificate_authority="google",
                hosts=["example.com", "*.example.com", "www.example.com"],
                type="advanced",
                validation_method="txt",
                validity_days=14,
            )
