# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.ai import AIRunResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAI:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_run_overload_1(self, client: Cloudflare) -> None:
        ai = client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_raw_response_run_overload_1(self, client: Cloudflare) -> None:
        response = client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_1(self, client: Cloudflare) -> None:
        with client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                text="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                text="x",
            )

    @parametrize
    def test_method_run_overload_2(self, client: Cloudflare) -> None:
        ai = client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_method_run_with_all_params_overload_2(self, client: Cloudflare) -> None:
        ai = client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
            guidance=0,
            height=256,
            image=[0],
            image_b64="image_b64",
            mask=[0],
            negative_prompt="negative_prompt",
            num_steps=20,
            seed=0,
            strength=0,
            width=256,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_raw_response_run_overload_2(self, client: Cloudflare) -> None:
        response = client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_2(self, client: Cloudflare) -> None:
        with client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                prompt="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prompt="x",
            )

    @parametrize
    def test_method_run_overload_3(self, client: Cloudflare) -> None:
        ai = client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_method_run_with_all_params_overload_3(self, client: Cloudflare) -> None:
        ai = client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
            lang="lang",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_raw_response_run_overload_3(self, client: Cloudflare) -> None:
        response = client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_3(self, client: Cloudflare) -> None:
        with client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                prompt="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prompt="x",
            )

    @parametrize
    def test_method_run_overload_4(self, client: Cloudflare) -> None:
        ai = client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_raw_response_run_overload_4(self, client: Cloudflare) -> None:
        response = client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_4(self, client: Cloudflare) -> None:
        with client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                text="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                text="x",
            )

    @parametrize
    def test_method_run_overload_5(self, client: Cloudflare) -> None:
        ai = client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            audio=[0],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_method_run_with_all_params_overload_5(self, client: Cloudflare) -> None:
        ai = client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            audio=[0],
            source_lang="source_lang",
            target_lang="target_lang",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_raw_response_run_overload_5(self, client: Cloudflare) -> None:
        response = client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            audio=[0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_5(self, client: Cloudflare) -> None:
        with client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            audio=[0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                audio=[0],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                audio=[0],
            )

    @parametrize
    def test_method_run_overload_6(self, client: Cloudflare) -> None:
        ai = client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_raw_response_run_overload_6(self, client: Cloudflare) -> None:
        response = client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_6(self, client: Cloudflare) -> None:
        with client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                image=[0],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                image=[0],
            )

    @parametrize
    def test_method_run_overload_7(self, client: Cloudflare) -> None:
        ai = client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_method_run_with_all_params_overload_7(self, client: Cloudflare) -> None:
        ai = client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_raw_response_run_overload_7(self, client: Cloudflare) -> None:
        response = client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_7(self, client: Cloudflare) -> None:
        with client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_overload_7(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_run_overload_8(self, client: Cloudflare) -> None:
        ai = client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_method_run_with_all_params_overload_8(self, client: Cloudflare) -> None:
        ai = client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
            frequency_penalty=0,
            lora="lora",
            max_tokens=0,
            presence_penalty=0,
            raw=True,
            repetition_penalty=0,
            response_format={
                "json_schema": {},
                "type": "json_object",
            },
            seed=1,
            stream=True,
            temperature=0,
            top_k=1,
            top_p=0,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_raw_response_run_overload_8(self, client: Cloudflare) -> None:
        response = client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_8(self, client: Cloudflare) -> None:
        with client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_overload_8(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                prompt="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prompt="x",
            )

    @parametrize
    def test_method_run_overload_9(self, client: Cloudflare) -> None:
        ai = client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_method_run_with_all_params_overload_9(self, client: Cloudflare) -> None:
        ai = client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
            frequency_penalty=0,
            functions=[
                {
                    "code": "code",
                    "name": "name",
                }
            ],
            max_tokens=0,
            presence_penalty=0,
            repetition_penalty=0,
            response_format={
                "json_schema": {},
                "type": "json_object",
            },
            seed=1,
            stream=True,
            temperature=0,
            tools=[
                {
                    "description": "description",
                    "name": "name",
                    "parameters": {
                        "properties": {
                            "foo": {
                                "description": "description",
                                "type": "type",
                            }
                        },
                        "type": "type",
                        "required": ["string"],
                    },
                }
            ],
            top_k=1,
            top_p=0,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_raw_response_run_overload_9(self, client: Cloudflare) -> None:
        response = client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_9(self, client: Cloudflare) -> None:
        with client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_overload_9(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                messages=[
                    {
                        "content": "content",
                        "role": "role",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                messages=[
                    {
                        "content": "content",
                        "role": "role",
                    }
                ],
            )

    @parametrize
    def test_method_run_overload_10(self, client: Cloudflare) -> None:
        ai = client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="target_lang",
            text="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_method_run_with_all_params_overload_10(self, client: Cloudflare) -> None:
        ai = client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="target_lang",
            text="x",
            source_lang="source_lang",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_raw_response_run_overload_10(self, client: Cloudflare) -> None:
        response = client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="target_lang",
            text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_10(self, client: Cloudflare) -> None:
        with client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="target_lang",
            text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_overload_10(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                target_lang="target_lang",
                text="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                target_lang="target_lang",
                text="x",
            )

    @parametrize
    def test_method_run_overload_11(self, client: Cloudflare) -> None:
        ai = client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_method_run_with_all_params_overload_11(self, client: Cloudflare) -> None:
        ai = client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="x",
            max_length=0,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_raw_response_run_overload_11(self, client: Cloudflare) -> None:
        response = client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_11(self, client: Cloudflare) -> None:
        with client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_overload_11(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                input_text="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                input_text="x",
            )

    @parametrize
    def test_method_run_overload_12(self, client: Cloudflare) -> None:
        ai = client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_method_run_with_all_params_overload_12(self, client: Cloudflare) -> None:
        ai = client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0],
            frequency_penalty=0,
            max_tokens=0,
            presence_penalty=0,
            prompt="prompt",
            raw=True,
            repetition_penalty=0,
            seed=0,
            temperature=0,
            top_k=0,
            top_p=0,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_raw_response_run_overload_12(self, client: Cloudflare) -> None:
        response = client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    def test_streaming_response_run_overload_12(self, client: Cloudflare) -> None:
        with client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_run_overload_12(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                image=[0],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                image=[0],
            )


class TestAsyncAI:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_run_overload_1(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                text="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                text="x",
            )

    @parametrize
    async def test_method_run_overload_2(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_method_run_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
            guidance=0,
            height=256,
            image=[0],
            image_b64="image_b64",
            mask=[0],
            negative_prompt="negative_prompt",
            num_steps=20,
            seed=0,
            strength=0,
            width=256,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                prompt="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prompt="x",
            )

    @parametrize
    async def test_method_run_overload_3(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_method_run_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
            lang="lang",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                prompt="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prompt="x",
            )

    @parametrize
    async def test_method_run_overload_4(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                text="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                text="x",
            )

    @parametrize
    async def test_method_run_overload_5(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            audio=[0],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_method_run_with_all_params_overload_5(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            audio=[0],
            source_lang="source_lang",
            target_lang="target_lang",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            audio=[0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            audio=[0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                audio=[0],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                audio=[0],
            )

    @parametrize
    async def test_method_run_overload_6(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                image=[0],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                image=[0],
            )

    @parametrize
    async def test_method_run_overload_7(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_method_run_with_all_params_overload_7(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_7(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_7(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_overload_7(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_run_overload_8(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_method_run_with_all_params_overload_8(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
            frequency_penalty=0,
            lora="lora",
            max_tokens=0,
            presence_penalty=0,
            raw=True,
            repetition_penalty=0,
            response_format={
                "json_schema": {},
                "type": "json_object",
            },
            seed=1,
            stream=True,
            temperature=0,
            top_k=1,
            top_p=0,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_8(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_8(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prompt="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_overload_8(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                prompt="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prompt="x",
            )

    @parametrize
    async def test_method_run_overload_9(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_method_run_with_all_params_overload_9(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
            frequency_penalty=0,
            functions=[
                {
                    "code": "code",
                    "name": "name",
                }
            ],
            max_tokens=0,
            presence_penalty=0,
            repetition_penalty=0,
            response_format={
                "json_schema": {},
                "type": "json_object",
            },
            seed=1,
            stream=True,
            temperature=0,
            tools=[
                {
                    "description": "description",
                    "name": "name",
                    "parameters": {
                        "properties": {
                            "foo": {
                                "description": "description",
                                "type": "type",
                            }
                        },
                        "type": "type",
                        "required": ["string"],
                    },
                }
            ],
            top_k=1,
            top_p=0,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_9(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_9(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            messages=[
                {
                    "content": "content",
                    "role": "role",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_overload_9(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                messages=[
                    {
                        "content": "content",
                        "role": "role",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                messages=[
                    {
                        "content": "content",
                        "role": "role",
                    }
                ],
            )

    @parametrize
    async def test_method_run_overload_10(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="target_lang",
            text="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_method_run_with_all_params_overload_10(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="target_lang",
            text="x",
            source_lang="source_lang",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_10(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="target_lang",
            text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_10(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            target_lang="target_lang",
            text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_overload_10(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                target_lang="target_lang",
                text="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                target_lang="target_lang",
                text="x",
            )

    @parametrize
    async def test_method_run_overload_11(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="x",
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_method_run_with_all_params_overload_11(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="x",
            max_length=0,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_11(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_11(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            input_text="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_overload_11(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                input_text="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                input_text="x",
            )

    @parametrize
    async def test_method_run_overload_12(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0],
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_method_run_with_all_params_overload_12(self, async_client: AsyncCloudflare) -> None:
        ai = await async_client.ai.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0],
            frequency_penalty=0,
            max_tokens=0,
            presence_penalty=0,
            prompt="prompt",
            raw=True,
            repetition_penalty=0,
            seed=0,
            temperature=0,
            top_k=0,
            top_p=0,
        )
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_raw_response_run_overload_12(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.ai.with_raw_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

    @parametrize
    async def test_streaming_response_run_overload_12(self, async_client: AsyncCloudflare) -> None:
        async with async_client.ai.with_streaming_response.run(
            model_name="model_name",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            image=[0],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(Optional[AIRunResponse], ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_run_overload_12(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="model_name",
                account_id="",
                image=[0],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_name` but received ''"):
            await async_client.ai.with_raw_response.run(
                model_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                image=[0],
            )
