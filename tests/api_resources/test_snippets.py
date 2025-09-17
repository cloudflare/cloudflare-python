# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.snippets import (
    SnippetGetResponse,
    SnippetListResponse,
    SnippetUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSnippets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        snippet = client.snippets.update(
            snippet_name="my_snippet",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            files=[b"raw file contents"],
            metadata={"main_module": "main.js"},
        )
        assert_matches_type(SnippetUpdateResponse, snippet, path=["response"])

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.snippets.with_raw_response.update(
            snippet_name="my_snippet",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            files=[b"raw file contents"],
            metadata={"main_module": "main.js"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snippet = response.parse()
        assert_matches_type(SnippetUpdateResponse, snippet, path=["response"])

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.snippets.with_streaming_response.update(
            snippet_name="my_snippet",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            files=[b"raw file contents"],
            metadata={"main_module": "main.js"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snippet = response.parse()
            assert_matches_type(SnippetUpdateResponse, snippet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.snippets.with_raw_response.update(
                snippet_name="my_snippet",
                zone_id="",
                files=[b"raw file contents"],
                metadata={"main_module": "main.js"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snippet_name` but received ''"):
            client.snippets.with_raw_response.update(
                snippet_name="",
                zone_id="9f1839b6152d298aca64c4e906b6d074",
                files=[b"raw file contents"],
                metadata={"main_module": "main.js"},
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        snippet = client.snippets.list(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert_matches_type(SyncV4PagePaginationArray[SnippetListResponse], snippet, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        snippet = client.snippets.list(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            page=1,
            per_page=25,
        )
        assert_matches_type(SyncV4PagePaginationArray[SnippetListResponse], snippet, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.snippets.with_raw_response.list(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snippet = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[SnippetListResponse], snippet, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.snippets.with_streaming_response.list(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snippet = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[SnippetListResponse], snippet, path=["response"])

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
            snippet_name="my_snippet",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert_matches_type(str, snippet, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.snippets.with_raw_response.delete(
            snippet_name="my_snippet",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snippet = response.parse()
        assert_matches_type(str, snippet, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.snippets.with_streaming_response.delete(
            snippet_name="my_snippet",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snippet = response.parse()
            assert_matches_type(str, snippet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.snippets.with_raw_response.delete(
                snippet_name="my_snippet",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snippet_name` but received ''"):
            client.snippets.with_raw_response.delete(
                snippet_name="",
                zone_id="9f1839b6152d298aca64c4e906b6d074",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        snippet = client.snippets.get(
            snippet_name="my_snippet",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert_matches_type(SnippetGetResponse, snippet, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.snippets.with_raw_response.get(
            snippet_name="my_snippet",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snippet = response.parse()
        assert_matches_type(SnippetGetResponse, snippet, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.snippets.with_streaming_response.get(
            snippet_name="my_snippet",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snippet = response.parse()
            assert_matches_type(SnippetGetResponse, snippet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.snippets.with_raw_response.get(
                snippet_name="my_snippet",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snippet_name` but received ''"):
            client.snippets.with_raw_response.get(
                snippet_name="",
                zone_id="9f1839b6152d298aca64c4e906b6d074",
            )


class TestAsyncSnippets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        snippet = await async_client.snippets.update(
            snippet_name="my_snippet",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            files=[b"raw file contents"],
            metadata={"main_module": "main.js"},
        )
        assert_matches_type(SnippetUpdateResponse, snippet, path=["response"])

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.snippets.with_raw_response.update(
            snippet_name="my_snippet",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            files=[b"raw file contents"],
            metadata={"main_module": "main.js"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snippet = await response.parse()
        assert_matches_type(SnippetUpdateResponse, snippet, path=["response"])

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.snippets.with_streaming_response.update(
            snippet_name="my_snippet",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            files=[b"raw file contents"],
            metadata={"main_module": "main.js"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snippet = await response.parse()
            assert_matches_type(SnippetUpdateResponse, snippet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="throwing HTTP 415")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.snippets.with_raw_response.update(
                snippet_name="my_snippet",
                zone_id="",
                files=[b"raw file contents"],
                metadata={"main_module": "main.js"},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snippet_name` but received ''"):
            await async_client.snippets.with_raw_response.update(
                snippet_name="",
                zone_id="9f1839b6152d298aca64c4e906b6d074",
                files=[b"raw file contents"],
                metadata={"main_module": "main.js"},
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        snippet = await async_client.snippets.list(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert_matches_type(AsyncV4PagePaginationArray[SnippetListResponse], snippet, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        snippet = await async_client.snippets.list(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
            page=1,
            per_page=25,
        )
        assert_matches_type(AsyncV4PagePaginationArray[SnippetListResponse], snippet, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.snippets.with_raw_response.list(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snippet = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[SnippetListResponse], snippet, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.snippets.with_streaming_response.list(
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snippet = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[SnippetListResponse], snippet, path=["response"])

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
            snippet_name="my_snippet",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert_matches_type(str, snippet, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.snippets.with_raw_response.delete(
            snippet_name="my_snippet",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snippet = await response.parse()
        assert_matches_type(str, snippet, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.snippets.with_streaming_response.delete(
            snippet_name="my_snippet",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snippet = await response.parse()
            assert_matches_type(str, snippet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.snippets.with_raw_response.delete(
                snippet_name="my_snippet",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snippet_name` but received ''"):
            await async_client.snippets.with_raw_response.delete(
                snippet_name="",
                zone_id="9f1839b6152d298aca64c4e906b6d074",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        snippet = await async_client.snippets.get(
            snippet_name="my_snippet",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )
        assert_matches_type(SnippetGetResponse, snippet, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.snippets.with_raw_response.get(
            snippet_name="my_snippet",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snippet = await response.parse()
        assert_matches_type(SnippetGetResponse, snippet, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.snippets.with_streaming_response.get(
            snippet_name="my_snippet",
            zone_id="9f1839b6152d298aca64c4e906b6d074",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snippet = await response.parse()
            assert_matches_type(SnippetGetResponse, snippet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.snippets.with_raw_response.get(
                snippet_name="my_snippet",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `snippet_name` but received ''"):
            await async_client.snippets.with_raw_response.get(
                snippet_name="",
                zone_id="9f1839b6152d298aca64c4e906b6d074",
            )
