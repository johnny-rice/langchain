from langchain_community.retrievers import __all__, _module_lookup

EXPECTED_ALL = [
    "AmazonKendraRetriever",
    "AmazonKnowledgeBasesRetriever",
    "ArceeRetriever",
    "ArxivRetriever",
    "AskNewsRetriever",
    "AzureAISearchRetriever",
    "AzureCognitiveSearchRetriever",
    "BreebsRetriever",
    "ChatGPTPluginRetriever",
    "ChaindeskRetriever",
    "CohereRagRetriever",
    "DriaRetriever",
    "ElasticSearchBM25Retriever",
    "EmbedchainRetriever",
    "GoogleDocumentAIWarehouseRetriever",
    "GoogleCloudEnterpriseSearchRetriever",
    "GoogleVertexAIMultiTurnSearchRetriever",
    "GoogleVertexAISearchRetriever",
    "KayAiRetriever",
    "KNNRetriever",
    "LlamaIndexGraphRetriever",
    "LlamaIndexRetriever",
    "MetalRetriever",
    "MilvusRetriever",
    "NanoPQRetriever",
    "NeedleRetriever",
    "OutlineRetriever",
    "PineconeHybridSearchRetriever",
    "PubMedRetriever",
    "QdrantSparseVectorRetriever",
    "RemoteLangChainRetriever",
    "RememberizerRetriever",
    "SVMRetriever",
    "TavilySearchAPIRetriever",
    "NeuralDBRetriever",
    "RememberizerRetriever",
    "TFIDFRetriever",
    "BM25Retriever",
    "VespaRetriever",
    "WeaviateHybridSearchRetriever",
    "WikipediaRetriever",
    "WebResearchRetriever",
    "YouRetriever",
    "ZepRetriever",
    "ZepCloudRetriever",
    "ZillizRetriever",
    "DocArrayRetriever",
    "NeuralDBRetriever",
]


def test_all_imports() -> None:
    assert set(__all__) == set(EXPECTED_ALL)
    assert set(__all__) == set(_module_lookup.keys())
