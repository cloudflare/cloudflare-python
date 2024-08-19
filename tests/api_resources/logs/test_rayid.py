# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.logs import RayIDGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRayID:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        rayid = client.logs.rayid.get(
            rayid="41ddf1740f67442d",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RayIDGetResponse, rayid, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        rayid = client.logs.rayid.get(
            rayid="41ddf1740f67442d",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            fields="ClientIP,RayID,EdgeStartTimestamp",
            timestamps="unix",
        )
        assert_matches_type(RayIDGetResponse, rayid, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.logs.rayid.with_raw_response.get(
            rayid="41ddf1740f67442d",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rayid = response.parse()
        assert_matches_type(RayIDGetResponse, rayid, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.logs.rayid.with_streaming_response.get(
            rayid="41ddf1740f67442d",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rayid = response.parse()
            assert_matches_type(RayIDGetResponse, rayid, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.logs.rayid.with_raw_response.get(
                rayid="41ddf1740f67442d",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rayid` but received ''"):
            client.logs.rayid.with_raw_response.get(
                rayid="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncRayID:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        rayid = await async_client.logs.rayid.get(
            rayid="41ddf1740f67442d",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RayIDGetResponse, rayid, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rayid = await async_client.logs.rayid.get(
            rayid="41ddf1740f67442d",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            fields="ClientIP,RayID,EdgeStartTimestamp",
            timestamps="unix",
        )
        assert_matches_type(RayIDGetResponse, rayid, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.logs.rayid.with_raw_response.get(
            rayid="41ddf1740f67442d",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rayid = await response.parse()
        assert_matches_type(RayIDGetResponse, rayid, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.logs.rayid.with_streaming_response.get(
            rayid="41ddf1740f67442d",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rayid = await response.parse()
            assert_matches_type(RayIDGetResponse, rayid, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.logs.rayid.with_raw_response.get(
                rayid="41ddf1740f67442d",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rayid` but received ''"):
            await async_client.logs.rayid.with_raw_response.get(
                rayid="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
