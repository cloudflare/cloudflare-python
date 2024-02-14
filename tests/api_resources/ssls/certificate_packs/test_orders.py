# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.ssls.certificate_packs import (
    OrderCertificatePacksOrderAdvancedCertificateManagerCertificatePackResponse,
)

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.ssls.certificate_packs import (
    order_certificate_packs_order_advanced_certificate_manager_certificate_pack_params,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_certificate_packs_order_advanced_certificate_manager_certificate_pack(
        self, client: Cloudflare
    ) -> None:
        order = (
            client.ssls.certificate_packs.orders.certificate_packs_order_advanced_certificate_manager_certificate_pack(
                "023e105f4ecef8ad9ca31a8372d0c353",
                certificate_authority="lets_encrypt",
                hosts=["example.com", "*.example.com", "www.example.com"],
                type="advanced",
                validation_method="txt",
                validity_days=14,
            )
        )
        assert_matches_type(
            OrderCertificatePacksOrderAdvancedCertificateManagerCertificatePackResponse, order, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_certificate_packs_order_advanced_certificate_manager_certificate_pack_with_all_params(
        self, client: Cloudflare
    ) -> None:
        order = (
            client.ssls.certificate_packs.orders.certificate_packs_order_advanced_certificate_manager_certificate_pack(
                "023e105f4ecef8ad9ca31a8372d0c353",
                certificate_authority="lets_encrypt",
                hosts=["example.com", "*.example.com", "www.example.com"],
                type="advanced",
                validation_method="txt",
                validity_days=14,
                cloudflare_branding=False,
            )
        )
        assert_matches_type(
            OrderCertificatePacksOrderAdvancedCertificateManagerCertificatePackResponse, order, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_certificate_packs_order_advanced_certificate_manager_certificate_pack(
        self, client: Cloudflare
    ) -> None:
        response = client.ssls.certificate_packs.orders.with_raw_response.certificate_packs_order_advanced_certificate_manager_certificate_pack(
            "023e105f4ecef8ad9ca31a8372d0c353",
            certificate_authority="lets_encrypt",
            hosts=["example.com", "*.example.com", "www.example.com"],
            type="advanced",
            validation_method="txt",
            validity_days=14,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(
            OrderCertificatePacksOrderAdvancedCertificateManagerCertificatePackResponse, order, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_certificate_packs_order_advanced_certificate_manager_certificate_pack(
        self, client: Cloudflare
    ) -> None:
        with client.ssls.certificate_packs.orders.with_streaming_response.certificate_packs_order_advanced_certificate_manager_certificate_pack(
            "023e105f4ecef8ad9ca31a8372d0c353",
            certificate_authority="lets_encrypt",
            hosts=["example.com", "*.example.com", "www.example.com"],
            type="advanced",
            validation_method="txt",
            validity_days=14,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(
                OrderCertificatePacksOrderAdvancedCertificateManagerCertificatePackResponse, order, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_certificate_packs_order_advanced_certificate_manager_certificate_pack(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.ssls.certificate_packs.orders.with_raw_response.certificate_packs_order_advanced_certificate_manager_certificate_pack(
                "",
                certificate_authority="lets_encrypt",
                hosts=["example.com", "*.example.com", "www.example.com"],
                type="advanced",
                validation_method="txt",
                validity_days=14,
            )


class TestAsyncOrders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_certificate_packs_order_advanced_certificate_manager_certificate_pack(
        self, async_client: AsyncCloudflare
    ) -> None:
        order = await async_client.ssls.certificate_packs.orders.certificate_packs_order_advanced_certificate_manager_certificate_pack(
            "023e105f4ecef8ad9ca31a8372d0c353",
            certificate_authority="lets_encrypt",
            hosts=["example.com", "*.example.com", "www.example.com"],
            type="advanced",
            validation_method="txt",
            validity_days=14,
        )
        assert_matches_type(
            OrderCertificatePacksOrderAdvancedCertificateManagerCertificatePackResponse, order, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_certificate_packs_order_advanced_certificate_manager_certificate_pack_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        order = await async_client.ssls.certificate_packs.orders.certificate_packs_order_advanced_certificate_manager_certificate_pack(
            "023e105f4ecef8ad9ca31a8372d0c353",
            certificate_authority="lets_encrypt",
            hosts=["example.com", "*.example.com", "www.example.com"],
            type="advanced",
            validation_method="txt",
            validity_days=14,
            cloudflare_branding=False,
        )
        assert_matches_type(
            OrderCertificatePacksOrderAdvancedCertificateManagerCertificatePackResponse, order, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_certificate_packs_order_advanced_certificate_manager_certificate_pack(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.ssls.certificate_packs.orders.with_raw_response.certificate_packs_order_advanced_certificate_manager_certificate_pack(
            "023e105f4ecef8ad9ca31a8372d0c353",
            certificate_authority="lets_encrypt",
            hosts=["example.com", "*.example.com", "www.example.com"],
            type="advanced",
            validation_method="txt",
            validity_days=14,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(
            OrderCertificatePacksOrderAdvancedCertificateManagerCertificatePackResponse, order, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_certificate_packs_order_advanced_certificate_manager_certificate_pack(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.ssls.certificate_packs.orders.with_streaming_response.certificate_packs_order_advanced_certificate_manager_certificate_pack(
            "023e105f4ecef8ad9ca31a8372d0c353",
            certificate_authority="lets_encrypt",
            hosts=["example.com", "*.example.com", "www.example.com"],
            type="advanced",
            validation_method="txt",
            validity_days=14,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(
                OrderCertificatePacksOrderAdvancedCertificateManagerCertificatePackResponse, order, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_certificate_packs_order_advanced_certificate_manager_certificate_pack(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.ssls.certificate_packs.orders.with_raw_response.certificate_packs_order_advanced_certificate_manager_certificate_pack(
                "",
                certificate_authority="lets_encrypt",
                hosts=["example.com", "*.example.com", "www.example.com"],
                type="advanced",
                validation_method="txt",
                validity_days=14,
            )
