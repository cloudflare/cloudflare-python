# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.stream import (
    LiveInputGetResponse,
    LiveInputUpdateResponse,
    LiveInputStreamLiveInputsListLiveInputsResponse,
    LiveInputStreamLiveInputsCreateALiveInputResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLiveInputs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        live_input = client.stream.live_inputs.update(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LiveInputUpdateResponse, live_input, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        live_input = client.stream.live_inputs.update(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            default_creator="string",
            delete_recording_after_days=45,
            meta={"name": "test stream 1"},
            recording={
                "allowed_origins": ["example.com"],
                "mode": "off",
                "require_signed_urls": False,
                "timeout_seconds": 0,
            },
        )
        assert_matches_type(LiveInputUpdateResponse, live_input, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.stream.live_inputs.with_raw_response.update(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_input = response.parse()
        assert_matches_type(LiveInputUpdateResponse, live_input, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.stream.live_inputs.with_streaming_response.update(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_input = response.parse()
            assert_matches_type(LiveInputUpdateResponse, live_input, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.live_inputs.with_raw_response.update(
                "66be4bf738797e01e1fca35a7bdecdcd",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            client.stream.live_inputs.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        live_input = client.stream.live_inputs.delete(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert live_input is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.stream.live_inputs.with_raw_response.delete(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_input = response.parse()
        assert live_input is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.stream.live_inputs.with_streaming_response.delete(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_input = response.parse()
            assert live_input is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.live_inputs.with_raw_response.delete(
                "66be4bf738797e01e1fca35a7bdecdcd",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            client.stream.live_inputs.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        live_input = client.stream.live_inputs.get(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LiveInputGetResponse, live_input, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.stream.live_inputs.with_raw_response.get(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_input = response.parse()
        assert_matches_type(LiveInputGetResponse, live_input, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.stream.live_inputs.with_streaming_response.get(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_input = response.parse()
            assert_matches_type(LiveInputGetResponse, live_input, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.live_inputs.with_raw_response.get(
                "66be4bf738797e01e1fca35a7bdecdcd",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            client.stream.live_inputs.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_live_inputs_create_a_live_input(self, client: Cloudflare) -> None:
        live_input = client.stream.live_inputs.stream_live_inputs_create_a_live_input(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LiveInputStreamLiveInputsCreateALiveInputResponse, live_input, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_live_inputs_create_a_live_input_with_all_params(self, client: Cloudflare) -> None:
        live_input = client.stream.live_inputs.stream_live_inputs_create_a_live_input(
            "023e105f4ecef8ad9ca31a8372d0c353",
            default_creator="string",
            delete_recording_after_days=45,
            meta={"name": "test stream 1"},
            recording={
                "allowed_origins": ["example.com"],
                "mode": "off",
                "require_signed_urls": False,
                "timeout_seconds": 0,
            },
        )
        assert_matches_type(LiveInputStreamLiveInputsCreateALiveInputResponse, live_input, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stream_live_inputs_create_a_live_input(self, client: Cloudflare) -> None:
        response = client.stream.live_inputs.with_raw_response.stream_live_inputs_create_a_live_input(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_input = response.parse()
        assert_matches_type(LiveInputStreamLiveInputsCreateALiveInputResponse, live_input, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stream_live_inputs_create_a_live_input(self, client: Cloudflare) -> None:
        with client.stream.live_inputs.with_streaming_response.stream_live_inputs_create_a_live_input(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_input = response.parse()
            assert_matches_type(LiveInputStreamLiveInputsCreateALiveInputResponse, live_input, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_stream_live_inputs_create_a_live_input(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.live_inputs.with_raw_response.stream_live_inputs_create_a_live_input(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_live_inputs_list_live_inputs(self, client: Cloudflare) -> None:
        live_input = client.stream.live_inputs.stream_live_inputs_list_live_inputs(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LiveInputStreamLiveInputsListLiveInputsResponse, live_input, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_live_inputs_list_live_inputs_with_all_params(self, client: Cloudflare) -> None:
        live_input = client.stream.live_inputs.stream_live_inputs_list_live_inputs(
            "023e105f4ecef8ad9ca31a8372d0c353",
            include_counts=True,
        )
        assert_matches_type(LiveInputStreamLiveInputsListLiveInputsResponse, live_input, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stream_live_inputs_list_live_inputs(self, client: Cloudflare) -> None:
        response = client.stream.live_inputs.with_raw_response.stream_live_inputs_list_live_inputs(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_input = response.parse()
        assert_matches_type(LiveInputStreamLiveInputsListLiveInputsResponse, live_input, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stream_live_inputs_list_live_inputs(self, client: Cloudflare) -> None:
        with client.stream.live_inputs.with_streaming_response.stream_live_inputs_list_live_inputs(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_input = response.parse()
            assert_matches_type(LiveInputStreamLiveInputsListLiveInputsResponse, live_input, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_stream_live_inputs_list_live_inputs(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.live_inputs.with_raw_response.stream_live_inputs_list_live_inputs(
                "",
            )


class TestAsyncLiveInputs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        live_input = await async_client.stream.live_inputs.update(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LiveInputUpdateResponse, live_input, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        live_input = await async_client.stream.live_inputs.update(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            default_creator="string",
            delete_recording_after_days=45,
            meta={"name": "test stream 1"},
            recording={
                "allowed_origins": ["example.com"],
                "mode": "off",
                "require_signed_urls": False,
                "timeout_seconds": 0,
            },
        )
        assert_matches_type(LiveInputUpdateResponse, live_input, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.live_inputs.with_raw_response.update(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_input = await response.parse()
        assert_matches_type(LiveInputUpdateResponse, live_input, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.live_inputs.with_streaming_response.update(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_input = await response.parse()
            assert_matches_type(LiveInputUpdateResponse, live_input, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.live_inputs.with_raw_response.update(
                "66be4bf738797e01e1fca35a7bdecdcd",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            await async_client.stream.live_inputs.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        live_input = await async_client.stream.live_inputs.delete(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert live_input is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.live_inputs.with_raw_response.delete(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_input = await response.parse()
        assert live_input is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.live_inputs.with_streaming_response.delete(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_input = await response.parse()
            assert live_input is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.live_inputs.with_raw_response.delete(
                "66be4bf738797e01e1fca35a7bdecdcd",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            await async_client.stream.live_inputs.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        live_input = await async_client.stream.live_inputs.get(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LiveInputGetResponse, live_input, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.live_inputs.with_raw_response.get(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_input = await response.parse()
        assert_matches_type(LiveInputGetResponse, live_input, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.live_inputs.with_streaming_response.get(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_input = await response.parse()
            assert_matches_type(LiveInputGetResponse, live_input, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.live_inputs.with_raw_response.get(
                "66be4bf738797e01e1fca35a7bdecdcd",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            await async_client.stream.live_inputs.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_live_inputs_create_a_live_input(self, async_client: AsyncCloudflare) -> None:
        live_input = await async_client.stream.live_inputs.stream_live_inputs_create_a_live_input(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LiveInputStreamLiveInputsCreateALiveInputResponse, live_input, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_live_inputs_create_a_live_input_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        live_input = await async_client.stream.live_inputs.stream_live_inputs_create_a_live_input(
            "023e105f4ecef8ad9ca31a8372d0c353",
            default_creator="string",
            delete_recording_after_days=45,
            meta={"name": "test stream 1"},
            recording={
                "allowed_origins": ["example.com"],
                "mode": "off",
                "require_signed_urls": False,
                "timeout_seconds": 0,
            },
        )
        assert_matches_type(LiveInputStreamLiveInputsCreateALiveInputResponse, live_input, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stream_live_inputs_create_a_live_input(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.live_inputs.with_raw_response.stream_live_inputs_create_a_live_input(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_input = await response.parse()
        assert_matches_type(LiveInputStreamLiveInputsCreateALiveInputResponse, live_input, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stream_live_inputs_create_a_live_input(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.stream.live_inputs.with_streaming_response.stream_live_inputs_create_a_live_input(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_input = await response.parse()
            assert_matches_type(LiveInputStreamLiveInputsCreateALiveInputResponse, live_input, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_stream_live_inputs_create_a_live_input(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.live_inputs.with_raw_response.stream_live_inputs_create_a_live_input(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_live_inputs_list_live_inputs(self, async_client: AsyncCloudflare) -> None:
        live_input = await async_client.stream.live_inputs.stream_live_inputs_list_live_inputs(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LiveInputStreamLiveInputsListLiveInputsResponse, live_input, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_live_inputs_list_live_inputs_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        live_input = await async_client.stream.live_inputs.stream_live_inputs_list_live_inputs(
            "023e105f4ecef8ad9ca31a8372d0c353",
            include_counts=True,
        )
        assert_matches_type(LiveInputStreamLiveInputsListLiveInputsResponse, live_input, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stream_live_inputs_list_live_inputs(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.live_inputs.with_raw_response.stream_live_inputs_list_live_inputs(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_input = await response.parse()
        assert_matches_type(LiveInputStreamLiveInputsListLiveInputsResponse, live_input, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stream_live_inputs_list_live_inputs(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.live_inputs.with_streaming_response.stream_live_inputs_list_live_inputs(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_input = await response.parse()
            assert_matches_type(LiveInputStreamLiveInputsListLiveInputsResponse, live_input, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_stream_live_inputs_list_live_inputs(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.live_inputs.with_raw_response.stream_live_inputs_list_live_inputs(
                "",
            )
