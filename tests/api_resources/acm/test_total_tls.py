# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from typing import Optional, Any, cast

from cloudflare.types.acm import TotalTLSCreateResponse, TotalTLSGetResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.acm import total_tls_create_params
from cloudflare.types.acm import CertificateAuthority

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTotalTLS:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        total_tls = client.acm.total_tls.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        )
        assert_matches_type(Optional[TotalTLSCreateResponse], total_tls, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        total_tls = client.acm.total_tls.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            certificate_authority="google",
        )
        assert_matches_type(Optional[TotalTLSCreateResponse], total_tls, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.acm.total_tls.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        total_tls = response.parse()
        assert_matches_type(Optional[TotalTLSCreateResponse], total_tls, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.acm.total_tls.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            total_tls = response.parse()
            assert_matches_type(Optional[TotalTLSCreateResponse], total_tls, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.acm.total_tls.with_raw_response.create(
                zone_id="",
                enabled=True,
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        total_tls = client.acm.total_tls.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[TotalTLSGetResponse], total_tls, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.acm.total_tls.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        total_tls = response.parse()
        assert_matches_type(Optional[TotalTLSGetResponse], total_tls, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.acm.total_tls.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            total_tls = response.parse()
            assert_matches_type(Optional[TotalTLSGetResponse], total_tls, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.acm.total_tls.with_raw_response.get(
                zone_id="",
            )


class TestAsyncTotalTLS:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        total_tls = await async_client.acm.total_tls.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        )
        assert_matches_type(Optional[TotalTLSCreateResponse], total_tls, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        total_tls = await async_client.acm.total_tls.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            certificate_authority="google",
        )
        assert_matches_type(Optional[TotalTLSCreateResponse], total_tls, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.acm.total_tls.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        total_tls = await response.parse()
        assert_matches_type(Optional[TotalTLSCreateResponse], total_tls, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.acm.total_tls.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            total_tls = await response.parse()
            assert_matches_type(Optional[TotalTLSCreateResponse], total_tls, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.acm.total_tls.with_raw_response.create(
                zone_id="",
                enabled=True,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        total_tls = await async_client.acm.total_tls.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[TotalTLSGetResponse], total_tls, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.acm.total_tls.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        total_tls = await response.parse()
        assert_matches_type(Optional[TotalTLSGetResponse], total_tls, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.acm.total_tls.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            total_tls = await response.parse()
            assert_matches_type(Optional[TotalTLSGetResponse], total_tls, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.acm.total_tls.with_raw_response.get(
                zone_id="",
            )
