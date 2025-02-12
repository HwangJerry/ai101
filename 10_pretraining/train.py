from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Arguments:
    model_name_or_path: Optional[str] = field(default=None)  # HuggingFace hub에서 pre-trained 모델로 사용할 모델의 이름
    torch_dtype: Optional[str] = field(default=None, metadata={'choices': ['auto', 'bfloat16', 'float16', 'float32']})  # 우리 모델의 precision(data type이라고 이해하시면 됩니다)

    dataset_name: Optional[str] = field(default=None)  # Fine-tuning으로 사용할 huggingface hub에서의 dataset 이름
    dataset_config_name: Optional[str] = field(default=None)  # Fine-tuning으로 사용할 huggingface hub에서의 dataset configuration
    block_size: int = field(default=1024)  # Fine-tuning에 사용할 input text의 길이
    num_workers: Optional[int] = field(default=None)  # Data를 업로드하거나 전처리할 때 사용할 worker 숫자