# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.secondary_dns import (
    IncomingDeleteResponse,
    IncomingSecondaryDNSSecondaryZoneCreateSecondaryZoneConfigurationResponse,
    IncomingSecondaryDNSSecondaryZoneSecondaryZoneConfigurationDetailsResponse,
    IncomingSecondaryDNSSecondaryZoneUpdateSecondaryZoneConfigurationResponse,
)

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.secondary_dns import (
    incoming_secondary_dns_secondary_zone_create_secondary_zone_configuration_params,
)
from cloudflare.types.secondary_dns import (
    incoming_secondary_dns_secondary_zone_update_secondary_zone_configuration_params,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIncomings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        incoming = client.secondary_dns.incomings.delete(
            "269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(IncomingDeleteResponse, incoming, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.secondary_dns.incomings.with_raw_response.delete(
            "269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incoming = response.parse()
        assert_matches_type(IncomingDeleteResponse, incoming, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.secondary_dns.incomings.with_streaming_response.delete(
            "269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incoming = response.parse()
            assert_matches_type(IncomingDeleteResponse, incoming, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_secondary_dns_secondary_zone_create_secondary_zone_configuration(self, client: Cloudflare) -> None:
        incoming = client.secondary_dns.incomings.secondary_dns_secondary_zone_create_secondary_zone_configuration(
            "269d8f4853475ca241c4e730be286b20",
            auto_refresh_seconds=86400,
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )
        assert_matches_type(
            IncomingSecondaryDNSSecondaryZoneCreateSecondaryZoneConfigurationResponse, incoming, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_secondary_dns_secondary_zone_create_secondary_zone_configuration(
        self, client: Cloudflare
    ) -> None:
        response = client.secondary_dns.incomings.with_raw_response.secondary_dns_secondary_zone_create_secondary_zone_configuration(
            "269d8f4853475ca241c4e730be286b20",
            auto_refresh_seconds=86400,
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incoming = response.parse()
        assert_matches_type(
            IncomingSecondaryDNSSecondaryZoneCreateSecondaryZoneConfigurationResponse, incoming, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_secondary_dns_secondary_zone_create_secondary_zone_configuration(
        self, client: Cloudflare
    ) -> None:
        with client.secondary_dns.incomings.with_streaming_response.secondary_dns_secondary_zone_create_secondary_zone_configuration(
            "269d8f4853475ca241c4e730be286b20",
            auto_refresh_seconds=86400,
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incoming = response.parse()
            assert_matches_type(
                IncomingSecondaryDNSSecondaryZoneCreateSecondaryZoneConfigurationResponse, incoming, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_secondary_dns_secondary_zone_secondary_zone_configuration_details(self, client: Cloudflare) -> None:
        incoming = client.secondary_dns.incomings.secondary_dns_secondary_zone_secondary_zone_configuration_details(
            "269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(
            IncomingSecondaryDNSSecondaryZoneSecondaryZoneConfigurationDetailsResponse, incoming, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_secondary_dns_secondary_zone_secondary_zone_configuration_details(
        self, client: Cloudflare
    ) -> None:
        response = client.secondary_dns.incomings.with_raw_response.secondary_dns_secondary_zone_secondary_zone_configuration_details(
            "269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incoming = response.parse()
        assert_matches_type(
            IncomingSecondaryDNSSecondaryZoneSecondaryZoneConfigurationDetailsResponse, incoming, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_secondary_dns_secondary_zone_secondary_zone_configuration_details(
        self, client: Cloudflare
    ) -> None:
        with client.secondary_dns.incomings.with_streaming_response.secondary_dns_secondary_zone_secondary_zone_configuration_details(
            "269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incoming = response.parse()
            assert_matches_type(
                IncomingSecondaryDNSSecondaryZoneSecondaryZoneConfigurationDetailsResponse, incoming, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_secondary_dns_secondary_zone_update_secondary_zone_configuration(self, client: Cloudflare) -> None:
        incoming = client.secondary_dns.incomings.secondary_dns_secondary_zone_update_secondary_zone_configuration(
            "269d8f4853475ca241c4e730be286b20",
            auto_refresh_seconds=86400,
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )
        assert_matches_type(
            IncomingSecondaryDNSSecondaryZoneUpdateSecondaryZoneConfigurationResponse, incoming, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_secondary_dns_secondary_zone_update_secondary_zone_configuration(
        self, client: Cloudflare
    ) -> None:
        response = client.secondary_dns.incomings.with_raw_response.secondary_dns_secondary_zone_update_secondary_zone_configuration(
            "269d8f4853475ca241c4e730be286b20",
            auto_refresh_seconds=86400,
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incoming = response.parse()
        assert_matches_type(
            IncomingSecondaryDNSSecondaryZoneUpdateSecondaryZoneConfigurationResponse, incoming, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_secondary_dns_secondary_zone_update_secondary_zone_configuration(
        self, client: Cloudflare
    ) -> None:
        with client.secondary_dns.incomings.with_streaming_response.secondary_dns_secondary_zone_update_secondary_zone_configuration(
            "269d8f4853475ca241c4e730be286b20",
            auto_refresh_seconds=86400,
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incoming = response.parse()
            assert_matches_type(
                IncomingSecondaryDNSSecondaryZoneUpdateSecondaryZoneConfigurationResponse, incoming, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncIncomings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        incoming = await async_client.secondary_dns.incomings.delete(
            "269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(IncomingDeleteResponse, incoming, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secondary_dns.incomings.with_raw_response.delete(
            "269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incoming = await response.parse()
        assert_matches_type(IncomingDeleteResponse, incoming, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.incomings.with_streaming_response.delete(
            "269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incoming = await response.parse()
            assert_matches_type(IncomingDeleteResponse, incoming, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_secondary_dns_secondary_zone_create_secondary_zone_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        incoming = (
            await async_client.secondary_dns.incomings.secondary_dns_secondary_zone_create_secondary_zone_configuration(
                "269d8f4853475ca241c4e730be286b20",
                auto_refresh_seconds=86400,
                name="www.example.com.",
                peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
            )
        )
        assert_matches_type(
            IncomingSecondaryDNSSecondaryZoneCreateSecondaryZoneConfigurationResponse, incoming, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_secondary_dns_secondary_zone_create_secondary_zone_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.secondary_dns.incomings.with_raw_response.secondary_dns_secondary_zone_create_secondary_zone_configuration(
            "269d8f4853475ca241c4e730be286b20",
            auto_refresh_seconds=86400,
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incoming = await response.parse()
        assert_matches_type(
            IncomingSecondaryDNSSecondaryZoneCreateSecondaryZoneConfigurationResponse, incoming, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_secondary_dns_secondary_zone_create_secondary_zone_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.secondary_dns.incomings.with_streaming_response.secondary_dns_secondary_zone_create_secondary_zone_configuration(
            "269d8f4853475ca241c4e730be286b20",
            auto_refresh_seconds=86400,
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incoming = await response.parse()
            assert_matches_type(
                IncomingSecondaryDNSSecondaryZoneCreateSecondaryZoneConfigurationResponse, incoming, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_secondary_dns_secondary_zone_secondary_zone_configuration_details(
        self, async_client: AsyncCloudflare
    ) -> None:
        incoming = await async_client.secondary_dns.incomings.secondary_dns_secondary_zone_secondary_zone_configuration_details(
            "269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(
            IncomingSecondaryDNSSecondaryZoneSecondaryZoneConfigurationDetailsResponse, incoming, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_secondary_dns_secondary_zone_secondary_zone_configuration_details(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.secondary_dns.incomings.with_raw_response.secondary_dns_secondary_zone_secondary_zone_configuration_details(
            "269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incoming = await response.parse()
        assert_matches_type(
            IncomingSecondaryDNSSecondaryZoneSecondaryZoneConfigurationDetailsResponse, incoming, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_secondary_dns_secondary_zone_secondary_zone_configuration_details(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.secondary_dns.incomings.with_streaming_response.secondary_dns_secondary_zone_secondary_zone_configuration_details(
            "269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incoming = await response.parse()
            assert_matches_type(
                IncomingSecondaryDNSSecondaryZoneSecondaryZoneConfigurationDetailsResponse, incoming, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_secondary_dns_secondary_zone_update_secondary_zone_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        incoming = (
            await async_client.secondary_dns.incomings.secondary_dns_secondary_zone_update_secondary_zone_configuration(
                "269d8f4853475ca241c4e730be286b20",
                auto_refresh_seconds=86400,
                name="www.example.com.",
                peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
            )
        )
        assert_matches_type(
            IncomingSecondaryDNSSecondaryZoneUpdateSecondaryZoneConfigurationResponse, incoming, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_secondary_dns_secondary_zone_update_secondary_zone_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.secondary_dns.incomings.with_raw_response.secondary_dns_secondary_zone_update_secondary_zone_configuration(
            "269d8f4853475ca241c4e730be286b20",
            auto_refresh_seconds=86400,
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incoming = await response.parse()
        assert_matches_type(
            IncomingSecondaryDNSSecondaryZoneUpdateSecondaryZoneConfigurationResponse, incoming, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_secondary_dns_secondary_zone_update_secondary_zone_configuration(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.secondary_dns.incomings.with_streaming_response.secondary_dns_secondary_zone_update_secondary_zone_configuration(
            "269d8f4853475ca241c4e730be286b20",
            auto_refresh_seconds=86400,
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incoming = await response.parse()
            assert_matches_type(
                IncomingSecondaryDNSSecondaryZoneUpdateSecondaryZoneConfigurationResponse, incoming, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
