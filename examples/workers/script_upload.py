"""Workers Script Upload Example

Generate an API token:
https://developers.cloudflare.com/fundamentals/api/get-started/create-token/
(Not Global API Key!)

Find your account id:
https://developers.cloudflare.com/fundamentals/setup/find-account-and-zone-ids/

Set these environment variables:
- CLOUDFLARE_API_TOKEN
- CLOUDFLARE_ACCOUNT_ID


### Workers for Platforms ###

For uploading a User Worker to a dispatch namespace:
https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/

Change the entire "script = " line to the following:
"script = client.workers_for_platforms.dispatch.namespaces.scripts.update("

Then, define a "dispatch_namespace_name" variable and add a
"dispatch_namespace=dispatch_namespace_name" keyword argument to the "update" method.
"""

import os

from cloudflare import Cloudflare, BadRequestError

API_TOKEN = os.environ.get("CLOUDFLARE_API_TOKEN")
if API_TOKEN is None:
    raise RuntimeError("Please set envar CLOUDFLARE_API_TOKEN")

ACCOUNT_ID = os.environ.get("CLOUDFLARE_ACCOUNT_ID")
if ACCOUNT_ID is None:
    raise RuntimeError("Please set envar CLOUDFLARE_ACCOUNT_ID")

client = Cloudflare(api_token=API_TOKEN)


def main() -> None:
    """Workers Script Upload Example"""

    script_name = "my-hello-world-script"
    script_file_name = f"{script_name}.mjs"

    # Workers Scripts prefer Module Syntax
    # https://blog.cloudflare.com/workers-javascript-modules/
    script_content = """
    export default {
        async fetch(request, env, ctx) {
            return new Response(env.MESSAGE, { status: 200 });
        }
    };
    """

    try:
        # https://developers.cloudflare.com/api/resources/workers/subresources/scripts/methods/update/
        script = client.workers.scripts.update(
            script_name,
            account_id=ACCOUNT_ID, # type: ignore
            # https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/
            metadata={
                "main_module": script_file_name,
                "bindings": [
                    {
                        "type": "plain_text",
                        "name": "MESSAGE",
                        "text": "Hello World!",
                    }
                ],
            },
            files={
                # Add main_module file
                script_file_name: (
                    script_file_name,
                    bytes(script_content, "utf-8"),
                    "application/javascript+module",
                )
                # Can add other files, such as more modules or source maps
                # source_map_file_name: (
                #   source_map_file_name,
                #   bytes(source_map_content, "utf-8"),
                #   "application/source-map"
                #)
            },
        )
        print("Script Upload success!")
        print(script.to_json(indent=2))
    except BadRequestError as err:
        print("Script Upload failure!")
        print(err)


if __name__ == "__main__":
    main()
