# このリポジトリについて

Azure OpenAIサービスにデプロイしたモデルに対して対話的に応答を取得するAPIリクエストサンプルです。

## 前提

 * Azure OpenAIサービスでアカウントが作られていること
 * Public AccessがAllowされていること(リソース管理>ネットワークから確認)
 * (EntraID認証を行う場合)認証する主体がAzure OpenAIサービスアカウントに対してCognitive Services OpenAI Userロールを持っていること

## ファイルの説明

1. openai_apikey_request_sample.py

APIキーで認証する例です。

2. openai_aad_oauth_request_sample.py

EntraID認証する例です。

3. openai_apikey_request_async_sample.py

APIキーで認証、かつストリーム取得の例です。また、このサンプルでは``AsyncAzureOpenAI``を用いることで並列実行にも対応しています。

4. openai_entraid_oauth_request_async_sample.py

EntraID認証、かつ非同期取得の例です。

## 使い方

### パッケージのインストール
#### Option 1: Pythonが既にローカルにインストールされている場合
```bash
pip install -r requirements.txt
```
#### Option 2: dev containerを使う場合
以下の手順を使うと、`.devcontainer/devcontainer.json`に指定しているdev containerが起動し、その中からVS Codeが起動します。Python・Azure CLI・requirementsがインストールされている環境でVS Codeが再起動されます。
1. VS CodeのCommand Palette（Ctrl + Shift + P）を開き
2. Dev Containers: Reopen in Containerを選択

### 変数の定義

（値は例です、OPENAI_API_KEYはAPIキー認証の場合のみ)
```bash
export MODEL_DEPLOY_NAME="yourmodeldeployname"
export AOAI_ENDPOINT="https://youraoai.openai.azure.com/"
export API_VERSION="2024-02-01"
export OPENAI_API_KEY="xxxxxxxxxxxxxxxxxxxx"
```
* APIキーはポータルのAzure OpenAIアカウントの「リソース管理」 > 「キーとエンドポイント」から確認できます。
* APIバージョンについては ``https://learn.microsoft.com/ja-jp/azure/ai-services/openai/reference`` で確認ください

### 呼び出し
引数は特に不要です

```bash
python openai_apikey_request_sample.py
```

```bash
python openai_aad_oauth_request_sample.py
```

特に引数は要りません。

### 参考

https://github.com/openai/openai-python
