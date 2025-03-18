# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.dns.settings import ZoneGetResponse, ZoneEditResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestZone:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        zone = client.dns.settings.zone.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ZoneEditResponse], zone, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        zone = client.dns.settings.zone.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            flatten_all_cnames=False,
            foundation_dns=False,
            internal_dns={"reference_zone_id": "reference_zone_id"},
            multi_provider=False,
            nameservers={
                "type": "cloudflare.standard",
                "ns_set": 1,
            },
            ns_ttl=86400,
            secondary_overrides=False,
            soa={
                "expire": 604800,
                "min_ttl": 1800,
                "mname": "kristina.ns.cloudflare.com",
                "refresh": 10000,
                "retry": 2400,
                "rname": "admin.example.com",
                "ttl": 3600,
            },
            zone_mode="standard",
        )
        assert_matches_type(Optional[ZoneEditResponse], zone, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.dns.settings.zone.with_raw_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(Optional[ZoneEditResponse], zone, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.dns.settings.zone.with_streaming_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert_matches_type(Optional[ZoneEditResponse], zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.settings.zone.with_raw_response.edit(
                zone_id="",
            )

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        zone = client.dns.settings.zone.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ZoneGetResponse], zone, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.dns.settings.zone.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = response.parse()
        assert_matches_type(Optional[ZoneGetResponse], zone, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.dns.settings.zone.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = response.parse()
            assert_matches_type(Optional[ZoneGetResponse], zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.dns.settings.zone.with_raw_response.get(
                zone_id="",
            )


class TestAsyncZone:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        zone = await async_client.dns.settings.zone.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ZoneEditResponse], zone, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        zone = await async_client.dns.settings.zone.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            flatten_all_cnames=False,
            foundation_dns=False,
            internal_dns={"reference_zone_id": "reference_zone_id"},
            multi_provider=False,
            nameservers={
                "type": "cloudflare.standard",
                "ns_set": 1,
            },
            ns_ttl=86400,
            secondary_overrides=False,
            soa={
                "expire": 604800,
                "min_ttl": 1800,
                "mname": "kristina.ns.cloudflare.com",
                "refresh": 10000,
                "retry": 2400,
                "rname": "admin.example.com",
                "ttl": 3600,
            },
            zone_mode="standard",
        )
        assert_matches_type(Optional[ZoneEditResponse], zone, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.settings.zone.with_raw_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(Optional[ZoneEditResponse], zone, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.settings.zone.with_streaming_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert_matches_type(Optional[ZoneEditResponse], zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.settings.zone.with_raw_response.edit(
                zone_id="",
            )

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        zone = await async_client.dns.settings.zone.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ZoneGetResponse], zone, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dns.settings.zone.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zone = await response.parse()
        assert_matches_type(Optional[ZoneGetResponse], zone, path=["response"])

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dns.settings.zone.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zone = await response.parse()
            assert_matches_type(Optional[ZoneGetResponse], zone, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 422 from prism")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.dns.settings.zone.with_raw_response.get(
                zone_id="",
            )
