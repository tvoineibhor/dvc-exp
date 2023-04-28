# dvc-exp
## Stages of data sci task
- Data scientists create new branch from main.
- Data scientists make experimets and push new model.
- Data scientists create pull request for changes.
- CI pipeline: tests code and model.
- Changes are merged if all tests pass.
- Merge triggers CD pipeline for model deployment "somewhere".

## clone and run local

1. clone: 
```shell 
git clone https://github.com/tvoineibhor
```

2. crete new branch

```shell
git branch -b `name_of_ur_branch`
```

3. create venv and activate it:
```shell 
make all

source env/bin/activate .
```

4. install py req:
```shell
make install_req
```

5. login into dagshub
```shell
make login
```

6. pull the data 
```shell
dvc pull -r origin
```

## change something
1. change src/** or params.yaml

2. run repro to regenerate data pipelines

```sell
dvc repro
```

3. push new to dagsshub

```shell
dvc push -r origin
```
4. commit and push new files

```shell
git add .
git push origin `name_of_ur_branch`
```


