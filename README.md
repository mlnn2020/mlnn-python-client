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
response = mlnnClient.request(text='English')  
```

<h3> Testing </h3>

First install the test requirements with the following command:  
```
$ pip install -r test_requirements.txt
```

Currently there are some simple unit tests. From the project directory, simply run:  
```
$ nosetests
```
