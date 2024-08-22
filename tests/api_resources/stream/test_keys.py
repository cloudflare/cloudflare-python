# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from typing import Optional, Any, cast

from cloudflare.types.stream import Keys, KeyDeleteResponse, KeyGetResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.stream import key_create_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        key = client.stream.keys.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[Keys], key, path=['response'])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:

        response = client.stream.keys.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        key = response.parse()
        assert_matches_type(Optional[Keys], key, path=['response'])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.stream.keys.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            key = response.parse()
            assert_matches_type(Optional[Keys], key, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.stream.keys.with_raw_response.create(
              account_id="",
              body={},
          )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        key = client.stream.keys.delete(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(str, key, path=['response'])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:

        response = client.stream.keys.with_raw_response.delete(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        key = response.parse()
        assert_matches_type(str, key, path=['response'])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.stream.keys.with_streaming_response.delete(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            key = response.parse()
            assert_matches_type(str, key, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.stream.keys.with_raw_response.delete(
              identifier="023e105f4ecef8ad9ca31a8372d0c353",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
          client.stream.keys.with_raw_response.delete(
              identifier="",
              account_id="023e105f4ecef8ad9ca31a8372d0c353",
          )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        key = client.stream.keys.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[KeyGetResponse], key, path=['response'])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:

        response = client.stream.keys.with_raw_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        key = response.parse()
        assert_matches_type(Optional[KeyGetResponse], key, path=['response'])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.stream.keys.with_streaming_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            key = response.parse()
            assert_matches_type(Optional[KeyGetResponse], key, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          client.stream.keys.with_raw_response.get(
              account_id="",
          )
class TestAsyncKeys:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        key = await async_client.stream.keys.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[Keys], key, path=['response'])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.stream.keys.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        key = await response.parse()
        assert_matches_type(Optional[Keys], key, path=['response'])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.keys.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            key = await response.parse()
            assert_matches_type(Optional[Keys], key, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.stream.keys.with_raw_response.create(
              account_id="",
              body={},
          )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        key = await async_client.stream.keys.delete(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(str, key, path=['response'])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.stream.keys.with_raw_response.delete(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        key = await response.parse()
        assert_matches_type(str, key, path=['response'])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.keys.with_streaming_response.delete(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            key = await response.parse()
            assert_matches_type(str, key, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.stream.keys.with_raw_response.delete(
              identifier="023e105f4ecef8ad9ca31a8372d0c353",
              account_id="",
          )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
          await async_client.stream.keys.with_raw_response.delete(
              identifier="",
              account_id="023e105f4ecef8ad9ca31a8372d0c353",
          )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        key = await async_client.stream.keys.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[KeyGetResponse], key, path=['response'])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.stream.keys.with_raw_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        key = await response.parse()
        assert_matches_type(Optional[KeyGetResponse], key, path=['response'])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.keys.with_streaming_response.get(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            key = await response.parse()
            assert_matches_type(Optional[KeyGetResponse], key, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
          await async_client.stream.keys.with_raw_response.get(
              account_id="",
          )