# EXAONE 3.5

EXAONE 3.5 is a collection of instruction-tuned bilingual (English and Korean) generative models ranging from 2.4B to 32B parameters, developed and released by LG AI Research.

## Model Sizes
- **2.4B**
- **7.8B**
- **32B**

## Pulls
- **Total Pulls**: 1,265
- **Updated**: 2 days ago

## Tags
- **Tags**: 13

## Run Command
```bash
ollama run exaone3.5:2.4b
```

## Model Info
- **Size**: 1.6GB
- **ID**: 13644fc3d28e

## Model Description
You are EXAONE model from LG AI Research, a helpful assistant.

## Parameters
- **Params**: 2.67B
- **Quantization**: Q4_K_M

## System
- **Arch**: exaone

## Template
{{- range $i, $_ := .Messages }} {{- $last := eq (len (slice $.Messages $i)) 1 -}} {{ if eq .Role "s

## License
EXAONE AI Model License Agreement 1.1 - NC This License Agreement (“Agreement”) is entered into

## Readme
EXAONE 3.5 is a collection of instruction-tuned bilingual (English and Korean) generative models ranging from 2.4B to 32B parameters, developed and released by LG AI Research. EXAONE 3.5 language models include:

- 2.4B model optimized for deployment on small or resource-constrained devices
- 7.8B model matching the size of its predecessor but offering improved performance
- 32B model delivering powerful performance.

All models support long-context processing of up to 32K tokens. Each model demonstrates state-of-the-art performance in real-world use cases and long-context understanding, while remaining competitive in general domains compared to recently released models of similar sizes.

## Benchmarks

## References
- **Paper**
- **Hugging Face**
- **Blog**