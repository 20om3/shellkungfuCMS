#!/bin/bash -xv

dir=$(dirname $0)
exec 2> $dir/../www-data/$(basename $0).$(date +%Y%m%d%s).$$

#GETの文字列から記事ディレクトリ名を得る
page=$(tr -dc '0-9a-zA-Z_' <<< "${QUERY_STRING:2}") #()や[]の中など、いたらくくられていたら""で囲む習慣を！

#チェック
#空文字ならトップ表示
[ "$page" = "" ]	&& page=top
#ディレクトリが存在しないならトップ表示
[ -d "$dir/pages/$page" ] || page=top

echo "Content-Type: text/html"
echo
sed 's/^/\t/' $dir/pages/$page/html |

#リンク先を変える
sed "s;\(href\|src\)=\";&/pages/$page/;g"|
sed "s;\"/pages/$page/\([^:\"]*\)://;\"\1://;g"|
sed "s;\"/pages/$page//;\"?p=;g"


filehame -lDOCUMENT $dir/template.0.html -




