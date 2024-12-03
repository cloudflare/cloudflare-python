# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.stream import (
    LiveInput,
    LiveInputListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLiveInputs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        live_input = client.stream.live_inputs.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[LiveInput], live_input, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        live_input = client.stream.live_inputs.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            default_creator="defaultCreator",
            delete_recording_after_days=45,
            meta={"name": "test stream 1"},
            recording={
                "allowed_origins": ["example.com"],
                "hide_live_viewer_count": False,
                "mode": "off",
                "require_signed_urls": False,
                "timeout_seconds": 0,
            },
        )
        assert_matches_type(Optional[LiveInput], live_input, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.stream.live_inputs.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_input = response.parse()
        assert_matches_type(Optional[LiveInput], live_input, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.stream.live_inputs.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_input = response.parse()
            assert_matches_type(Optional[LiveInput], live_input, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.live_inputs.with_raw_response.create(
                account_id="",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        live_input = client.stream.live_inputs.update(
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[LiveInput], live_input, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        live_input = client.stream.live_inputs.update(
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            default_creator="defaultCreator",
            delete_recording_after_days=45,
            meta={"name": "test stream 1"},
            recording={
                "allowed_origins": ["example.com"],
                "hide_live_viewer_count": False,
                "mode": "off",
                "require_signed_urls": False,
                "timeout_seconds": 0,
            },
        )
        assert_matches_type(Optional[LiveInput], live_input, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.stream.live_inputs.with_raw_response.update(
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_input = response.parse()
        assert_matches_type(Optional[LiveInput], live_input, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.stream.live_inputs.with_streaming_response.update(
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_input = response.parse()
            assert_matches_type(Optional[LiveInput], live_input, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.live_inputs.with_raw_response.update(
                live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            client.stream.live_inputs.with_raw_response.update(
                live_input_identifier="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        live_input = client.stream.live_inputs.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[LiveInputListResponse], live_input, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        live_input = client.stream.live_inputs.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            include_counts=True,
        )
        assert_matches_type(Optional[LiveInputListResponse], live_input, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.stream.live_inputs.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_input = response.parse()
        assert_matches_type(Optional[LiveInputListResponse], live_input, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.stream.live_inputs.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_input = response.parse()
            assert_matches_type(Optional[LiveInputListResponse], live_input, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.live_inputs.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        live_input = client.stream.live_inputs.delete(
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert live_input is None

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.stream.live_inputs.with_raw_response.delete(
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_input = response.parse()
        assert live_input is None

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.stream.live_inputs.with_streaming_response.delete(
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_input = response.parse()
            assert live_input is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.live_inputs.with_raw_response.delete(
                live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            client.stream.live_inputs.with_raw_response.delete(
                live_input_identifier="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        live_input = client.stream.live_inputs.get(
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[LiveInput], live_input, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.stream.live_inputs.with_raw_response.get(
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_input = response.parse()
        assert_matches_type(Optional[LiveInput], live_input, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.stream.live_inputs.with_streaming_response.get(
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_input = response.parse()
            assert_matches_type(Optional[LiveInput], live_input, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.live_inputs.with_raw_response.get(
                live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            client.stream.live_inputs.with_raw_response.get(
                live_input_identifier="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncLiveInputs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        live_input = await async_client.stream.live_inputs.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[LiveInput], live_input, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        live_input = await async_client.stream.live_inputs.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            default_creator="defaultCreator",
            delete_recording_after_days=45,
            meta={"name": "test stream 1"},
            recording={
                "allowed_origins": ["example.com"],
                "hide_live_viewer_count": False,
                "mode": "off",
                "require_signed_urls": False,
                "timeout_seconds": 0,
            },
        )
        assert_matches_type(Optional[LiveInput], live_input, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.live_inputs.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_input = await response.parse()
        assert_matches_type(Optional[LiveInput], live_input, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.live_inputs.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_input = await response.parse()
            assert_matches_type(Optional[LiveInput], live_input, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.live_inputs.with_raw_response.create(
                account_id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        live_input = await async_client.stream.live_inputs.update(
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[LiveInput], live_input, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        live_input = await async_client.stream.live_inputs.update(
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            default_creator="defaultCreator",
            delete_recording_after_days=45,
            meta={"name": "test stream 1"},
            recording={
                "allowed_origins": ["example.com"],
                "hide_live_viewer_count": False,
                "mode": "off",
                "require_signed_urls": False,
                "timeout_seconds": 0,
            },
        )
        assert_matches_type(Optional[LiveInput], live_input, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.live_inputs.with_raw_response.update(
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_input = await response.parse()
        assert_matches_type(Optional[LiveInput], live_input, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.live_inputs.with_streaming_response.update(
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_input = await response.parse()
            assert_matches_type(Optional[LiveInput], live_input, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.live_inputs.with_raw_response.update(
                live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            await async_client.stream.live_inputs.with_raw_response.update(
                live_input_identifier="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        live_input = await async_client.stream.live_inputs.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[LiveInputListResponse], live_input, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        live_input = await async_client.stream.live_inputs.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            include_counts=True,
        )
        assert_matches_type(Optional[LiveInputListResponse], live_input, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.live_inputs.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_input = await response.parse()
        assert_matches_type(Optional[LiveInputListResponse], live_input, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.live_inputs.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_input = await response.parse()
            assert_matches_type(Optional[LiveInputListResponse], live_input, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.live_inputs.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        live_input = await async_client.stream.live_inputs.delete(
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert live_input is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.live_inputs.with_raw_response.delete(
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_input = await response.parse()
        assert live_input is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.live_inputs.with_streaming_response.delete(
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_input = await response.parse()
            assert live_input is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.live_inputs.with_raw_response.delete(
                live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            await async_client.stream.live_inputs.with_raw_response.delete(
                live_input_identifier="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        live_input = await async_client.stream.live_inputs.get(
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[LiveInput], live_input, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.live_inputs.with_raw_response.get(
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_input = await response.parse()
        assert_matches_type(Optional[LiveInput], live_input, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.live_inputs.with_streaming_response.get(
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_input = await response.parse()
            assert_matches_type(Optional[LiveInput], live_input, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.live_inputs.with_raw_response.get(
                live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            await async_client.stream.live_inputs.with_raw_response.get(
                live_input_identifier="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
