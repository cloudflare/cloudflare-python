from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.workers import ScriptUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScriptUpload:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: Prism multipart/form-data validation incompatible with SDK encoding")
    @parametrize
    def test_basic_script_upload(self, client: Cloudflare) -> None:
        script_content = """
        export default {
            async fetch(request, env, ctx) {
                return new Response(env.MESSAGE, { status: 200 });
            }
        };
        """

        script = client.workers.scripts.update(
            "my-hello-world-script",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={
                "main_module": "my-hello-world-script.mjs",
                "bindings": [
                    {
                        "type": "plain_text",
                        "name": "MESSAGE",
                        "text": "Hello World!",
                    }
                ],
            },
            files={
                "my-hello-world-script.mjs": (
                    "my-hello-world-script.mjs",
                    bytes(script_content, "utf-8"),
                    "application/javascript+module",
                )
            },
        )
        assert_matches_type(ScriptUpdateResponse, script, path=["response"])

    @pytest.mark.skip(reason="TODO: Prism multipart/form-data validation incompatible with SDK encoding")
    @parametrize
    def test_script_upload_with_multiple_files(self, client: Cloudflare) -> None:
        main_script = """
        import { helper } from './helper.js';
        export default {
            async fetch(request, env, ctx) {
                return new Response(helper(), { status: 200 });
            }
        };
        """

        helper_script = """
        export function helper() {
            return 'Hello from helper!';
        }
        """

        script = client.workers.scripts.update(
            "multi-file-script",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={
                "main_module": "index.mjs",
            },
            files={
                "index.mjs": (
                    "index.mjs",
                    bytes(main_script, "utf-8"),
                    "application/javascript+module",
                ),
                "helper.js": (
                    "helper.js",
                    bytes(helper_script, "utf-8"),
                    "application/javascript+module",
                ),
            },
        )
        assert_matches_type(ScriptUpdateResponse, script, path=["response"])

    @pytest.mark.skip(reason="TODO: Prism multipart/form-data validation incompatible with SDK encoding")
    @parametrize
    def test_script_upload_with_bindings(self, client: Cloudflare) -> None:
        script_content = """
        export default {
            async fetch(request, env, ctx) {
                const value = await env.MY_KV.get('key');
                return new Response(value || env.MESSAGE, { status: 200 });
            }
        };
        """

        script = client.workers.scripts.update(
            "script-with-bindings",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={
                "main_module": "worker.mjs",
                "bindings": [
                    {
                        "type": "plain_text",
                        "name": "MESSAGE",
                        "text": "Default message",
                    },
                    {
                        "type": "kv_namespace",
                        "name": "MY_KV",
                        "namespace_id": "abc123",
                    },
                ],
            },
            files={
                "worker.mjs": (
                    "worker.mjs",
                    bytes(script_content, "utf-8"),
                    "application/javascript+module",
                )
            },
        )
        assert_matches_type(ScriptUpdateResponse, script, path=["response"])

    @pytest.mark.skip(reason="TODO: Prism multipart/form-data validation incompatible with SDK encoding")
    @parametrize
    def test_script_upload_with_compatibility_flags(self, client: Cloudflare) -> None:
        script_content = """
        export default {
            async fetch(request, env, ctx) {
                return new Response('Node.js compatibility enabled', { status: 200 });
            }
        };
        """

        script = client.workers.scripts.update(
            "nodejs-compat-script",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={
                "main_module": "worker.mjs",
                "compatibility_date": "2024-01-01",
                "compatibility_flags": ["nodejs_compat"],
            },
            files={
                "worker.mjs": (
                    "worker.mjs",
                    bytes(script_content, "utf-8"),
                    "application/javascript+module",
                )
            },
        )
        assert_matches_type(ScriptUpdateResponse, script, path=["response"])

    @pytest.mark.skip(reason="TODO: Prism multipart/form-data validation incompatible with SDK encoding")
    @parametrize
    def test_script_upload_with_source_map(self, client: Cloudflare) -> None:
        script_content = """
        export default {
            async fetch(request, env, ctx) {
                return new Response('Hello', { status: 200 });
            }
        };
        """

        source_map = '{"version":3,"sources":["worker.js"],"names":[],"mappings":"AAAA"}'

        script = client.workers.scripts.update(
            "script-with-sourcemap",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={
                "main_module": "worker.mjs",
            },
            files={
                "worker.mjs": (
                    "worker.mjs",
                    bytes(script_content, "utf-8"),
                    "application/javascript+module",
                ),
                "worker.mjs.map": (
                    "worker.mjs.map",
                    bytes(source_map, "utf-8"),
                    "application/source-map",
                ),
            },
        )
        assert_matches_type(ScriptUpdateResponse, script, path=["response"])

    @pytest.mark.skip(reason="TODO: Prism multipart/form-data validation incompatible with SDK encoding")
    @parametrize
    def test_script_upload_raw_response(self, client: Cloudflare) -> None:
        script_content = """
        export default {
            async fetch(request, env, ctx) {
                return new Response('Hello', { status: 200 });
            }
        };
        """

        response = client.workers.scripts.with_raw_response.update(
            "test-script",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={
                "main_module": "worker.mjs",
            },
            files={
                "worker.mjs": (
                    "worker.mjs",
                    bytes(script_content, "utf-8"),
                    "application/javascript+module",
                )
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = response.parse()
        assert_matches_type(ScriptUpdateResponse, script, path=["response"])

    @pytest.mark.skip(reason="TODO: Prism multipart/form-data validation incompatible with SDK encoding")
    @parametrize
    def test_script_upload_streaming_response(self, client: Cloudflare) -> None:
        script_content = """
        export default {
            async fetch(request, env, ctx) {
                return new Response('Hello', { status: 200 });
            }
        };
        """

        with client.workers.scripts.with_streaming_response.update(
            "test-script",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={
                "main_module": "worker.mjs",
            },
            files={
                "worker.mjs": (
                    "worker.mjs",
                    bytes(script_content, "utf-8"),
                    "application/javascript+module",
                )
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = response.parse()
            assert_matches_type(ScriptUpdateResponse, script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_script_upload_missing_account_id(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.scripts.with_raw_response.update(
                "test-script",
                account_id="",
                metadata={},
            )

    @parametrize
    def test_script_upload_missing_script_name(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            client.workers.scripts.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                metadata={},
            )


class TestAsyncScriptUpload:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: Prism multipart/form-data validation incompatible with SDK encoding")
    @parametrize
    async def test_basic_script_upload(self, async_client: AsyncCloudflare) -> None:
        script_content = """
        export default {
            async fetch(request, env, ctx) {
                return new Response(env.MESSAGE, { status: 200 });
            }
        };
        """

        script = await async_client.workers.scripts.update(
            "my-hello-world-script",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={
                "main_module": "my-hello-world-script.mjs",
                "bindings": [
                    {
                        "type": "plain_text",
                        "name": "MESSAGE",
                        "text": "Hello World!",
                    }
                ],
            },
            files={
                "my-hello-world-script.mjs": (
                    "my-hello-world-script.mjs",
                    bytes(script_content, "utf-8"),
                    "application/javascript+module",
                )
            },
        )
        assert_matches_type(ScriptUpdateResponse, script, path=["response"])

    @pytest.mark.skip(reason="TODO: Prism multipart/form-data validation incompatible with SDK encoding")
    @parametrize
    async def test_script_upload_with_multiple_files(self, async_client: AsyncCloudflare) -> None:
        main_script = """
        import { helper } from './helper.js';
        export default {
            async fetch(request, env, ctx) {
                return new Response(helper(), { status: 200 });
            }
        };
        """

        helper_script = """
        export function helper() {
            return 'Hello from helper!';
        }
        """

        script = await async_client.workers.scripts.update(
            "multi-file-script",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={
                "main_module": "index.mjs",
            },
            files={
                "index.mjs": (
                    "index.mjs",
                    bytes(main_script, "utf-8"),
                    "application/javascript+module",
                ),
                "helper.js": (
                    "helper.js",
                    bytes(helper_script, "utf-8"),
                    "application/javascript+module",
                ),
            },
        )
        assert_matches_type(ScriptUpdateResponse, script, path=["response"])

    @pytest.mark.skip(reason="TODO: Prism multipart/form-data validation incompatible with SDK encoding")
    @parametrize
    async def test_script_upload_with_bindings(self, async_client: AsyncCloudflare) -> None:
        script_content = """
        export default {
            async fetch(request, env, ctx) {
                const value = await env.MY_KV.get('key');
                return new Response(value || env.MESSAGE, { status: 200 });
            }
        };
        """

        script = await async_client.workers.scripts.update(
            "script-with-bindings",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={
                "main_module": "worker.mjs",
                "bindings": [
                    {
                        "type": "plain_text",
                        "name": "MESSAGE",
                        "text": "Default message",
                    },
                    {
                        "type": "kv_namespace",
                        "name": "MY_KV",
                        "namespace_id": "abc123",
                    },
                ],
            },
            files={
                "worker.mjs": (
                    "worker.mjs",
                    bytes(script_content, "utf-8"),
                    "application/javascript+module",
                )
            },
        )
        assert_matches_type(ScriptUpdateResponse, script, path=["response"])

    @pytest.mark.skip(reason="TODO: Prism multipart/form-data validation incompatible with SDK encoding")
    @parametrize
    async def test_script_upload_with_compatibility_flags(self, async_client: AsyncCloudflare) -> None:
        script_content = """
        export default {
            async fetch(request, env, ctx) {
                return new Response('Node.js compatibility enabled', { status: 200 });
            }
        };
        """

        script = await async_client.workers.scripts.update(
            "nodejs-compat-script",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={
                "main_module": "worker.mjs",
                "compatibility_date": "2024-01-01",
                "compatibility_flags": ["nodejs_compat"],
            },
            files={
                "worker.mjs": (
                    "worker.mjs",
                    bytes(script_content, "utf-8"),
                    "application/javascript+module",
                )
            },
        )
        assert_matches_type(ScriptUpdateResponse, script, path=["response"])

    @pytest.mark.skip(reason="TODO: Prism multipart/form-data validation incompatible with SDK encoding")
    @parametrize
    async def test_script_upload_with_source_map(self, async_client: AsyncCloudflare) -> None:
        script_content = """
        export default {
            async fetch(request, env, ctx) {
                return new Response('Hello', { status: 200 });
            }
        };
        """

        source_map = '{"version":3,"sources":["worker.js"],"names":[],"mappings":"AAAA"}'

        script = await async_client.workers.scripts.update(
            "script-with-sourcemap",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={
                "main_module": "worker.mjs",
            },
            files={
                "worker.mjs": (
                    "worker.mjs",
                    bytes(script_content, "utf-8"),
                    "application/javascript+module",
                ),
                "worker.mjs.map": (
                    "worker.mjs.map",
                    bytes(source_map, "utf-8"),
                    "application/source-map",
                ),
            },
        )
        assert_matches_type(ScriptUpdateResponse, script, path=["response"])

    @pytest.mark.skip(reason="TODO: Prism multipart/form-data validation incompatible with SDK encoding")
    @parametrize
    async def test_script_upload_raw_response(self, async_client: AsyncCloudflare) -> None:
        script_content = """
        export default {
            async fetch(request, env, ctx) {
                return new Response('Hello', { status: 200 });
            }
        };
        """

        response = await async_client.workers.scripts.with_raw_response.update(
            "test-script",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={
                "main_module": "worker.mjs",
            },
            files={
                "worker.mjs": (
                    "worker.mjs",
                    bytes(script_content, "utf-8"),
                    "application/javascript+module",
                )
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        script = await response.parse()
        assert_matches_type(ScriptUpdateResponse, script, path=["response"])

    @pytest.mark.skip(reason="TODO: Prism multipart/form-data validation incompatible with SDK encoding")
    @parametrize
    async def test_script_upload_streaming_response(self, async_client: AsyncCloudflare) -> None:
        script_content = """
        export default {
            async fetch(request, env, ctx) {
                return new Response('Hello', { status: 200 });
            }
        };
        """

        async with async_client.workers.scripts.with_streaming_response.update(
            "test-script",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            metadata={
                "main_module": "worker.mjs",
            },
            files={
                "worker.mjs": (
                    "worker.mjs",
                    bytes(script_content, "utf-8"),
                    "application/javascript+module",
                )
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            script = await response.parse()
            assert_matches_type(ScriptUpdateResponse, script, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_script_upload_missing_account_id(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.scripts.with_raw_response.update(
                "test-script",
                account_id="",
                metadata={},
            )

    @parametrize
    async def test_script_upload_missing_script_name(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `script_name` but received ''"):
            await async_client.workers.scripts.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                metadata={},
            )

