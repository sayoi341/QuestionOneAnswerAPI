# API仕様書



## ~~生存報告~~ 済

| メゾット | GET                         |
| -------- | --------------------------- |
| URL      | `hello`                     |
| curl     | `curl localhost:5000/hello` |

```json
{"massage" : "hello"}
```



---



## 問題集系



### ~~問題集一覧~~ 済

| メゾット | GET                        |
| -------- | -------------------------- |
| URL      | `dics`                     |
| curl     | `curl localhost:5000/dics` |



```json
{
	"1" : "($任意の問題集名)",
    "2" : "($任意の問題集名)"
}
```



### ~~問題集追加~~ 済

| メゾット | POST                                                         |
| -------- | ------------------------------------------------------------ |
| URL      | `dics`                                                       |
| curl     | `curl -X POST -H 'Content-Type:application/json' -d '{"dic": "($任意の問題集名)"}' localhost:5000/dics` |



```json
{
    "massage" : "new Dictionary created!"
}
```



### 問題集削除

| メゾット | DELETE                                             |
| -------- | -------------------------------------------------- |
| URL      | `dics`                                             |
| curl     | `curl -X DELETE localhost:5000/dics/($問題集番号)` |

```json
{
	"message" : "Dictionary ($削除した問題集名) deleted"
}
```



### 問題集名変更

| メゾット | PUT                                                          |
| -------- | ------------------------------------------------------------ |
| URL      | `dics`                                                       |
| curl     | `curl -X PUT -H 'Accept:application/json' -H 'Content-Type:application/json' -d '{"dic": "($変更後問題集名)"}' localhost:5000/dics/($問題集番号)` |

```json
{
    "messeage" : "Dictionary ($問題集番号) is changed to ($変更後問題襲名)"
}
```



---



## 個別問題集

