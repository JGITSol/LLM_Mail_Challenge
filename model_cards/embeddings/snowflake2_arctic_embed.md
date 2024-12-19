# Snowflake Arctic Embed 2.0

**Snowflake's frontier embedding model**, Arctic Embed 2.0 adds multilingual support without sacrificing English performance or scalability.

## Model Information
- **Size**: 568M
- **Total Pulls**: 2,303
- **Updated**: 7 days ago

## Tags
- **Tags**: 3

## Pull Command
```bash
ollama pull snowflake-arctic-embed2
```

## Model Architecture
- **Architecture**: BERT

## Model Details
- **Parameters**: 567M
- **Quantization**: F16
- **Size**: 1.2GB

## License
- **License**: Apache License Version 2.0, January 2004

## Readme
Snowflake is excited to announce the release of Arctic Embed 2.0, the next iteration of our frontier embedding models, which now empower multilingual search. While our previous releases have been well received by our customers, partners and the open source community, leading to millions of downloads, we have consistently received one request: Can you make this model multilingual? Arctic Embed 2.0 builds on the robust foundation of our previous releases, adding multilingual support without sacrificing English performance or scalability, to address the needs of an even broader user base that spans a wide range of languages and applications.

Snowflake dataFigure 1. Single-vector dense retrieval performance of open source multilingual embedding models with fewer than 1B parameters. Scores are average nDCG@10 on MTEB Retrieval and the subset of CLEF (ELRA, 2006) covering English, French, Spanish, Italian and German.

The diverse and powerful feature set of Arctic Embed 2.0
Enterprise-ready throughput and efficiency: The Arctic Embed 2.0 models are built for large-scale enterprise demands. Even our “large” model weighs in well under 1B parameters and delivers fast, high-throughput embedding capabilities. Based on internal testing, it easily handles more than 100 documents per second (on average) on NVIDIA A10 GPUs and achieves sub-10ms query embedding latency, enabling practical deployment on budget-friendly hardware.
Uncompromising quality for English and non-English retrieval: Despite their compact sizes, both Arctic Embed 2.0 models achieve impressive NDCG@10 scores across a variety of English and non-English benchmark data sets, demonstrating a capability to generalize well even to languages not included in the training recipe. These impressive benchmark scores position Arctic Embed 2.0 as a leader among frontier retrieval models.
Enabling scalable retrieval through Matryoshka Representation Learning (MRL): The Arctic Embed 2.0 release includes the same quantization-friendly MRL functionality introduced in Arctic Embed 1.5, allowing users to reduce cost and optimize scale when performing searches over large data sets. With both model sizes, users can achieve high-quality retrieval with as few as 128 bytes per vector (96x smaller than uncompressed embeddings from OpenAI’s popular text-embedding-3-large model1). Just like Arctic Embed 1.5, the Arctic Embed 2.0 models also outshine several MRL-supporting peers with substantially lower quality degradation and higher benchmark scores in the compressed regime.
Truly open source: The Arctic Embed 2.0 models are released under the permissive Apache 2.0 license.