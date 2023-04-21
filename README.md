# このリポジトリについて

Azure OpenAIサービスにデプロイしたモデルに対して対話的に応答を取得するAPIリクエストサンプルです。

## 前提

 * Azure OpenAIサービスでアカウントが作られていること
 * Public AccessがAllowされていること(リソース管理>ネットワークから確認)
 * (Azure AD認証を行う場合)認証する主体がAzure OpenAIサービスアカウントに対してCognitive Services OpenAI Userロールを持っていること

## ファイルの説明

1. openai_apikey_request_sample.py

APIキーで認証する例です。

2. openai_aad_oauth_request_sample.py

Azure AD認証する例です。
（デフォルトではAZ CLIで認証する形になっていますが、コメントアウトする箇所を変えていただくことで環境変数のCLIENT_ID認証やDefaultToken取得も行えます）

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

### APIキーの定義

（APIキー認証の場合のみ)
```bash
export OPENAI_API_KEY="xxxxxxxxxxxxxxxxxxxx"
```
APIキーはポータルのAzure OpenAIアカウントの「リソース管理」 > 「キーとエンドポイント」から確認できます。

### エンドポイントの修正

* 環境に合わせて各ファイル内の ``openai.api_base`` と ``engine`` を適宜書き換えてください。
  * openai.api_base: 作成されたAzure OpenAIアカウントの概要 > エンドポイント
  * engine: Azure OpenAIアカウントのリソース管理 > モデル デプロイ から確認できるモデル デプロイ名

### 呼び出し

```bash
python openai_apikey_request_sample.py
```

```bash
python openai_aad_oauth_request_sample.py
```

特に引数は要りません。

### 参考

https://github.com/openai/openai-python
