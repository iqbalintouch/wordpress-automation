WordPress Automation Deployment Guide
Overview
This guide provides a comprehensive walkthrough for setting up and automating the deployment of a WordPress site using AWS services. It includes steps for deploying a WordPress instance on EC2, configuring a MySQL database, automating backups, and setting up scheduled operations for your development instance.

Table of Contents
Introduction

Deployment Steps

Configuring Business Hours for Dev Instance

Setting Up Monitoring with Route 53

Conclusion

1️⃣ Introduction
This guide focuses on automating the deployment and maintenance of a WordPress site using AWS services, including EC2, RDS, and EventBridge. It covers key tasks such as setting up your WordPress site, automating instance start/stop based on business hours, and configuring DNS failover for high availability.

2️⃣ Deployment Steps
Follow these steps to deploy your WordPress site:

Set up an EC2 instance for WordPress
Follow the AWS EC2 documentation to create an EC2 instance with a suitable AMI for WordPress.

Configure a MySQL database
Use AWS RDS or install MySQL manually on your EC2 instance to manage your WordPress database.

Set up a reverse proxy (optional)
For better performance and security, configure a reverse proxy (e.g., NGINX) between the users and your WordPress site.

Automate backups
Set up scheduled backups using AWS services like EC2 snapshots or AWS Backup to ensure your data is safe.

3️⃣ Configuring Business Hours for Dev Instance (Using AWS EventBridge)
To automatically start and stop your development instance during business hours, we will use AWS EventBridge instead of AWS Instance Scheduler.

🔹 Step 3.1: Create a Rule to Start the Instance at 9 AM
Open AWS EventBridge
Navigate to AWS Console → EventBridge → Rules → Create Rule.

Configure the Rule

Rule Name: Start-Dev-Instance

Schedule Pattern: Use Cron expression

Cron Expression (for 9 AM every weekday):

Copy
Edit
0 3 ? * MON-FRI *
(AWS uses UTC, so 9 AM IST = 3:30 AM UTC, rounded to 3 AM UTC.)

Add Target

Select EC2 → StartInstances

Choose your Dev instance from the list.

Create the Rule
Click Create.

🔹 Step 3.2: Create a Rule to Stop the Instance at 6 PM
Open AWS EventBridge
Navigate to AWS Console → EventBridge → Rules → Create Rule.

Configure the Rule

Rule Name: Stop-Dev-Instance

Schedule Pattern: Use Cron expression

Cron Expression (for 6 PM every weekday):

Copy
Edit
30 12 ? * MON-FRI *
(AWS uses UTC, so 6 PM IST = 12:30 PM UTC, rounded to 12 PM UTC.)

Add Target

Select EC2 → StopInstances

Choose your Dev instance from the list.

Create the Rule
Click Create.

🔹 Step 3.3: Test the Setup
Wait for 9 AM or 6 PM to check if the instance starts/stops automatically.

Alternatively, you can manually trigger the rule by going to EventBridge → Rules → Actions → Simulate Run.

4️⃣ Setting Up Monitoring with Route 53
To monitor the health of your WordPress site, configure Route 53 health checks and DNS failover for high availability.

🔹 Step 4.1: Create a Health Check
Open AWS Route 53
Navigate to AWS Console → Route 53 → Health Checks → Create Health Check.

Configure Health Check

Name: WordPress-Health-Check

Monitor: Select Endpoint

Protocol: HTTP or HTTPS

Domain Name or IP Address: Enter your website’s URL or EC2 instance IP

Request Interval: 30 seconds

Failure Threshold: 3

Click Create.

🔹 Step 4.2: Set Up DNS Failover (Optional)
To ensure high availability, configure DNS failover:

Go to Route 53 → Hosted Zones.

Select your domain name.

Click Create Record.

Enable the Failover Routing Policy.

Set your main instance to Primary and backup instance to Secondary.

5️⃣ Conclusion
By following this guide, your WordPress site will be automated for scheduled operations, including starting and stopping the EC2 instance based on business hours. Additionally, Route 53 will monitor the health of your site and provide failover capabilities in case of any issues. This setup ensures smooth operations with minimal manual intervention. 