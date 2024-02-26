# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestForceAxfrs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        force_axfr = client.secondary_dns.force_axfrs.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(str, force_axfr, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.secondary_dns.force_axfrs.with_raw_response.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        force_axfr = response.parse()
        assert_matches_type(str, force_axfr, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.secondary_dns.force_axfrs.with_streaming_response.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            force_axfr = response.parse()
            assert_matches_type(str, force_axfr, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncForceAxfrs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        force_axfr = await async_client.secondary_dns.force_axfrs.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(str, force_axfr, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secondary_dns.force_axfrs.with_raw_response.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        force_axfr = await response.parse()
        assert_matches_type(str, force_axfr, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.force_axfrs.with_streaming_response.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            force_axfr = await response.parse()
            assert_matches_type(str, force_axfr, path=["response"])

        assert cast(Any, response.is_closed) is True
