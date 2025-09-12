import requests
import os
from datetime import datetime

def get_ip_list_from_url(url):
    """
    Mengambil daftar IP dari sebuah URL, mengabaikan baris komentar (#)
    dan mengembalikan dalam bentuk list.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        lines = response.text.splitlines()
        ip_ranges = []
        for line in lines:
            clean_line = line.strip()
            if clean_line and not clean_line.startswith('#'):
                ip_ranges.append(clean_line)
        
        return ip_ranges
    except requests.exceptions.RequestException as e:
        print(f"Error saat mengambil data dari {url}: {e}")
        return []

def combine_and_save_ips():
    """Menggabungkan IP dari CloudFlare dan IPVerse RIR-IP Indonesia."""
    cloudflare_url = "https://www.cloudflare.com/ips-v4"
    ipverse_url = "https://github.com/ipverse/rir-ip/raw/master/country/id/ipv4-aggregated.txt"
    output_file = "cf_ipverse_id.txt"

    # Periksa keberadaan file dan hapus jika sudah ada
    if os.path.exists(output_file):
        print(f"File '{output_file}' ditemukan. Menghapus file lama...")
        os.remove(output_file)
    
    print("Mendapatkan IP range dari CloudFlare...")
    cloudflare_ips = get_ip_list_from_url(cloudflare_url)
    
    print("Mendapatkan IP range dari IPVerse (Indonesia)...")
    ipverse_ips = get_ip_list_from_url(ipverse_url)

    # Menggabungkan kedua list dan menghapus duplikat menggunakan set
    combined_ips = set(cloudflare_ips + ipverse_ips)

    # Menyimpan daftar IP yang digabungkan ke file baru
    with open(output_file, 'w') as f:
        for ip in sorted(list(combined_ips)):
            f.write(f"{ip}\n")
        # Menambahkan timestamp ke file
        f.write(f"# Updated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    print(f"\nSelesai! {len(combined_ips)} IP range unik telah disimpan ke {output_file}")

if __name__ == "__main__":
    combine_and_save_ips()