# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.custom_certificates import CustomCertificate

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrioritize:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        prioritize = client.custom_certificates.prioritize.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificates=[{}, {}],
        )
        assert_matches_type(SyncSinglePage[CustomCertificate], prioritize, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.custom_certificates.prioritize.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificates=[{}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prioritize = response.parse()
        assert_matches_type(SyncSinglePage[CustomCertificate], prioritize, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.custom_certificates.prioritize.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificates=[{}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prioritize = response.parse()
            assert_matches_type(SyncSinglePage[CustomCertificate], prioritize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.custom_certificates.prioritize.with_raw_response.update(
                zone_id="",
                certificates=[{}, {}],
            )


class TestAsyncPrioritize:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        prioritize = await async_client.custom_certificates.prioritize.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificates=[{}, {}],
        )
        assert_matches_type(AsyncSinglePage[CustomCertificate], prioritize, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_certificates.prioritize.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificates=[{}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prioritize = await response.parse()
        assert_matches_type(AsyncSinglePage[CustomCertificate], prioritize, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_certificates.prioritize.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificates=[{}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prioritize = await response.parse()
            assert_matches_type(AsyncSinglePage[CustomCertificate], prioritize, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.custom_certificates.prioritize.with_raw_response.update(
                zone_id="",
                certificates=[{}, {}],
            )
