
#!/bin/sh
#dac 20150717 for krm
homepath=('/data/www/' '/app/www/')
runfile=('app/run/cupRankingDayAwardDo.php' 'app/run/cupRankingWeekAwardDo.php' 'app/run/cupRankingDo.php' 'app/run/hotTimeDo.php')
for i in ${homepath[@]};do
    [ -d ${i} ]&&{
        for j in ${runfile[@]};do
            fname=${i}${j}
            [ -f ${fname} ]&&{
                sfname=${fname//\//\\\/}
                #sed  "s/include_once '..\/config\/Main.config.inc';/include_once '${sfname}';/g" ${fname} 
            }
        done
    }
done
echo "Check crontab:"
for i in ${homepath[@]};do
    [ -d ${i} ]&&{
        for j in ${runfile[@]};do
            fname=${i}${j}
			echo $fname
            [ -f ${fname} ]&&{
                fcron=`cat /etc/crontab |grep "^[^#| ]"|grep ${fname}|wc -l`
                if [ ${fcron} == 1 ];then
                    rcron=`cat /etc/crontab|grep ${fname}`;
echo $rcron
                fi
            }
        done
    }
done
