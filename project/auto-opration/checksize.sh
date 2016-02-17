#!/bin/sh
ipath=/data/www/qacdn/assetbundles/iphone/
[ -d ${ipath} ] || {
        echo "Not exist ${ipath}!";
}
ixml=CheckList.xml
[ -f ${ipath}${ixml} ] || {
        echo "Not exist ${ipath}${ixml}!";
}
tmpf1=tmpf1.log
tmpf2=tmpf2.log
clearlog(){
        [ -f ${tmpf1} ] && {
                #echo > ${tmpf1};
                rm -f ${tmpf1};
        }
        [ -f ${tmpf2} ] && {
                #echo > ${tmpf2};
                rm -f ${tmpf2};
        }
}
checkmd5(){
ls -l ${1}*.assetbundle | awk -F" " '{print $5}' | sort>>${tmpf1}
cat ${1}${2} | grep md5 | awk -F"<length>" '{print $2}' | awk -F"</length>" '{print $1}' | sort>>${tmpf2}
echo "Starting diff ${1}${2}..............";
diff ${tmpf1} ${tmpf2}
echo "Diff end...................";
}
checkmd5 ${ipath} ${ixml}
clearlog
