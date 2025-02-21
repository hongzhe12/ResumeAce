from sparkai.core.outputs import LLMResult
from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage

#星火认知大模型Spark Max的URL值，其他版本大模型URL值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
SPARKAI_URL = 'wss://spark-api.xf-yun.com/v4.0/chat'
#星火认知大模型调用秘钥信息，请前往讯飞开放平台控制台（https://console.xfyun.cn/services/bm35）查看
SPARKAI_APP_ID = 'd556db59'
SPARKAI_API_SECRET = 'ZWZlZmMzMWIyZDg5ZGI5YzdhMjAzZTFk'
SPARKAI_API_KEY = '6e8ce352b289b970b4fe335a426f0320'


#星火认知大模型Spark Max的domain值，其他版本大模型domain值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
SPARKAI_DOMAIN = '4.0Ultra'

def get_xinghuo_response(user_input):
    """
    获取星火大模型的回复
    :param user_input: 用户输入的内容
    :return: 大模型的回复
    """
    spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=True,
        request_timeout=10
    )
    messages = [ChatMessage(
        role="user",
        content=user_input
    )]
    handler = ChunkPrintHandler()
    response = spark.generate([messages], callbacks=[handler])
    return response


if __name__ == '__main__':
    spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=False,
    )
    messages = [ChatMessage(
        role="user",
        content='你好呀'
    )]
    handler = ChunkPrintHandler()
    result = spark.generate([messages], callbacks=[handler])
    # 从结果中提取回复文本
    if isinstance(result, LLMResult):
        # 通常 generations 是一个二维列表，这里假设取第一个生成结果
        first_generation = result.generations[0][0]
        reply_text = first_generation.text
    else:
        print("结果不是 LLMResult 类型")
