<h2> Demo </h2>
You can find demo of all our products on our site: http://mlnn.net/

<h2> Python Millennium API Client </h2>
<h3> Preface </h3>
Installation  
To install activate a new virtual environment and run the following command:

```
$ pip install -r requirements.txt
```

<h3> Usage </h3>

<h4>Language detection API </h4>

An example call to the language detection API:

```python
import client
mlnnClient = client.MlnnClient()
response = mlnnClient.langdet(text='Example')  
```

<h4>Named Entity Recognition API (SMI) </h4>

An example call to the named entity recognition API for smi:

```python
import client
mlnnClient = client.MlnnClient()
response = mlnnClient.ner_smi(text='Example')  
```

<h4>Named Entity Recognition API (Arbitration) </h4>

An example call to the named entity recognition API for arbitration:

```python
import client
mlnnClient = client.MlnnClient()
response = mlnnClient.ner_arb(text='Example')  
```

<h3> Testing </h3>

First install the test requirements with the following command:  
```
$ pip install -r requirements_test.txt
```

Currently there are some simple unit tests. From the project directory, simply run:  
```
$ nosetests
```
