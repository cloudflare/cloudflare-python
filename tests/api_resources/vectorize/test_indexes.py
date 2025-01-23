# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.vectorize import (
    CreateIndex,
    IndexInfoResponse,
    IndexQueryResponse,
    IndexDeleteResponse,
    IndexInsertResponse,
    IndexUpsertResponse,
    IndexDeleteByIDsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIndexes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "dimensions": 768,
                "metric": "cosine",
            },
            name="example-index",
        )
        assert_matches_type(Optional[CreateIndex], index, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "dimensions": 768,
                "metric": "cosine",
            },
            name="example-index",
            description="This is my example index.",
        )
        assert_matches_type(Optional[CreateIndex], index, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.vectorize.indexes.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "dimensions": 768,
                "metric": "cosine",
            },
            name="example-index",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(Optional[CreateIndex], index, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.vectorize.indexes.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "dimensions": 768,
                "metric": "cosine",
            },
            name="example-index",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(Optional[CreateIndex], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.vectorize.indexes.with_raw_response.create(
                account_id="",
                config={
                    "dimensions": 768,
                    "metric": "cosine",
                },
                name="example-index",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[CreateIndex], index, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.vectorize.indexes.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(SyncSinglePage[CreateIndex], index, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.vectorize.indexes.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(SyncSinglePage[CreateIndex], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.vectorize.indexes.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.delete(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndexDeleteResponse], index, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.vectorize.indexes.with_raw_response.delete(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(Optional[IndexDeleteResponse], index, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.vectorize.indexes.with_streaming_response.delete(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(Optional[IndexDeleteResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.vectorize.indexes.with_raw_response.delete(
                index_name="example-index",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            client.vectorize.indexes.with_raw_response.delete(
                index_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete_by_ids(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.delete_by_ids(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndexDeleteByIDsResponse], index, path=["response"])

    @parametrize
    def test_method_delete_by_ids_with_all_params(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.delete_by_ids(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ids=["5121db81354a40c6aedc3fe1ace51c59", "f90eb49c2107486abdfd78c67e853430"],
        )
        assert_matches_type(Optional[IndexDeleteByIDsResponse], index, path=["response"])

    @parametrize
    def test_raw_response_delete_by_ids(self, client: Cloudflare) -> None:
        response = client.vectorize.indexes.with_raw_response.delete_by_ids(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(Optional[IndexDeleteByIDsResponse], index, path=["response"])

    @parametrize
    def test_streaming_response_delete_by_ids(self, client: Cloudflare) -> None:
        with client.vectorize.indexes.with_streaming_response.delete_by_ids(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(Optional[IndexDeleteByIDsResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_by_ids(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.vectorize.indexes.with_raw_response.delete_by_ids(
                index_name="example-index",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            client.vectorize.indexes.with_raw_response.delete_by_ids(
                index_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.get(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CreateIndex], index, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.vectorize.indexes.with_raw_response.get(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(Optional[CreateIndex], index, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.vectorize.indexes.with_streaming_response.get(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(Optional[CreateIndex], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.vectorize.indexes.with_raw_response.get(
                index_name="example-index",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            client.vectorize.indexes.with_raw_response.get(
                index_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get_by_ids(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.get_by_ids(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, index, path=["response"])

    @parametrize
    def test_method_get_by_ids_with_all_params(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.get_by_ids(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ids=["5121db81354a40c6aedc3fe1ace51c59", "f90eb49c2107486abdfd78c67e853430"],
        )
        assert_matches_type(object, index, path=["response"])

    @parametrize
    def test_raw_response_get_by_ids(self, client: Cloudflare) -> None:
        response = client.vectorize.indexes.with_raw_response.get_by_ids(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(object, index, path=["response"])

    @parametrize
    def test_streaming_response_get_by_ids(self, client: Cloudflare) -> None:
        with client.vectorize.indexes.with_streaming_response.get_by_ids(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(object, index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_ids(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.vectorize.indexes.with_raw_response.get_by_ids(
                index_name="example-index",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            client.vectorize.indexes.with_raw_response.get_by_ids(
                index_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_info(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.info(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndexInfoResponse], index, path=["response"])

    @parametrize
    def test_raw_response_info(self, client: Cloudflare) -> None:
        response = client.vectorize.indexes.with_raw_response.info(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(Optional[IndexInfoResponse], index, path=["response"])

    @parametrize
    def test_streaming_response_info(self, client: Cloudflare) -> None:
        with client.vectorize.indexes.with_streaming_response.info(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(Optional[IndexInfoResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_info(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.vectorize.indexes.with_raw_response.info(
                index_name="example-index",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            client.vectorize.indexes.with_raw_response.info(
                index_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_insert(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.insert(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="@/path/to/vectors.ndjson",
        )
        assert_matches_type(Optional[IndexInsertResponse], index, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_insert_with_all_params(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.insert(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="@/path/to/vectors.ndjson",
            unparsable_behavior="error",
        )
        assert_matches_type(Optional[IndexInsertResponse], index, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_insert(self, client: Cloudflare) -> None:
        response = client.vectorize.indexes.with_raw_response.insert(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="@/path/to/vectors.ndjson",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(Optional[IndexInsertResponse], index, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_insert(self, client: Cloudflare) -> None:
        with client.vectorize.indexes.with_streaming_response.insert(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="@/path/to/vectors.ndjson",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(Optional[IndexInsertResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_insert(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.vectorize.indexes.with_raw_response.insert(
                index_name="example-index",
                account_id="",
                body="@/path/to/vectors.ndjson",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            client.vectorize.indexes.with_raw_response.insert(
                index_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body="@/path/to/vectors.ndjson",
            )

    @parametrize
    def test_method_query(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.query(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            vector=[0.5, 0.5, 0.5],
        )
        assert_matches_type(Optional[IndexQueryResponse], index, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.query(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            vector=[0.5, 0.5, 0.5],
            filter={
                "has_viewed": {"$ne": True},
                "streaming_platform": "netflix",
            },
            return_metadata="none",
            return_values=True,
            top_k=5,
        )
        assert_matches_type(Optional[IndexQueryResponse], index, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Cloudflare) -> None:
        response = client.vectorize.indexes.with_raw_response.query(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            vector=[0.5, 0.5, 0.5],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(Optional[IndexQueryResponse], index, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Cloudflare) -> None:
        with client.vectorize.indexes.with_streaming_response.query(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            vector=[0.5, 0.5, 0.5],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(Optional[IndexQueryResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_query(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.vectorize.indexes.with_raw_response.query(
                index_name="example-index",
                account_id="",
                vector=[0.5, 0.5, 0.5],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            client.vectorize.indexes.with_raw_response.query(
                index_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                vector=[0.5, 0.5, 0.5],
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_upsert(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.upsert(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="@/path/to/vectors.ndjson",
        )
        assert_matches_type(Optional[IndexUpsertResponse], index, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_upsert_with_all_params(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.upsert(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="@/path/to/vectors.ndjson",
            unparsable_behavior="error",
        )
        assert_matches_type(Optional[IndexUpsertResponse], index, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_upsert(self, client: Cloudflare) -> None:
        response = client.vectorize.indexes.with_raw_response.upsert(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="@/path/to/vectors.ndjson",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(Optional[IndexUpsertResponse], index, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_upsert(self, client: Cloudflare) -> None:
        with client.vectorize.indexes.with_streaming_response.upsert(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="@/path/to/vectors.ndjson",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(Optional[IndexUpsertResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_upsert(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.vectorize.indexes.with_raw_response.upsert(
                index_name="example-index",
                account_id="",
                body="@/path/to/vectors.ndjson",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            client.vectorize.indexes.with_raw_response.upsert(
                index_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body="@/path/to/vectors.ndjson",
            )


class TestAsyncIndexes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "dimensions": 768,
                "metric": "cosine",
            },
            name="example-index",
        )
        assert_matches_type(Optional[CreateIndex], index, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "dimensions": 768,
                "metric": "cosine",
            },
            name="example-index",
            description="This is my example index.",
        )
        assert_matches_type(Optional[CreateIndex], index, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.vectorize.indexes.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "dimensions": 768,
                "metric": "cosine",
            },
            name="example-index",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(Optional[CreateIndex], index, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.vectorize.indexes.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            config={
                "dimensions": 768,
                "metric": "cosine",
            },
            name="example-index",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(Optional[CreateIndex], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.create(
                account_id="",
                config={
                    "dimensions": 768,
                    "metric": "cosine",
                },
                name="example-index",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[CreateIndex], index, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.vectorize.indexes.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(AsyncSinglePage[CreateIndex], index, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.vectorize.indexes.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(AsyncSinglePage[CreateIndex], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.delete(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndexDeleteResponse], index, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.vectorize.indexes.with_raw_response.delete(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(Optional[IndexDeleteResponse], index, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.vectorize.indexes.with_streaming_response.delete(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(Optional[IndexDeleteResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.delete(
                index_name="example-index",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.delete(
                index_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete_by_ids(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.delete_by_ids(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndexDeleteByIDsResponse], index, path=["response"])

    @parametrize
    async def test_method_delete_by_ids_with_all_params(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.delete_by_ids(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ids=["5121db81354a40c6aedc3fe1ace51c59", "f90eb49c2107486abdfd78c67e853430"],
        )
        assert_matches_type(Optional[IndexDeleteByIDsResponse], index, path=["response"])

    @parametrize
    async def test_raw_response_delete_by_ids(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.vectorize.indexes.with_raw_response.delete_by_ids(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(Optional[IndexDeleteByIDsResponse], index, path=["response"])

    @parametrize
    async def test_streaming_response_delete_by_ids(self, async_client: AsyncCloudflare) -> None:
        async with async_client.vectorize.indexes.with_streaming_response.delete_by_ids(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(Optional[IndexDeleteByIDsResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_by_ids(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.delete_by_ids(
                index_name="example-index",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.delete_by_ids(
                index_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.get(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CreateIndex], index, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.vectorize.indexes.with_raw_response.get(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(Optional[CreateIndex], index, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.vectorize.indexes.with_streaming_response.get(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(Optional[CreateIndex], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.get(
                index_name="example-index",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.get(
                index_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get_by_ids(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.get_by_ids(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, index, path=["response"])

    @parametrize
    async def test_method_get_by_ids_with_all_params(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.get_by_ids(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ids=["5121db81354a40c6aedc3fe1ace51c59", "f90eb49c2107486abdfd78c67e853430"],
        )
        assert_matches_type(object, index, path=["response"])

    @parametrize
    async def test_raw_response_get_by_ids(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.vectorize.indexes.with_raw_response.get_by_ids(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(object, index, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_ids(self, async_client: AsyncCloudflare) -> None:
        async with async_client.vectorize.indexes.with_streaming_response.get_by_ids(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(object, index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_ids(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.get_by_ids(
                index_name="example-index",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.get_by_ids(
                index_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_info(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.info(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndexInfoResponse], index, path=["response"])

    @parametrize
    async def test_raw_response_info(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.vectorize.indexes.with_raw_response.info(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(Optional[IndexInfoResponse], index, path=["response"])

    @parametrize
    async def test_streaming_response_info(self, async_client: AsyncCloudflare) -> None:
        async with async_client.vectorize.indexes.with_streaming_response.info(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(Optional[IndexInfoResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_info(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.info(
                index_name="example-index",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.info(
                index_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_insert(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.insert(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="@/path/to/vectors.ndjson",
        )
        assert_matches_type(Optional[IndexInsertResponse], index, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_insert_with_all_params(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.insert(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="@/path/to/vectors.ndjson",
            unparsable_behavior="error",
        )
        assert_matches_type(Optional[IndexInsertResponse], index, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_insert(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.vectorize.indexes.with_raw_response.insert(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="@/path/to/vectors.ndjson",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(Optional[IndexInsertResponse], index, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_insert(self, async_client: AsyncCloudflare) -> None:
        async with async_client.vectorize.indexes.with_streaming_response.insert(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="@/path/to/vectors.ndjson",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(Optional[IndexInsertResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_insert(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.insert(
                index_name="example-index",
                account_id="",
                body="@/path/to/vectors.ndjson",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.insert(
                index_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body="@/path/to/vectors.ndjson",
            )

    @parametrize
    async def test_method_query(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.query(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            vector=[0.5, 0.5, 0.5],
        )
        assert_matches_type(Optional[IndexQueryResponse], index, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.query(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            vector=[0.5, 0.5, 0.5],
            filter={
                "has_viewed": {"$ne": True},
                "streaming_platform": "netflix",
            },
            return_metadata="none",
            return_values=True,
            top_k=5,
        )
        assert_matches_type(Optional[IndexQueryResponse], index, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.vectorize.indexes.with_raw_response.query(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            vector=[0.5, 0.5, 0.5],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(Optional[IndexQueryResponse], index, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncCloudflare) -> None:
        async with async_client.vectorize.indexes.with_streaming_response.query(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            vector=[0.5, 0.5, 0.5],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(Optional[IndexQueryResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_query(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.query(
                index_name="example-index",
                account_id="",
                vector=[0.5, 0.5, 0.5],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.query(
                index_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                vector=[0.5, 0.5, 0.5],
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.upsert(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="@/path/to/vectors.ndjson",
        )
        assert_matches_type(Optional[IndexUpsertResponse], index, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.upsert(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="@/path/to/vectors.ndjson",
            unparsable_behavior="error",
        )
        assert_matches_type(Optional[IndexUpsertResponse], index, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.vectorize.indexes.with_raw_response.upsert(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="@/path/to/vectors.ndjson",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(Optional[IndexUpsertResponse], index, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncCloudflare) -> None:
        async with async_client.vectorize.indexes.with_streaming_response.upsert(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body="@/path/to/vectors.ndjson",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(Optional[IndexUpsertResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.upsert(
                index_name="example-index",
                account_id="",
                body="@/path/to/vectors.ndjson",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.upsert(
                index_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body="@/path/to/vectors.ndjson",
            )
