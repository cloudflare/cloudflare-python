# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.snippets import SnippetRuleUpdateResponse, SnippetRuleListResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.snippets import snippet_rule_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSnippetRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        snippet_rule = client.snippets.snippet_rules.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SnippetRuleUpdateResponse, snippet_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        snippet_rule = client.snippets.snippet_rules.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            rules=[
                {
                    "description": "Rule description",
                    "enabled": True,
                    "expression": 'http.cookie eq "a=b"',
                    "snippet_name": "snippet_name_01",
                },
                {
                    "description": "Rule description",
                    "enabled": True,
                    "expression": 'http.cookie eq "a=b"',
                    "snippet_name": "snippet_name_01",
                },
                {
                    "description": "Rule description",
                    "enabled": True,
                    "expression": 'http.cookie eq "a=b"',
                    "snippet_name": "snippet_name_01",
                },
            ],
        )
        assert_matches_type(SnippetRuleUpdateResponse, snippet_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.snippets.snippet_rules.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snippet_rule = response.parse()
        assert_matches_type(SnippetRuleUpdateResponse, snippet_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.snippets.snippet_rules.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snippet_rule = response.parse()
            assert_matches_type(SnippetRuleUpdateResponse, snippet_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.snippets.snippet_rules.with_raw_response.update(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        snippet_rule = client.snippets.snippet_rules.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SnippetRuleListResponse, snippet_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.snippets.snippet_rules.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snippet_rule = response.parse()
        assert_matches_type(SnippetRuleListResponse, snippet_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.snippets.snippet_rules.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snippet_rule = response.parse()
            assert_matches_type(SnippetRuleListResponse, snippet_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.snippets.snippet_rules.with_raw_response.list(
                "",
            )


class TestAsyncSnippetRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        snippet_rule = await async_client.snippets.snippet_rules.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SnippetRuleUpdateResponse, snippet_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        snippet_rule = await async_client.snippets.snippet_rules.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            rules=[
                {
                    "description": "Rule description",
                    "enabled": True,
                    "expression": 'http.cookie eq "a=b"',
                    "snippet_name": "snippet_name_01",
                },
                {
                    "description": "Rule description",
                    "enabled": True,
                    "expression": 'http.cookie eq "a=b"',
                    "snippet_name": "snippet_name_01",
                },
                {
                    "description": "Rule description",
                    "enabled": True,
                    "expression": 'http.cookie eq "a=b"',
                    "snippet_name": "snippet_name_01",
                },
            ],
        )
        assert_matches_type(SnippetRuleUpdateResponse, snippet_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.snippets.snippet_rules.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snippet_rule = await response.parse()
        assert_matches_type(SnippetRuleUpdateResponse, snippet_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.snippets.snippet_rules.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snippet_rule = await response.parse()
            assert_matches_type(SnippetRuleUpdateResponse, snippet_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.snippets.snippet_rules.with_raw_response.update(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        snippet_rule = await async_client.snippets.snippet_rules.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SnippetRuleListResponse, snippet_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.snippets.snippet_rules.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snippet_rule = await response.parse()
        assert_matches_type(SnippetRuleListResponse, snippet_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.snippets.snippet_rules.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snippet_rule = await response.parse()
            assert_matches_type(SnippetRuleListResponse, snippet_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.snippets.snippet_rules.with_raw_response.list(
                "",
            )
