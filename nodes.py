#import os
#import sys
#current_dir = os.path.dirname(os.path.abspath(__file__))
#sys.path.insert(0, current_dir)


import sys
import os
import importlib
import folder_paths
from .inference import Step1XImageGenerator, kiki_tensor_to_pil
import torch
import numpy as np
import comfy.utils

# sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

class Kiki_Step1XEdit:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ref_image": ("IMAGE",),
                "prompt": ("STRING", {"multiline": True,
                                      "default": ''}),
                "num_steps": ("INT", {"default": 28, "min": 1, "max": 0xffffffffffffffff}),
                "cfg_guidance": ("FLOAT", {"default": 6.0}),
                "size_level": ("INT", {"default": 1024}),
                "seed": ("INT", {"default": 42, "min": 0, "max": 0xffffffffffffffff,
                                 "tooltip": "The random seed used for creating the noise."}),
                "use_fp8": ("BOOLEAN", {"default": True})
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "run"
    TITLE = 'RunningHub Step1X Edit'

    CATEGORY = "Runninghub/Step1XEdit"
    DESCRIPTION = "RunningHub Step1X Edit in 24G"

    def __init__(self):
        model_path = os.path.join(folder_paths.models_dir, 'step-1')
        qwen2vl_model_path = os.path.join(model_path, 'Qwen2.5-VL-7B-Instruct')

        self.image_edit = Step1XImageGenerator(
            ae_path=os.path.join(model_path, 'vae.safetensors'),
            dit_path=os.path.join(model_path, "step1x-edit-i1258.safetensors"),
            qwen2vl_model_path=qwen2vl_model_path,
            max_length=640,
        )

    # def run(self, **kwargs):
    #     lib_name = 'ComfyUI_RH_Step1XEdit.inference'
    #     if lib_name in sys.modules:
    #         importlib.reload(sys.modules[lib_name])
    #     import ComfyUI_RH_Step1XEdit.inference as rsi
    #     img = rsi.run(**kwargs)
    #     return (img, )

    def run(self, **kwargs):
        prompt = kwargs['prompt']
        img = kiki_tensor_to_pil(kwargs['ref_image'][0])
        num_steps = kwargs['num_steps']
        self.pbar = comfy.utils.ProgressBar(num_steps)
        use_fp8 = kwargs['use_fp8'] if 'use_fp8' in kwargs else False

        image = self.image_edit.generate_image(
            prompt,
            negative_prompt="",
            ref_images=img,
            num_samples=1,
            num_steps=num_steps,
            cfg_guidance=kwargs['cfg_guidance'],
            seed=kwargs['seed'],
            show_progress=True,
            size_level=kwargs['size_level'],
            rh_hook=self.update,
            use_fp8=use_fp8
        )[0]
    
        image = np.array(image).astype(np.float32) / 255.0
        image = torch.from_numpy(image)[None,]
        return (image, )
    
    def update(self):
        self.pbar.update(1)

NODE_CLASS_MAPPINGS = {
    "RunningHub_Step1XEdit": Kiki_Step1XEdit,
}
