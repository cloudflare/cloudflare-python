# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.pages import Project, Deployment

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        project = client.pages.projects.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        project = client.pages.projects.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            build_config={
                "build_caching": True,
                "build_command": "npm run build",
                "destination_dir": "build",
                "root_dir": "/",
                "web_analytics_tag": "cee1c73f6e4743d0b5e6bb1a0bcaabcc",
                "web_analytics_token": "021e1057c18547eca7b79f2516f06o7x",
            },
            deployment_configs={
                "preview": {
                    "ai_bindings": {"AI_BINDING": {"project_id": "some-project-id"}},
                    "analytics_engine_datasets": {"ANALYTICS_ENGINE_BINDING": {"dataset": "api_analytics"}},
                    "browsers": {"BROWSER": {}},
                    "compatibility_date": "2022-01-01",
                    "compatibility_flags": ["url_standard"],
                    "d1_databases": {"D1_BINDING": {"id": "445e2955-951a-43f8-a35b-a4d0c8138f63"}},
                    "durable_object_namespaces": {"DO_BINDING": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "env_vars": {
                        "foo": {
                            "type": "plain_text",
                            "value": "hello world",
                        }
                    },
                    "hyperdrive_bindings": {"HYPERDRIVE": {"id": "a76a99bc342644deb02c38d66082262a"}},
                    "kv_namespaces": {"KV_BINDING": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "mtls_certificates": {"MTLS": {"certificate_id": "d7cdd17c-916f-4cb7-aabe-585eb382ec4e"}},
                    "placement": {"mode": "smart"},
                    "queue_producers": {"QUEUE_PRODUCER_BINDING": {"name": "some-queue"}},
                    "r2_buckets": {
                        "R2_BINDING": {
                            "jurisdiction": "eu",
                            "name": "some-bucket",
                        }
                    },
                    "services": {
                        "SERVICE_BINDING": {
                            "entrypoint": "MyHandler",
                            "environment": "production",
                            "service": "example-worker",
                        }
                    },
                    "vectorize_bindings": {"VECTORIZE": {"index_name": "my_index"}},
                },
                "production": {
                    "ai_bindings": {"AI_BINDING": {"project_id": "some-project-id"}},
                    "analytics_engine_datasets": {"ANALYTICS_ENGINE_BINDING": {"dataset": "api_analytics"}},
                    "browsers": {"BROWSER": {}},
                    "compatibility_date": "2022-01-01",
                    "compatibility_flags": ["url_standard"],
                    "d1_databases": {"D1_BINDING": {"id": "445e2955-951a-43f8-a35b-a4d0c8138f63"}},
                    "durable_object_namespaces": {"DO_BINDING": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "env_vars": {
                        "foo": {
                            "type": "plain_text",
                            "value": "hello world",
                        }
                    },
                    "hyperdrive_bindings": {"HYPERDRIVE": {"id": "a76a99bc342644deb02c38d66082262a"}},
                    "kv_namespaces": {"KV_BINDING": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "mtls_certificates": {"MTLS": {"certificate_id": "d7cdd17c-916f-4cb7-aabe-585eb382ec4e"}},
                    "placement": {"mode": "smart"},
                    "queue_producers": {"QUEUE_PRODUCER_BINDING": {"name": "some-queue"}},
                    "r2_buckets": {
                        "R2_BINDING": {
                            "jurisdiction": "eu",
                            "name": "some-bucket",
                        }
                    },
                    "services": {
                        "SERVICE_BINDING": {
                            "entrypoint": "MyHandler",
                            "environment": "production",
                            "service": "example-worker",
                        }
                    },
                    "vectorize_bindings": {"VECTORIZE": {"index_name": "my_index"}},
                },
            },
            name="NextJS Blog",
            production_branch="main",
        )
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.pages.projects.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.pages.projects.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.with_raw_response.create(
                account_id="",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        project = client.pages.projects.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[Deployment], project, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.pages.projects.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(SyncSinglePage[Deployment], project, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.pages.projects.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(SyncSinglePage[Deployment], project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        project = client.pages.projects.delete(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, project, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.pages.projects.with_raw_response.delete(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(object, project, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.pages.projects.with_streaming_response.delete(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(object, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.with_raw_response.delete(
                project_name="this-is-my-project-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            client.pages.projects.with_raw_response.delete(
                project_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        project = client.pages.projects.edit(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        project = client.pages.projects.edit(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            build_config={
                "build_caching": True,
                "build_command": "npm run build",
                "destination_dir": "build",
                "root_dir": "/",
                "web_analytics_tag": "cee1c73f6e4743d0b5e6bb1a0bcaabcc",
                "web_analytics_token": "021e1057c18547eca7b79f2516f06o7x",
            },
            deployment_configs={
                "preview": {
                    "ai_bindings": {"AI_BINDING": {"project_id": "some-project-id"}},
                    "analytics_engine_datasets": {"ANALYTICS_ENGINE_BINDING": {"dataset": "api_analytics"}},
                    "browsers": {"BROWSER": {}},
                    "compatibility_date": "2022-01-01",
                    "compatibility_flags": ["url_standard"],
                    "d1_databases": {"D1_BINDING": {"id": "445e2955-951a-43f8-a35b-a4d0c8138f63"}},
                    "durable_object_namespaces": {"DO_BINDING": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "env_vars": {
                        "foo": {
                            "type": "plain_text",
                            "value": "hello world",
                        }
                    },
                    "hyperdrive_bindings": {"HYPERDRIVE": {"id": "a76a99bc342644deb02c38d66082262a"}},
                    "kv_namespaces": {"KV_BINDING": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "mtls_certificates": {"MTLS": {"certificate_id": "d7cdd17c-916f-4cb7-aabe-585eb382ec4e"}},
                    "placement": {"mode": "smart"},
                    "queue_producers": {"QUEUE_PRODUCER_BINDING": {"name": "some-queue"}},
                    "r2_buckets": {
                        "R2_BINDING": {
                            "jurisdiction": "eu",
                            "name": "some-bucket",
                        }
                    },
                    "services": {
                        "SERVICE_BINDING": {
                            "entrypoint": "MyHandler",
                            "environment": "production",
                            "service": "example-worker",
                        }
                    },
                    "vectorize_bindings": {"VECTORIZE": {"index_name": "my_index"}},
                },
                "production": {
                    "ai_bindings": {"AI_BINDING": {"project_id": "some-project-id"}},
                    "analytics_engine_datasets": {"ANALYTICS_ENGINE_BINDING": {"dataset": "api_analytics"}},
                    "browsers": {"BROWSER": {}},
                    "compatibility_date": "2022-01-01",
                    "compatibility_flags": ["url_standard"],
                    "d1_databases": {"D1_BINDING": {"id": "445e2955-951a-43f8-a35b-a4d0c8138f63"}},
                    "durable_object_namespaces": {"DO_BINDING": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "env_vars": {
                        "foo": {
                            "type": "plain_text",
                            "value": "hello world",
                        }
                    },
                    "hyperdrive_bindings": {"HYPERDRIVE": {"id": "a76a99bc342644deb02c38d66082262a"}},
                    "kv_namespaces": {"KV_BINDING": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "mtls_certificates": {"MTLS": {"certificate_id": "d7cdd17c-916f-4cb7-aabe-585eb382ec4e"}},
                    "placement": {"mode": "smart"},
                    "queue_producers": {"QUEUE_PRODUCER_BINDING": {"name": "some-queue"}},
                    "r2_buckets": {
                        "R2_BINDING": {
                            "jurisdiction": "eu",
                            "name": "some-bucket",
                        }
                    },
                    "services": {
                        "SERVICE_BINDING": {
                            "entrypoint": "MyHandler",
                            "environment": "production",
                            "service": "example-worker",
                        }
                    },
                    "vectorize_bindings": {"VECTORIZE": {"index_name": "my_index"}},
                },
            },
            name="NextJS Blog",
            production_branch="main",
        )
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.pages.projects.with_raw_response.edit(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.pages.projects.with_streaming_response.edit(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.with_raw_response.edit(
                project_name="this-is-my-project-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            client.pages.projects.with_raw_response.edit(
                project_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        project = client.pages.projects.get(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.pages.projects.with_raw_response.get(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.pages.projects.with_streaming_response.get(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.with_raw_response.get(
                project_name="this-is-my-project-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            client.pages.projects.with_raw_response.get(
                project_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_purge_build_cache(self, client: Cloudflare) -> None:
        project = client.pages.projects.purge_build_cache(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, project, path=["response"])

    @parametrize
    def test_raw_response_purge_build_cache(self, client: Cloudflare) -> None:
        response = client.pages.projects.with_raw_response.purge_build_cache(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(object, project, path=["response"])

    @parametrize
    def test_streaming_response_purge_build_cache(self, client: Cloudflare) -> None:
        with client.pages.projects.with_streaming_response.purge_build_cache(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(object, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_purge_build_cache(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pages.projects.with_raw_response.purge_build_cache(
                project_name="this-is-my-project-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            client.pages.projects.with_raw_response.purge_build_cache(
                project_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncProjects:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        project = await async_client.pages.projects.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        project = await async_client.pages.projects.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            build_config={
                "build_caching": True,
                "build_command": "npm run build",
                "destination_dir": "build",
                "root_dir": "/",
                "web_analytics_tag": "cee1c73f6e4743d0b5e6bb1a0bcaabcc",
                "web_analytics_token": "021e1057c18547eca7b79f2516f06o7x",
            },
            deployment_configs={
                "preview": {
                    "ai_bindings": {"AI_BINDING": {"project_id": "some-project-id"}},
                    "analytics_engine_datasets": {"ANALYTICS_ENGINE_BINDING": {"dataset": "api_analytics"}},
                    "browsers": {"BROWSER": {}},
                    "compatibility_date": "2022-01-01",
                    "compatibility_flags": ["url_standard"],
                    "d1_databases": {"D1_BINDING": {"id": "445e2955-951a-43f8-a35b-a4d0c8138f63"}},
                    "durable_object_namespaces": {"DO_BINDING": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "env_vars": {
                        "foo": {
                            "type": "plain_text",
                            "value": "hello world",
                        }
                    },
                    "hyperdrive_bindings": {"HYPERDRIVE": {"id": "a76a99bc342644deb02c38d66082262a"}},
                    "kv_namespaces": {"KV_BINDING": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "mtls_certificates": {"MTLS": {"certificate_id": "d7cdd17c-916f-4cb7-aabe-585eb382ec4e"}},
                    "placement": {"mode": "smart"},
                    "queue_producers": {"QUEUE_PRODUCER_BINDING": {"name": "some-queue"}},
                    "r2_buckets": {
                        "R2_BINDING": {
                            "jurisdiction": "eu",
                            "name": "some-bucket",
                        }
                    },
                    "services": {
                        "SERVICE_BINDING": {
                            "entrypoint": "MyHandler",
                            "environment": "production",
                            "service": "example-worker",
                        }
                    },
                    "vectorize_bindings": {"VECTORIZE": {"index_name": "my_index"}},
                },
                "production": {
                    "ai_bindings": {"AI_BINDING": {"project_id": "some-project-id"}},
                    "analytics_engine_datasets": {"ANALYTICS_ENGINE_BINDING": {"dataset": "api_analytics"}},
                    "browsers": {"BROWSER": {}},
                    "compatibility_date": "2022-01-01",
                    "compatibility_flags": ["url_standard"],
                    "d1_databases": {"D1_BINDING": {"id": "445e2955-951a-43f8-a35b-a4d0c8138f63"}},
                    "durable_object_namespaces": {"DO_BINDING": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "env_vars": {
                        "foo": {
                            "type": "plain_text",
                            "value": "hello world",
                        }
                    },
                    "hyperdrive_bindings": {"HYPERDRIVE": {"id": "a76a99bc342644deb02c38d66082262a"}},
                    "kv_namespaces": {"KV_BINDING": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "mtls_certificates": {"MTLS": {"certificate_id": "d7cdd17c-916f-4cb7-aabe-585eb382ec4e"}},
                    "placement": {"mode": "smart"},
                    "queue_producers": {"QUEUE_PRODUCER_BINDING": {"name": "some-queue"}},
                    "r2_buckets": {
                        "R2_BINDING": {
                            "jurisdiction": "eu",
                            "name": "some-bucket",
                        }
                    },
                    "services": {
                        "SERVICE_BINDING": {
                            "entrypoint": "MyHandler",
                            "environment": "production",
                            "service": "example-worker",
                        }
                    },
                    "vectorize_bindings": {"VECTORIZE": {"index_name": "my_index"}},
                },
            },
            name="NextJS Blog",
            production_branch="main",
        )
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pages.projects.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pages.projects.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.with_raw_response.create(
                account_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        project = await async_client.pages.projects.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[Deployment], project, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pages.projects.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(AsyncSinglePage[Deployment], project, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pages.projects.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(AsyncSinglePage[Deployment], project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        project = await async_client.pages.projects.delete(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, project, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pages.projects.with_raw_response.delete(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(object, project, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pages.projects.with_streaming_response.delete(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(object, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.with_raw_response.delete(
                project_name="this-is-my-project-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            await async_client.pages.projects.with_raw_response.delete(
                project_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        project = await async_client.pages.projects.edit(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        project = await async_client.pages.projects.edit(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            build_config={
                "build_caching": True,
                "build_command": "npm run build",
                "destination_dir": "build",
                "root_dir": "/",
                "web_analytics_tag": "cee1c73f6e4743d0b5e6bb1a0bcaabcc",
                "web_analytics_token": "021e1057c18547eca7b79f2516f06o7x",
            },
            deployment_configs={
                "preview": {
                    "ai_bindings": {"AI_BINDING": {"project_id": "some-project-id"}},
                    "analytics_engine_datasets": {"ANALYTICS_ENGINE_BINDING": {"dataset": "api_analytics"}},
                    "browsers": {"BROWSER": {}},
                    "compatibility_date": "2022-01-01",
                    "compatibility_flags": ["url_standard"],
                    "d1_databases": {"D1_BINDING": {"id": "445e2955-951a-43f8-a35b-a4d0c8138f63"}},
                    "durable_object_namespaces": {"DO_BINDING": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "env_vars": {
                        "foo": {
                            "type": "plain_text",
                            "value": "hello world",
                        }
                    },
                    "hyperdrive_bindings": {"HYPERDRIVE": {"id": "a76a99bc342644deb02c38d66082262a"}},
                    "kv_namespaces": {"KV_BINDING": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "mtls_certificates": {"MTLS": {"certificate_id": "d7cdd17c-916f-4cb7-aabe-585eb382ec4e"}},
                    "placement": {"mode": "smart"},
                    "queue_producers": {"QUEUE_PRODUCER_BINDING": {"name": "some-queue"}},
                    "r2_buckets": {
                        "R2_BINDING": {
                            "jurisdiction": "eu",
                            "name": "some-bucket",
                        }
                    },
                    "services": {
                        "SERVICE_BINDING": {
                            "entrypoint": "MyHandler",
                            "environment": "production",
                            "service": "example-worker",
                        }
                    },
                    "vectorize_bindings": {"VECTORIZE": {"index_name": "my_index"}},
                },
                "production": {
                    "ai_bindings": {"AI_BINDING": {"project_id": "some-project-id"}},
                    "analytics_engine_datasets": {"ANALYTICS_ENGINE_BINDING": {"dataset": "api_analytics"}},
                    "browsers": {"BROWSER": {}},
                    "compatibility_date": "2022-01-01",
                    "compatibility_flags": ["url_standard"],
                    "d1_databases": {"D1_BINDING": {"id": "445e2955-951a-43f8-a35b-a4d0c8138f63"}},
                    "durable_object_namespaces": {"DO_BINDING": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "env_vars": {
                        "foo": {
                            "type": "plain_text",
                            "value": "hello world",
                        }
                    },
                    "hyperdrive_bindings": {"HYPERDRIVE": {"id": "a76a99bc342644deb02c38d66082262a"}},
                    "kv_namespaces": {"KV_BINDING": {"namespace_id": "5eb63bbbe01eeed093cb22bb8f5acdc3"}},
                    "mtls_certificates": {"MTLS": {"certificate_id": "d7cdd17c-916f-4cb7-aabe-585eb382ec4e"}},
                    "placement": {"mode": "smart"},
                    "queue_producers": {"QUEUE_PRODUCER_BINDING": {"name": "some-queue"}},
                    "r2_buckets": {
                        "R2_BINDING": {
                            "jurisdiction": "eu",
                            "name": "some-bucket",
                        }
                    },
                    "services": {
                        "SERVICE_BINDING": {
                            "entrypoint": "MyHandler",
                            "environment": "production",
                            "service": "example-worker",
                        }
                    },
                    "vectorize_bindings": {"VECTORIZE": {"index_name": "my_index"}},
                },
            },
            name="NextJS Blog",
            production_branch="main",
        )
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pages.projects.with_raw_response.edit(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pages.projects.with_streaming_response.edit(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.with_raw_response.edit(
                project_name="this-is-my-project-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            await async_client.pages.projects.with_raw_response.edit(
                project_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        project = await async_client.pages.projects.get(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pages.projects.with_raw_response.get(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(Project, project, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pages.projects.with_streaming_response.get(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(Project, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.with_raw_response.get(
                project_name="this-is-my-project-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            await async_client.pages.projects.with_raw_response.get(
                project_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_purge_build_cache(self, async_client: AsyncCloudflare) -> None:
        project = await async_client.pages.projects.purge_build_cache(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, project, path=["response"])

    @parametrize
    async def test_raw_response_purge_build_cache(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pages.projects.with_raw_response.purge_build_cache(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(object, project, path=["response"])

    @parametrize
    async def test_streaming_response_purge_build_cache(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pages.projects.with_streaming_response.purge_build_cache(
            project_name="this-is-my-project-01",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(object, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_purge_build_cache(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pages.projects.with_raw_response.purge_build_cache(
                project_name="this-is-my-project-01",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_name` but received ''"):
            await async_client.pages.projects.with_raw_response.purge_build_cache(
                project_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
