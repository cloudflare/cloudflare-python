# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.stream.live_inputs import (
    OutputUpdateResponse,
    OutputStreamLiveInputsCreateANewOutputConnectedToALiveInputResponse,
    OutputStreamLiveInputsListAllOutputsAssociatedWithASpecifiedLiveInputResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOutputs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        output = client.stream.live_inputs.outputs.update(
            "baea4d9c515887b80289d5c33cf01145",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            enabled=True,
        )
        assert_matches_type(OutputUpdateResponse, output, path=["response"])

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
        assert_matches_type(OutputUpdateResponse, output, path=["response"])

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
            assert_matches_type(OutputUpdateResponse, output, path=["response"])

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
    def test_method_delete(self, client: Cloudflare) -> None:
        output = client.stream.live_inputs.outputs.delete(
            "baea4d9c515887b80289d5c33cf01145",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
        )
        assert output is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.stream.live_inputs.outputs.with_raw_response.delete(
            "baea4d9c515887b80289d5c33cf01145",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
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
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            client.stream.live_inputs.outputs.with_raw_response.delete(
                "baea4d9c515887b80289d5c33cf01145",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                live_input_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `output_identifier` but received ''"):
            client.stream.live_inputs.outputs.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_live_inputs_create_a_new_output_connected_to_a_live_input(self, client: Cloudflare) -> None:
        output = client.stream.live_inputs.outputs.stream_live_inputs_create_a_new_output_connected_to_a_live_input(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            stream_key="uzya-f19y-g2g9-a2ee-51j2",
            url="rtmp://a.rtmp.youtube.com/live2",
        )
        assert_matches_type(
            OutputStreamLiveInputsCreateANewOutputConnectedToALiveInputResponse, output, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_live_inputs_create_a_new_output_connected_to_a_live_input_with_all_params(
        self, client: Cloudflare
    ) -> None:
        output = client.stream.live_inputs.outputs.stream_live_inputs_create_a_new_output_connected_to_a_live_input(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            stream_key="uzya-f19y-g2g9-a2ee-51j2",
            url="rtmp://a.rtmp.youtube.com/live2",
            enabled=True,
        )
        assert_matches_type(
            OutputStreamLiveInputsCreateANewOutputConnectedToALiveInputResponse, output, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stream_live_inputs_create_a_new_output_connected_to_a_live_input(
        self, client: Cloudflare
    ) -> None:
        response = client.stream.live_inputs.outputs.with_raw_response.stream_live_inputs_create_a_new_output_connected_to_a_live_input(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            stream_key="uzya-f19y-g2g9-a2ee-51j2",
            url="rtmp://a.rtmp.youtube.com/live2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = response.parse()
        assert_matches_type(
            OutputStreamLiveInputsCreateANewOutputConnectedToALiveInputResponse, output, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stream_live_inputs_create_a_new_output_connected_to_a_live_input(
        self, client: Cloudflare
    ) -> None:
        with client.stream.live_inputs.outputs.with_streaming_response.stream_live_inputs_create_a_new_output_connected_to_a_live_input(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            stream_key="uzya-f19y-g2g9-a2ee-51j2",
            url="rtmp://a.rtmp.youtube.com/live2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = response.parse()
            assert_matches_type(
                OutputStreamLiveInputsCreateANewOutputConnectedToALiveInputResponse, output, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_stream_live_inputs_create_a_new_output_connected_to_a_live_input(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.live_inputs.outputs.with_raw_response.stream_live_inputs_create_a_new_output_connected_to_a_live_input(
                "66be4bf738797e01e1fca35a7bdecdcd",
                account_id="",
                stream_key="uzya-f19y-g2g9-a2ee-51j2",
                url="rtmp://a.rtmp.youtube.com/live2",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            client.stream.live_inputs.outputs.with_raw_response.stream_live_inputs_create_a_new_output_connected_to_a_live_input(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                stream_key="uzya-f19y-g2g9-a2ee-51j2",
                url="rtmp://a.rtmp.youtube.com/live2",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input(
        self, client: Cloudflare
    ) -> None:
        output = client.stream.live_inputs.outputs.stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            OutputStreamLiveInputsListAllOutputsAssociatedWithASpecifiedLiveInputResponse, output, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input(
        self, client: Cloudflare
    ) -> None:
        response = client.stream.live_inputs.outputs.with_raw_response.stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = response.parse()
        assert_matches_type(
            OutputStreamLiveInputsListAllOutputsAssociatedWithASpecifiedLiveInputResponse, output, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input(
        self, client: Cloudflare
    ) -> None:
        with client.stream.live_inputs.outputs.with_streaming_response.stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = response.parse()
            assert_matches_type(
                OutputStreamLiveInputsListAllOutputsAssociatedWithASpecifiedLiveInputResponse, output, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.live_inputs.outputs.with_raw_response.stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input(
                "66be4bf738797e01e1fca35a7bdecdcd",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            client.stream.live_inputs.outputs.with_raw_response.stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncOutputs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        output = await async_client.stream.live_inputs.outputs.update(
            "baea4d9c515887b80289d5c33cf01145",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            enabled=True,
        )
        assert_matches_type(OutputUpdateResponse, output, path=["response"])

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
        assert_matches_type(OutputUpdateResponse, output, path=["response"])

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
            assert_matches_type(OutputUpdateResponse, output, path=["response"])

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
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        output = await async_client.stream.live_inputs.outputs.delete(
            "baea4d9c515887b80289d5c33cf01145",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
        )
        assert output is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.live_inputs.outputs.with_raw_response.delete(
            "baea4d9c515887b80289d5c33cf01145",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
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
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            await async_client.stream.live_inputs.outputs.with_raw_response.delete(
                "baea4d9c515887b80289d5c33cf01145",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                live_input_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `output_identifier` but received ''"):
            await async_client.stream.live_inputs.outputs.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                live_input_identifier="66be4bf738797e01e1fca35a7bdecdcd",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_live_inputs_create_a_new_output_connected_to_a_live_input(
        self, async_client: AsyncCloudflare
    ) -> None:
        output = await async_client.stream.live_inputs.outputs.stream_live_inputs_create_a_new_output_connected_to_a_live_input(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            stream_key="uzya-f19y-g2g9-a2ee-51j2",
            url="rtmp://a.rtmp.youtube.com/live2",
        )
        assert_matches_type(
            OutputStreamLiveInputsCreateANewOutputConnectedToALiveInputResponse, output, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_live_inputs_create_a_new_output_connected_to_a_live_input_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        output = await async_client.stream.live_inputs.outputs.stream_live_inputs_create_a_new_output_connected_to_a_live_input(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            stream_key="uzya-f19y-g2g9-a2ee-51j2",
            url="rtmp://a.rtmp.youtube.com/live2",
            enabled=True,
        )
        assert_matches_type(
            OutputStreamLiveInputsCreateANewOutputConnectedToALiveInputResponse, output, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stream_live_inputs_create_a_new_output_connected_to_a_live_input(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.stream.live_inputs.outputs.with_raw_response.stream_live_inputs_create_a_new_output_connected_to_a_live_input(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            stream_key="uzya-f19y-g2g9-a2ee-51j2",
            url="rtmp://a.rtmp.youtube.com/live2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = await response.parse()
        assert_matches_type(
            OutputStreamLiveInputsCreateANewOutputConnectedToALiveInputResponse, output, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stream_live_inputs_create_a_new_output_connected_to_a_live_input(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.stream.live_inputs.outputs.with_streaming_response.stream_live_inputs_create_a_new_output_connected_to_a_live_input(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            stream_key="uzya-f19y-g2g9-a2ee-51j2",
            url="rtmp://a.rtmp.youtube.com/live2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = await response.parse()
            assert_matches_type(
                OutputStreamLiveInputsCreateANewOutputConnectedToALiveInputResponse, output, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_stream_live_inputs_create_a_new_output_connected_to_a_live_input(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.live_inputs.outputs.with_raw_response.stream_live_inputs_create_a_new_output_connected_to_a_live_input(
                "66be4bf738797e01e1fca35a7bdecdcd",
                account_id="",
                stream_key="uzya-f19y-g2g9-a2ee-51j2",
                url="rtmp://a.rtmp.youtube.com/live2",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            await async_client.stream.live_inputs.outputs.with_raw_response.stream_live_inputs_create_a_new_output_connected_to_a_live_input(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                stream_key="uzya-f19y-g2g9-a2ee-51j2",
                url="rtmp://a.rtmp.youtube.com/live2",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input(
        self, async_client: AsyncCloudflare
    ) -> None:
        output = await async_client.stream.live_inputs.outputs.stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            OutputStreamLiveInputsListAllOutputsAssociatedWithASpecifiedLiveInputResponse, output, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.stream.live_inputs.outputs.with_raw_response.stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = await response.parse()
        assert_matches_type(
            OutputStreamLiveInputsListAllOutputsAssociatedWithASpecifiedLiveInputResponse, output, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.stream.live_inputs.outputs.with_streaming_response.stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input(
            "66be4bf738797e01e1fca35a7bdecdcd",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = await response.parse()
            assert_matches_type(
                OutputStreamLiveInputsListAllOutputsAssociatedWithASpecifiedLiveInputResponse, output, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.live_inputs.outputs.with_raw_response.stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input(
                "66be4bf738797e01e1fca35a7bdecdcd",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `live_input_identifier` but received ''"):
            await async_client.stream.live_inputs.outputs.with_raw_response.stream_live_inputs_list_all_outputs_associated_with_a_specified_live_input(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
