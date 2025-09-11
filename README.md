# IPList - Combined CloudFlare and IPVerse (Indonesia) IPv4 Ranges

This project provides an automated solution for managing firewall IP lists. The script fetches the latest IPv4 address ranges from **CloudFlare** and all IP addresses from **Indonesia (IPVerse)**, then merges them into a single file. This combined list can be used to secure your servers by limiting access to trusted sources only.

## 🛡️ Project Goal

The primary goal of this project is to enhance server security by implementing a **"deny-all, allow-list"** policy on your firewall.  By restricting access to IPs originating from CloudFlare and Indonesia, you can effectively mitigate various cyber threats from outside these regions, such as:

  * **DDoS Attacks**: Restricting traffic from unknown sources.
  * **Brute-force Attacks**: Preventing unauthorized login attempts from foreign IPs.
  * **Malicious Scanning**: Stopping port and vulnerability scanning.

## ⚙️ How the Script Works

The Python script (`combine_ips.py`) performs the following steps:

1.  **Data Retrieval**: It downloads the latest IPv4 address lists from the official CloudFlare URL and the Regional Internet Registry (RIR) data for Indonesia from IPVerse.
2.  **Merge and Clean**: It combines both lists, removes any empty lines or comments, and eliminates duplicate IP addresses.
3.  **Save**: It saves the combined list into a single file named **`firewall_combined_ips.txt`**.
4.  **Automation**: A GitHub Action is scheduled to run the script **twice a day**, ensuring your IP list is always up-to-date.

-----

## 🚀 Getting Started

### Prerequisites

  * [Python 3](https://www.python.org/)
  * The `requests` library (`pip install requests`)

### Manual Installation and Usage

1.  Download the [`combine_ips.py`](https://www.google.com/search?q=combine_ips.py) file to your server.
2.  Run the script from your terminal:
    ```bash
    python combine_ips.py
    ```
3.  A file named `cf_ipverse_id.txt` will be created. This file contains all the IP addresses ready for you to add to your firewall configuration (e.g., `iptables`, `UFW`, `Firewalld`, or a cloud solution).

### Automation with GitHub Actions

For automatic updates, you can implement this script as a GitHub Action:

1.  Create a new GitHub repository and add the `combine_ips.py` file.
2.  Create a `.github/workflows/` directory inside your repository.
3.  Create an `update_ips.yml` file within that directory and paste in the provided configuration code.

After you commit, GitHub will automatically run the script on schedule, keeping your IP list relevant without any manual intervention.

-----

### Credits

This project uses IP address data collected and maintained by IPVerse. We would like to extend our sincere gratitude to the IPVerse project for providing this valuable resource.

IPVerse: https://github.com/ipverse/rir-ip