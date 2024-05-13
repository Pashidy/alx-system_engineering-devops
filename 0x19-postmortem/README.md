Postmortem: Outage Incident - Web Server Downtime

Issue Summary:

Duration: The outage occurred on May 2, 2024, from 10:00 AM to 12:00 PM (WAT).
Impact: The web server hosting our company's website experienced downtime during the outage,
resulting in 100% of users being unable to access the website.
Users attempting to visit the site received a "Server Unavailable" error message.
Root Cause: The root cause of the outage was identified as a misconfiguration in the web server's 
firewall settings, which inadvertently blocked all incoming traffic to the server.
Timeline:

10:00 AM (WAT): The issue was detected when monitoring alerts indicated a sudden drop in server traffic.
10:05 AM (WAT): Engineers noticed the issue when attempting to access the website for routine maintenance tasks.
10:10 AM (WAT): Initial investigation focused on checking server logs and network connectivity to identify the cause of the downtime.
10:30 AM (WAT): Assumption was made that the outage might be due to a DDoS attack or server overload.
10:45 AM (WAT): The incident was escalated to the infrastructure team for further investigation.
11:00 AM (WAT): Detailed analysis revealed that the firewall rules were incorrectly configured, leading to the blocking of all incoming traffic.
11:30 AM (WAT): The firewall settings were adjusted to allow incoming traffic, restoring normal operation of the web server.
12:00 PM (WAT): The website became accessible again, and the outage was resolved.

Root Cause and Resolution:

Root Cause: The misconfiguration of the firewall settings resulted in the blocking of all incoming traffic to the web server.
Resolution: The issue was fixed by adjusting the firewall rules to allow incoming traffic, restoring access to the website for users.
Corrective and Preventative Measures:

Improvement/Fixes:
Implement stricter change control procedures to prevent unauthorized changes to critical server configurations.
Enhance monitoring and alerting systems to provide more timely detection of similar issues in the future.
Tasks to Address the Issue:
Conduct a thorough review of firewall configurations to identify and rectify any other potential misconfigurations.
Implement automated backup and rollback procedures for firewall rule changes to quickly revert to a known good state in case of issues.
Provide additional training to infrastructure team members on best practices for configuring and managing firewall settings.
This incident highlighted the importance of robust configuration management and proactive 
monitoring to ensure the reliability and availability of critical systems. By implementing
the corrective and preventative measures outlined above, we aim to minimize the risk of similar
incidents occurring in the future and improve the overall resilience of our infrastructure.
