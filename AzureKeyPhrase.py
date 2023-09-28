from asyncio import constants
from queue import Empty
from xml.dom.minidom import Document
import Environment
import Constants
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

credential = AzureKeyCredential(Environment.key)
text_analytics_client = TextAnalyticsClient(endpoint=Environment.endpoint, credential=credential)

def azureService(document, active):
    if active==True and document is not Empty:
        response = text_analytics_client.extract_key_phrases(document)
        return score(response[0].key_phrases)
    else:
        return 0


def score(keyphrase):
    score = 0
    for x in Constants.keyWords:
        for y in keyphrase:
            if (x in y.lower()):
                score += 1
    return score
            




