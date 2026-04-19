# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.google_tag_gateway import Config

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        config = client.google_tag_gateway.config.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            endpoint="/metrics",
            hide_original_ip=True,
            measurement_id="GTM-P2F3N47Q",
        )
        assert_matches_type(Optional[Config], config, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        config = client.google_tag_gateway.config.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            endpoint="/metrics",
            hide_original_ip=True,
            measurement_id="GTM-P2F3N47Q",
            set_up_tag=True,
        )
        assert_matches_type(Optional[Config], config, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.google_tag_gateway.config.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            endpoint="/metrics",
            hide_original_ip=True,
            measurement_id="GTM-P2F3N47Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(Optional[Config], config, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.google_tag_gateway.config.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            endpoint="/metrics",
            hide_original_ip=True,
            measurement_id="GTM-P2F3N47Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(Optional[Config], config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.google_tag_gateway.config.with_raw_response.update(
                zone_id="",
                enabled=True,
                endpoint="/metrics",
                hide_original_ip=True,
                measurement_id="GTM-P2F3N47Q",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        config = client.google_tag_gateway.config.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Config], config, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.google_tag_gateway.config.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(Optional[Config], config, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.google_tag_gateway.config.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(Optional[Config], config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.google_tag_gateway.config.with_raw_response.get(
                zone_id="",
            )


class TestAsyncConfig:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.google_tag_gateway.config.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            endpoint="/metrics",
            hide_original_ip=True,
            measurement_id="GTM-P2F3N47Q",
        )
        assert_matches_type(Optional[Config], config, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.google_tag_gateway.config.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            endpoint="/metrics",
            hide_original_ip=True,
            measurement_id="GTM-P2F3N47Q",
            set_up_tag=True,
        )
        assert_matches_type(Optional[Config], config, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.google_tag_gateway.config.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            endpoint="/metrics",
            hide_original_ip=True,
            measurement_id="GTM-P2F3N47Q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(Optional[Config], config, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.google_tag_gateway.config.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            endpoint="/metrics",
            hide_original_ip=True,
            measurement_id="GTM-P2F3N47Q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(Optional[Config], config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.google_tag_gateway.config.with_raw_response.update(
                zone_id="",
                enabled=True,
                endpoint="/metrics",
                hide_original_ip=True,
                measurement_id="GTM-P2F3N47Q",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        config = await async_client.google_tag_gateway.config.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Config], config, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.google_tag_gateway.config.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(Optional[Config], config, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.google_tag_gateway.config.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(Optional[Config], config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.google_tag_gateway.config.with_raw_response.get(
                zone_id="",
            )
