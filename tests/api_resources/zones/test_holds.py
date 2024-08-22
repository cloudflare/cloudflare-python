# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.zones import ZoneHold

from typing import Any, cast, Optional

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zones import hold_create_params
from cloudflare.types.zones import hold_delete_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestHolds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        hold = client.zones.holds.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ZoneHold, hold, path=['response'])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        hold = client.zones.holds.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            include_subdomains=True,
        )
        assert_matches_type(ZoneHold, hold, path=['response'])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:

        response = client.zones.holds.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        hold = response.parse()
        assert_matches_type(ZoneHold, hold, path=['response'])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zones.holds.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            hold = response.parse()
            assert_matches_type(ZoneHold, hold, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          client.zones.holds.with_raw_response.create(
              zone_id="",
          )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        hold = client.zones.holds.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ZoneHold], hold, path=['response'])

    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        hold = client.zones.holds.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hold_after="hold_after",
        )
        assert_matches_type(Optional[ZoneHold], hold, path=['response'])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:

        response = client.zones.holds.with_raw_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        hold = response.parse()
        assert_matches_type(Optional[ZoneHold], hold, path=['response'])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zones.holds.with_streaming_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            hold = response.parse()
            assert_matches_type(Optional[ZoneHold], hold, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          client.zones.holds.with_raw_response.delete(
              zone_id="",
          )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        hold = client.zones.holds.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ZoneHold, hold, path=['response'])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:

        response = client.zones.holds.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        hold = response.parse()
        assert_matches_type(ZoneHold, hold, path=['response'])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zones.holds.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            hold = response.parse()
            assert_matches_type(ZoneHold, hold, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          client.zones.holds.with_raw_response.get(
              zone_id="",
          )
class TestAsyncHolds:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        hold = await async_client.zones.holds.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ZoneHold, hold, path=['response'])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        hold = await async_client.zones.holds.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            include_subdomains=True,
        )
        assert_matches_type(ZoneHold, hold, path=['response'])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.zones.holds.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        hold = await response.parse()
        assert_matches_type(ZoneHold, hold, path=['response'])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.holds.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            hold = await response.parse()
            assert_matches_type(ZoneHold, hold, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          await async_client.zones.holds.with_raw_response.create(
              zone_id="",
          )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        hold = await async_client.zones.holds.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ZoneHold], hold, path=['response'])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        hold = await async_client.zones.holds.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            hold_after="hold_after",
        )
        assert_matches_type(Optional[ZoneHold], hold, path=['response'])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.zones.holds.with_raw_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        hold = await response.parse()
        assert_matches_type(Optional[ZoneHold], hold, path=['response'])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.holds.with_streaming_response.delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            hold = await response.parse()
            assert_matches_type(Optional[ZoneHold], hold, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          await async_client.zones.holds.with_raw_response.delete(
              zone_id="",
          )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        hold = await async_client.zones.holds.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ZoneHold, hold, path=['response'])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.zones.holds.with_raw_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        hold = await response.parse()
        assert_matches_type(ZoneHold, hold, path=['response'])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.holds.with_streaming_response.get(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            hold = await response.parse()
            assert_matches_type(ZoneHold, hold, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          await async_client.zones.holds.with_raw_response.get(
              zone_id="",
          )