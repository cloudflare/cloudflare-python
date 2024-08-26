# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.workers.scripts import TailGetResponse, TailCreateResponse, TailDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTail:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        tail = client.workers.scripts.tail.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[TailCreateResponse], tail, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.workers.scripts.tail.with_raw_response.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tail = response.parse()
        assert_matches_type(Optional[TailCreateResponse], tail, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.workers.scripts.tail.with_streaming_response.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tail = response.parse()
            assert_matches_type(Optional[TailCreateResponse], tail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.tail.with_raw_response.create(
                script_name="this-is_my_script-01",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.tail.with_raw_response.create(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        tail = client.workers.scripts.tail.delete(
            id="03dc9f77817b488fb26c5861ec18f791",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )
        assert_matches_type(TailDeleteResponse, tail, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.workers.scripts.tail.with_raw_response.delete(
            id="03dc9f77817b488fb26c5861ec18f791",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tail = response.parse()
        assert_matches_type(TailDeleteResponse, tail, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.workers.scripts.tail.with_streaming_response.delete(
            id="03dc9f77817b488fb26c5861ec18f791",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tail = response.parse()
            assert_matches_type(TailDeleteResponse, tail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.tail.with_raw_response.delete(
                id="03dc9f77817b488fb26c5861ec18f791",
                account_id="",
                script_name="this-is_my_script-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.tail.with_raw_response.delete(
                id="03dc9f77817b488fb26c5861ec18f791",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workers.scripts.tail.with_raw_response.delete(
                id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="this-is_my_script-01",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        tail = client.workers.scripts.tail.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[TailGetResponse], tail, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.workers.scripts.tail.with_raw_response.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tail = response.parse()
        assert_matches_type(Optional[TailGetResponse], tail, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.workers.scripts.tail.with_streaming_response.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tail = response.parse()
            assert_matches_type(Optional[TailGetResponse], tail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.tail.with_raw_response.get(
                script_name="this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.tail.with_raw_response.get(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncTail:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        tail = await async_client.workers.scripts.tail.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[TailCreateResponse], tail, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.scripts.tail.with_raw_response.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tail = await response.parse()
        assert_matches_type(Optional[TailCreateResponse], tail, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.scripts.tail.with_streaming_response.create(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tail = await response.parse()
            assert_matches_type(Optional[TailCreateResponse], tail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.tail.with_raw_response.create(
                script_name="this-is_my_script-01",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.tail.with_raw_response.create(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        tail = await async_client.workers.scripts.tail.delete(
            id="03dc9f77817b488fb26c5861ec18f791",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )
        assert_matches_type(TailDeleteResponse, tail, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.scripts.tail.with_raw_response.delete(
            id="03dc9f77817b488fb26c5861ec18f791",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tail = await response.parse()
        assert_matches_type(TailDeleteResponse, tail, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.scripts.tail.with_streaming_response.delete(
            id="03dc9f77817b488fb26c5861ec18f791",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            script_name="this-is_my_script-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tail = await response.parse()
            assert_matches_type(TailDeleteResponse, tail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.tail.with_raw_response.delete(
                id="03dc9f77817b488fb26c5861ec18f791",
                account_id="",
                script_name="this-is_my_script-01",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.tail.with_raw_response.delete(
                id="03dc9f77817b488fb26c5861ec18f791",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workers.scripts.tail.with_raw_response.delete(
                id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                script_name="this-is_my_script-01",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        tail = await async_client.workers.scripts.tail.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[TailGetResponse], tail, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.scripts.tail.with_raw_response.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tail = await response.parse()
        assert_matches_type(Optional[TailGetResponse], tail, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.scripts.tail.with_streaming_response.get(
            script_name="this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tail = await response.parse()
            assert_matches_type(Optional[TailGetResponse], tail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.tail.with_raw_response.get(
                script_name="this-is_my_script-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.tail.with_raw_response.get(
                script_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
