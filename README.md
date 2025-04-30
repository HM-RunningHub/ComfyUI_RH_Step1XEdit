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

    # --- Download Step1X Edit Model (Replace with actual repo_id if available) ---
    # Note: The specific HF repo for 'step1x-edit-i1258.safetensors' is not provided.
    # Please download it manually or update the repo_id below if known.
    # Example placeholder:
    # snapshot_download(
    #     repo_id="YOUR_REPO_ID/step1x-edit",
    #     local_dir=target_dir,
    #     allow_patterns=["step1x-edit-i1258.safetensors"],
    #     local_dir_use_symlinks=False
    # )
    print("Please manually download 'step1x-edit-i1258.safetensors' and place it in:", target_dir)

    # --- Download VAE --- 
    # Assuming a standard SDXL VAE or similar is used. Adjust repo_id if needed.
    snapshot_download(
        repo_id="madebyollin/sdxl-vae-fp16-fix", # Or stabilityai/sdxl-vae
        local_dir=target_dir,
        allow_patterns=["vae.safetensors", "*.json"], # Adjust pattern if filename differs
        local_dir_use_symlinks=False
    )
    # Rename if necessary
    # os.rename(os.path.join(target_dir, "diffusion_pytorch_model.safetensors"), os.path.join(target_dir, "vae.safetensors"))

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
    *   **Step1X Edit:** Download `step1x-edit-i1258.safetensors` (Source link needed - Please update)
    *   **VAE:** [madebyollin/sdxl-vae-fp16-fix](https://huggingface.co/madebyollin/sdxl-vae-fp16-fix) or [stabilityai/sdxl-vae](https://huggingface.co/stabilityai/sdxl-vae) (Download `.safetensors` file, rename to `vae.safetensors`)
    *   **Qwen2.5-VL:** [Qwen/Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct)

### Expected File Structure

```
ComfyUI/models/
└── step-1/
    ├── step1x-edit-i1258.safetensors
    ├── vae.safetensors
    └── Qwen2.5-VL-7B-Instruct/
        ├── config.json
        ├── generation_config.json
        ├── model-00001-of-00004.safetensors
        ├── model-00002-of-00004.safetensors
        ├── model-00003-of-00004.safetensors
        ├── model-00004-of-00004.safetensors
        ├── model.safetensors.index.json
        ├── qwen_tokenizer.py
        ├── tokenization_qwen2_fast.py
        ├── tokenizer.json
        ├── tokenizer_config.json
        └── ... (other files)
```

## Installation

1.  Clone this repository into your `ComfyUI/custom_nodes/` directory:
    ```bash
    cd ComfyUI/custom_nodes/
    git clone <repository_url> ComfyUI_RH_Step1XEdit
    ```
2.  Install the required dependencies:
    ```bash
    cd ComfyUI_RH_Step1XEdit
    pip install -r requirements.txt
    ```
    *(Note: Ensure the versions in `requirements.txt` are compatible with your ComfyUI environment, especially PyTorch and CUDA versions).* 
3.  Restart ComfyUI.

## Usage

Look for the `RunningHub Step1X Edit` node under the `Runninghub/Step1XEdit` category in ComfyUI.

**Inputs:**

*   `ref_image`: The input image to be edited.
*   `prompt`: Text description of the desired edit.
*   `num_steps`: Number of diffusion steps.
*   `cfg_guidance`: Guidance scale.
*   `size_level`: Approximate target size for processing (internal resolution is adjusted based on aspect ratio).
*   `seed`: Random seed.
*   `use_fp8`: Enable/disable FP8 inference.

**(Example Image/Workflow)**

![image](https://github.com/user-attachments/assets/035274a4-fc47-4249-acf0-a5e31cdd1671)
