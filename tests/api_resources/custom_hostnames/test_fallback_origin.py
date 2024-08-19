# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.custom_hostnames import (
    FallbackOriginGetResponse,
    FallbackOriginDeleteResponse,
    FallbackOriginUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFallbackOrigin:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        fallback_origin = client.custom_hostnames.fallback_origin.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            origin="fallback.example.com",
        )
        assert_matches_type(Optional[FallbackOriginUpdateResponse], fallback_origin, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.custom_hostnames.fallback_origin.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            origin="fallback.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_origin = response.parse()
        assert_matches_type(Optional[FallbackOriginUpdateResponse], fallback_origin, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.custom_hostnames.fallback_origin.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            origin="fallback.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_origin = response.parse()
            assert_matches_type(Optional[FallbackOriginUpdateResponse], fallback_origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.custom_hostnames.fallback_origin.with_raw_response.update(
                zone_id="",
                origin="fallback.example.com",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        fallback_origin = client.custom_hostnames.fallback_origin.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[FallbackOriginDeleteResponse], fallback_origin, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.custom_hostnames.fallback_origin.with_raw_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_origin = response.parse()
        assert_matches_type(Optional[FallbackOriginDeleteResponse], fallback_origin, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.custom_hostnames.fallback_origin.with_streaming_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_origin = response.parse()
            assert_matches_type(Optional[FallbackOriginDeleteResponse], fallback_origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.custom_hostnames.fallback_origin.with_raw_response.delete(
                zone_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        fallback_origin = client.custom_hostnames.fallback_origin.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[FallbackOriginGetResponse], fallback_origin, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.custom_hostnames.fallback_origin.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_origin = response.parse()
        assert_matches_type(Optional[FallbackOriginGetResponse], fallback_origin, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.custom_hostnames.fallback_origin.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_origin = response.parse()
            assert_matches_type(Optional[FallbackOriginGetResponse], fallback_origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.custom_hostnames.fallback_origin.with_raw_response.get(
                zone_id="",
            )


class TestAsyncFallbackOrigin:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        fallback_origin = await async_client.custom_hostnames.fallback_origin.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            origin="fallback.example.com",
        )
        assert_matches_type(Optional[FallbackOriginUpdateResponse], fallback_origin, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_hostnames.fallback_origin.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            origin="fallback.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_origin = await response.parse()
        assert_matches_type(Optional[FallbackOriginUpdateResponse], fallback_origin, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_hostnames.fallback_origin.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            origin="fallback.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_origin = await response.parse()
            assert_matches_type(Optional[FallbackOriginUpdateResponse], fallback_origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.custom_hostnames.fallback_origin.with_raw_response.update(
                zone_id="",
                origin="fallback.example.com",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        fallback_origin = await async_client.custom_hostnames.fallback_origin.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[FallbackOriginDeleteResponse], fallback_origin, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_hostnames.fallback_origin.with_raw_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_origin = await response.parse()
        assert_matches_type(Optional[FallbackOriginDeleteResponse], fallback_origin, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_hostnames.fallback_origin.with_streaming_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_origin = await response.parse()
            assert_matches_type(Optional[FallbackOriginDeleteResponse], fallback_origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.custom_hostnames.fallback_origin.with_raw_response.delete(
                zone_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        fallback_origin = await async_client.custom_hostnames.fallback_origin.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[FallbackOriginGetResponse], fallback_origin, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_hostnames.fallback_origin.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fallback_origin = await response.parse()
        assert_matches_type(Optional[FallbackOriginGetResponse], fallback_origin, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_hostnames.fallback_origin.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fallback_origin = await response.parse()
            assert_matches_type(Optional[FallbackOriginGetResponse], fallback_origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.custom_hostnames.fallback_origin.with_raw_response.get(
                zone_id="",
            )
