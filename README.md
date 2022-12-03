# quickfoo

## Create Package

```
sudo apt update
sudo apt install python3-pip
sudo apt install python3.10-venv
```

Install requirements:
```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install –-upgrade setuptools wheel
```

Build distribution:
```
python3 setup.py sdist bdist_wheel
```

Install package locally:
```
pip install -e .
```

Test installed package:
```
python3

import quickfoo
quickfoo.quicktext()
```

Install helper package:
```
python3 -m pip install --upgrade twine
```

Upload to test repo:
```
python3 -m twine upload --repository testpypi dist/*
```

Uninstall previous installed package:
```
pip uninstall quickfoo
```

Install from test repo:
```
pip install -i https://test.pypi.org/simple/ quickfoo==0.0.1
```

## multipass

```
multipass launch jammy --cpus 4 --disk 20G --mem 8G --name python-ili-build
```

```
multipass mount $HOME/sources python-ili-build:/home/ubuntu/sources
```

```
multipass mount $HOME keen-yak
```

```
multipass shell python-ili-build
```

```
multipass stop python-ili-build
```