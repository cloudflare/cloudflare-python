# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from typing import Optional, Any, cast

from cloudflare.types.registrar import DomainUpdateResponse, DomainListResponse, DomainGetResponse

from cloudflare.pagination import SyncSinglePage, AsyncSinglePage

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.registrar import domain_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        domain = client.registrar.domains.update(
            domain_name="cloudflare.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[DomainUpdateResponse], domain, path=['response'])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        domain = client.registrar.domains.update(
            domain_name="cloudflare.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            auto_renew=True,
            locked=False,
            privacy=True,
        )
        assert_matches_type(Optional[DomainUpdateResponse], domain, path=['response'])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:

        response = client.registrar.domains.with_raw_response.update(
            domain_name="cloudflare.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        domain = response.parse()
        assert_matches_type(Optional[DomainUpdateResponse], domain, path=['response'])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.registrar.domains.with_streaming_response.update(
            domain_name="cloudflare.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            domain = response.parse()
            assert_matches_type(Optional[DomainUpdateResponse], domain, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.registrar.domains.with_raw_response.update(
              domain_name="cloudflare.com",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
          client.registrar.domains.with_raw_response.update(
              domain_name="",
              account_id="023e105f4ecef8ad9ca31a8372d0c353",
          )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        domain = client.registrar.domains.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[DomainListResponse], domain, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:

        response = client.registrar.domains.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        domain = response.parse()
        assert_matches_type(SyncSinglePage[DomainListResponse], domain, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.registrar.domains.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            domain = response.parse()
            assert_matches_type(SyncSinglePage[DomainListResponse], domain, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.registrar.domains.with_raw_response.list(
              account_id="",
          )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        domain = client.registrar.domains.get(
            domain_name="cloudflare.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[DomainGetResponse], domain, path=['response'])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:

        response = client.registrar.domains.with_raw_response.get(
            domain_name="cloudflare.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        domain = response.parse()
        assert_matches_type(Optional[DomainGetResponse], domain, path=['response'])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.registrar.domains.with_streaming_response.get(
            domain_name="cloudflare.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            domain = response.parse()
            assert_matches_type(Optional[DomainGetResponse], domain, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.registrar.domains.with_raw_response.get(
              domain_name="cloudflare.com",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
          client.registrar.domains.with_raw_response.get(
              domain_name="",
              account_id="023e105f4ecef8ad9ca31a8372d0c353",
          )
class TestAsyncDomains:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.registrar.domains.update(
            domain_name="cloudflare.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[DomainUpdateResponse], domain, path=['response'])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.registrar.domains.update(
            domain_name="cloudflare.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            auto_renew=True,
            locked=False,
            privacy=True,
        )
        assert_matches_type(Optional[DomainUpdateResponse], domain, path=['response'])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.registrar.domains.with_raw_response.update(
            domain_name="cloudflare.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        domain = await response.parse()
        assert_matches_type(Optional[DomainUpdateResponse], domain, path=['response'])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.registrar.domains.with_streaming_response.update(
            domain_name="cloudflare.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            domain = await response.parse()
            assert_matches_type(Optional[DomainUpdateResponse], domain, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.registrar.domains.with_raw_response.update(
              domain_name="cloudflare.com",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
          await async_client.registrar.domains.with_raw_response.update(
              domain_name="",
              account_id="023e105f4ecef8ad9ca31a8372d0c353",
          )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.registrar.domains.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[DomainListResponse], domain, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.registrar.domains.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        domain = await response.parse()
        assert_matches_type(AsyncSinglePage[DomainListResponse], domain, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.registrar.domains.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            domain = await response.parse()
            assert_matches_type(AsyncSinglePage[DomainListResponse], domain, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.registrar.domains.with_raw_response.list(
              account_id="",
          )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.registrar.domains.get(
            domain_name="cloudflare.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[DomainGetResponse], domain, path=['response'])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.registrar.domains.with_raw_response.get(
            domain_name="cloudflare.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        domain = await response.parse()
        assert_matches_type(Optional[DomainGetResponse], domain, path=['response'])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.registrar.domains.with_streaming_response.get(
            domain_name="cloudflare.com",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            domain = await response.parse()
            assert_matches_type(Optional[DomainGetResponse], domain, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.registrar.domains.with_raw_response.get(
              domain_name="cloudflare.com",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `domain_name` but received ''"):
          await async_client.registrar.domains.with_raw_response.get(
              domain_name="",
              account_id="023e105f4ecef8ad9ca31a8372d0c353",
          )