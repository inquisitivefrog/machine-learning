
AWS SageMaker AI
----------------
1. Create a Quick Setup Domain
2. click on domain name, find User Profiles tab and Launch user profile as Studio
3. from SageMaker Studio tab, click on Open JupyterLab icon to start NoteBook in new tab
   choose personal not collaborative
4. Select Terminal and click
5. clone the AWS SageMaker examples from GitHub
   sagemaker-user@default:~/amazon-sagemaker-examples$ git clone https://github.com/aws/amazon-sagemaker-examples.git
6. update the branch as the default branch does not contain XGBoost Customer Churn Noteebook file
   sagemaker-user@default:~/amazon-sagemaker-examples$ git checkout main
   sagemaker-user@default:~/amazon-sagemaker-examples$ git stash
   sagemaker-user@default:~/amazon-sagemaker-examples$ git checkout main
   sagemaker-user@default:~/amazon-sagemaker-examples$ git pull origin main
   sagemaker-user@default:~/amazon-sagemaker-examples$ find /home/sagemaker-user/amazon-sagemaker-examples -name "xgboost_customer_churn_s

JupyterLabs
-----------
1. In the SageMaker Studio JupyterLab UI, navigate to the notebook in the File Browser 
2. select /home/sagemaker-user/amazon-sagemaker-examples/aws_sagemaker_studio/getting_started/xgboost_customer_churn_studio.ipynb
3. Double-click xgboost_customer_churn_studio.ipynb to open it
4. Select Python 3 (ipykernel) from the list
5. Wait for the kernel to initialize (you’ll see a status indicator, like a circle, change to “idle”)

New Terminal
------------
sagemaker-user@default:~/amazon-sagemaker-examples$ pip3 install --upgrade jupyter boto3 aws-glue-sessions
sagemaker-user@default:~/amazon-sagemaker-examples$ install-glue-kernels
sagemaker-user@default:~/amazon-sagemaker-examples$ pip install sagemaker awswrangler pandas numpy
Requirement already satisfied: sagemaker in /opt/conda/lib/python3.12/site-packages (2.242.0)
Collecting awswrangler
  Downloading awswrangler-3.11.0-py3-none-any.whl.metadata (17 kB)
Requirement already satisfied: pandas in /opt/conda/lib/python3.12/site-packages (2.2.3)
Requirement already satisfied: numpy in /opt/conda/lib/python3.12/site-packages (1.26.4)
Requirement already satisfied: attrs<24,>=23.1.0 in /opt/conda/lib/python3.12/site-packages (from sagemaker) (23.2.0)
Requirement already satisfied: boto3<2.0,>=1.35.75 in /opt/conda/lib/python3.12/site-packages (from sagemaker) (1.38.22)
Requirement already satisfied: cloudpickle>=2.2.1 in /opt/conda/lib/python3.12/site-packages (from sagemaker) (3.1.1)
Requirement already satisfied: docker in /opt/conda/lib/python3.12/site-packages (from sagemaker) (7.1.0)
Requirement already satisfied: fastapi in /opt/conda/lib/python3.12/site-packages (from sagemaker) (0.115.12)
Requirement already satisfied: google-pasta in /opt/conda/lib/python3.12/site-packages (from sagemaker) (0.2.0)
Requirement already satisfied: importlib-metadata<7.0,>=1.4.0 in /opt/conda/lib/python3.12/site-packages (from sagemaker) (6.10.0)
Requirement already satisfied: jsonschema in /opt/conda/lib/python3.12/site-packages (from sagemaker) (4.23.0)
Requirement already satisfied: omegaconf<=2.3,>=2.2 in /opt/conda/lib/python3.12/site-packages (from sagemaker) (2.3.0)
Requirement already satisfied: packaging>=20.0 in /opt/conda/lib/python3.12/site-packages (from sagemaker) (24.2)
Requirement already satisfied: pathos in /opt/conda/lib/python3.12/site-packages (from sagemaker) (0.3.4)
Requirement already satisfied: platformdirs in /opt/conda/lib/python3.12/site-packages (from sagemaker) (4.3.7)
Requirement already satisfied: protobuf<6.0,>=3.12 in /opt/conda/lib/python3.12/site-packages (from sagemaker) (5.28.3)
Requirement already satisfied: psutil in /opt/conda/lib/python3.12/site-packages (from sagemaker) (5.9.8)
Requirement already satisfied: pyyaml~=6.0 in /opt/conda/lib/python3.12/site-packages (from sagemaker) (6.0.2)
Requirement already satisfied: requests in /opt/conda/lib/python3.12/site-packages (from sagemaker) (2.32.3)
Requirement already satisfied: sagemaker-core<2.0.0,>=1.0.17 in /opt/conda/lib/python3.12/site-packages (from sagemaker) (1.0.31)
Requirement already satisfied: schema in /opt/conda/lib/python3.12/site-packages (from sagemaker) (0.7.7)
Requirement already satisfied: smdebug-rulesconfig==1.0.1 in /opt/conda/lib/python3.12/site-packages (from sagemaker) (1.0.1)
Requirement already satisfied: tblib<4,>=1.7.0 in /opt/conda/lib/python3.12/site-packages (from sagemaker) (3.1.0)
Requirement already satisfied: tqdm in /opt/conda/lib/python3.12/site-packages (from sagemaker) (4.67.1)
Requirement already satisfied: urllib3<3.0.0,>=1.26.8 in /opt/conda/lib/python3.12/site-packages (from sagemaker) (2.4.0)
Requirement already satisfied: uvicorn in /opt/conda/lib/python3.12/site-packages (from sagemaker) (0.34.2)
Requirement already satisfied: botocore<2.0.0,>=1.23.32 in /opt/conda/lib/python3.12/site-packages (from awswrangler) (1.38.22)
Collecting pyarrow<19.0.0,>=8.0.0 (from awswrangler)
  Downloading pyarrow-18.1.0-cp312-cp312-manylinux_2_28_x86_64.whl.metadata (3.3 kB)
Requirement already satisfied: setuptools in /opt/conda/lib/python3.12/site-packages (from awswrangler) (80.1.0)
Requirement already satisfied: typing-extensions<5.0.0,>=4.4.0 in /opt/conda/lib/python3.12/site-packages (from awswrangler) (4.13.2)
Requirement already satisfied: python-dateutil>=2.8.2 in /opt/conda/lib/python3.12/site-packages (from pandas) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in /opt/conda/lib/python3.12/site-packages (from pandas) (2024.2)
Requirement already satisfied: tzdata>=2022.7 in /opt/conda/lib/python3.12/site-packages (from pandas) (2025.2)
Requirement already satisfied: jmespath<2.0.0,>=0.7.1 in /opt/conda/lib/python3.12/site-packages (from boto3<2.0,>=1.35.75->sagemaker) (1.0.1)
Requirement already satisfied: s3transfer<0.14.0,>=0.13.0 in /opt/conda/lib/python3.12/site-packages (from boto3<2.0,>=1.35.75->sagemaker) (0.13.0)
Requirement already satisfied: zipp>=0.5 in /opt/conda/lib/python3.12/site-packages (from importlib-metadata<7.0,>=1.4.0->sagemaker) (3.21.0)
Requirement already satisfied: antlr4-python3-runtime==4.9.* in /opt/conda/lib/python3.12/site-packages (from omegaconf<=2.3,>=2.2->sagemaker) (4.9.3)
Requirement already satisfied: six>=1.5 in /opt/conda/lib/python3.12/site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)
Requirement already satisfied: pydantic<3.0.0,>=2.0.0 in /opt/conda/lib/python3.12/site-packages (from sagemaker-core<2.0.0,>=1.0.17->sagemaker) (2.11.3)
Requirement already satisfied: rich<14.0.0,>=13.0.0 in /opt/conda/lib/python3.12/site-packages (from sagemaker-core<2.0.0,>=1.0.17->sagemaker) (13.9.4)
Requirement already satisfied: mock<5.0,>4.0 in /opt/conda/lib/python3.12/site-packages (from sagemaker-core<2.0.0,>=1.0.17->sagemaker) (4.0.3)
Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /opt/conda/lib/python3.12/site-packages (from jsonschema->sagemaker) (2025.4.1)
Requirement already satisfied: referencing>=0.28.4 in /opt/conda/lib/python3.12/site-packages (from jsonschema->sagemaker) (0.36.2)
Requirement already satisfied: rpds-py>=0.7.1 in /opt/conda/lib/python3.12/site-packages (from jsonschema->sagemaker) (0.24.0)
Requirement already satisfied: charset_normalizer<4,>=2 in /opt/conda/lib/python3.12/site-packages (from requests->sagemaker) (3.4.2)
Requirement already satisfied: idna<4,>=2.5 in /opt/conda/lib/python3.12/site-packages (from requests->sagemaker) (3.10)
Requirement already satisfied: certifi>=2017.4.17 in /opt/conda/lib/python3.12/site-packages (from requests->sagemaker) (2025.1.31)
Requirement already satisfied: starlette<0.47.0,>=0.40.0 in /opt/conda/lib/python3.12/site-packages (from fastapi->sagemaker) (0.46.2)
Requirement already satisfied: ppft>=1.7.7 in /opt/conda/lib/python3.12/site-packages (from pathos->sagemaker) (1.7.7)
Requirement already satisfied: dill>=0.4.0 in /opt/conda/lib/python3.12/site-packages (from pathos->sagemaker) (0.4.0)
Requirement already satisfied: pox>=0.3.6 in /opt/conda/lib/python3.12/site-packages (from pathos->sagemaker) (0.3.6)
Requirement already satisfied: multiprocess>=0.70.18 in /opt/conda/lib/python3.12/site-packages (from pathos->sagemaker) (0.70.18)
Requirement already satisfied: click>=7.0 in /opt/conda/lib/python3.12/site-packages (from uvicorn->sagemaker) (8.1.8)
Requirement already satisfied: h11>=0.8 in /opt/conda/lib/python3.12/site-packages (from uvicorn->sagemaker) (0.16.0)
Requirement already satisfied: annotated-types>=0.6.0 in /opt/conda/lib/python3.12/site-packages (from pydantic<3.0.0,>=2.0.0->sagemaker-core<2.0.0,>=1.0.17->sagemaker) (0.7.0)
Requirement already satisfied: pydantic-core==2.33.1 in /opt/conda/lib/python3.12/site-packages (from pydantic<3.0.0,>=2.0.0->sagemaker-core<2.0.0,>=1.0.17->sagemaker) (2.33.1)
Requirement already satisfied: typing-inspection>=0.4.0 in /opt/conda/lib/python3.12/site-packages (from pydantic<3.0.0,>=2.0.0->sagemaker-core<2.0.0,>=1.0.17->sagemaker) (0.4.0)
Requirement already satisfied: markdown-it-py>=2.2.0 in /opt/conda/lib/python3.12/site-packages (from rich<14.0.0,>=13.0.0->sagemaker-core<2.0.0,>=1.0.17->sagemaker) (3.0.0)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /opt/conda/lib/python3.12/site-packages (from rich<14.0.0,>=13.0.0->sagemaker-core<2.0.0,>=1.0.17->sagemaker) (2.19.1)
Requirement already satisfied: anyio<5,>=3.6.2 in /opt/conda/lib/python3.12/site-packages (from starlette<0.47.0,>=0.40.0->fastapi->sagemaker) (4.9.0)
Requirement already satisfied: sniffio>=1.1 in /opt/conda/lib/python3.12/site-packages (from anyio<5,>=3.6.2->starlette<0.47.0,>=0.40.0->fastapi->sagemaker) (1.3.1)
Requirement already satisfied: mdurl~=0.1 in /opt/conda/lib/python3.12/site-packages (from markdown-it-py>=2.2.0->rich<14.0.0,>=13.0.0->sagemaker-core<2.0.0,>=1.0.17->sagemaker) (0.1.2)
Downloading awswrangler-3.11.0-py3-none-any.whl (379 kB)
Downloading pyarrow-18.1.0-cp312-cp312-manylinux_2_28_x86_64.whl (40.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 40.1/40.1 MB 64.3 MB/s eta 0:00:00
Installing collected packages: pyarrow, awswrangler
  Attempting uninstall: pyarrow
    Found existing installation: pyarrow 19.0.1
    Uninstalling pyarrow-19.0.1:
      Successfully uninstalled pyarrow-19.0.1
Successfully installed awswrangler-3.11.0 pyarrow-18.1.0
sagemaker-user@default:~/amazon-sagemaker-examples$ pip install ipykernel
Requirement already satisfied: ipykernel in /opt/conda/lib/python3.12/site-packages (6.29.5)
Requirement already satisfied: comm>=0.1.1 in /opt/conda/lib/python3.12/site-packages (from ipykernel) (0.2.2)
Requirement already satisfied: debugpy>=1.6.5 in /opt/conda/lib/python3.12/site-packages (from ipykernel) (1.8.14)
Requirement already satisfied: ipython>=7.23.1 in /opt/conda/lib/python3.12/site-packages (from ipykernel) (8.34.0)
Requirement already satisfied: jupyter-client>=6.1.12 in /opt/conda/lib/python3.12/site-packages (from ipykernel) (8.6.3)
Requirement already satisfied: jupyter-core!=5.0.*,>=4.12 in /opt/conda/lib/python3.12/site-packages (from ipykernel) (5.7.2)
Requirement already satisfied: matplotlib-inline>=0.1 in /opt/conda/lib/python3.12/site-packages (from ipykernel) (0.1.7)
Requirement already satisfied: nest-asyncio in /opt/conda/lib/python3.12/site-packages (from ipykernel) (1.6.0)
Requirement already satisfied: packaging in /opt/conda/lib/python3.12/site-packages (from ipykernel) (24.2)
Requirement already satisfied: psutil in /opt/conda/lib/python3.12/site-packages (from ipykernel) (5.9.8)
Requirement already satisfied: pyzmq>=24 in /opt/conda/lib/python3.12/site-packages (from ipykernel) (26.4.0)
Requirement already satisfied: tornado>=6.1 in /opt/conda/lib/python3.12/site-packages (from ipykernel) (6.4.2)
Requirement already satisfied: traitlets>=5.4.0 in /opt/conda/lib/python3.12/site-packages (from ipykernel) (5.14.3)
Requirement already satisfied: decorator in /opt/conda/lib/python3.12/site-packages (from ipython>=7.23.1->ipykernel) (5.2.1)
Requirement already satisfied: jedi>=0.16 in /opt/conda/lib/python3.12/site-packages (from ipython>=7.23.1->ipykernel) (0.19.2)
Requirement already satisfied: pexpect>4.3 in /opt/conda/lib/python3.12/site-packages (from ipython>=7.23.1->ipykernel) (4.9.0)
Requirement already satisfied: prompt_toolkit<3.1.0,>=3.0.41 in /opt/conda/lib/python3.12/site-packages (from ipython>=7.23.1->ipykernel) (3.0.51)
Requirement already satisfied: pygments>=2.4.0 in /opt/conda/lib/python3.12/site-packages (from ipython>=7.23.1->ipykernel) (2.19.1)
Requirement already satisfied: stack_data in /opt/conda/lib/python3.12/site-packages (from ipython>=7.23.1->ipykernel) (0.6.3)
Requirement already satisfied: python-dateutil>=2.8.2 in /opt/conda/lib/python3.12/site-packages (from jupyter-client>=6.1.12->ipykernel) (2.9.0.post0)
Requirement already satisfied: platformdirs>=2.5 in /opt/conda/lib/python3.12/site-packages (from jupyter-core!=5.0.*,>=4.12->ipykernel) (4.3.7)
Requirement already satisfied: parso<0.9.0,>=0.8.4 in /opt/conda/lib/python3.12/site-packages (from jedi>=0.16->ipython>=7.23.1->ipykernel) (0.8.4)
Requirement already satisfied: ptyprocess>=0.5 in /opt/conda/lib/python3.12/site-packages (from pexpect>4.3->ipython>=7.23.1->ipykernel) (0.7.0)
Requirement already satisfied: wcwidth in /opt/conda/lib/python3.12/site-packages (from prompt_toolkit<3.1.0,>=3.0.41->ipython>=7.23.1->ipykernel) (0.2.13)
Requirement already satisfied: six>=1.5 in /opt/conda/lib/python3.12/site-packages (from python-dateutil>=2.8.2->jupyter-client>=6.1.12->ipykernel) (1.17.0)
Requirement already satisfied: executing>=1.2.0 in /opt/conda/lib/python3.12/site-packages (from stack_data->ipython>=7.23.1->ipykernel) (2.2.0)
Requirement already satisfied: asttokens>=2.1.0 in /opt/conda/lib/python3.12/site-packages (from stack_data->ipython>=7.23.1->ipykernel) (3.0.0)
Requirement already satisfied: pure_eval in /opt/conda/lib/python3.12/site-packages (from stack_data->ipython>=7.23.1->ipykernel) (0.2.3)
sagemaker-user@default:~/amazon-sagemaker-examples$ python -m ipykernel install --user --name py3ml --display-name "Python 3 (py3ml)"
Installed kernelspec py3ml in /home/sagemaker-user/.local/share/jupyter/kernels/py3ml
sagemaker-user@default:~/amazon-sagemaker-examples$ 

File/Shutdown Terminal
Kernel/Change Kernel
Select new Kernel Python py3ml
With Notebook file open, click Play button at top of terminal, it will step through JSON file
attempting to complete each section.  Watch for error

New Terminal#2
--------------
pip install -qU awscli boto3 "sagemaker>=1.71.0,<2.0.0"
pip install sagemaker-experiments

