# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.cloudforce_one.threat_signals import (
    ArticleGetResponse,
    ArticleEditResponse,
    ArticleListResponse,
    ArticleBulkEditResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArticles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        article = client.cloudforce_one.threat_signals.articles.list(
            account_id="account_id",
        )
        assert_matches_type(ArticleListResponse, article, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        article = client.cloudforce_one.threat_signals.articles.list(
            account_id="account_id",
            article_id=["550e8400-e29b-41d4-a716-446655440000", "660e8400-e29b-41d4-a716-446655440000"],
            cursor="x",
            feed_category="feed_category",
            feed_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            fetched_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            fetched_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_total=True,
            per_page=1,
            published_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            published_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            read=True,
            search="x",
            sort="sort",
            source_type="curated",
            tag="tag",
            tag_applied_by="ai",
            tag_category="tag_category",
            tag_category_id=["660e8400-e29b-41d4-a716-446655440000"],
            tag_id=["550e8400-e29b-41d4-a716-446655440000"],
        )
        assert_matches_type(ArticleListResponse, article, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_signals.articles.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = response.parse()
        assert_matches_type(ArticleListResponse, article, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_signals.articles.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = response.parse()
            assert_matches_type(ArticleListResponse, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_signals.articles.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_bulk_edit(self, client: Cloudflare) -> None:
        article = client.cloudforce_one.threat_signals.articles.bulk_edit(
            account_id="account_id",
            article_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            read=True,
        )
        assert_matches_type(ArticleBulkEditResponse, article, path=["response"])

    @parametrize
    def test_raw_response_bulk_edit(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_signals.articles.with_raw_response.bulk_edit(
            account_id="account_id",
            article_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            read=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = response.parse()
        assert_matches_type(ArticleBulkEditResponse, article, path=["response"])

    @parametrize
    def test_streaming_response_bulk_edit(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_signals.articles.with_streaming_response.bulk_edit(
            account_id="account_id",
            article_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            read=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = response.parse()
            assert_matches_type(ArticleBulkEditResponse, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_signals.articles.with_raw_response.bulk_edit(
                account_id="",
                article_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                read=True,
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        article = client.cloudforce_one.threat_signals.articles.edit(
            article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            read=True,
        )
        assert_matches_type(ArticleEditResponse, article, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_signals.articles.with_raw_response.edit(
            article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            read=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = response.parse()
        assert_matches_type(ArticleEditResponse, article, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_signals.articles.with_streaming_response.edit(
            article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            read=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = response.parse()
            assert_matches_type(ArticleEditResponse, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_signals.articles.with_raw_response.edit(
                article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                read=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `article_id` but received ''"):
            client.cloudforce_one.threat_signals.articles.with_raw_response.edit(
                article_id="",
                account_id="account_id",
                read=True,
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        article = client.cloudforce_one.threat_signals.articles.get(
            article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(ArticleGetResponse, article, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_signals.articles.with_raw_response.get(
            article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = response.parse()
        assert_matches_type(ArticleGetResponse, article, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_signals.articles.with_streaming_response.get(
            article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = response.parse()
            assert_matches_type(ArticleGetResponse, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_signals.articles.with_raw_response.get(
                article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `article_id` but received ''"):
            client.cloudforce_one.threat_signals.articles.with_raw_response.get(
                article_id="",
                account_id="account_id",
            )


class TestAsyncArticles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        article = await async_client.cloudforce_one.threat_signals.articles.list(
            account_id="account_id",
        )
        assert_matches_type(ArticleListResponse, article, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        article = await async_client.cloudforce_one.threat_signals.articles.list(
            account_id="account_id",
            article_id=["550e8400-e29b-41d4-a716-446655440000", "660e8400-e29b-41d4-a716-446655440000"],
            cursor="x",
            feed_category="feed_category",
            feed_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            fetched_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            fetched_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_total=True,
            per_page=1,
            published_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            published_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            read=True,
            search="x",
            sort="sort",
            source_type="curated",
            tag="tag",
            tag_applied_by="ai",
            tag_category="tag_category",
            tag_category_id=["660e8400-e29b-41d4-a716-446655440000"],
            tag_id=["550e8400-e29b-41d4-a716-446655440000"],
        )
        assert_matches_type(ArticleListResponse, article, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_signals.articles.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = await response.parse()
        assert_matches_type(ArticleListResponse, article, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_signals.articles.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = await response.parse()
            assert_matches_type(ArticleListResponse, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.articles.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_bulk_edit(self, async_client: AsyncCloudflare) -> None:
        article = await async_client.cloudforce_one.threat_signals.articles.bulk_edit(
            account_id="account_id",
            article_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            read=True,
        )
        assert_matches_type(ArticleBulkEditResponse, article, path=["response"])

    @parametrize
    async def test_raw_response_bulk_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_signals.articles.with_raw_response.bulk_edit(
            account_id="account_id",
            article_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            read=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = await response.parse()
        assert_matches_type(ArticleBulkEditResponse, article, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_signals.articles.with_streaming_response.bulk_edit(
            account_id="account_id",
            article_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            read=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = await response.parse()
            assert_matches_type(ArticleBulkEditResponse, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.articles.with_raw_response.bulk_edit(
                account_id="",
                article_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                read=True,
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        article = await async_client.cloudforce_one.threat_signals.articles.edit(
            article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            read=True,
        )
        assert_matches_type(ArticleEditResponse, article, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_signals.articles.with_raw_response.edit(
            article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            read=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = await response.parse()
        assert_matches_type(ArticleEditResponse, article, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_signals.articles.with_streaming_response.edit(
            article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            read=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = await response.parse()
            assert_matches_type(ArticleEditResponse, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.articles.with_raw_response.edit(
                article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                read=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `article_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.articles.with_raw_response.edit(
                article_id="",
                account_id="account_id",
                read=True,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        article = await async_client.cloudforce_one.threat_signals.articles.get(
            article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(ArticleGetResponse, article, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_signals.articles.with_raw_response.get(
            article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        article = await response.parse()
        assert_matches_type(ArticleGetResponse, article, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_signals.articles.with_streaming_response.get(
            article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            article = await response.parse()
            assert_matches_type(ArticleGetResponse, article, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.articles.with_raw_response.get(
                article_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `article_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.articles.with_raw_response.get(
                article_id="",
                account_id="account_id",
            )
