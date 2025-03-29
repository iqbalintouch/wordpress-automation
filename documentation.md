# WordPress Automation Deployment Guide

## 1️⃣ Introduction
This guide covers the setup, deployment, and automation of a WordPress site using AWS services.

## 2️⃣ Deployment Steps
- Set up an EC2 instance for WordPress
- Configure a MySQL database
- Set up a reverse proxy (if applicable)
- Automate backups

## 3️⃣ Configuring Business Hours for Dev Instance (Using AWS EventBridge)
Instead of AWS Instance Scheduler, we'll use **AWS EventBridge** to start and stop the development instance at specific times.

### 🔹 Step 3.1: Create a Rule to Start the Instance at 9 AM
1. **Open AWS EventBridge**  
   - Go to **AWS Console → EventBridge**
   - Click **Rules → Create Rule**

2. **Configure the Rule**  
   - **Rule Name:** `Start-Dev-Instance`  
   - **Rule Type:** Schedule-based rule  
   - **Schedule Pattern:** Choose **Cron expression**  
   - **Enter this Cron Expression (for 9 AM every weekday):**  
     ```
     0 3 ? * MON-FRI *
     ```  
     *(AWS uses UTC, so 9 AM IST = 3:30 AM UTC, rounded to 3 AM UTC.)*

3. **Add Target (EC2 Instance)**  
   - Click **Add Target → EC2**  
   - Select **Action:** `StartInstances`  
   - Select **Instance ID:** (Choose your Dev instance from the list)  

4. **Create the Rule**  
   - Click **Create** ✅

### 🔹 Step 3.2: Create a Rule to Stop the Instance at 6 PM
1. **Open AWS EventBridge**
   - Go to **AWS Console → EventBridge**
   - Click **Rules → Create Rule**

2. **Configure the Rule**
   - **Rule Name:** `Stop-Dev-Instance`
   - **Rule Type:** Schedule-based rule
   - **Schedule Pattern:** Choose **Cron expression**
   - **Enter this Cron Expression (for 6 PM every weekday):**
     ```
     30 12 ? * MON-FRI *
     ```
     *(AWS uses UTC, so 6 PM IST = 12:30 PM UTC, rounded to 12 PM UTC.)*

3. **Add Target (EC2 Instance)**
   - Click **Add Target → EC2**
   - Select **Action:** `StopInstances`
   - Select **Instance ID:** (Choose your Dev instance from the list)

4. **Create the Rule**
   - Click **Create** ✅

### 🔹 Step 3.3: Test the Setup
- Wait until **9 AM or 6 PM** to see if the instance starts/stops automatically.
- Manually trigger the rule: **EventBridge → Rules → Actions → Simulate Run**

✅ DONE! Your Dev WordPress instance will now automatically start at **9 AM** and stop at **6 PM** on weekdays. 🚀

## 4️⃣ Setting Up Monitoring with Route 53

### 🔹 Step 4.1: Create a Health Check
1. **Open AWS Route 53**
   - Go to **AWS Console → Route 53 → Health Checks**
   - Click **Create Health Check**

2. **Configure Health Check**
   - **Name:** `WordPress-Health-Check`
   - **What to Monitor?** Select `Endpoint`
   - **Protocol:** HTTP or HTTPS (depending on your site)
   - **Domain Name or IP Address:** Enter your website's URL or EC2 instance IP
   - **Request Interval:** 30 seconds
   - **Failure Threshold:** 3

3. **Click Create** ✅

### 🔹 Step 4.2: Set Up DNS Failover (Optional)
If you want automatic failover to another instance:
1. **Go to Route 53 → Hosted Zones**
2. Select your domain name
3. Click **Create Record**
4. **Enable Failover Routing Policy**
5. Choose **Primary** for your main instance
6. Choose **Secondary** for your backup instance

✅ DONE! Route 53 will now monitor your site and provide failover if needed. 🚀

## 5️⃣ Conclusion
With this setup, your WordPress site is now **automated, scheduled, and monitored**, ensuring smooth operations and minimal manual intervention.
