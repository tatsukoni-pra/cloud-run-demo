## ローカル環境起動方法

以下コマンド実行後、`http://0.0.0.0:8080/` にてアクセス可能。

```
$ docker build -t flask-cloud-run-demo .
$ docker run -p 8080:8080 -e PORT=8080 flask-cloud-run-demo
```
