import socket

def get_banner(ip, port):
    try:
        # Soket oluştur ve bağlantıyı kur
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except Exception as e:
        return str(e)

def main():
    target = "141.148.243.218"  # Hedef IP adresi
    port = 3000  # Hedef port
    banner = get_banner(target, port)
    if banner:
        print(f"Banner bilgisi: {banner}")
    else:
        print("Banner alınamadı.")

if __name__ == "__main__":
    main()
