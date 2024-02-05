#!/bin/bash

#GIT
alias pull='git pull'
alias add='git add'
alias branch='git branch'
alias commit='git commit -a'
alias push='git push'
alias status='git status'
alias log='git log'

Compress() {
    if [[ -n "$1" ]]; then
        FILE=$1
        case $FILE in
        *.tar ) shift && tar cf $FILE $* ;;
    *.tar.bz2 ) shift && tar cjf $FILE $* ;;
     *.tar.gz ) shift && tar czf $FILE $* ;;
        *.tgz ) shift && tar czf $FILE $* ;;
        *.zip ) shift && zip $FILE $* ;;
        *.rar ) shift && rar $FILE $* ;;
        esac
      else
        echo "usage: compress <foo.tar.gz> ./foo ./bar"
      fi
    echo "Compression successful. Output file: $output_file"
}
#extract all archives!
Extract () {
   if [ -f $1 ] ; then
       case $1 in
	*.tar.bz2)	tar xvjf $1;;
	*.tar.gz)	tar xvzf $1;;
	*.tar.xz)	tar Jxvf $1;;
	*.bz2)		bunzip2 $1;;
	*.rar)		unrar x $1;;
	*.gz)		gunzip $1;;
	*.tar)		tar xvf $1;;
	*.tbz2)		tar xvjf $1;;
	*.tgz)		tar xvzf $1;;
	*.zip)		unzip $1;;
	*.Z)		uncompress $1;;
	*.7z)		7z x $1;;
	*)		echo "don't know how to extract '$1'..." ;;
       esac
   else
       echo "'$1' is not a valid file!"
   fi
 }
