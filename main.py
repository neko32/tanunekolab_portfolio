"""Main entry point for the project."""

from pathlib import Path

from ftp_client import FtpClient



def main() -> None:
    print("Hello from the Python project!")
    
    # FTP接続情報
    host = "192.168.0.159"
    user = "neko32"  # FTPユーザー名（匿名FTPの場合は空文字列）
    passwd = "e99g0475"  # FTPパスワード（匿名FTPの場合は空文字列）
    
    # アップロードするファイルのパス
    local_file = Path("img/16_9.png")
    remote_file = "16_9.png"  # リモートサーバー上のパス
    
    # FTPクライアントを使用してファイルをアップロード
    try:
        with FtpClient(host=host, user=user, passwd=passwd) as client:
            print(f"Uploading {local_file} to {host}{remote_file}...")
            client.upload_file(local_file, remote_file)
            print("Upload completed successfully!")
    except Exception as e:
        print(f"Error uploading file: {e}")


if __name__ == "__main__":
    main()
