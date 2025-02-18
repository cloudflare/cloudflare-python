# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zaraz import Workflow

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestZaraz:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        zaraz = client.zaraz.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            workflow="realtime",
        )
        assert_matches_type(Workflow, zaraz, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zaraz.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            workflow="realtime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zaraz = response.parse()
        assert_matches_type(Workflow, zaraz, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zaraz.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            workflow="realtime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zaraz = response.parse()
            assert_matches_type(Workflow, zaraz, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zaraz.with_raw_response.update(
                zone_id="",
                workflow="realtime",
            )


class TestAsyncZaraz:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        zaraz = await async_client.zaraz.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            workflow="realtime",
        )
        assert_matches_type(Workflow, zaraz, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zaraz.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            workflow="realtime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zaraz = await response.parse()
        assert_matches_type(Workflow, zaraz, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zaraz.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            workflow="realtime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zaraz = await response.parse()
            assert_matches_type(Workflow, zaraz, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zaraz.with_raw_response.update(
                zone_id="",
                workflow="realtime",
            )
