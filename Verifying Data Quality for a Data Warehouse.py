#  download the staging area setup script:
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Verifying%20Data%20Quality%20for%20a%20Data%20Warehouse/setup_staging_area.sh



# Run the command below to execute the staging area setup script :
bash setup_staging_area.sh


# Getting the testing framework ready :
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Verifying%20Data%20Quality%20for%20a%20Data%20Warehouse/dataqualitychecks.py

wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Verifying%20Data%20Quality%20for%20a%20Data%20Warehouse/dbconnect.py

wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Verifying%20Data%20Quality%20for%20a%20Data%20Warehouse/mytests.py

wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Verifying%20Data%20Quality%20for%20a%20Data%20Warehouse/generate-data-quality-report.py

ls




# Install the python driver for Postgresql :
python3 -m pip install psycopg2


#  Test database connectivity.
# Now we need to check
# if the Postgresql python driver is installed properly.
# if Postgresql server is up and running.
# if our micro framework can connect to the database.
# The command below to check all the above cases:
python3 dbconnect.py





# Create a sample data quality report =======> Run the command below to install pandas:
python3 -m pip install pandas tabulate


# Run the command below to generate a sample data quality report:
python3 generate-data-quality-report.py


