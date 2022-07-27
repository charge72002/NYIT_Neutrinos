read -p "How many beams? " nbeams
read -p "How many paths? " npaths

#make IC folders
for((i=1; i<=$npaths; i++))
	do
		mkdir IC$i
		mv TSeries_all_IC*_beta*_edit_P*z.png IC$i
	done

#organise beams in each path
for path in IC*
do
	echo
	cd $path	
	pwd
	for((i=1; i<=$nbeams; i++))
	do
		mkdir P$i
		mv TSeries_all_IC*_beta*_edit_P${i}z.png P$i
	done
	cd ..
done
