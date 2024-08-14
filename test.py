import sagemaker
import boto3
from sagemaker import get_execution_role

region = boto3.Session().region_name

session = sagemaker.Session()

# You can modify the following to use a bucket of your choosing
bucket = session.default_bucket()
prefix = "sagemaker/DEMO-autopilot-churn"

role = get_execution_role()

# This is the client we will use to interact with SageMaker AutoPilot
sm = boto3.Session().client(service_name="sagemaker", region_name=region)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import os
import sys
import time
import json
from IPython.display import display
from time import strftime, gmtime
import boto3
import sagemaker
#from sagemaker.predictor import csv_serializer
from sagemaker.serializers import CSVSerializer

s3 = boto3.client("s3")
s3.download_file(
    f"sagemaker-example-files-prod-{region}", "datasets/tabular/synthetic/churn.txt", "churn.txt"
)

churn = pd.read_csv("./churn.txt")
pd.set_option("display.max_columns", 500)
print(churn)