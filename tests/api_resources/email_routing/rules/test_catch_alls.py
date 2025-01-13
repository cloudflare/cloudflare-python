# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.email_routing.rules import CatchAllGetResponse, CatchAllUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCatchAlls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        catch_all = client.email_routing.rules.catch_alls.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{"type": "drop"}],
            matchers=[{"type": "all"}],
        )
        assert_matches_type(Optional[CatchAllUpdateResponse], catch_all, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        catch_all = client.email_routing.rules.catch_alls.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "drop",
                    "value": ["destinationaddress@example.net"],
                }
            ],
            matchers=[{"type": "all"}],
            enabled=True,
            name="Send to user@example.net rule.",
        )
        assert_matches_type(Optional[CatchAllUpdateResponse], catch_all, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.email_routing.rules.catch_alls.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{"type": "drop"}],
            matchers=[{"type": "all"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catch_all = response.parse()
        assert_matches_type(Optional[CatchAllUpdateResponse], catch_all, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.email_routing.rules.catch_alls.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{"type": "drop"}],
            matchers=[{"type": "all"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catch_all = response.parse()
            assert_matches_type(Optional[CatchAllUpdateResponse], catch_all, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.email_routing.rules.catch_alls.with_raw_response.update(
                zone_id="",
                actions=[{"type": "drop"}],
                matchers=[{"type": "all"}],
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        catch_all = client.email_routing.rules.catch_alls.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CatchAllGetResponse], catch_all, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.email_routing.rules.catch_alls.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catch_all = response.parse()
        assert_matches_type(Optional[CatchAllGetResponse], catch_all, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.email_routing.rules.catch_alls.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catch_all = response.parse()
            assert_matches_type(Optional[CatchAllGetResponse], catch_all, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.email_routing.rules.catch_alls.with_raw_response.get(
                zone_id="",
            )


class TestAsyncCatchAlls:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        catch_all = await async_client.email_routing.rules.catch_alls.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{"type": "drop"}],
            matchers=[{"type": "all"}],
        )
        assert_matches_type(Optional[CatchAllUpdateResponse], catch_all, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        catch_all = await async_client.email_routing.rules.catch_alls.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "drop",
                    "value": ["destinationaddress@example.net"],
                }
            ],
            matchers=[{"type": "all"}],
            enabled=True,
            name="Send to user@example.net rule.",
        )
        assert_matches_type(Optional[CatchAllUpdateResponse], catch_all, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_routing.rules.catch_alls.with_raw_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{"type": "drop"}],
            matchers=[{"type": "all"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catch_all = await response.parse()
        assert_matches_type(Optional[CatchAllUpdateResponse], catch_all, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_routing.rules.catch_alls.with_streaming_response.update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{"type": "drop"}],
            matchers=[{"type": "all"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catch_all = await response.parse()
            assert_matches_type(Optional[CatchAllUpdateResponse], catch_all, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.email_routing.rules.catch_alls.with_raw_response.update(
                zone_id="",
                actions=[{"type": "drop"}],
                matchers=[{"type": "all"}],
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        catch_all = await async_client.email_routing.rules.catch_alls.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CatchAllGetResponse], catch_all, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_routing.rules.catch_alls.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catch_all = await response.parse()
        assert_matches_type(Optional[CatchAllGetResponse], catch_all, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_routing.rules.catch_alls.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catch_all = await response.parse()
            assert_matches_type(Optional[CatchAllGetResponse], catch_all, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.email_routing.rules.catch_alls.with_raw_response.get(
                zone_id="",
            )
