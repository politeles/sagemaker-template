#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import sagemaker
from flask import Flask,render_template
from transformers import pipeline;
import os
import boto3

app = Flask(__name__)

def test_hugging_face():
    return pipeline('sentiment-analysis')('we love you')

hf_data = test_hugging_face()


@app.route("/")
def hello():
    #testing hugging face library
    return render_template("index.html",data=hf_data)
