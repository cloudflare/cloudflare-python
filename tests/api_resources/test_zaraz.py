# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types import ZarazWorkflowUpdateResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import zaraz_workflow_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestZaraz:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_workflow_update(self, client: Cloudflare) -> None:
        zaraz = client.zaraz.workflow_update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body="realtime",
        )
        assert_matches_type(ZarazWorkflowUpdateResponse, zaraz, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_workflow_update(self, client: Cloudflare) -> None:
        response = client.zaraz.with_raw_response.workflow_update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body="realtime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zaraz = response.parse()
        assert_matches_type(ZarazWorkflowUpdateResponse, zaraz, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_workflow_update(self, client: Cloudflare) -> None:
        with client.zaraz.with_streaming_response.workflow_update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body="realtime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zaraz = response.parse()
            assert_matches_type(ZarazWorkflowUpdateResponse, zaraz, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_workflow_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zaraz.with_raw_response.workflow_update(
                "",
                body="realtime",
            )


class TestAsyncZaraz:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_workflow_update(self, async_client: AsyncCloudflare) -> None:
        zaraz = await async_client.zaraz.workflow_update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body="realtime",
        )
        assert_matches_type(ZarazWorkflowUpdateResponse, zaraz, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_workflow_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zaraz.with_raw_response.workflow_update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body="realtime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        zaraz = await response.parse()
        assert_matches_type(ZarazWorkflowUpdateResponse, zaraz, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_workflow_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zaraz.with_streaming_response.workflow_update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body="realtime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            zaraz = await response.parse()
            assert_matches_type(ZarazWorkflowUpdateResponse, zaraz, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_workflow_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zaraz.with_raw_response.workflow_update(
                "",
                body="realtime",
            )
