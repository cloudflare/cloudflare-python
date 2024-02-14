# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.secondary_dns.outgoings import EnableSecondaryDNSPrimaryZoneEnableOutgoingZoneTransfersResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnables:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_secondary_dns_primary_zone_enable_outgoing_zone_transfers(self, client: Cloudflare) -> None:
        enable = client.secondary_dns.outgoings.enables.secondary_dns_primary_zone_enable_outgoing_zone_transfers(
            "269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(str, enable, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_secondary_dns_primary_zone_enable_outgoing_zone_transfers(self, client: Cloudflare) -> None:
        response = client.secondary_dns.outgoings.enables.with_raw_response.secondary_dns_primary_zone_enable_outgoing_zone_transfers(
            "269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enable = response.parse()
        assert_matches_type(str, enable, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_secondary_dns_primary_zone_enable_outgoing_zone_transfers(
        self, client: Cloudflare
    ) -> None:
        with client.secondary_dns.outgoings.enables.with_streaming_response.secondary_dns_primary_zone_enable_outgoing_zone_transfers(
            "269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enable = response.parse()
            assert_matches_type(str, enable, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEnables:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_secondary_dns_primary_zone_enable_outgoing_zone_transfers(
        self, async_client: AsyncCloudflare
    ) -> None:
        enable = await async_client.secondary_dns.outgoings.enables.secondary_dns_primary_zone_enable_outgoing_zone_transfers(
            "269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(str, enable, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_secondary_dns_primary_zone_enable_outgoing_zone_transfers(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.secondary_dns.outgoings.enables.with_raw_response.secondary_dns_primary_zone_enable_outgoing_zone_transfers(
            "269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enable = await response.parse()
        assert_matches_type(str, enable, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_secondary_dns_primary_zone_enable_outgoing_zone_transfers(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.secondary_dns.outgoings.enables.with_streaming_response.secondary_dns_primary_zone_enable_outgoing_zone_transfers(
            "269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enable = await response.parse()
            assert_matches_type(str, enable, path=["response"])

        assert cast(Any, response.is_closed) is True
