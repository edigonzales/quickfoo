# quickfoo

## Ideen / Frage

- ili2gpkg!!!!

- "Korrekter" wäre wohl der Weg ohne `--plat-name`. Soweit ich es verstehe, benötige ich dazu einen custom build Befehl, der mit die shared lib mit GraalVM buildet. Siehe z.B. https://jichu4n.com/posts/how-to-add-custom-build-steps-and-commands-to-setuppy/ 
- Projektstruktur nochmals überdenken bzw. einlesen. Gibt es dazu irgendein Skript?
- Wie muss/kann die Shared Lib getestet werden?
- Python Tests ganz allgemein?
- source dist sollte m.E. keine shared libs enthalten, da diese os abhängig sind. 
- Welche Python-Version? Mit 3.8 muss 3rd party importlib-resources verwendet werden.

## Create Package

```
sudo apt update
sudo apt install python3-pip
sudo apt install python3.10-venv
sudo apt-get install unzip zip
sudo apt-get install build-essential libz-dev zlib1g-dev
```

Install requirements:
```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade setuptools wheel
```

Build distribution:
```
python3 setup.py sdist bdist_wheel
python3 setup.py sdist bdist_wheel --plat-name=manylinux2014_aarch64 
```
manylinux2014_x86_64
macosx_11_0_x86_64
win_amd64

manylinux2014_aarch64 
macosx_11_0_arm64

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

Install Java etc.
```
curl -s "https://get.sdkman.io" | bash
source ...
sdk i java 22.3.r17-grl
```

## GraalVM

