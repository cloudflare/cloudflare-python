# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.pipelines import (
    PipelineGetResponse,
    PipelineListResponse,
    PipelineCreateResponse,
    PipelineUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPipelines:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        pipeline = client.pipelines.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination={
                "batch": {},
                "compression": {},
                "credentials": {
                    "access_key_id": "<access key id>",
                    "endpoint": "https://123f8a8258064ed892a347f173372359.r2.cloudflarestorage.com",
                    "secret_access_key": "<secret key>",
                },
                "format": "json",
                "path": {"bucket": "bucket"},
                "type": "r2",
            },
            name="sample_pipeline",
            source=[
                {
                    "format": "json",
                    "type": "type",
                }
            ],
        )
        assert_matches_type(PipelineCreateResponse, pipeline, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.pipelines.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination={
                "batch": {},
                "compression": {},
                "credentials": {
                    "access_key_id": "<access key id>",
                    "endpoint": "https://123f8a8258064ed892a347f173372359.r2.cloudflarestorage.com",
                    "secret_access_key": "<secret key>",
                },
                "format": "json",
                "path": {"bucket": "bucket"},
                "type": "r2",
            },
            name="sample_pipeline",
            source=[
                {
                    "format": "json",
                    "type": "type",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(PipelineCreateResponse, pipeline, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.pipelines.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination={
                "batch": {},
                "compression": {},
                "credentials": {
                    "access_key_id": "<access key id>",
                    "endpoint": "https://123f8a8258064ed892a347f173372359.r2.cloudflarestorage.com",
                    "secret_access_key": "<secret key>",
                },
                "format": "json",
                "path": {"bucket": "bucket"},
                "type": "r2",
            },
            name="sample_pipeline",
            source=[
                {
                    "format": "json",
                    "type": "type",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = response.parse()
            assert_matches_type(PipelineCreateResponse, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pipelines.with_raw_response.create(
                account_id="",
                destination={
                    "batch": {},
                    "compression": {},
                    "credentials": {
                        "access_key_id": "<access key id>",
                        "endpoint": "https://123f8a8258064ed892a347f173372359.r2.cloudflarestorage.com",
                        "secret_access_key": "<secret key>",
                    },
                    "format": "json",
                    "path": {"bucket": "bucket"},
                    "type": "r2",
                },
                name="sample_pipeline",
                source=[
                    {
                        "format": "json",
                        "type": "type",
                    }
                ],
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        pipeline = client.pipelines.update(
            pipeline_name="sample_pipeline",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination={
                "batch": {},
                "compression": {},
                "format": "json",
                "path": {"bucket": "bucket"},
                "type": "r2",
            },
            name="sample_pipeline",
            source=[
                {
                    "format": "json",
                    "type": "type",
                }
            ],
        )
        assert_matches_type(PipelineUpdateResponse, pipeline, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        pipeline = client.pipelines.update(
            pipeline_name="sample_pipeline",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination={
                "batch": {
                    "max_bytes": 1000,
                    "max_duration_s": 0.25,
                    "max_rows": 100,
                },
                "compression": {"type": "gzip"},
                "format": "json",
                "path": {
                    "bucket": "bucket",
                    "filename": "${slug}${extension}",
                    "filepath": "${date}/${hour}",
                    "prefix": "base",
                },
                "type": "r2",
                "credentials": {
                    "access_key_id": "<access key id>",
                    "endpoint": "https://123f8a8258064ed892a347f173372359.r2.cloudflarestorage.com",
                    "secret_access_key": "<secret key>",
                },
            },
            name="sample_pipeline",
            source=[
                {
                    "format": "json",
                    "type": "type",
                    "authentication": True,
                    "cors": {"origins": ["*"]},
                }
            ],
        )
        assert_matches_type(PipelineUpdateResponse, pipeline, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.pipelines.with_raw_response.update(
            pipeline_name="sample_pipeline",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination={
                "batch": {},
                "compression": {},
                "format": "json",
                "path": {"bucket": "bucket"},
                "type": "r2",
            },
            name="sample_pipeline",
            source=[
                {
                    "format": "json",
                    "type": "type",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(PipelineUpdateResponse, pipeline, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.pipelines.with_streaming_response.update(
            pipeline_name="sample_pipeline",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination={
                "batch": {},
                "compression": {},
                "format": "json",
                "path": {"bucket": "bucket"},
                "type": "r2",
            },
            name="sample_pipeline",
            source=[
                {
                    "format": "json",
                    "type": "type",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = response.parse()
            assert_matches_type(PipelineUpdateResponse, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pipelines.with_raw_response.update(
                pipeline_name="sample_pipeline",
                account_id="",
                destination={
                    "batch": {},
                    "compression": {},
                    "format": "json",
                    "path": {"bucket": "bucket"},
                    "type": "r2",
                },
                name="sample_pipeline",
                source=[
                    {
                        "format": "json",
                        "type": "type",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_name` but received ''"):
            client.pipelines.with_raw_response.update(
                pipeline_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                destination={
                    "batch": {},
                    "compression": {},
                    "format": "json",
                    "path": {"bucket": "bucket"},
                    "type": "r2",
                },
                name="sample_pipeline",
                source=[
                    {
                        "format": "json",
                        "type": "type",
                    }
                ],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        pipeline = client.pipelines.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PipelineListResponse, pipeline, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        pipeline = client.pipelines.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page="page",
            per_page="per_page",
            search="search",
        )
        assert_matches_type(PipelineListResponse, pipeline, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.pipelines.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(PipelineListResponse, pipeline, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.pipelines.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = response.parse()
            assert_matches_type(PipelineListResponse, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pipelines.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        pipeline = client.pipelines.delete(
            pipeline_name="sample_pipeline",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert pipeline is None

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.pipelines.with_raw_response.delete(
            pipeline_name="sample_pipeline",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert pipeline is None

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.pipelines.with_streaming_response.delete(
            pipeline_name="sample_pipeline",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = response.parse()
            assert pipeline is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pipelines.with_raw_response.delete(
                pipeline_name="sample_pipeline",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_name` but received ''"):
            client.pipelines.with_raw_response.delete(
                pipeline_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        pipeline = client.pipelines.get(
            pipeline_name="sample_pipeline",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PipelineGetResponse, pipeline, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.pipelines.with_raw_response.get(
            pipeline_name="sample_pipeline",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(PipelineGetResponse, pipeline, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.pipelines.with_streaming_response.get(
            pipeline_name="sample_pipeline",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = response.parse()
            assert_matches_type(PipelineGetResponse, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pipelines.with_raw_response.get(
                pipeline_name="sample_pipeline",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_name` but received ''"):
            client.pipelines.with_raw_response.get(
                pipeline_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncPipelines:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        pipeline = await async_client.pipelines.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination={
                "batch": {},
                "compression": {},
                "credentials": {
                    "access_key_id": "<access key id>",
                    "endpoint": "https://123f8a8258064ed892a347f173372359.r2.cloudflarestorage.com",
                    "secret_access_key": "<secret key>",
                },
                "format": "json",
                "path": {"bucket": "bucket"},
                "type": "r2",
            },
            name="sample_pipeline",
            source=[
                {
                    "format": "json",
                    "type": "type",
                }
            ],
        )
        assert_matches_type(PipelineCreateResponse, pipeline, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pipelines.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination={
                "batch": {},
                "compression": {},
                "credentials": {
                    "access_key_id": "<access key id>",
                    "endpoint": "https://123f8a8258064ed892a347f173372359.r2.cloudflarestorage.com",
                    "secret_access_key": "<secret key>",
                },
                "format": "json",
                "path": {"bucket": "bucket"},
                "type": "r2",
            },
            name="sample_pipeline",
            source=[
                {
                    "format": "json",
                    "type": "type",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(PipelineCreateResponse, pipeline, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pipelines.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination={
                "batch": {},
                "compression": {},
                "credentials": {
                    "access_key_id": "<access key id>",
                    "endpoint": "https://123f8a8258064ed892a347f173372359.r2.cloudflarestorage.com",
                    "secret_access_key": "<secret key>",
                },
                "format": "json",
                "path": {"bucket": "bucket"},
                "type": "r2",
            },
            name="sample_pipeline",
            source=[
                {
                    "format": "json",
                    "type": "type",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = await response.parse()
            assert_matches_type(PipelineCreateResponse, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pipelines.with_raw_response.create(
                account_id="",
                destination={
                    "batch": {},
                    "compression": {},
                    "credentials": {
                        "access_key_id": "<access key id>",
                        "endpoint": "https://123f8a8258064ed892a347f173372359.r2.cloudflarestorage.com",
                        "secret_access_key": "<secret key>",
                    },
                    "format": "json",
                    "path": {"bucket": "bucket"},
                    "type": "r2",
                },
                name="sample_pipeline",
                source=[
                    {
                        "format": "json",
                        "type": "type",
                    }
                ],
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        pipeline = await async_client.pipelines.update(
            pipeline_name="sample_pipeline",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination={
                "batch": {},
                "compression": {},
                "format": "json",
                "path": {"bucket": "bucket"},
                "type": "r2",
            },
            name="sample_pipeline",
            source=[
                {
                    "format": "json",
                    "type": "type",
                }
            ],
        )
        assert_matches_type(PipelineUpdateResponse, pipeline, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        pipeline = await async_client.pipelines.update(
            pipeline_name="sample_pipeline",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination={
                "batch": {
                    "max_bytes": 1000,
                    "max_duration_s": 0.25,
                    "max_rows": 100,
                },
                "compression": {"type": "gzip"},
                "format": "json",
                "path": {
                    "bucket": "bucket",
                    "filename": "${slug}${extension}",
                    "filepath": "${date}/${hour}",
                    "prefix": "base",
                },
                "type": "r2",
                "credentials": {
                    "access_key_id": "<access key id>",
                    "endpoint": "https://123f8a8258064ed892a347f173372359.r2.cloudflarestorage.com",
                    "secret_access_key": "<secret key>",
                },
            },
            name="sample_pipeline",
            source=[
                {
                    "format": "json",
                    "type": "type",
                    "authentication": True,
                    "cors": {"origins": ["*"]},
                }
            ],
        )
        assert_matches_type(PipelineUpdateResponse, pipeline, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pipelines.with_raw_response.update(
            pipeline_name="sample_pipeline",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination={
                "batch": {},
                "compression": {},
                "format": "json",
                "path": {"bucket": "bucket"},
                "type": "r2",
            },
            name="sample_pipeline",
            source=[
                {
                    "format": "json",
                    "type": "type",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(PipelineUpdateResponse, pipeline, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pipelines.with_streaming_response.update(
            pipeline_name="sample_pipeline",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            destination={
                "batch": {},
                "compression": {},
                "format": "json",
                "path": {"bucket": "bucket"},
                "type": "r2",
            },
            name="sample_pipeline",
            source=[
                {
                    "format": "json",
                    "type": "type",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = await response.parse()
            assert_matches_type(PipelineUpdateResponse, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pipelines.with_raw_response.update(
                pipeline_name="sample_pipeline",
                account_id="",
                destination={
                    "batch": {},
                    "compression": {},
                    "format": "json",
                    "path": {"bucket": "bucket"},
                    "type": "r2",
                },
                name="sample_pipeline",
                source=[
                    {
                        "format": "json",
                        "type": "type",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_name` but received ''"):
            await async_client.pipelines.with_raw_response.update(
                pipeline_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                destination={
                    "batch": {},
                    "compression": {},
                    "format": "json",
                    "path": {"bucket": "bucket"},
                    "type": "r2",
                },
                name="sample_pipeline",
                source=[
                    {
                        "format": "json",
                        "type": "type",
                    }
                ],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        pipeline = await async_client.pipelines.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PipelineListResponse, pipeline, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        pipeline = await async_client.pipelines.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page="page",
            per_page="per_page",
            search="search",
        )
        assert_matches_type(PipelineListResponse, pipeline, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pipelines.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(PipelineListResponse, pipeline, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pipelines.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = await response.parse()
            assert_matches_type(PipelineListResponse, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pipelines.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        pipeline = await async_client.pipelines.delete(
            pipeline_name="sample_pipeline",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert pipeline is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pipelines.with_raw_response.delete(
            pipeline_name="sample_pipeline",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert pipeline is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pipelines.with_streaming_response.delete(
            pipeline_name="sample_pipeline",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = await response.parse()
            assert pipeline is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pipelines.with_raw_response.delete(
                pipeline_name="sample_pipeline",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_name` but received ''"):
            await async_client.pipelines.with_raw_response.delete(
                pipeline_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        pipeline = await async_client.pipelines.get(
            pipeline_name="sample_pipeline",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PipelineGetResponse, pipeline, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pipelines.with_raw_response.get(
            pipeline_name="sample_pipeline",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(PipelineGetResponse, pipeline, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pipelines.with_streaming_response.get(
            pipeline_name="sample_pipeline",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pipeline = await response.parse()
            assert_matches_type(PipelineGetResponse, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pipelines.with_raw_response.get(
                pipeline_name="sample_pipeline",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_name` but received ''"):
            await async_client.pipelines.with_raw_response.get(
                pipeline_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
