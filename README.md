# Repro Serverless Requirements


This is a reproduction of trying to install a Python package located in a sub-directory from Github within the [`serverless-python-requirments`](https://github.com/UnitedIncome/serverless-python-requirements).


## Verify

You can verify that the package can be installed by running the following locally:

```bash
pip install git+https://github.com/bryantbiggs/repro-serverless-requirements.git@master#"egg=sdk&subdirectory=sdk"
```

Then from a ipython or whatever repl/shell:
```python
In [1]: from sdk.foo import foo
In [2]: foo()
Out[2]: b'<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" ...
```

## Setup

Install `serverless` requirements:

```bash
$ cd serverless && npm i
```

## Deploy

From within the `serverless/` directory:

```bash
$ SLS_DEBUG=* sls deploy --stage=dev
```

Currently this returns an error:

```
Serverless: Docker Image: lambci/lambda:build-python3.6
Collecting git+https://github.com/bryantbiggs/repro-serverless-requirements.git@master#"egg=sdk&subdirectory=sdk" (from -r /var/task/requirements.txt (line 1))
  Cloning https://github.com/bryantbiggs/repro-serverless-requirements.git (to revision master) to /tmp/pip-req-build-0erop1zh
    Complete output from command python setup.py egg_info:
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/var/lang/lib/python3.6/tokenize.py", line 452, in open
        buffer = _builtin_open(filename, 'rb')
    FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pip-req-build-0erop1zh/sdk"/setup.py'

    ----------------------------------------
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-req-build-0erop1zh/sdk"

  Error --------------------------------------------------

  null

     For debugging logs, run again after setting the "SLS_DEBUG=*" environment variable.

  Stack Trace --------------------------------------------

Error: null
    at installRequirements (/Users/B2/Downloads/repro-serverless-requirements/serverless/node_modules/serverless-python-requirements/lib/pip.js:247:11)
    at installRequirementsIfNeeded (/Users/B2/Downloads/repro-serverless-requirements/serverless/node_modules/serverless-python-requirements/lib/pip.js:423:3)
    at ServerlessPythonRequirements.installAllRequirements (/Users/B2/Downloads/repro-serverless-requirements/serverless/node_modules/serverless-python-requirements/lib/pip.js:502:29)
From previous event:
    at PluginManager.invoke (/Users/B2/.nvm/versions/node/v8.11.4/lib/node_modules/serverless/lib/classes/PluginManager.js:390:22)
    at PluginManager.spawn (/Users/B2/.nvm/versions/node/v8.11.4/lib/node_modules/serverless/lib/classes/PluginManager.js:408:17)
    at Deploy.BbPromise.bind.then.then (/Users/B2/.nvm/versions/node/v8.11.4/lib/node_modules/serverless/lib/plugins/deploy/deploy.js:123:50)
From previous event:
    at Object.before:deploy:deploy [as hook] (/Users/B2/.nvm/versions/node/v8.11.4/lib/node_modules/serverless/lib/plugins/deploy/deploy.js:113:10)
    at BbPromise.reduce (/Users/B2/.nvm/versions/node/v8.11.4/lib/node_modules/serverless/lib/classes/PluginManager.js:390:55)
From previous event:
    at PluginManager.invoke (/Users/B2/.nvm/versions/node/v8.11.4/lib/node_modules/serverless/lib/classes/PluginManager.js:390:22)
    at PluginManager.run (/Users/B2/.nvm/versions/node/v8.11.4/lib/node_modules/serverless/lib/classes/PluginManager.js:421:17)
    at variables.populateService.then.then (/Users/B2/.nvm/versions/node/v8.11.4/lib/node_modules/serverless/lib/Serverless.js:157:33)
    at runCallback (timers.js:810:20)
    at tryOnImmediate (timers.js:768:5)
    at processImmediate [as _immediateCallback] (timers.js:745:5)
From previous event:
    at Serverless.run (/Users/B2/.nvm/versions/node/v8.11.4/lib/node_modules/serverless/lib/Serverless.js:144:8)
    at serverless.init.then (/Users/B2/.nvm/versions/node/v8.11.4/lib/node_modules/serverless/bin/serverless:43:50)
    at <anonymous>

  Get Support --------------------------------------------
     Docs:          docs.serverless.com
     Bugs:          github.com/serverless/serverless/issues
     Issues:        forum.serverless.com

  Your Environment Information -----------------------------
     OS:                     darwin
     Node Version:           8.11.4
     Serverless Version:     1.31.0
```