#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "requests",
#     "hs-py-auth",
# ]
# ///
"""Generate images via HubSpot's LiteLLM proxy (Gemini/Nano Banana).

Usage:
    uvx generate-image.py -o output.png "a friendly cartoon robot"
    uv run scripts/generate-image.py -o output.png -i ref.png "redraw in this style"
    uv run scripts/generate-image.py -o output.png -a 9:16 "tall portrait"
    uv run scripts/generate-image.py -o output.png --pro "high quality illustration"
"""

import argparse
import base64
import sys
from pathlib import Path

import requests
from hs_py_auth.plugins import InfraIdpAuth


ENDPOINT = "https://litellm.hubteam.com/v1/chat/completions"
MODEL_FLASH = "gemini-3.1-flash-image-preview"
MODEL_PRO = "gemini-3-pro-image-preview"

ASPECT_RATIO_HINTS = {
    "1:1": "Square 1:1 aspect ratio.",
    "16:9": "Landscape 16:9 widescreen aspect ratio.",
    "9:16": "Portrait 9:16 tall and narrow aspect ratio.",
    "4:3": "4:3 aspect ratio.",
    "3:4": "Portrait 3:4 aspect ratio.",
}


def encode_image(path):
    import mimetypes
    data = Path(path).read_bytes()
    b64 = base64.b64encode(data).decode()
    mime, _ = mimetypes.guess_type(str(path))
    mime = mime or "image/png"
    return f"data:{mime};base64,{b64}"


def generate(prompt, output, images=None, aspect_ratio="1:1", pro=False):
    model = MODEL_PRO if pro else MODEL_FLASH

    content = []
    if images:
        for img_path in images:
            if not Path(img_path).exists():
                print(f"Error: image not found: {img_path}", file=sys.stderr)
                sys.exit(1)
            content.append({
                "type": "image_url",
                "image_url": {"url": encode_image(img_path)}
            })

    ar_hint = ASPECT_RATIO_HINTS.get(aspect_ratio, f"{aspect_ratio} aspect ratio.")
    full_prompt = f"{prompt} {ar_hint}"
    content.append({"type": "text", "text": full_prompt})

    payload = {
        "model": model,
        "modalities": ["text", "image"],
        "messages": [{"role": "user", "content": content}],
    }

    print(f"Generating image with {model} ({aspect_ratio})...")

    try:
        resp = requests.post(
            ENDPOINT,
            json=payload,
            auth=InfraIdpAuth(),
            timeout=120,
        )
        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP {e.response.status_code}: {e.response.text[:500]}", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Failed to parse response as JSON: {e}", file=sys.stderr)
        sys.exit(1)

    if "error" in data:
        print(f"API error: {data['error']}", file=sys.stderr)
        sys.exit(1)

    msg = data.get("choices", [{}])[0].get("message", {})
    images_out = msg.get("images", [])
    if not images_out:
        print("No image returned.", file=sys.stderr)
        if msg.get("content"):
            print(f"Response: {msg['content']}", file=sys.stderr)
        sys.exit(1)

    img_data = images_out[0]["image_url"]["url"]
    if "," in img_data:
        img_data = img_data.split(",", 1)[1]

    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(base64.b64decode(img_data))
    print(f"Saved to {output_path}")

    if msg.get("content"):
        print(msg["content"])


def main():
    parser = argparse.ArgumentParser(
        description="Generate images via HubSpot's LiteLLM proxy (Gemini)"
    )
    parser.add_argument("prompt", help="Text prompt for image generation")
    parser.add_argument("-o", "--output", required=True, help="Output file path")
    parser.add_argument("-i", "--image", action="append", dest="images",
                        help="Reference image(s) for style matching (can specify multiple)")
    parser.add_argument("-a", "--aspect-ratio", default="1:1",
                        choices=["1:1", "16:9", "9:16", "4:3", "3:4"],
                        help="Aspect ratio (default: 1:1)")
    parser.add_argument("--pro", action="store_true",
                        help="Use the pro model for higher quality")

    args = parser.parse_args()
    generate(args.prompt, args.output, args.images, args.aspect_ratio, args.pro)


if __name__ == "__main__":
    main()