# MovableType-Editor

このライブラリは、MovableType形式のエクスポートファイルに含まれた記事データを編集するためのライブラリです。

現在は、カテゴリ情報の編集に特化しています。

# 使い方

まずは、パッケージを読み込みます。

```
>>> import mt_editor.article as article
```

ブログインスタンスを作って、エクスポートファイルを読み込みます。

```
>>> myBlog = article.Blog()
>>> myBlog.load('/path/to/my/export/file.txt')
```

読み込んだブログ記事に、セットされているカテゴリをリセットしたい場合、次のメソッドを実行します。

```
>>> myBlog.reset_all_article_category()
```

読み込んだブログ記事に、セットされているカテゴリの一覧を確認したい場合、次のメソッドを実行します。

```
>>> myBlog.get_all_category()
```

記事に、カテゴリを設定したい場合、次のメソッドが便利です。
次のメソッドを実行すると、タイトルもしくは、本文に `Python` と言う文字が含まれている記事に `Python` カテゴリがセットされます。
```
>>> myBlog.try_paste_category('Python')
```


