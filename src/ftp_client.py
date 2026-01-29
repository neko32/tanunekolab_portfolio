"""Python FTP client for uploading binary image files.

Usage:
    from ftp_client import FtpClient

    client = FtpClient(host='ftp.example.com', user='username',
                       passwd='password')
    client.upload_file('local/path/image.png', '/remote/dir/image.png')
"""

import ftplib
from pathlib import Path


class FtpClient:
    """
    Simple FTP client wrapper that supports uploading binary files.
    """

    def __init__(self, host: str, user: str = "", passwd: str = "",
                 port: int = 21, timeout: int | None = None):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.timeout = timeout
        self._conn: ftplib.FTP | None = None

    def _connect(self) -> ftplib.FTP:
        if self._conn is None or not self._is_connected():
            self._conn = ftplib.FTP()
            self._conn.connect(host=self.host, port=self.port,
                               timeout=self.timeout)
            self._conn.login(user=self.user, passwd=self.passwd)
        return self._conn

    def _is_connected(self) -> bool:
        try:
            if self._conn is None:
                return False
            # A NOOP command checks the connection without affecting state.
            self._conn.voidcmd("NOOP")
            return True
        except (ftplib.error_temp, ftplib.error_perm):
            return False

    def upload_file(self, local_path: str | Path,
                    remote_path: str | Path) -> None:
        """
        Upload a binary file to the FTP server.

        Parameters
        ----------
        local_path : str or pathlib.Path
            Path to the local image file.
        remote_path : str or pathlib.Path
            Destination path on the FTP server, including filename.
        """
        conn = self._connect()
        with open(local_path, "rb") as f:
            # Use STOR for binary upload. The rest of the path is handled by
            # the server's current working directory; use cwd if needed.
            conn.storbinary(f"STOR {remote_path}", f)

    def close(self) -> None:
        """Close the FTP connection."""
        if self._conn is not None:
            try:
                self._conn.quit()
            finally:
                self._conn = None

    # Context manager support
    def __enter__(self):
        self._connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# Example usage (uncomment for testing)
# if __name__ == "__main__":
#     client = FtpClient(host="ftp.example.com",
#                       user="user", passwd="pass")
#     client.upload_file("image.png", "/uploads/image.png")
#     client.close()