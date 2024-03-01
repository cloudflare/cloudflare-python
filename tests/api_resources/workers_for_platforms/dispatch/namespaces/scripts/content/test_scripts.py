# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from cloudflare.types.workers_for_platforms.dispatch.namespaces.scripts.content import (
    ScriptUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScripts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        script = client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.update(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )
        assert_matches_type(ScriptUpdateResponse, script, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        script = client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.update(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            any_part_name=[b"raw file contents", b"raw file contents", b"raw file contents"],
            metadata={
                "body_part": "worker.js",
                "main_module": "worker.js",
            },
        )
        assert_matches_type(ScriptUpdateResponse, script, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.with_raw_response.update(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = response.parse()
        assert_matches_type(ScriptUpdateResponse, script, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.with_streaming_response.update(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = response.parse()
            assert_matches_type(ScriptUpdateResponse, script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.with_raw_response.update(
                "this-is_my_script-01",
                account_id="",
                dispatch_namespace="my-dispatch-namespace",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispatch_namespace` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.with_raw_response.update(
                "this-is_my_script-01",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="my-dispatch-namespace",
            )

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/dispatch/namespaces/my-dispatch-namespace/scripts/this-is_my_script-01/content"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        script = client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.get(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )
        assert script.is_closed
        assert script.json() == {"foo": "bar"}
        assert cast(Any, script.is_closed) is True
        assert isinstance(script, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/dispatch/namespaces/my-dispatch-namespace/scripts/this-is_my_script-01/content"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        script = client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.with_raw_response.get(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )

        assert script.is_closed is True
        assert script.http_request.headers.get("X-Stainless-Lang") == "python"
        assert script.json() == {"foo": "bar"}
        assert isinstance(script, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/dispatch/namespaces/my-dispatch-namespace/scripts/this-is_my_script-01/content"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.with_streaming_response.get(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        ) as script:
            assert not script.is_closed
            assert script.http_request.headers.get("X-Stainless-Lang") == "python"

            assert script.json() == {"foo": "bar"}
            assert cast(Any, script.is_closed) is True
            assert isinstance(script, StreamedBinaryAPIResponse)

        assert cast(Any, script.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.with_raw_response.get(
                "this-is_my_script-01",
                account_id="",
                dispatch_namespace="my-dispatch-namespace",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispatch_namespace` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.with_raw_response.get(
                "this-is_my_script-01",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="my-dispatch-namespace",
            )


class TestAsyncScripts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        script = await async_client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.update(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )
        assert_matches_type(ScriptUpdateResponse, script, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        script = await async_client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.update(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
            any_part_name=[b"raw file contents", b"raw file contents", b"raw file contents"],
            metadata={
                "body_part": "worker.js",
                "main_module": "worker.js",
            },
        )
        assert_matches_type(ScriptUpdateResponse, script, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.with_raw_response.update(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = await response.parse()
        assert_matches_type(ScriptUpdateResponse, script, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.with_streaming_response.update(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = await response.parse()
            assert_matches_type(ScriptUpdateResponse, script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await (
                async_client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.with_raw_response.update(
                    "this-is_my_script-01",
                    account_id="",
                    dispatch_namespace="my-dispatch-namespace",
                )
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispatch_namespace` but received ''"):
            await (
                async_client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.with_raw_response.update(
                    "this-is_my_script-01",
                    account_id="023e105f4ecef8ad9ca31a8372d0c353",
                    dispatch_namespace="",
                )
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await (
                async_client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.with_raw_response.update(
                    "",
                    account_id="023e105f4ecef8ad9ca31a8372d0c353",
                    dispatch_namespace="my-dispatch-namespace",
                )
            )

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/dispatch/namespaces/my-dispatch-namespace/scripts/this-is_my_script-01/content"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        script = await async_client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.get(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        )
        assert script.is_closed
        assert await script.json() == {"foo": "bar"}
        assert cast(Any, script.is_closed) is True
        assert isinstance(script, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/dispatch/namespaces/my-dispatch-namespace/scripts/this-is_my_script-01/content"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        script = (
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.with_raw_response.get(
                "this-is_my_script-01",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="my-dispatch-namespace",
            )
        )

        assert script.is_closed is True
        assert script.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await script.json() == {"foo": "bar"}
        assert isinstance(script, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/dispatch/namespaces/my-dispatch-namespace/scripts/this-is_my_script-01/content"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.with_streaming_response.get(
            "this-is_my_script-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            dispatch_namespace="my-dispatch-namespace",
        ) as script:
            assert not script.is_closed
            assert script.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await script.json() == {"foo": "bar"}
            assert cast(Any, script.is_closed) is True
            assert isinstance(script, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, script.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.with_raw_response.get(
                "this-is_my_script-01",
                account_id="",
                dispatch_namespace="my-dispatch-namespace",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispatch_namespace` but received ''"):
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.with_raw_response.get(
                "this-is_my_script-01",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers_for_platforms.dispatch.namespaces.scripts.content.scripts.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                dispatch_namespace="my-dispatch-namespace",
            )
