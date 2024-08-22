# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from typing import Optional, Any, cast

from cloudflare.types.workers import SubdomainUpdateResponse, SubdomainGetResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.workers import subdomain_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestSubdomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        subdomain = client.workers.subdomains.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SubdomainUpdateResponse], subdomain, path=['response'])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        subdomain = client.workers.subdomains.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            subdomain="example-subdomain",
        )
        assert_matches_type(Optional[SubdomainUpdateResponse], subdomain, path=['response'])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:

        response = client.workers.subdomains.with_raw_response.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        subdomain = response.parse()
        assert_matches_type(Optional[SubdomainUpdateResponse], subdomain, path=['response'])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.workers.subdomains.with_streaming_response.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            subdomain = response.parse()
            assert_matches_type(Optional[SubdomainUpdateResponse], subdomain, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.workers.subdomains.with_raw_response.update(
              account_id="",
          )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        subdomain = client.workers.subdomains.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SubdomainGetResponse], subdomain, path=['response'])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:

        response = client.workers.subdomains.with_raw_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        subdomain = response.parse()
        assert_matches_type(Optional[SubdomainGetResponse], subdomain, path=['response'])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.workers.subdomains.with_streaming_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            subdomain = response.parse()
            assert_matches_type(Optional[SubdomainGetResponse], subdomain, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.workers.subdomains.with_raw_response.get(
              account_id="",
          )
class TestAsyncSubdomains:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        subdomain = await async_client.workers.subdomains.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SubdomainUpdateResponse], subdomain, path=['response'])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        subdomain = await async_client.workers.subdomains.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            subdomain="example-subdomain",
        )
        assert_matches_type(Optional[SubdomainUpdateResponse], subdomain, path=['response'])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.workers.subdomains.with_raw_response.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        subdomain = await response.parse()
        assert_matches_type(Optional[SubdomainUpdateResponse], subdomain, path=['response'])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.subdomains.with_streaming_response.update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            subdomain = await response.parse()
            assert_matches_type(Optional[SubdomainUpdateResponse], subdomain, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.workers.subdomains.with_raw_response.update(
              account_id="",
          )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        subdomain = await async_client.workers.subdomains.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SubdomainGetResponse], subdomain, path=['response'])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.workers.subdomains.with_raw_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        subdomain = await response.parse()
        assert_matches_type(Optional[SubdomainGetResponse], subdomain, path=['response'])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.subdomains.with_streaming_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            subdomain = await response.parse()
            assert_matches_type(Optional[SubdomainGetResponse], subdomain, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.workers.subdomains.with_raw_response.get(
              account_id="",
          )