# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.workers.services.environments import ContentUpdateResponse

from typing import Any, cast

from cloudflare._response import (
    BinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.workers.services.environments import content_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        content = client.workers.services.environments.content.update(
            "production",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            service_name="my-worker",
        )
        assert_matches_type(ContentUpdateResponse, content, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        content = client.workers.services.environments.content.update(
            "production",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            service_name="my-worker",
            any_part_name=[b"raw file contents", b"raw file contents", b"raw file contents"],
            metadata={
                "body_part": "worker.js",
                "main_module": "worker.js",
            },
        )
        assert_matches_type(ContentUpdateResponse, content, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.workers.services.environments.content.with_raw_response.update(
            "production",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            service_name="my-worker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = response.parse()
        assert_matches_type(ContentUpdateResponse, content, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.workers.services.environments.content.with_streaming_response.update(
            "production",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            service_name="my-worker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = response.parse()
            assert_matches_type(ContentUpdateResponse, content, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.services.environments.content.with_raw_response.update(
                "production",
                account_id="",
                service_name="my-worker",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_name` but received ''"):
            client.workers.services.environments.content.with_raw_response.update(
                "production",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                service_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_name` but received ''"):
            client.workers.services.environments.content.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                service_name="my-worker",
            )

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/services/my-worker/environments/production/content"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        content = client.workers.services.environments.content.get(
            "production",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            service_name="my-worker",
        )
        assert content.is_closed
        assert content.json() == {"foo": "bar"}
        assert cast(Any, content.is_closed) is True
        assert isinstance(content, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/services/my-worker/environments/production/content"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        content = client.workers.services.environments.content.with_raw_response.get(
            "production",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            service_name="my-worker",
        )

        assert content.is_closed is True
        assert content.http_request.headers.get("X-Stainless-Lang") == "python"
        assert content.json() == {"foo": "bar"}
        assert isinstance(content, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/services/my-worker/environments/production/content"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.workers.services.environments.content.with_streaming_response.get(
            "production",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            service_name="my-worker",
        ) as content:
            assert not content.is_closed
            assert content.http_request.headers.get("X-Stainless-Lang") == "python"

            assert content.json() == {"foo": "bar"}
            assert cast(Any, content.is_closed) is True
            assert isinstance(content, StreamedBinaryAPIResponse)

        assert cast(Any, content.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.services.environments.content.with_raw_response.get(
                "production",
                account_id="",
                service_name="my-worker",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_name` but received ''"):
            client.workers.services.environments.content.with_raw_response.get(
                "production",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                service_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_name` but received ''"):
            client.workers.services.environments.content.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                service_name="my-worker",
            )


class TestAsyncContent:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        content = await async_client.workers.services.environments.content.update(
            "production",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            service_name="my-worker",
        )
        assert_matches_type(ContentUpdateResponse, content, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        content = await async_client.workers.services.environments.content.update(
            "production",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            service_name="my-worker",
            any_part_name=[b"raw file contents", b"raw file contents", b"raw file contents"],
            metadata={
                "body_part": "worker.js",
                "main_module": "worker.js",
            },
        )
        assert_matches_type(ContentUpdateResponse, content, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.services.environments.content.with_raw_response.update(
            "production",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            service_name="my-worker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content = await response.parse()
        assert_matches_type(ContentUpdateResponse, content, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.services.environments.content.with_streaming_response.update(
            "production",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            service_name="my-worker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content = await response.parse()
            assert_matches_type(ContentUpdateResponse, content, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.services.environments.content.with_raw_response.update(
                "production",
                account_id="",
                service_name="my-worker",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_name` but received ''"):
            await async_client.workers.services.environments.content.with_raw_response.update(
                "production",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                service_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_name` but received ''"):
            await async_client.workers.services.environments.content.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                service_name="my-worker",
            )

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/services/my-worker/environments/production/content"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        content = await async_client.workers.services.environments.content.get(
            "production",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            service_name="my-worker",
        )
        assert content.is_closed
        assert await content.json() == {"foo": "bar"}
        assert cast(Any, content.is_closed) is True
        assert isinstance(content, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/services/my-worker/environments/production/content"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        content = await async_client.workers.services.environments.content.with_raw_response.get(
            "production",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            service_name="my-worker",
        )

        assert content.is_closed is True
        assert content.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await content.json() == {"foo": "bar"}
        assert isinstance(content, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/workers/services/my-worker/environments/production/content"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.workers.services.environments.content.with_streaming_response.get(
            "production",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            service_name="my-worker",
        ) as content:
            assert not content.is_closed
            assert content.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await content.json() == {"foo": "bar"}
            assert cast(Any, content.is_closed) is True
            assert isinstance(content, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, content.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.services.environments.content.with_raw_response.get(
                "production",
                account_id="",
                service_name="my-worker",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_name` but received ''"):
            await async_client.workers.services.environments.content.with_raw_response.get(
                "production",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                service_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `environment_name` but received ''"):
            await async_client.workers.services.environments.content.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                service_name="my-worker",
            )
