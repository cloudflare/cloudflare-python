# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.stream.live_inputs import Output

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOutputs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        output = client.stream.live_inputs.outputs.create(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            stream_key="uzya-f19y-g2g9-a2ee-51j2",
            url="rtmp://a.rtmp.youtube.com/live2",
        )
        assert_matches_type(Optional[Output], output, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        output = client.stream.live_inputs.outputs.create(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            stream_key="uzya-f19y-g2g9-a2ee-51j2",
            url="rtmp://a.rtmp.youtube.com/live2",
            enabled=True,
        )
        assert_matches_type(Optional[Output], output, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.stream.live_inputs.outputs.with_raw_response.create(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            stream_key="uzya-f19y-g2g9-a2ee-51j2",
            url="rtmp://a.rtmp.youtube.com/live2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = response.parse()
        assert_matches_type(Optional[Output], output, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.stream.live_inputs.outputs.with_streaming_response.create(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            stream_key="uzya-f19y-g2g9-a2ee-51j2",
            url="rtmp://a.rtmp.youtube.com/live2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = response.parse()
            assert_matches_type(Optional[Output], output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.live_inputs.outputs.with_raw_response.create(
                "66be4bf738797e01e1fca35a7bdecdcd",
                account_id="",
                stream_key="uzya-f19y-g2g9-a2ee-51j2",
                url="rtmp://a.rtmp.youtube.com/live2",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            client.stream.live_inputs.outputs.with_raw_response.create(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                stream_key="uzya-f19y-g2g9-a2ee-51j2",
                url="rtmp://a.rtmp.youtube.com/live2",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        output = client.stream.live_inputs.outputs.update(
            "baea4d9c515887b80289d5c33cf01145",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            enabled=True,
        )
        assert_matches_type(Optional[Output], output, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.stream.live_inputs.outputs.with_raw_response.update(
            "baea4d9c515887b80289d5c33cf01145",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = response.parse()
        assert_matches_type(Optional[Output], output, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.stream.live_inputs.outputs.with_streaming_response.update(
            "baea4d9c515887b80289d5c33cf01145",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = response.parse()
            assert_matches_type(Optional[Output], output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.live_inputs.outputs.with_raw_response.update(
                "baea4d9c515887b80289d5c33cf01145",
                account_id="",
                live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
                enabled=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            client.stream.live_inputs.outputs.with_raw_response.update(
                "baea4d9c515887b80289d5c33cf01145",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                live_input_identifier="",
                enabled=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `output_identifier` but received ''"):
            client.stream.live_inputs.outputs.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
                enabled=True,
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        output = client.stream.live_inputs.outputs.list(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[Output], output, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.stream.live_inputs.outputs.with_raw_response.list(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = response.parse()
        assert_matches_type(SyncSinglePage[Output], output, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.stream.live_inputs.outputs.with_streaming_response.list(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = response.parse()
            assert_matches_type(SyncSinglePage[Output], output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.live_inputs.outputs.with_raw_response.list(
                "66be4bf738797e01e1fca35a7bdecdcd",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            client.stream.live_inputs.outputs.with_raw_response.list(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        output = client.stream.live_inputs.outputs.delete(
            "baea4d9c515887b80289d5c33cf01145",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            body={},
        )
        assert output is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.stream.live_inputs.outputs.with_raw_response.delete(
            "baea4d9c515887b80289d5c33cf01145",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = response.parse()
        assert output is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.stream.live_inputs.outputs.with_streaming_response.delete(
            "baea4d9c515887b80289d5c33cf01145",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = response.parse()
            assert output is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.live_inputs.outputs.with_raw_response.delete(
                "baea4d9c515887b80289d5c33cf01145",
                account_id="",
                live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            client.stream.live_inputs.outputs.with_raw_response.delete(
                "baea4d9c515887b80289d5c33cf01145",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                live_input_identifier="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `output_identifier` but received ''"):
            client.stream.live_inputs.outputs.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
                body={},
            )


class TestAsyncOutputs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        output = await async_client.stream.live_inputs.outputs.create(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            stream_key="uzya-f19y-g2g9-a2ee-51j2",
            url="rtmp://a.rtmp.youtube.com/live2",
        )
        assert_matches_type(Optional[Output], output, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        output = await async_client.stream.live_inputs.outputs.create(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            stream_key="uzya-f19y-g2g9-a2ee-51j2",
            url="rtmp://a.rtmp.youtube.com/live2",
            enabled=True,
        )
        assert_matches_type(Optional[Output], output, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.live_inputs.outputs.with_raw_response.create(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            stream_key="uzya-f19y-g2g9-a2ee-51j2",
            url="rtmp://a.rtmp.youtube.com/live2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = await response.parse()
        assert_matches_type(Optional[Output], output, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.live_inputs.outputs.with_streaming_response.create(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            stream_key="uzya-f19y-g2g9-a2ee-51j2",
            url="rtmp://a.rtmp.youtube.com/live2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = await response.parse()
            assert_matches_type(Optional[Output], output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.live_inputs.outputs.with_raw_response.create(
                "66be4bf738797e01e1fca35a7bdecdcd",
                account_id="",
                stream_key="uzya-f19y-g2g9-a2ee-51j2",
                url="rtmp://a.rtmp.youtube.com/live2",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            await async_client.stream.live_inputs.outputs.with_raw_response.create(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                stream_key="uzya-f19y-g2g9-a2ee-51j2",
                url="rtmp://a.rtmp.youtube.com/live2",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        output = await async_client.stream.live_inputs.outputs.update(
            "baea4d9c515887b80289d5c33cf01145",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            enabled=True,
        )
        assert_matches_type(Optional[Output], output, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.live_inputs.outputs.with_raw_response.update(
            "baea4d9c515887b80289d5c33cf01145",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = await response.parse()
        assert_matches_type(Optional[Output], output, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.live_inputs.outputs.with_streaming_response.update(
            "baea4d9c515887b80289d5c33cf01145",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = await response.parse()
            assert_matches_type(Optional[Output], output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.live_inputs.outputs.with_raw_response.update(
                "baea4d9c515887b80289d5c33cf01145",
                account_id="",
                live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
                enabled=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            await async_client.stream.live_inputs.outputs.with_raw_response.update(
                "baea4d9c515887b80289d5c33cf01145",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                live_input_identifier="",
                enabled=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `output_identifier` but received ''"):
            await async_client.stream.live_inputs.outputs.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
                enabled=True,
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        output = await async_client.stream.live_inputs.outputs.list(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[Output], output, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.live_inputs.outputs.with_raw_response.list(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = await response.parse()
        assert_matches_type(AsyncSinglePage[Output], output, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.live_inputs.outputs.with_streaming_response.list(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = await response.parse()
            assert_matches_type(AsyncSinglePage[Output], output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.live_inputs.outputs.with_raw_response.list(
                "66be4bf738797e01e1fca35a7bdecdcd",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            await async_client.stream.live_inputs.outputs.with_raw_response.list(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        output = await async_client.stream.live_inputs.outputs.delete(
            "baea4d9c515887b80289d5c33cf01145",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            body={},
        )
        assert output is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.live_inputs.outputs.with_raw_response.delete(
            "baea4d9c515887b80289d5c33cf01145",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = await response.parse()
        assert output is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.live_inputs.outputs.with_streaming_response.delete(
            "baea4d9c515887b80289d5c33cf01145",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = await response.parse()
            assert output is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.live_inputs.outputs.with_raw_response.delete(
                "baea4d9c515887b80289d5c33cf01145",
                account_id="",
                live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            await async_client.stream.live_inputs.outputs.with_raw_response.delete(
                "baea4d9c515887b80289d5c33cf01145",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                live_input_identifier="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `output_identifier` but received ''"):
            await async_client.stream.live_inputs.outputs.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
                body={},
            )
