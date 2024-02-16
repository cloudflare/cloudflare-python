# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.vectorize import (
    IndexCreateResponse,
    IndexUpdateResponse,
    IndexListResponse,
    IndexDeleteResponse,
    IndexDeleteByIDsResponse,
    IndexGetResponse,
    IndexInsertResponse,
    IndexQueryResponse,
    IndexUpsertResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.vectorize import index_create_params
from cloudflare.types.vectorize import index_update_params
from cloudflare.types.vectorize import index_delete_by_ids_params
from cloudflare.types.vectorize import index_get_by_ids_params
from cloudflare.types.vectorize import index_query_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIndexes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            config={"preset": "@cf/baai/bge-small-en-v1.5"},
            name="example-index",
        )
        assert_matches_type(Optional[IndexCreateResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            config={"preset": "@cf/baai/bge-small-en-v1.5"},
            name="example-index",
            description="This is my example index.",
        )
        assert_matches_type(Optional[IndexCreateResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.vectorize.indexes.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            config={"preset": "@cf/baai/bge-small-en-v1.5"},
            name="example-index",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(Optional[IndexCreateResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.vectorize.indexes.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            config={"preset": "@cf/baai/bge-small-en-v1.5"},
            name="example-index",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(Optional[IndexCreateResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.vectorize.indexes.with_raw_response.create(
                "",
                config={"preset": "@cf/baai/bge-small-en-v1.5"},
                name="example-index",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.update(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            description="This is my example index.",
        )
        assert_matches_type(Optional[IndexUpdateResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.vectorize.indexes.with_raw_response.update(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            description="This is my example index.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(Optional[IndexUpdateResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.vectorize.indexes.with_streaming_response.update(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            description="This is my example index.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(Optional[IndexUpdateResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.vectorize.indexes.with_raw_response.update(
                "example-index",
                account_identifier="",
                description="This is my example index.",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            client.vectorize.indexes.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                description="This is my example index.",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IndexListResponse, index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.vectorize.indexes.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(IndexListResponse, index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.vectorize.indexes.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(IndexListResponse, index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.vectorize.indexes.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.delete(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndexDeleteResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.vectorize.indexes.with_raw_response.delete(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(Optional[IndexDeleteResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.vectorize.indexes.with_streaming_response.delete(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(Optional[IndexDeleteResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.vectorize.indexes.with_raw_response.delete(
                "example-index",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            client.vectorize.indexes.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_by_ids(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.delete_by_ids(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndexDeleteByIDsResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_by_ids_with_all_params(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.delete_by_ids(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            ids=["5121db81354a40c6aedc3fe1ace51c59", "f90eb49c2107486abdfd78c67e853430"],
        )
        assert_matches_type(Optional[IndexDeleteByIDsResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete_by_ids(self, client: Cloudflare) -> None:
        response = client.vectorize.indexes.with_raw_response.delete_by_ids(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(Optional[IndexDeleteByIDsResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete_by_ids(self, client: Cloudflare) -> None:
        with client.vectorize.indexes.with_streaming_response.delete_by_ids(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(Optional[IndexDeleteByIDsResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete_by_ids(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.vectorize.indexes.with_raw_response.delete_by_ids(
                "example-index",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            client.vectorize.indexes.with_raw_response.delete_by_ids(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.get(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndexGetResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.vectorize.indexes.with_raw_response.get(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(Optional[IndexGetResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.vectorize.indexes.with_streaming_response.get(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(Optional[IndexGetResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.vectorize.indexes.with_raw_response.get(
                "example-index",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            client.vectorize.indexes.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get_by_ids(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.get_by_ids(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_by_ids_with_all_params(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.get_by_ids(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            ids=["5121db81354a40c6aedc3fe1ace51c59", "f90eb49c2107486abdfd78c67e853430"],
        )
        assert_matches_type(object, index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_by_ids(self, client: Cloudflare) -> None:
        response = client.vectorize.indexes.with_raw_response.get_by_ids(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(object, index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_by_ids(self, client: Cloudflare) -> None:
        with client.vectorize.indexes.with_streaming_response.get_by_ids(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(object, index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_by_ids(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.vectorize.indexes.with_raw_response.get_by_ids(
                "example-index",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            client.vectorize.indexes.with_raw_response.get_by_ids(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_insert(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.insert(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndexInsertResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_insert(self, client: Cloudflare) -> None:
        response = client.vectorize.indexes.with_raw_response.insert(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(Optional[IndexInsertResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_insert(self, client: Cloudflare) -> None:
        with client.vectorize.indexes.with_streaming_response.insert(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(Optional[IndexInsertResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_insert(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.vectorize.indexes.with_raw_response.insert(
                "example-index",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            client.vectorize.indexes.with_raw_response.insert(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_query(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.query(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndexQueryResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_query_with_all_params(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.query(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            return_metadata=True,
            return_values=True,
            top_k=5,
            vector=[0.5, 0.5, 0.5],
        )
        assert_matches_type(Optional[IndexQueryResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_query(self, client: Cloudflare) -> None:
        response = client.vectorize.indexes.with_raw_response.query(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(Optional[IndexQueryResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_query(self, client: Cloudflare) -> None:
        with client.vectorize.indexes.with_streaming_response.query(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(Optional[IndexQueryResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_query(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.vectorize.indexes.with_raw_response.query(
                "example-index",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            client.vectorize.indexes.with_raw_response.query(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_upsert(self, client: Cloudflare) -> None:
        index = client.vectorize.indexes.upsert(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndexUpsertResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_upsert(self, client: Cloudflare) -> None:
        response = client.vectorize.indexes.with_raw_response.upsert(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(Optional[IndexUpsertResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_upsert(self, client: Cloudflare) -> None:
        with client.vectorize.indexes.with_streaming_response.upsert(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(Optional[IndexUpsertResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_upsert(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.vectorize.indexes.with_raw_response.upsert(
                "example-index",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            client.vectorize.indexes.with_raw_response.upsert(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncIndexes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            config={"preset": "@cf/baai/bge-small-en-v1.5"},
            name="example-index",
        )
        assert_matches_type(Optional[IndexCreateResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            config={"preset": "@cf/baai/bge-small-en-v1.5"},
            name="example-index",
            description="This is my example index.",
        )
        assert_matches_type(Optional[IndexCreateResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.vectorize.indexes.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            config={"preset": "@cf/baai/bge-small-en-v1.5"},
            name="example-index",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(Optional[IndexCreateResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.vectorize.indexes.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            config={"preset": "@cf/baai/bge-small-en-v1.5"},
            name="example-index",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(Optional[IndexCreateResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.create(
                "",
                config={"preset": "@cf/baai/bge-small-en-v1.5"},
                name="example-index",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.update(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            description="This is my example index.",
        )
        assert_matches_type(Optional[IndexUpdateResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.vectorize.indexes.with_raw_response.update(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            description="This is my example index.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(Optional[IndexUpdateResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.vectorize.indexes.with_streaming_response.update(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            description="This is my example index.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(Optional[IndexUpdateResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.update(
                "example-index",
                account_identifier="",
                description="This is my example index.",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                description="This is my example index.",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IndexListResponse, index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.vectorize.indexes.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(IndexListResponse, index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.vectorize.indexes.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(IndexListResponse, index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.delete(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndexDeleteResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.vectorize.indexes.with_raw_response.delete(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(Optional[IndexDeleteResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.vectorize.indexes.with_streaming_response.delete(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(Optional[IndexDeleteResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.delete(
                "example-index",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_by_ids(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.delete_by_ids(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndexDeleteByIDsResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_by_ids_with_all_params(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.delete_by_ids(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            ids=["5121db81354a40c6aedc3fe1ace51c59", "f90eb49c2107486abdfd78c67e853430"],
        )
        assert_matches_type(Optional[IndexDeleteByIDsResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete_by_ids(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.vectorize.indexes.with_raw_response.delete_by_ids(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(Optional[IndexDeleteByIDsResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete_by_ids(self, async_client: AsyncCloudflare) -> None:
        async with async_client.vectorize.indexes.with_streaming_response.delete_by_ids(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(Optional[IndexDeleteByIDsResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete_by_ids(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.delete_by_ids(
                "example-index",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.delete_by_ids(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.get(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndexGetResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.vectorize.indexes.with_raw_response.get(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(Optional[IndexGetResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.vectorize.indexes.with_streaming_response.get(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(Optional[IndexGetResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.get(
                "example-index",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_by_ids(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.get_by_ids(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_by_ids_with_all_params(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.get_by_ids(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            ids=["5121db81354a40c6aedc3fe1ace51c59", "f90eb49c2107486abdfd78c67e853430"],
        )
        assert_matches_type(object, index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_by_ids(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.vectorize.indexes.with_raw_response.get_by_ids(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(object, index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_by_ids(self, async_client: AsyncCloudflare) -> None:
        async with async_client.vectorize.indexes.with_streaming_response.get_by_ids(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(object, index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_by_ids(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.get_by_ids(
                "example-index",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.get_by_ids(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_insert(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.insert(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndexInsertResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_insert(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.vectorize.indexes.with_raw_response.insert(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(Optional[IndexInsertResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_insert(self, async_client: AsyncCloudflare) -> None:
        async with async_client.vectorize.indexes.with_streaming_response.insert(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(Optional[IndexInsertResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_insert(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.insert(
                "example-index",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.insert(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_query(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.query(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndexQueryResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.query(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            return_metadata=True,
            return_values=True,
            top_k=5,
            vector=[0.5, 0.5, 0.5],
        )
        assert_matches_type(Optional[IndexQueryResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_query(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.vectorize.indexes.with_raw_response.query(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(Optional[IndexQueryResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncCloudflare) -> None:
        async with async_client.vectorize.indexes.with_streaming_response.query(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(Optional[IndexQueryResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_query(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.query(
                "example-index",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.query(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_upsert(self, async_client: AsyncCloudflare) -> None:
        index = await async_client.vectorize.indexes.upsert(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndexUpsertResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.vectorize.indexes.with_raw_response.upsert(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(Optional[IndexUpsertResponse], index, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncCloudflare) -> None:
        async with async_client.vectorize.indexes.with_streaming_response.upsert(
            "example-index",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(Optional[IndexUpsertResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_upsert(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.upsert(
                "example-index",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            await async_client.vectorize.indexes.with_raw_response.upsert(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )
