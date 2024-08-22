# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.load_balancers.monitors import ReferenceGetResponse

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

class TestReferences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        reference = client.load_balancers.monitors.references.get(
            monitor_id="f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ReferenceGetResponse, reference, path=['response'])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:

        response = client.load_balancers.monitors.references.with_raw_response.get(
            monitor_id="f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        reference = response.parse()
        assert_matches_type(ReferenceGetResponse, reference, path=['response'])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.load_balancers.monitors.references.with_streaming_response.get(
            monitor_id="f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            reference = response.parse()
            assert_matches_type(ReferenceGetResponse, reference, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.load_balancers.monitors.references.with_raw_response.get(
              monitor_id="f1aba936b94213e5b8dca0c0dbf1f9cc",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
          client.load_balancers.monitors.references.with_raw_response.get(
              monitor_id="",
              account_id="023e105f4ecef8ad9ca31a8372d0c353",
          )
class TestAsyncReferences:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        reference = await async_client.load_balancers.monitors.references.get(
            monitor_id="f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ReferenceGetResponse, reference, path=['response'])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.load_balancers.monitors.references.with_raw_response.get(
            monitor_id="f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        reference = await response.parse()
        assert_matches_type(ReferenceGetResponse, reference, path=['response'])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.load_balancers.monitors.references.with_streaming_response.get(
            monitor_id="f1aba936b94213e5b8dca0c0dbf1f9cc",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            reference = await response.parse()
            assert_matches_type(ReferenceGetResponse, reference, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.load_balancers.monitors.references.with_raw_response.get(
              monitor_id="f1aba936b94213e5b8dca0c0dbf1f9cc",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
          await async_client.load_balancers.monitors.references.with_raw_response.get(
              monitor_id="",
              account_id="023e105f4ecef8ad9ca31a8372d0c353",
          )