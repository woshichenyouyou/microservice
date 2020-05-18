sleep 14400
python3 result_process.py
sleep 5
python3 ../common/sendmail.py ../result/all_result.csv
