### 使用说明

1. 建议安装anaconda

> 添加 channels bioconda

```
conda config --add channels bioconda
```

2. 然后执行

``` conda install --file requirements.txt ```


### 测试

1. siege

```
siege  -c 20 -r 1 "http://localhost/users/users/"
```

2. wrk

```
wrk -t12 -c400 -d30s http://localhost/users/users/
```


