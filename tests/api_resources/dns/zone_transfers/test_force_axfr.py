# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestForceAXFR:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        force_axfr = client.dns.zone_transfers.force_axfr.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        )
        assert_matches_type(str, force_axfr, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.dns.zone_transfers.force_axfr.with_raw_response.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        force_axfr = response.parse()
        assert_matches_type(str, force_axfr, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.dns.zone_transfers.force_axfr.with_streaming_response.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            force_axfr = response.parse()
            assert_matches_type(str, force_axfr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.zone_transfers.force_axfr.with_raw_response.create(
                zone_id="",
                body={},
            )


class TestAsyncForceAXFR:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        force_axfr = await async_client.dns.zone_transfers.force_axfr.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        )
        assert_matches_type(str, force_axfr, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.zone_transfers.force_axfr.with_raw_response.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        force_axfr = await response.parse()
        assert_matches_type(str, force_axfr, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.zone_transfers.force_axfr.with_streaming_response.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            force_axfr = await response.parse()
            assert_matches_type(str, force_axfr, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.zone_transfers.force_axfr.with_raw_response.create(
                zone_id="",
                body={},
            )
