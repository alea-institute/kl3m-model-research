---
language:
- en
library_name: transformers
license: cc-by-4.0
tags:
- kl3m
- kl3m-003
- legal
- financial
- enterprise
- slm
date: '2024-02-20T00:00:00.000Z'
pipeline_tag: text-generation
widget:
 - text: "Medical devices are regulated by"
 - temperature: 0.3
 - do_sample: True
---

# kl3m-003-1.7b Model

kl3m-1.7b is a small language model (SLM) model trained on clean, legally-permissible data. Originally 
developed by [273 Ventures](https://273ventures.com) and donated to the [ALEA Institute](https://aleainstitute.ai), 
kl3m-003-1.7b was part of the first LLM family to obtain the [Fairly Trained L-Certification](https://www.fairlytrained.org/certifications)
for its ethical training data and practices. The model is designed for legal, regulatory, and financial workflows,
with a focus on low toxicity and high efficiency.

Given its small size and lack of training data for instruction alignment, kl3m-003-1.7b is best suited for use either in
SLM fine-tuning or as part of training larger models without using unethical data or models.

The model was originally trained between January-February 2024 on a 8xA100-80G node in DDP.  A similar model is
being provided with complete source and data replication as part of the `kl3m-004` family to be released in Q4 2024.

## Source

[https://github.com/alea-institute/kl3m-model-research](https://github.com/alea-institute/kl3m-model-research)


## Training Data
While the original training data collection and training infrastructure relies on software that was not donated by
273 Ventures, ALEA Institute is open-sourcing an improved dataset, including both replication and an API.

[https://github.com/alea-institute/kl3m-data](https://github.com/alea-institute/kl3m-data)

Data is available upon request at this time via S3 under a Requester Pays model.  We are actively working on a
zero-cost distribution model as soon as we can obtain additional support.

This model, the original `kl3m-003-1.7b` model, was trained on a US-only subset of the Kelvin Legal DataPack that
we believe is 100% public domain material. However, so as to enforce maximum transparency to all 
downstream users in the event of any future determination otherwise, we are licensing this model under CC-BY 4.0.

## Model Details

### Summary
- **Architecture**: GPT-NeoX (i.e., ~GPT-3 architecture)
- **Parameters**: 1.7 billion
- **Context Window**: 8,192 tokens (true size, no sliding window)
- **Language(s)**: Primarily English
- **Tokenizer**: kl3m-001-32k BPE tokenizer (32,768 vocabulary size with unorthodox whitespace handling)
- **Developed by**: Originally by [273 Ventures LLC](https://273ventures.com), donated to [ALEA Institute](https://aleainstitute.ai)
- **License**: [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Hardware Requirements**: Runs real-time in bf16 on consumer NV/AMD GPUs

## Performance Metrics

### Perplexity Scores
| Dataset        | Score |
|---------------|-------|
| Wiki          | 18.25 |
| CNN/Daily Mail| 9.61  |
| Legal Domain  | 2.00  |

The model demonstrates particularly strong per-parameter performance on legal domain content, outperforming many 
larger models as of its training data.

## Key Features

- **Clean Training Data**: Built on what was originally referred to as the Kelvin Legal DataPack, ensuring all training data is ethically sourced and legally permissible.
- **Low Toxicity**: [Empirically lower toxicity and bias](https://github.com/alea-institute/kl3m-toxicity)
- **Enterprise Focus**: Specifically designed for legal, regulatory, and financial workflows.
- **Efficient Deployment**: Optimized for real-time inference on consumer hardware.

## Use Cases

- Basic regulatory question answering
- Contract provision drafting
- Structured JSON information extraction
- Foundation for downstream optimization
- Base model for domain-specific fine-tuning

## Getting Started

```python
import json
from transformers import pipeline

# Load the model and tokenizer
p = pipeline('text-generation', 'alea-institute/kl3m-003-1.7b', device='cuda')

# Example usage on CPU
text = "Under this"
print(
    json.dumps(
        [
            r.get("generated_text")
            for r in p(text, do_sample=True, temperature=0.5, num_return_sequences=3, max_new_tokens=32)
        ], 
        indent=2
    )
)
```

```json
[
  "Under this section, any person who is a party to the proceeding may be required to file ",
  "Under this subsection, the term **eligible entity** means a State, a political subdivision of ",
  "Under this section, the Secretary shall\u2014 (1)\nmake a grant to the National Academy of Sc"
]
```

## Contract Example
```python
text = "Governing Law. "
print(
    json.dumps(
        [
            r.get("generated_text")
            for r in p(text, do_sample=True, temperature=0.5, num_return_sequences=3, max_new_tokens=32)
        ], 
        indent=2
    )
)
```

```json
[
  "Governing Law. The validity, construction, enforcement and interpretation of this Agreement and of the War",
  "Governing Law. This Agreement shall be governed by and construed in accordance with the laws of",
  "Governing Law. This Agreement shall be governed by and construed and enforced in accordance"
]
```

## Technical Implementation

The model implements several techniques during training:

- Hybrid NTP and SFT cotraining
- Dynamic, document-aware segmentation
- Randomized padding
- Traditional fixed-attention mechanisms

## License

This model was originally developed by 273 Ventures and has been donated to the ALEA Institute. 

The model weights are released under the CC-BY 4.0 License.

## Contact

The KL3M model family is now maintained by the [ALEA Institute](https://aleainstitute.ai). For technical support, collaboration opportunities, or general inquiries:
 
- GitHub: https://github.com/alea-institute/kl3m-model-research
- Email: hello@aleainstitute.ai
- Website: https://aleainstitute.ai

## Acknowledgments

Special thanks to 273 Ventures for developing and donating this model to the open-source community through the Alea Institute.


## Citation

Tokenizer, dataset, and model publications are pending.

## Contact

For any questions, please contact [ALEA Institute](https://aleainstitute.ai) at [hello@aleainstitute.ai](mailto:hello@aleainstitute.ai) or
create an issue on this repository or [GitHub](https://github.com/alea-institute/kl3m-model-research).

![https://aleainstitute.ai](https://aleainstitute.ai/images/alea-logo-ascii-1x1.png)