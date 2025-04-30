# Step1X Edit for ComfyUI

This is a ComfyUI custom node implementation for image editing using the Step-1 model architecture, specifically adapted for reference-based image editing guided by text prompts.

## Online Access
You can access RunningHub online to use this plugin and models for free:
### English Version
- **Run & Download Workflow**:  
  [https://www.runninghub.ai/post/1916456042962817026](https://www.runninghub.ai/post/1916456042962817026)
### 中文版本
- **运行并下载工作流**:  
  [https://www.runninghub.cn/post/1912930457355517954](https://www.runninghub.cn/post/1916456042962817026)
## Features

*   Implementation of the Step-1 image editing concept within ComfyUI.
*   Optimized for running on GPUs with 24GB VRAM.
*   Inference for potentially faster performance and lower memory usage.
*   Simple node interface for ease of use.
*   Passed testing locally on Windows with an RTX 4090; generating a single image takes approximately 100 seconds.

## Model Download Guide

Place the downloaded models in your `ComfyUI/models/step-1/` directory.

### Required Models:

1.  **Step1X Edit Model:** Contains the main diffusion model weights adapted for editing.
2.  **VAE:** Used for encoding and decoding images to/from latent space.
3.  **Qwen2.5-VL-7B-Instruct:** The vision-language model used for text and image conditioning.

### Choose a Download Method (Pick One)

1.  **One-Click Download with Python Script:**
    *Requires the `huggingface_hub` library (`pip install huggingface-hub`)*
    ```python
    from huggingface_hub import snapshot_download
    import os

    # Define the target directory within ComfyUI models
    target_dir = "path/to/your/ComfyUI/models/step-1"
    os.makedirs(target_dir, exist_ok=True)

    # --- Download Step1X Edit Model ---
    snapshot_download(
        repo_id="stepfun-ai/Step1X-Edit",
        local_dir=target_dir,
        allow_patterns=["step1x-edit-i1258.safetensors"],
        local_dir_use_symlinks=False
    )

    # --- Download VAE ---
    snapshot_download(
        repo_id="stepfun-ai/Step1X-Edit", # VAE is in the same repo
        local_dir=target_dir,
        allow_patterns=["vae.safetensors"],
        local_dir_use_symlinks=False
    )

    # --- Download Qwen2.5-VL-7B-Instruct ---
    qwen_dir = os.path.join(target_dir, "Qwen2.5-VL-7B-Instruct")
    snapshot_download(
        repo_id="Qwen/Qwen2.5-VL-7B-Instruct",
        local_dir=qwen_dir,
        # ignore_patterns=["*.git*", "*.log*", "*.md", "*.jpg"], # Optional: reduce download size
        local_dir_use_symlinks=False
    )

    print(f"Downloads complete. Models should be in {target_dir}")
    ```

2.  **Manual Download:**
    *   **Step1X Edit:** Download `step1x-edit-i1258.safetensors` ([step1x-edit-i1258.safetensors](https://huggingface.co/stepfun-ai/Step1X-Edit/resolve/main/step1x-edit-i1258.safetensors))
    *   **VAE:** Download `vae.safetensors` ([vae.safetensors](https://huggingface.co/stepfun-ai/Step1X-Edit/resolve/main/vae.safetensors))
    *   **Qwen2.5-VL:** Download the entire repository: [Qwen/Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct)

    Place the `step1x-edit-i1258.safetensors` and `vae.safetensors` files, and the `Qwen2.5-VL-7B-Instruct` folder into your ComfyUI `models/step-1` directory (you might need to create the `step-1` subfolder). Your final structure should look like:
    ```
    ComfyUI/
    └── models/
        └── step-1/
            ├── step1x-edit-i1258.safetensors
            ├── vae.safetensors
            └── Qwen2.5-VL-7B-Instruct/
                ├── ... (all files from the Qwen repo)
    ```

## Installation

1.  Clone this repository into your `