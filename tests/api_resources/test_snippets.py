# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.snippets import Snippet, SnippetDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSnippets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        snippet = client.snippets.update(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Snippet], snippet, path=["response"])

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        snippet = client.snippets.update(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            files="export { async function fetch(request, env) {return new Response('some_response') } }",
            metadata={"main_module": "main.js"},
        )
        assert_matches_type(Optional[Snippet], snippet, path=["response"])

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.snippets.with_raw_response.update(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snippet = response.parse()
        assert_matches_type(Optional[Snippet], snippet, path=["response"])

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.snippets.with_streaming_response.update(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snippet = response.parse()
            assert_matches_type(Optional[Snippet], snippet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.snippets.with_raw_response.update(
                snippet_name="snippet_name_01",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snippet_name` but received ''"):
            client.snippets.with_raw_response.update(
                snippet_name="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        snippet = client.snippets.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[Snippet], snippet, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.snippets.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snippet = response.parse()
        assert_matches_type(SyncSinglePage[Snippet], snippet, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.snippets.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snippet = response.parse()
            assert_matches_type(SyncSinglePage[Snippet], snippet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.snippets.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        snippet = client.snippets.delete(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SnippetDeleteResponse, snippet, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.snippets.with_raw_response.delete(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snippet = response.parse()
        assert_matches_type(SnippetDeleteResponse, snippet, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.snippets.with_streaming_response.delete(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snippet = response.parse()
            assert_matches_type(SnippetDeleteResponse, snippet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.snippets.with_raw_response.delete(
                snippet_name="snippet_name_01",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snippet_name` but received ''"):
            client.snippets.with_raw_response.delete(
                snippet_name="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        snippet = client.snippets.get(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Snippet], snippet, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.snippets.with_raw_response.get(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snippet = response.parse()
        assert_matches_type(Optional[Snippet], snippet, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.snippets.with_streaming_response.get(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snippet = response.parse()
            assert_matches_type(Optional[Snippet], snippet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.snippets.with_raw_response.get(
                snippet_name="snippet_name_01",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snippet_name` but received ''"):
            client.snippets.with_raw_response.get(
                snippet_name="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncSnippets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        snippet = await async_client.snippets.update(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Snippet], snippet, path=["response"])

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        snippet = await async_client.snippets.update(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            files="export { async function fetch(request, env) {return new Response('some_response') } }",
            metadata={"main_module": "main.js"},
        )
        assert_matches_type(Optional[Snippet], snippet, path=["response"])

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.snippets.with_raw_response.update(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snippet = await response.parse()
        assert_matches_type(Optional[Snippet], snippet, path=["response"])

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.snippets.with_streaming_response.update(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snippet = await response.parse()
            assert_matches_type(Optional[Snippet], snippet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.snippets.with_raw_response.update(
                snippet_name="snippet_name_01",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snippet_name` but received ''"):
            await async_client.snippets.with_raw_response.update(
                snippet_name="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        snippet = await async_client.snippets.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[Snippet], snippet, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.snippets.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snippet = await response.parse()
        assert_matches_type(AsyncSinglePage[Snippet], snippet, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.snippets.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snippet = await response.parse()
            assert_matches_type(AsyncSinglePage[Snippet], snippet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.snippets.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        snippet = await async_client.snippets.delete(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SnippetDeleteResponse, snippet, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.snippets.with_raw_response.delete(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snippet = await response.parse()
        assert_matches_type(SnippetDeleteResponse, snippet, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.snippets.with_streaming_response.delete(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snippet = await response.parse()
            assert_matches_type(SnippetDeleteResponse, snippet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.snippets.with_raw_response.delete(
                snippet_name="snippet_name_01",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snippet_name` but received ''"):
            await async_client.snippets.with_raw_response.delete(
                snippet_name="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        snippet = await async_client.snippets.get(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Snippet], snippet, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.snippets.with_raw_response.get(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snippet = await response.parse()
        assert_matches_type(Optional[Snippet], snippet, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.snippets.with_streaming_response.get(
            snippet_name="snippet_name_01",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snippet = await response.parse()
            assert_matches_type(Optional[Snippet], snippet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.snippets.with_raw_response.get(
                snippet_name="snippet_name_01",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snippet_name` but received ''"):
            await async_client.snippets.with_raw_response.get(
                snippet_name="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
