# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from typing import Optional, Any, cast

from cloudflare.types.zones import ActivationCheckTriggerResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestActivationCheck:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_trigger(self, client: Cloudflare) -> None:
        activation_check = client.zones.activation_check.trigger(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ActivationCheckTriggerResponse], activation_check, path=['response'])

    @parametrize
    def test_raw_response_trigger(self, client: Cloudflare) -> None:

        response = client.zones.activation_check.with_raw_response.trigger(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        activation_check = response.parse()
        assert_matches_type(Optional[ActivationCheckTriggerResponse], activation_check, path=['response'])

    @parametrize
    def test_streaming_response_trigger(self, client: Cloudflare) -> None:
        with client.zones.activation_check.with_streaming_response.trigger(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            activation_check = response.parse()
            assert_matches_type(Optional[ActivationCheckTriggerResponse], activation_check, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_trigger(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          client.zones.activation_check.with_raw_response.trigger(
              zone_id="",
          )
class TestAsyncActivationCheck:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_trigger(self, async_client: AsyncCloudflare) -> None:
        activation_check = await async_client.zones.activation_check.trigger(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ActivationCheckTriggerResponse], activation_check, path=['response'])

    @parametrize
    async def test_raw_response_trigger(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.zones.activation_check.with_raw_response.trigger(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        activation_check = await response.parse()
        assert_matches_type(Optional[ActivationCheckTriggerResponse], activation_check, path=['response'])

    @parametrize
    async def test_streaming_response_trigger(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.activation_check.with_streaming_response.trigger(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            activation_check = await response.parse()
            assert_matches_type(Optional[ActivationCheckTriggerResponse], activation_check, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_trigger(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          await async_client.zones.activation_check.with_raw_response.trigger(
              zone_id="",
          )