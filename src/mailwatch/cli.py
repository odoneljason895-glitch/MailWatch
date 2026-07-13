"""
MailWatch command line interface.
"""

from mailwatch.core.app import MailWatchApp


def main():
    app = MailWatchApp("src/mailwatch/config/accounts.yml")
    app.start()

    print("MailWatch running")
    print(app.status())


if __name__ == "__main__":
    main()