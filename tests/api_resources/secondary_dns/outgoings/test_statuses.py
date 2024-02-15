# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.secondary_dns.outgoings import StatusSecondaryDNSPrimaryZoneGetOutgoingZoneTransferStatusResponse

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


class TestStatuses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_secondary_dns_primary_zone_get_outgoing_zone_transfer_status(self, client: Cloudflare) -> None:
        status = client.secondary_dns.outgoings.statuses.secondary_dns_primary_zone_get_outgoing_zone_transfer_status(
            "269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(str, status, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_secondary_dns_primary_zone_get_outgoing_zone_transfer_status(
        self, client: Cloudflare
    ) -> None:
        response = client.secondary_dns.outgoings.statuses.with_raw_response.secondary_dns_primary_zone_get_outgoing_zone_transfer_status(
            "269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(str, status, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_secondary_dns_primary_zone_get_outgoing_zone_transfer_status(
        self, client: Cloudflare
    ) -> None:
        with client.secondary_dns.outgoings.statuses.with_streaming_response.secondary_dns_primary_zone_get_outgoing_zone_transfer_status(
            "269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(str, status, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStatuses:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_secondary_dns_primary_zone_get_outgoing_zone_transfer_status(
        self, async_client: AsyncCloudflare
    ) -> None:
        status = await async_client.secondary_dns.outgoings.statuses.secondary_dns_primary_zone_get_outgoing_zone_transfer_status(
            "269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(str, status, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_secondary_dns_primary_zone_get_outgoing_zone_transfer_status(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.secondary_dns.outgoings.statuses.with_raw_response.secondary_dns_primary_zone_get_outgoing_zone_transfer_status(
            "269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(str, status, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_secondary_dns_primary_zone_get_outgoing_zone_transfer_status(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.secondary_dns.outgoings.statuses.with_streaming_response.secondary_dns_primary_zone_get_outgoing_zone_transfer_status(
            "269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(str, status, path=["response"])

        assert cast(Any, response.is_closed) is True
