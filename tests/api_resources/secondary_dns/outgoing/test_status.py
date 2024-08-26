# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from typing import Optional, Any, cast

from cloudflare.types.secondary_dns import EnableTransfer

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        status = client.secondary_dns.outgoing.status.get(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(str, status, path=['response'])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:

        response = client.secondary_dns.outgoing.status.with_raw_response.get(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        status = response.parse()
        assert_matches_type(str, status, path=['response'])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.secondary_dns.outgoing.status.with_streaming_response.get(
            zone_id="269d8f4853475ca241c4e730be286b20",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            status = response.parse()
            assert_matches_type(str, status, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          client.secondary_dns.outgoing.status.with_raw_response.get(
              zone_id="",
          )
class TestAsyncStatus:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        status = await async_client.secondary_dns.outgoing.status.get(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(str, status, path=['response'])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.secondary_dns.outgoing.status.with_raw_response.get(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        status = await response.parse()
        assert_matches_type(str, status, path=['response'])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.outgoing.status.with_streaming_response.get(
            zone_id="269d8f4853475ca241c4e730be286b20",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            status = await response.parse()
            assert_matches_type(str, status, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          await async_client.secondary_dns.outgoing.status.with_raw_response.get(
              zone_id="",
          )