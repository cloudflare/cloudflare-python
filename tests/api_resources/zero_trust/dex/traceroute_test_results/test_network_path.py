# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from typing import Optional, Any, cast

from cloudflare.types.zero_trust.dex.traceroute_test_results import NetworkPathGetResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestNetworkPath:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        network_path = client.zero_trust.dex.traceroute_test_results.network_path.get(
            test_result_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(Optional[NetworkPathGetResponse], network_path, path=['response'])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:

        response = client.zero_trust.dex.traceroute_test_results.network_path.with_raw_response.get(
            test_result_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        network_path = response.parse()
        assert_matches_type(Optional[NetworkPathGetResponse], network_path, path=['response'])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.dex.traceroute_test_results.network_path.with_streaming_response.get(
            test_result_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            network_path = response.parse()
            assert_matches_type(Optional[NetworkPathGetResponse], network_path, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.zero_trust.dex.traceroute_test_results.network_path.with_raw_response.get(
              test_result_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_result_id` but received ''"):
          client.zero_trust.dex.traceroute_test_results.network_path.with_raw_response.get(
              test_result_id="",
              account_id="01a7362d577a6c3019a474fd6f485823",
          )
class TestAsyncNetworkPath:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        network_path = await async_client.zero_trust.dex.traceroute_test_results.network_path.get(
            test_result_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(Optional[NetworkPathGetResponse], network_path, path=['response'])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.zero_trust.dex.traceroute_test_results.network_path.with_raw_response.get(
            test_result_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        network_path = await response.parse()
        assert_matches_type(Optional[NetworkPathGetResponse], network_path, path=['response'])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dex.traceroute_test_results.network_path.with_streaming_response.get(
            test_result_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            network_path = await response.parse()
            assert_matches_type(Optional[NetworkPathGetResponse], network_path, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.zero_trust.dex.traceroute_test_results.network_path.with_raw_response.get(
              test_result_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_result_id` but received ''"):
          await async_client.zero_trust.dex.traceroute_test_results.network_path.with_raw_response.get(
              test_result_id="",
              account_id="01a7362d577a6c3019a474fd6f485823",
          )